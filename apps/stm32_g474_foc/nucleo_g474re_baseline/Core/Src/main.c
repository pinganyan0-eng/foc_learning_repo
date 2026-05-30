/* USER CODE BEGIN Header */
/**
  ******************************************************************************
  * @file           : main.c
  * @brief          : Main program body
  ******************************************************************************
  * @attention
  *
  * Copyright (c) 2026 STMicroelectronics.
  * All rights reserved.
  *
  * This software is licensed under terms that can be found in the LICENSE file
  * in the root directory of this software component.
  * If no LICENSE file comes with this software, it is provided AS-IS.
  *
  ******************************************************************************
  */
/* USER CODE END Header */
/* Includes ------------------------------------------------------------------*/
#include "main.h"

/* Private includes ----------------------------------------------------------*/
/* USER CODE BEGIN Includes */
#include <stdlib.h>
#include <string.h>

/* USER CODE END Includes */

/* Private typedef -----------------------------------------------------------*/
/* USER CODE BEGIN PTD */
typedef enum
{
  APP_MODE_IDLE = 0U,
  APP_MODE_ARMED = 1U,
  APP_MODE_RUN_SIM = 2U
} app_mode_t;

/* USER CODE END PTD */

/* Private define ------------------------------------------------------------*/
/* USER CODE BEGIN PD */
#define APP_CMD_LINE_MAX 32U
#define APP_TARGET_RPM_MIN (-4000L)
#define APP_TARGET_RPM_MAX 4000L
#define APP_UART_RX_DMA_BUF_SIZE 64U
#define APP_UART_RX_RING_SIZE 128U

/* USER CODE END PD */

/* Private macro -------------------------------------------------------------*/
/* USER CODE BEGIN PM */

/* USER CODE END PM */

/* Private variables ---------------------------------------------------------*/

COM_InitTypeDef BspCOMInit;

/* USER CODE BEGIN PV */
DMA_HandleTypeDef hdma_lpuart1_rx;

static uint8_t app_uart_rx_dma_buf[APP_UART_RX_DMA_BUF_SIZE];
static uint8_t app_uart_rx_ring[APP_UART_RX_RING_SIZE];
static volatile uint16_t app_uart_rx_ring_head = 0U;
static volatile uint16_t app_uart_rx_ring_tail = 0U;
static volatile uint32_t app_uart_rx_bytes_total = 0U;
static volatile uint32_t app_uart_rx_drop_count = 0U;
static volatile uint32_t app_uart_rx_restart_error_count = 0U;
static volatile uint32_t app_uart_error_count = 0U;

/* USER CODE END PV */

/* Private function prototypes -----------------------------------------------*/
void SystemClock_Config(void);
static void MX_GPIO_Init(void);
/* USER CODE BEGIN PFP */
static const char *AppModeName(app_mode_t mode);
static void AppHandleCommand(const char *cmd, app_mode_t *app_mode, uint32_t *mode_change_count, int32_t *target_rpm);
static void AppFeedRxByte(uint8_t rx_ch, app_mode_t *app_mode, uint32_t *mode_change_count, int32_t *target_rpm);
static HAL_StatusTypeDef AppComRxDmaInit(void);
static HAL_StatusTypeDef AppStartUartRxDmaIdle(UART_HandleTypeDef *huart);
static void AppRxRingPushFromIsr(uint8_t rx_ch);
static uint8_t AppRxRingPop(uint8_t *rx_ch);
static uint32_t AppDrainRxQueue(app_mode_t *app_mode, uint32_t *mode_change_count, int32_t *target_rpm);

/* USER CODE END PFP */

/* Private user code ---------------------------------------------------------*/
/* USER CODE BEGIN 0 */
static const char *AppModeName(app_mode_t mode)
{
  switch (mode)
  {
    case APP_MODE_IDLE:
      return "IDLE";

    case APP_MODE_ARMED:
      return "ARMED";

    case APP_MODE_RUN_SIM:
      return "RUN_SIM";

    default:
      return "UNKNOWN";
  }
}

