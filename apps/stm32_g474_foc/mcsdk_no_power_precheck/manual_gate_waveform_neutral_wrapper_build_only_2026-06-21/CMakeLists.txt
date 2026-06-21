cmake_minimum_required(VERSION 3.22)

project(stdrive101_manual_gate_waveform_neutral_wrapper_build_only C ASM)

set(CMAKE_C_STANDARD 11)
set(CMAKE_C_STANDARD_REQUIRED ON)
set(CMAKE_C_EXTENSIONS ON)

set(REPO_ROOT "${CMAKE_CURRENT_LIST_DIR}/../../../..")
set(WAVEFORM_SOURCE_PACKAGE_DIR
    "${REPO_ROOT}/apps/stm32_g474_foc/mcsdk_no_power_precheck/manual_gate_waveform_source_package_2026-06-21")
set(NEUTRAL_WRAPPER_SOURCE_PACKAGE_DIR
    "${REPO_ROOT}/apps/stm32_g474_foc/mcsdk_no_power_precheck/manual_gate_waveform_neutral_wrapper_source_package_2026-06-21")
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

set(GATE_WAVEFORM_NEUTRAL_WRAPPER_SOURCES
    "${WAVEFORM_SOURCE_PACKAGE_DIR}/Src/gate_waveform_candidate.c"
    "${NEUTRAL_WRAPPER_SOURCE_PACKAGE_DIR}/Src/main_neutral_wrapper.c"
)

set(GATE_WAVEFORM_NEUTRAL_WRAPPER_INCLUDE_DIRS
    "${WAVEFORM_SOURCE_PACKAGE_DIR}/Inc"
    "${NEUTRAL_WRAPPER_SOURCE_PACKAGE_DIR}/Inc"
    "${CMSIS_DEVICE_DIR}"
    "${CMSIS_CORE_DIR}"
)

set(GATE_WAVEFORM_NEUTRAL_WRAPPER_DEFINITIONS
    STM32G474xx
    GATE_WAVEFORM_CANDIDATE_GATE_E2_BUILD_ACK
    GATE_WAVEFORM_NEUTRAL_WRAPPER_BUILD_ACK
)

set(GATE_WAVEFORM_NEUTRAL_WRAPPER_COMPILE_OPTIONS
    -mcpu=cortex-m4
    -mthumb
    -Wall
    -Wextra
    -Werror
    -ffunction-sections
    -fdata-sections
)

add_library(stdrive101_gate_waveform_neutral_wrapper_objects OBJECT
    ${GATE_WAVEFORM_NEUTRAL_WRAPPER_SOURCES}
)

target_compile_definitions(stdrive101_gate_waveform_neutral_wrapper_objects PRIVATE
    ${GATE_WAVEFORM_NEUTRAL_WRAPPER_DEFINITIONS}
)

target_include_directories(stdrive101_gate_waveform_neutral_wrapper_objects PRIVATE
    ${GATE_WAVEFORM_NEUTRAL_WRAPPER_INCLUDE_DIRS}
)

target_compile_options(stdrive101_gate_waveform_neutral_wrapper_objects PRIVATE
    ${GATE_WAVEFORM_NEUTRAL_WRAPPER_COMPILE_OPTIONS}
)

add_executable(stdrive101_gate_waveform_neutral_wrapper_image
    ${GATE_WAVEFORM_NEUTRAL_WRAPPER_SOURCES}
    Src/minimal_runtime.c
    "${NUCLEO_BASELINE_DIR}/startup_stm32g474xx.s"
    "${NUCLEO_BASELINE_CORE_SRC_DIR}/system_stm32g4xx.c"
)

set_target_properties(stdrive101_gate_waveform_neutral_wrapper_image PROPERTIES
    OUTPUT_NAME stdrive101_gate_waveform_neutral_wrapper_image
    SUFFIX ".elf"
)

target_compile_definitions(stdrive101_gate_waveform_neutral_wrapper_image PRIVATE
    ${GATE_WAVEFORM_NEUTRAL_WRAPPER_DEFINITIONS}
)

target_include_directories(stdrive101_gate_waveform_neutral_wrapper_image PRIVATE
    ${GATE_WAVEFORM_NEUTRAL_WRAPPER_INCLUDE_DIRS}
)

target_compile_options(stdrive101_gate_waveform_neutral_wrapper_image PRIVATE
    ${GATE_WAVEFORM_NEUTRAL_WRAPPER_COMPILE_OPTIONS}
)

target_link_options(stdrive101_gate_waveform_neutral_wrapper_image PRIVATE
    -mcpu=cortex-m4
    -mthumb
    -T "${NUCLEO_BASELINE_LINKER_SCRIPT}"
    -nostdlib
    -Wl,-Map=$<TARGET_FILE_DIR:stdrive101_gate_waveform_neutral_wrapper_image>/stdrive101_gate_waveform_neutral_wrapper_image.map
    -Wl,--gc-sections
    -Wl,--print-memory-usage
)

target_link_libraries(stdrive101_gate_waveform_neutral_wrapper_image PRIVATE
    gcc
)
