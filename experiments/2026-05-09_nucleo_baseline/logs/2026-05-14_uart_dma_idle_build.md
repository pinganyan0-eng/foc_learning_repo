# 2026-05-14 UART DMA + IDLE Build

## Feature Sentence

The NUCLEO-G474RE baseline now receives COM1 bytes through
`HAL_UARTEx_ReceiveToIdle_DMA()`, stores received bytes in an ISR-fed ring
buffer, and parses complete command lines from the main loop.

## Code Change

- `Core/Src/main.c`
  - Adds LPUART1 RX DMA buffer and a 128-byte ring buffer.
  - Configures `DMA1_Channel1` with `DMA_REQUEST_LPUART1_RX`.
  - Starts receive-to-idle DMA after `BSP_COM_Init(COM1, ...)`.
  - Implements `HAL_UARTEx_RxEventCallback()` to copy received bytes only.
  - Keeps `AppHandleCommand()` and `printf()` execution in the main loop.
  - Adds UART receive counters to the 500 ms status line:
    `rx_bytes`, `rx_drop`, `rx_restart_err`, and `uart_err`.
- `Core/Src/stm32g4xx_it.c`
  - Adds `DMA1_Channel1_IRQHandler()`.
  - Adds `LPUART1_IRQHandler()`.
- `Core/Inc/stm32g4xx_it.h`
  - Adds the new interrupt prototypes.

## Build Command

Run from `apps/stm32_g474_foc/nucleo_g474re_baseline/` with STM32Cube bundle
`ninja` and `gnu-tools-for-stm32` on `PATH`:

```powershell
cmake --preset Debug
cmake --build --preset Debug
```

## Build Result

The Debug build completed and linked:

```text
[3/3] Linking C executable nucleo_g474re_baseline.elf
RAM:   2552 B / 128 KB  (1.95%)
FLASH: 23652 B / 512 KB (4.51%)
```

## Hardware Boundary

This is a no-power firmware build. It does not authorize 24V, a power board,
a motor, Gate PWM, Motor Profiler, Hall closed-loop, or SMO work.

## Next Useful Check

When using only the NUCLEO USB/ST-LINK VCP, send these commands over COM5 and
confirm the same command semantics as the previous polling implementation:

```text
PING
MODE?
ARM
SET_RPM 1200
STOP
```