static void AppHandleCommand(const char *cmd, app_mode_t *app_mode, uint32_t *mode_change_count, int32_t *target_rpm)
{
  if (strcmp(cmd, "PING") == 0)
  {
    printf("PONG\r\n");
  }
  else if (strcmp(cmd, "MODE?") == 0)
  {
    printf("OK unchanged mode=%u mode_name=%s\r\n",
           (unsigned int)(*app_mode),
           AppModeName(*app_mode));
  }
  else if (strncmp(cmd, "SET_RPM", 7U) == 0)
  {
    const char *arg = &cmd[7];
    char *end = NULL;
    long requested_rpm = 0L;

    if (*arg != ' ')
    {
      printf("ERR parse cmd=SET_RPM\r\n");
      return;
    }

    while (*arg == ' ')
    {
      arg++;
    }

    requested_rpm = strtol(arg, &end, 10);
    if ((end == arg) || (*arg == '\0'))
    {
      printf("ERR parse cmd=SET_RPM\r\n");
      return;
    }

    while (*end == ' ')
    {
      end++;
    }

    if (*end != '\0')
    {
      printf("ERR parse cmd=SET_RPM\r\n");
      return;
    }

    if ((requested_rpm < APP_TARGET_RPM_MIN) || (requested_rpm > APP_TARGET_RPM_MAX))
    {
      printf("ERR range cmd=SET_RPM rpm=%ld min=%ld max=%ld\r\n",
             requested_rpm,
             APP_TARGET_RPM_MIN,
             APP_TARGET_RPM_MAX);
      return;
    }

    if (*app_mode == APP_MODE_IDLE)
    {
      printf("ERR bad_state cmd=SET_RPM mode=%u mode_name=%s\r\n",
             (unsigned int)(*app_mode),
             AppModeName(*app_mode));
      return;
    }

    *target_rpm = (int32_t)requested_rpm;
    printf("OK target_rpm=%ld mode=%u mode_name=%s\r\n",
           (long)(*target_rpm),
           (unsigned int)(*app_mode),
           AppModeName(*app_mode));
  }
  else if (strcmp(cmd, "ARM") == 0)
  {
    if (*app_mode == APP_MODE_IDLE)
    {
      *app_mode = APP_MODE_ARMED;
      (*mode_change_count)++;
      printf("OK changed mode=%u mode_name=%s\r\n",
             (unsigned int)(*app_mode),
             AppModeName(*app_mode));
    }
    else
    {
      printf("ERR bad_state cmd=ARM mode=%u mode_name=%s\r\n",
             (unsigned int)(*app_mode),
             AppModeName(*app_mode));
    }
  }
  else if (strcmp(cmd, "STOP") == 0)
  {
    *target_rpm = 0;

    if (*app_mode == APP_MODE_IDLE)
    {
      printf("OK unchanged mode=%u mode_name=%s target_rpm=%ld\r\n",
             (unsigned int)(*app_mode),
             AppModeName(*app_mode),
             (long)(*target_rpm));
    }
    else
    {
      *app_mode = APP_MODE_IDLE;
      (*mode_change_count)++;
      printf("OK changed mode=%u mode_name=%s\r\n",
             (unsigned int)(*app_mode),
             AppModeName(*app_mode));
    }
  }
  else
  {
    printf("ERR unknown_cmd cmd=%s\r\n", cmd);
  }
}

static void AppFeedRxByte(uint8_t rx_ch, app_mode_t *app_mode, uint32_t *mode_change_count, int32_t *target_rpm)
{
  static char rx_line[APP_CMD_LINE_MAX];
  static uint32_t rx_len = 0U;

  if ((rx_ch == '\r') || (rx_ch == '\n'))
  {
    if (rx_len > 0U)
    {
      rx_line[rx_len] = '\0';
      AppHandleCommand(rx_line, app_mode, mode_change_count, target_rpm);
      rx_len = 0U;
    }
  }
  else if (rx_len < (APP_CMD_LINE_MAX - 1U))
  {
    rx_line[rx_len] = (char)rx_ch;
    rx_len++;
  }
  else
  {
    rx_len = 0U;
    printf("ERR line_too_long\r\n");
  }
}

