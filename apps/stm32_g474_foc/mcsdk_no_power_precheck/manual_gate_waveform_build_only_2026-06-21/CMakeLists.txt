cmake_minimum_required(VERSION 3.22)

project(stdrive101_manual_gate_waveform_build_only C ASM)

set(CMAKE_C_STANDARD 11)
set(CMAKE_C_STANDARD_REQUIRED ON)
set(CMAKE_C_EXTENSIONS ON)

set(REPO_ROOT "${CMAKE_CURRENT_LIST_DIR}/../../../..")
set(SOURCE_PACKAGE_DIR
    "${REPO_ROOT}/apps/stm32_g474_foc/mcsdk_no_power_precheck/manual_gate_waveform_source_package_2026-06-21")
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

set(GATE_WAVEFORM_SOURCES
    "${SOURCE_PACKAGE_DIR}/Src/gate_waveform_candidate.c"
    "${SOURCE_PACKAGE_DIR}/Src/main_waveform_candidate.c"
)

set(GATE_WAVEFORM_INCLUDE_DIRS
    "${SOURCE_PACKAGE_DIR}/Inc"
    "${CMSIS_DEVICE_DIR}"
    "${CMSIS_CORE_DIR}"
)

set(GATE_WAVEFORM_DEFINITIONS
    STM32G474xx
    GATE_WAVEFORM_CANDIDATE_GATE_E2_BUILD_ACK
)

set(GATE_WAVEFORM_COMPILE_OPTIONS
    -mcpu=cortex-m4
    -mthumb
    -Wall
    -Wextra
    -Werror
    -ffunction-sections
    -fdata-sections
)

add_library(stdrive101_gate_waveform_candidate_objects OBJECT
    ${GATE_WAVEFORM_SOURCES}
)

target_compile_definitions(stdrive101_gate_waveform_candidate_objects PRIVATE
    ${GATE_WAVEFORM_DEFINITIONS}
)

target_include_directories(stdrive101_gate_waveform_candidate_objects PRIVATE
    ${GATE_WAVEFORM_INCLUDE_DIRS}
)

target_compile_options(stdrive101_gate_waveform_candidate_objects PRIVATE
    ${GATE_WAVEFORM_COMPILE_OPTIONS}
)

add_executable(stdrive101_gate_waveform_candidate_image
    ${GATE_WAVEFORM_SOURCES}
    Src/minimal_runtime.c
    "${NUCLEO_BASELINE_DIR}/startup_stm32g474xx.s"
    "${NUCLEO_BASELINE_CORE_SRC_DIR}/system_stm32g4xx.c"
)

add_executable(stdrive101_force_gpio_toggle_image
    Src/force_gpio_toggle_main.c
    Src/minimal_runtime.c
    "${NUCLEO_BASELINE_DIR}/startup_stm32g474xx.s"
    "${NUCLEO_BASELINE_CORE_SRC_DIR}/system_stm32g4xx.c"
)

add_executable(stdrive101_pa7_hold_high_image
    Src/pa7_hold_high_main.c
    Src/minimal_runtime.c
    "${NUCLEO_BASELINE_DIR}/startup_stm32g474xx.s"
    "${NUCLEO_BASELINE_CORE_SRC_DIR}/system_stm32g4xx.c"
)

set_target_properties(stdrive101_gate_waveform_candidate_image PROPERTIES
    OUTPUT_NAME stdrive101_gate_waveform_candidate_image
    SUFFIX ".elf"
)

target_compile_definitions(stdrive101_gate_waveform_candidate_image PRIVATE
    ${GATE_WAVEFORM_DEFINITIONS}
)

target_include_directories(stdrive101_gate_waveform_candidate_image PRIVATE
    ${GATE_WAVEFORM_INCLUDE_DIRS}
)

target_compile_options(stdrive101_gate_waveform_candidate_image PRIVATE
    ${GATE_WAVEFORM_COMPILE_OPTIONS}
)

target_link_options(stdrive101_gate_waveform_candidate_image PRIVATE
    -mcpu=cortex-m4
    -mthumb
    -T "${NUCLEO_BASELINE_LINKER_SCRIPT}"
    -nostdlib
    -Wl,-Map=$<TARGET_FILE_DIR:stdrive101_gate_waveform_candidate_image>/stdrive101_gate_waveform_candidate_image.map
    -Wl,--gc-sections
    -Wl,--print-memory-usage
)

target_link_libraries(stdrive101_gate_waveform_candidate_image PRIVATE
    gcc
)

set_target_properties(stdrive101_force_gpio_toggle_image PROPERTIES
    OUTPUT_NAME stdrive101_force_gpio_toggle_image
    SUFFIX ".elf"
)

target_compile_definitions(stdrive101_force_gpio_toggle_image PRIVATE
    STM32G474xx
)

target_include_directories(stdrive101_force_gpio_toggle_image PRIVATE
    "${CMSIS_DEVICE_DIR}"
    "${CMSIS_CORE_DIR}"
)

target_compile_options(stdrive101_force_gpio_toggle_image PRIVATE
    ${GATE_WAVEFORM_COMPILE_OPTIONS}
)

target_link_options(stdrive101_force_gpio_toggle_image PRIVATE
    -mcpu=cortex-m4
    -mthumb
    -T "${NUCLEO_BASELINE_LINKER_SCRIPT}"
    -nostdlib
    -Wl,-Map=$<TARGET_FILE_DIR:stdrive101_force_gpio_toggle_image>/stdrive101_force_gpio_toggle_image.map
    -Wl,--gc-sections
    -Wl,--print-memory-usage
)

target_link_libraries(stdrive101_force_gpio_toggle_image PRIVATE
    gcc
)

set_target_properties(stdrive101_pa7_hold_high_image PROPERTIES
    OUTPUT_NAME stdrive101_pa7_hold_high_image
    SUFFIX ".elf"
)

target_compile_definitions(stdrive101_pa7_hold_high_image PRIVATE
    STM32G474xx
)

target_include_directories(stdrive101_pa7_hold_high_image PRIVATE
    "${CMSIS_DEVICE_DIR}"
    "${CMSIS_CORE_DIR}"
)

target_compile_options(stdrive101_pa7_hold_high_image PRIVATE
    ${GATE_WAVEFORM_COMPILE_OPTIONS}
)

target_link_options(stdrive101_pa7_hold_high_image PRIVATE
    -mcpu=cortex-m4
    -mthumb
    -T "${NUCLEO_BASELINE_LINKER_SCRIPT}"
    -nostdlib
    -Wl,-Map=$<TARGET_FILE_DIR:stdrive101_pa7_hold_high_image>/stdrive101_pa7_hold_high_image.map
    -Wl,--gc-sections
    -Wl,--print-memory-usage
)

target_link_libraries(stdrive101_pa7_hold_high_image PRIVATE
    gcc
)
