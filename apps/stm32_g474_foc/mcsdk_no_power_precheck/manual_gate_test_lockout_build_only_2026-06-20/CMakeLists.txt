cmake_minimum_required(VERSION 3.22)

project(stdrive101_manual_gate_test_lockout_compile_only C ASM)

set(CMAKE_C_STANDARD 11)
set(CMAKE_C_STANDARD_REQUIRED ON)
set(CMAKE_C_EXTENSIONS ON)

set(REPO_ROOT "${CMAKE_CURRENT_LIST_DIR}/../../../..")
set(CMSIS_DEVICE_DIR
    "${REPO_ROOT}/apps/stm32_g474_foc/nucleo_g474re_baseline/Drivers/CMSIS/Device/ST/STM32G4xx/Include")
set(CMSIS_CORE_DIR
    "${REPO_ROOT}/apps/stm32_g474_foc/nucleo_g474re_baseline/Drivers/CMSIS/Include")
set(NUCLEO_BASELINE_DIR
    "${REPO_ROOT}/apps/stm32_g474_foc/nucleo_g474re_baseline")
set(NUCLEO_BASELINE_CORE_SRC_DIR
    "${NUCLEO_BASELINE_DIR}/Core/Src")
set(NUCLEO_BASELINE_LINKER_SCRIPT
    "${NUCLEO_BASELINE_DIR}/STM32G474XX_FLASH.ld")

add_library(stdrive101_gate_lockout_objects OBJECT
    Src/gate_test_lockout.c
    Src/main_lockout.c
)

target_compile_definitions(stdrive101_gate_lockout_objects PRIVATE
    STM32G474xx
)

target_include_directories(stdrive101_gate_lockout_objects PRIVATE
    Inc
    "${CMSIS_DEVICE_DIR}"
    "${CMSIS_CORE_DIR}"
)

target_compile_options(stdrive101_gate_lockout_objects PRIVATE
    -mcpu=cortex-m4
    -mthumb
    -Wall
    -Wextra
    -Werror
)

add_executable(stdrive101_gate_lockout_image
    Src/gate_test_lockout.c
    Src/main_lockout.c
    "${NUCLEO_BASELINE_DIR}/startup_stm32g474xx.s"
    "${NUCLEO_BASELINE_CORE_SRC_DIR}/system_stm32g4xx.c"
    "${NUCLEO_BASELINE_CORE_SRC_DIR}/syscalls.c"
    "${NUCLEO_BASELINE_CORE_SRC_DIR}/sysmem.c"
)

set_target_properties(stdrive101_gate_lockout_image PROPERTIES
    OUTPUT_NAME stdrive101_gate_lockout_image
    SUFFIX ".elf"
)

target_compile_definitions(stdrive101_gate_lockout_image PRIVATE
    STM32G474xx
)

target_include_directories(stdrive101_gate_lockout_image PRIVATE
    Inc
    "${CMSIS_DEVICE_DIR}"
    "${CMSIS_CORE_DIR}"
)

target_compile_options(stdrive101_gate_lockout_image PRIVATE
    -mcpu=cortex-m4
    -mthumb
    -Wall
    -Wextra
    -Werror
    -ffunction-sections
    -fdata-sections
)

target_link_options(stdrive101_gate_lockout_image PRIVATE
    -mcpu=cortex-m4
    -mthumb
    -T "${NUCLEO_BASELINE_LINKER_SCRIPT}"
    --specs=nano.specs
    -Wl,-Map=$<TARGET_FILE_DIR:stdrive101_gate_lockout_image>/stdrive101_gate_lockout_image.map
    -Wl,--gc-sections
    -Wl,--print-memory-usage
)