static HAL_StatusTypeDef AppComRxDmaInit(void)
{
  __HAL_RCC_DMAMUX1_CLK_ENABLE();
  __HAL_RCC_DMA1_CLK_ENABLE();

  hdma_lpuart1_rx.Instance = DMA1_Channel1;
  hdma_lpuart1_rx.Init.Request = DMA_REQUEST_LPUART1_RX;
  hdma_lpuart1_rx.Init.Direction = DMA_PERIPH_TO_MEMORY;
  hdma_lpuart1_rx.Init.PeriphInc = DMA_PINC_DISABLE;
  hdma_lpuart1_rx.Init.MemInc = DMA_MINC_ENABLE;
  hdma_lpuart1_rx.Init.PeriphDataAlignment = DMA_PDATAALIGN_BYTE;
  hdma_lpuart1_rx.Init.MemDataAlignment = DMA_MDATAALIGN_BYTE;
  hdma_lpuart1_rx.Init.Mode = DMA_NORMAL;
  hdma_lpuart1_rx.Init.Priority = DMA_PRIORITY_LOW;

  if (HAL_DMA_Init(&hdma_lpuart1_rx) != HAL_OK)
  {
    return HAL_ERROR;
  }

  __HAL_LINKDMA(&hcom_uart[COM1], hdmarx, hdma_lpuart1_rx);

  HAL_NVIC_SetPriority(DMA1_Channel1_IRQn, 1U, 0U);
  HAL_NVIC_EnableIRQ(DMA1_Channel1_IRQn);
  HAL_NVIC_SetPriority(LPUART1_IRQn, 1U, 1U);
  HAL_NVIC_EnableIRQ(LPUART1_IRQn);

  return HAL_OK;
}

static HAL_StatusTypeDef AppStartUartRxDmaIdle(UART_HandleTypeDef *huart)
{
  HAL_StatusTypeDef status = HAL_UARTEx_ReceiveToIdle_DMA(huart,
                                                          app_uart_rx_dma_buf,
                                                          sizeof(app_uart_rx_dma_buf));

  if ((status == HAL_OK) && (huart->hdmarx != NULL))
  {
    __HAL_DMA_DISABLE_IT(huart->hdmarx, DMA_IT_HT);
  }

  return status;
}

static void AppRxRingPushFromIsr(uint8_t rx_ch)
{
  uint16_t next_head = (uint16_t)((app_uart_rx_ring_head + 1U) % APP_UART_RX_RING_SIZE);

  if (next_head == app_uart_rx_ring_tail)
  {
    app_uart_rx_drop_count++;
    return;
  }

  app_uart_rx_ring[app_uart_rx_ring_head] = rx_ch;
  app_uart_rx_ring_head = next_head;
  app_uart_rx_bytes_total++;
}

static uint8_t AppRxRingPop(uint8_t *rx_ch)
{
  uint8_t has_byte = 0U;

  __disable_irq();
  if (app_uart_rx_ring_tail != app_uart_rx_ring_head)
  {
    *rx_ch = app_uart_rx_ring[app_uart_rx_ring_tail];
    app_uart_rx_ring_tail = (uint16_t)((app_uart_rx_ring_tail + 1U) % APP_UART_RX_RING_SIZE);
    has_byte = 1U;
  }
  __enable_irq();

  return has_byte;
}

static uint32_t AppDrainRxQueue(app_mode_t *app_mode, uint32_t *mode_change_count, int32_t *target_rpm)
{
  uint8_t rx_ch = 0U;
  uint32_t drained = 0U;

  while (AppRxRingPop(&rx_ch) != 0U)
  {
    AppFeedRxByte(rx_ch, app_mode, mode_change_count, target_rpm);
    drained++;
  }

  return drained;
}

void HAL_UARTEx_RxEventCallback(UART_HandleTypeDef *huart, uint16_t Size)
{
  if (huart->Instance == LPUART1)
  {
    for (uint16_t i = 0U; i < Size; i++)
    {
      AppRxRingPushFromIsr(app_uart_rx_dma_buf[i]);
    }

    if (AppStartUartRxDmaIdle(huart) != HAL_OK)
    {
      app_uart_rx_restart_error_count++;
    }
  }
}

