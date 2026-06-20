cmake_minimum_required(VERSION 3.22)

project(stdrive101_manual_gate_test_lockout_compile_only C)

set(CMAKE_C_STANDARD 11)
set(CMAKE_C_STANDARD_REQUIRED ON)
set(CMAKE_C_EXTENSIONS ON)

set(REPO_ROOT "${CMAKE_CURRENT_LIST_DIR}/../../../..")
set(CMSIS_DEVICE_DIR
    "${REPO_ROOT}/apps/stm32_g474_foc/nucleo_g474re_baseline/Drivers/CMSIS/Device/ST/STM32G4xx/Include")
set(CMSIS_CORE_DIR
    "${REPO_ROOT}/apps/stm32_g474_foc/nucleo_g474re_baseline/Drivers/CMSIS/Include")

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