void HAL_UART_ErrorCallback(UART_HandleTypeDef *huart)
{
  if (huart->Instance == LPUART1)
  {
    app_uart_error_count++;
    if (AppStartUartRxDmaIdle(huart) != HAL_OK)
    {
      app_uart_rx_restart_error_count++;
    }
  }
}

/* USER CODE END 0 */

/**
  * @brief  The application entry point.
  * @retval int
  */
int main(void)
{

  /* USER CODE BEGIN 1 */

  /* USER CODE END 1 */

  /* MCU Configuration--------------------------------------------------------*/

  /* Reset of all peripherals, Initializes the Flash interface and the Systick. */
  HAL_Init();

  /* USER CODE BEGIN Init */

  /* USER CODE END Init */

  /* Configure the system clock */
  SystemClock_Config();

  /* USER CODE BEGIN SysInit */

  /* USER CODE END SysInit */

  /* Initialize all configured peripherals */
  MX_GPIO_Init();
  /* USER CODE BEGIN 2 */
  /* 记录上一次翻转 LD2 的时间戳，单位 ms */
  uint32_t led_last_tick = 0U;

  /* 记录上一次串口上报的时间戳，单位 ms */
  uint32_t report_last_tick = 0U;

  /* 软件里保存 LED 当前状态：0=灭，1=亮 */
  uint8_t led_state = 0U;

  /* 统计 LD2 已经翻转了多少次，用来观察 100 ms 任务执行次数 */
  uint32_t led_toggle_count = 0U;

  /* 统计串口已经上报了多少次，用来观察 500 ms 任务执行次数 */
  uint32_t report_count = 0U;
  /* USER CODE END 2 */

  /* 每 10 ms 扫描一次 B1 按键，避免主循环每圈都读按键 */
  uint32_t button_sample_last_tick = 0U;

  /* 记录上一次按键有效事件的时间，用于简单消抖 */
  uint32_t button_last_event_tick = 0U;

  /* 当前按键电平：BUTTON_RELEASED=松开，BUTTON_PRESSED=按下 */
  uint8_t button_state = BUTTON_RELEASED;

  /* 上一次扫描到的按键电平，用于判断“松开 -> 按下” */
  uint8_t button_last_state = BUTTON_RELEASED;

  /* 统计用户按下 B1 的有效次数 */
  uint32_t button_press_count = 0U;

  /* 当前应用模式：0=IDLE, 1=ARMED, 2=RUN_SIM */
  app_mode_t app_mode = APP_MODE_IDLE;

  /* 统计模式切换次数, 用来验证状态机只在有效按键事件发生时切换 */
  uint32_t mode_change_count = 0U;

  /* 当前只作为通信层学习用的模拟目标转速，不驱动电机或 PWM */
  int32_t target_rpm = 0;


  /* Initialize led */
  BSP_LED_Init(LED_GREEN);

  /* Initialize USER push-button, will be used to trigger an interrupt each time it's pressed.*/
  BSP_PB_Init(BUTTON_USER, BUTTON_MODE_EXTI);

  /* Initialize COM1 port (115200, 8 bits (7-bit data + 1 stop bit), no parity */
  BspCOMInit.BaudRate   = 115200;
  BspCOMInit.WordLength = COM_WORDLENGTH_8B;
  BspCOMInit.StopBits   = COM_STOPBITS_1;
  BspCOMInit.Parity     = COM_PARITY_NONE;
  BspCOMInit.HwFlowCtl  = COM_HWCONTROL_NONE;
  if (BSP_COM_Init(COM1, &BspCOMInit) != BSP_ERROR_NONE)
  {
    Error_Handler();
  }

  if (AppComRxDmaInit() != HAL_OK)
  {
    Error_Handler();
  }

  if (AppStartUartRxDmaIdle(&hcom_uart[COM1]) != HAL_OK)
  {
    Error_Handler();
  }

  /* USER CODE BEGIN COM_READY */
  /* 上电后先强制关灯，让 LED 初始状态可预测 */
  BSP_LED_Off(LED_GREEN);
  led_state = 0U;

  /* 串口就绪后读取一次按键初始状态，避免上电瞬间误判一次按下 */
  button_state = (uint8_t)BSP_PB_GetState(BUTTON_USER);
  button_last_state = button_state;

  /* 串口初始化完成后的启动标记，复位后应只打印一次 */
  printf("BOOT OK rx=dma_idle\r\n");
  /* USER CODE END COM_READY */

  /* Infinite loop */
  /* USER CODE BEGIN WHILE */
  while (1)
  {

    /* USER CODE END WHILE */

    /* USER CODE BEGIN 3 */
    /* HAL_GetTick() 是系统毫秒计数器，来自 SysTick */
    uint32_t now = HAL_GetTick();

    /* Drain bytes captured by DMA + IDLE; command parsing stays in main loop. */
    (void)AppDrainRxQueue(&app_mode, &mode_change_count, &target_rpm);

    /* 每 100 ms 翻转一次 LD2：亮 100 ms，灭 100 ms */
    if ((now - led_last_tick) >= 100U)
    {
      led_last_tick = now;

      BSP_LED_Toggle(LED_GREEN);

      /* 同步维护软件状态，后面串口上报时不用再读 GPIO */
      led_state ^= 1U;
      
      /* 每翻转一次就加 1，验证 100 ms 任务真的在按节拍运行 */
      led_toggle_count++;
    }

     /* 每 10 ms 扫描一次按键：把物理电平转换成“按下一次”的事件 */
    if ((now - button_sample_last_tick) >= 10U)
    {
     button_sample_last_tick = now;

     /* BSP 返回 1 表示按下，0 表示松开 */
     button_state = (uint8_t)BSP_PB_GetState(BUTTON_USER);

     /* 只统计“松开 -> 按下”的瞬间；按住不放不会重复计数 */
     if ((button_last_state == BUTTON_RELEASED) &&
       (button_state == BUTTON_PRESSED) &&
       ((now - button_last_event_tick) >= 50U))
     {
       /* 50 ms 简单消抖：过滤机械按键弹跳造成的重复触发 */
       button_last_event_tick = now;
       button_press_count++;

       /* 每次有效按下 B1, 按显式状态转移表切换模式 */
       switch (app_mode)
        {
          case APP_MODE_IDLE:
            /* IDLE: 空闲状态。按键后进入准备状态。 */
            app_mode = APP_MODE_ARMED;
            break;

          case APP_MODE_ARMED:
            /* ARMED: 已准备。按键后进入模拟运行状态。 */
            app_mode = APP_MODE_RUN_SIM;
            break;

          case APP_MODE_RUN_SIM:
            /* RUN_SIM: 模拟运行。按键后回到空闲状态。 */
            app_mode = APP_MODE_IDLE;
            break;

          default:
            /* 异常状态兜底：如果状态值被写坏，回到安全的 IDLE。 */
            app_mode = APP_MODE_IDLE;
            break;
        }

        /* 只有发生有效按键事件，才记录一次状态切换 */
        mode_change_count++;

      }

      button_last_state = button_state;
    }

    /* 每 500 ms 上报一次状态；这和 LED 翻转互不阻塞 */
    if ((now - report_last_tick) >= 500U)
    {
     report_last_tick = now;

      /* 每上报一次就加 1，验证 500 ms 任务的执行次数 */
      report_count++;

      /* 每 500 ms 打印一次状态，观察两个任务的执行次数关系 */
      printf("tick_ms=%lu, led=%u, led_toggle=%lu, report=%lu, btn=%u, btn_press=%lu, mode=%u, mode_name=%s, mode_chg=%lu, target_rpm=%ld, rx_bytes=%lu, rx_drop=%lu, rx_restart_err=%lu, uart_err=%lu\r\n",
       (unsigned long)now,
       led_state,
       (unsigned long)led_toggle_count,
       (unsigned long)report_count,
       button_state,
       (unsigned long)button_press_count,
       (unsigned int)app_mode,
       AppModeName(app_mode),
       (unsigned long)mode_change_count,
       (long)target_rpm,
       (unsigned long)app_uart_rx_bytes_total,
       (unsigned long)app_uart_rx_drop_count,
       (unsigned long)app_uart_rx_restart_error_count,
       (unsigned long)app_uart_error_count);


    }
  }
  /* USER CODE END 3 */
}

/**
  * @brief System Clock Configuration
  * @retval None
  */
void SystemClock_Config(void)
{
  RCC_OscInitTypeDef RCC_OscInitStruct = {0};
  RCC_ClkInitTypeDef RCC_ClkInitStruct = {0};

  /** Configure the main internal regulator output voltage
  */
  HAL_PWREx_ControlVoltageScaling(PWR_REGULATOR_VOLTAGE_SCALE1_BOOST);

  /** Initializes the RCC Oscillators according to the specified parameters
  * in the RCC_OscInitTypeDef structure.
  */
  RCC_OscInitStruct.OscillatorType = RCC_OSCILLATORTYPE_HSI;
  RCC_OscInitStruct.HSIState = RCC_HSI_ON;
  RCC_OscInitStruct.HSICalibrationValue = RCC_HSICALIBRATION_DEFAULT;
  RCC_OscInitStruct.PLL.PLLState = RCC_PLL_ON;
  RCC_OscInitStruct.PLL.PLLSource = RCC_PLLSOURCE_HSI;
  RCC_OscInitStruct.PLL.PLLM = RCC_PLLM_DIV4;
  RCC_OscInitStruct.PLL.PLLN = 85;
  RCC_OscInitStruct.PLL.PLLP = RCC_PLLP_DIV2;
  RCC_OscInitStruct.PLL.PLLQ = RCC_PLLQ_DIV2;
  RCC_OscInitStruct.PLL.PLLR = RCC_PLLR_DIV2;
  if (HAL_RCC_OscConfig(&RCC_OscInitStruct) != HAL_OK)
  {
    Error_Handler();
  }

  /** Initializes the CPU, AHB and APB buses clocks
  */
  RCC_ClkInitStruct.ClockType = RCC_CLOCKTYPE_HCLK|RCC_CLOCKTYPE_SYSCLK
                              |RCC_CLOCKTYPE_PCLK1|RCC_CLOCKTYPE_PCLK2;
  RCC_ClkInitStruct.SYSCLKSource = RCC_SYSCLKSOURCE_PLLCLK;
  RCC_ClkInitStruct.AHBCLKDivider = RCC_SYSCLK_DIV1;
  RCC_ClkInitStruct.APB1CLKDivider = RCC_HCLK_DIV1;
  RCC_ClkInitStruct.APB2CLKDivider = RCC_HCLK_DIV1;

  if (HAL_RCC_ClockConfig(&RCC_ClkInitStruct, FLASH_LATENCY_4) != HAL_OK)
  {
    Error_Handler();
  }
}

/**
  * @brief GPIO Initialization Function
  * @param None
  * @retval None
  */
static void MX_GPIO_Init(void)
{
  /* USER CODE BEGIN MX_GPIO_Init_1 */

  /* USER CODE END MX_GPIO_Init_1 */

  /* GPIO Ports Clock Enable */
  __HAL_RCC_GPIOC_CLK_ENABLE();
  __HAL_RCC_GPIOF_CLK_ENABLE();
  __HAL_RCC_GPIOA_CLK_ENABLE();
  __HAL_RCC_GPIOB_CLK_ENABLE();

  /* USER CODE BEGIN MX_GPIO_Init_2 */

  /* USER CODE END MX_GPIO_Init_2 */
}

/* USER CODE BEGIN 4 */

/* USER CODE END 4 */

/**
  * @brief  This function is executed in case of error occurrence.
  * @retval None
  */
void Error_Handler(void)
{
  /* USER CODE BEGIN Error_Handler_Debug */
  /* User can add his own implementation to report the HAL error return state */
  __disable_irq();
  while (1)
  {
  }
  /* USER CODE END Error_Handler_Debug */
}
#ifdef USE_FULL_ASSERT
/**
  * @brief  Reports the name of the source file and the source line number
  *         where the assert_param error has occurred.
  * @param  file: pointer to the source file name
  * @param  line: assert_param error line source number
  * @retval None
  */
void assert_failed(uint8_t *file, uint32_t line)
{
  /* USER CODE BEGIN 6 */
  /* User can add his own implementation to report the file name and line number,
     ex: printf("Wrong parameters value: file %s on line %d\r\n", file, line) */
  /* USER CODE END 6 */
}
#endif /* USE_FULL_ASSERT */
