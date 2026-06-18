# 2026-06-16 PA7/PA8 external voltage mismatch support packet

## 2026-06-17 resolution update

The apparent mismatch is now resolved as a measurement-state/contact/path issue,
not as evidence of a failed NUCLEO-G474RE board or failed PA7/PA8 GPIO pins.

After reflashing the bare-register GPIO diagnostic and rechecking the physical
CN10 points, the user reported:

```text
CN10-11 / PA5: 3.3 V
CN10-15 / PA7: 3.3 V
CN10-23 / PA8: 3.3 V
```

Therefore:

- `PA7 / CN10-15 / D11` is usable at the connector level.
- `PA8 / CN10-23 / D7` is usable at the connector level.
- The earlier `0 V` readings on PA7/PA8 are not accepted as hardware-failure
  evidence.
- This diagnostic still does not approve power-board connection, 24 V, Gate
  probing, or motor operation.

The temporary `pa7_gpio_probe` firmware has served its diagnostic purpose. The
next firmware step is to restore the NUCLEO-only TIM1 complementary PWM probe
before any PWM waveform retest.

## Summary

This packet documents an unresolved NUCLEO-G474RE-only diagnostic issue.

The temporary GPIO diagnostic firmware configures `PA5`, `PA7`, and `PA8` as
push-pull GPIO outputs and writes all three pins high. ST-LINK register reads
show `GPIOA_ODR` and `GPIOA_IDR` both reporting `PA5/PA7/PA8` high. However,
external DMM measurements on the board report:

- `CN10-11 / PA5`: about `3.3 V`
- `CN10-15 / PA7`: `0 V`
- `CN10-23 / PA8`: `0 V`
- `D11 / PA7`: `0 V`
- `D7 / PA8`: `0 V`

The unresolved contradiction is: the MCU register view reports `PA7` and `PA8`
high, but the physical connector measurements report `0 V`.

## Safety boundary

Current bench scope:

- Only NUCLEO-G474RE USB power through ST-LINK.
- No power board connection.
- No CN3/CN8 cable during this diagnostic unless explicitly stated otherwise.
- No 24 V.
- No motor.
- No phase wires.
- No Gate, OUTx, BOOTx, high-side Vgs, Motor Pilot, or Motor Profiler test.

This issue is not evidence of power-board, Gate, motor, MCSDK, Hall closed-loop,
or FOC behavior.

## Hardware and tool context

- Board detected by STM32CubeProgrammer: `NUCLEO-G474RE`
- Device: `STM32G47x/G48x/G414`
- ST-LINK SN: `002F00253235511337333439`
- ST-LINK firmware: `V3J17M10`
- Reported target voltage during ST-LINK connection: `3.28 V`
- Programmer: `STM32CubeProgrammer v2.22.0`
- DMM: user handheld multimeter, DC voltage and continuity modes

## Official pin mapping used

From `UM2505`, local extracted manual:

Arduino connector mapping:

```text
CN5 pin 4  PWM/MOSI/D11  ARD_D11  PA7  TIM3_CH2 / SPI1_MOSI
CN9 pin 8  D7            ARD_D7   PA8  I/O
```

Morpho connector mapping:

```text
CN10-11  PA5
CN10-15  PA7
CN10-23  PA8
```

Therefore:

```text
D11 == PA7 == CN10-15
D7  == PA8 == CN10-23
D13 == PA5 == CN10-11
```

## Relevant firmware

Project:

```text
apps/stm32_g474_foc/pa7_gpio_probe/
```

This firmware is a temporary NUCLEO-only diagnostic. It is not TIM1 PWM.

Current `Core/Src/main.c` core logic:

```c
#include "stm32g474xx.h"

#define PA5_STATUS_LED_BIT      (1UL << 5)
#define PA7_TEST_BIT            (1UL << 7)
#define PA8_CONTROL_BIT         (1UL << 8)
#define GPIOA_PROBE_BITS        (PA5_STATUS_LED_BIT | PA7_TEST_BIT | PA8_CONTROL_BIT)

int main(void)
{
  RCC->AHB2ENR |= RCC_AHB2ENR_GPIOAEN;
  __DSB();

  GPIOA->MODER &= ~((3UL << (5U * 2U)) |
                    (3UL << (7U * 2U)) |
                    (3UL << (8U * 2U)));
  GPIOA->MODER |=  ((1UL << (5U * 2U)) |
                    (1UL << (7U * 2U)) |
                    (1UL << (8U * 2U)));

  GPIOA->OTYPER &= ~GPIOA_PROBE_BITS;
  GPIOA->PUPDR &= ~((3UL << (5U * 2U)) |
                    (3UL << (7U * 2U)) |
                    (3UL << (8U * 2U)));
  GPIOA->OSPEEDR &= ~((3UL << (5U * 2U)) |
                      (3UL << (7U * 2U)) |
                      (3UL << (8U * 2U)));

  GPIOA->BSRR = GPIOA_PROBE_BITS;

  while (1)
  {
    __NOP();
  }
}
```

Intent:

- Enable `GPIOA` peripheral clock.
- Configure `PA5`, `PA7`, and `PA8` as general-purpose output.
- Configure push-pull, no pull-up/down, low speed.
- Write `PA5`, `PA7`, and `PA8` high.

## Build and flash evidence

Build command:

```powershell
cmake --build --preset Debug --target pa7_gpio_probe
```

Build result:

```text
[100%] Built target pa7_gpio_probe
FLASH: 896 B / 512 KB
```

Flash command:

```powershell
& 'F:\STMCubePROG\bin\STM32_Programmer_CLI.exe' `
  -c port=SWD mode=UR `
  -d 'C:\Users\gregrg\Documents\Codex\2026-04-30\qiansai\foc_learning_repo_master_sync\apps\stm32_g474_foc\pa7_gpio_probe\build\Debug-mingw\pa7_gpio_probe.hex' `
  0x08000000 -v -rst
```

Flash result:

```text
File          : pa7_gpio_probe.hex
Size          : 896.00 B
Address       : 0x08000000
Download verified successfully
MCU Reset
Software reset is performed
```

## ST-LINK register read evidence

Command:

```powershell
& 'F:\STMCubePROG\bin\STM32_Programmer_CLI.exe' `
  -c port=SWD mode=HOTPLUG `
  -r32 0x48000000 24
```

Raw output:

```text
Reading 32-bit memory content
  Size          : 24 Bytes
  Address:      : 0x48000000
0x48000000 : ABFD77FF 00000000 0C000000 64000000
0x48000010 : 0000C1A0 000001A0
```

Decode:

```text
GPIOA base      = 0x48000000
GPIOA_MODER     = 0xABFD77FF
GPIOA_OTYPER    = 0x00000000
GPIOA_OSPEEDR   = 0x0C000000
GPIOA_PUPDR     = 0x64000000
GPIOA_IDR       = 0x0000C1A0
GPIOA_ODR       = 0x000001A0
```

`GPIOA_ODR = 0x000001A0` means these output bits are high:

```text
PA5 = 1
PA7 = 1
PA8 = 1
```

`GPIOA_IDR = 0x0000C1A0` also includes these input-readback bits high:

```text
PA5 = 1
PA7 = 1
PA8 = 1
```

Core status was also checked after flashing:

```text
Core is running
```

## External DMM observations

The user reported these measurements with black probe fixed to NUCLEO GND:

```text
3V3: 3.3 V
PA5 / D13: 3.3 V
CN10-11 / PA5: 3.3 V
CN10-15 / PA7: 0 V
CN10-23 / PA8: 0 V
D11 / PA7: 0 V
D7 / PA8: 0 V
LD2: on
```

Continuity checks previously reported by the user:

```text
D11 point to CN10-15 / PA7: beeps
D7 point to CN10-23 / PA8: beeps
```

Additional resistance readings during earlier PA7 diagnosis:

```text
PA7/D11 to GND: about 2.5 Mohm
PA7/D11 to 3V3: about 44 kohm
```

These readings do not indicate a hard short to ground.

## Expected behavior

With the current bare-register diagnostic firmware:

```text
PA5 / D13 / CN10-11  ~= 3.3 V
PA7 / D11 / CN10-15  ~= 3.3 V
PA8 / D7  / CN10-23  ~= 3.3 V
LD2                  on
```

## Actual behavior

Observed externally:

```text
PA5 / D13 / CN10-11  ~= 3.3 V
PA7 / D11 / CN10-15  = 0 V
PA8 / D7  / CN10-23  = 0 V
LD2                  on
```

Observed through ST-LINK register read:

```text
GPIOA_ODR reports PA5, PA7, and PA8 high.
GPIOA_IDR reports PA5, PA7, and PA8 high.
```

## Why this is unresolved

The external DMM result and MCU register result contradict each other:

- If `GPIOA_ODR` and `GPIOA_IDR` are both high for `PA7/PA8`, the physical pins
  should normally measure near `3.3 V` relative to board GND.
- The same measurement setup can measure `PA5/CN10-11` at `3.3 V`, so the DMM,
  board power, and at least one CN10 reference point are functioning.
- User reports continuity from `D11` to `CN10-15` and from `D7` to `CN10-23`,
  so the named test points appear connected.

## Reproduction steps

1. Disconnect power board, CN3/CN8 cable, 24 V, motor, and phase wires.
2. Connect only the NUCLEO-G474RE ST-LINK USB.
3. Build `apps/stm32_g474_foc/pa7_gpio_probe`.
4. Flash `pa7_gpio_probe.hex` with STM32CubeProgrammer CLI.
5. Confirm ST-LINK reports the board as `NUCLEO-G474RE` and target voltage near
   `3.28 V`.
6. Read GPIOA registers:

   ```powershell
   & 'F:\STMCubePROG\bin\STM32_Programmer_CLI.exe' `
     -c port=SWD mode=HOTPLUG `
     -r32 0x48000000 24
   ```

7. Measure external connector voltages with DMM:

   ```text
   Black probe: NUCLEO GND
   Red probe:  CN10-11 / PA5
   Red probe:  CN10-15 / PA7
   Red probe:  CN10-23 / PA8
   Red probe:  Arduino D13 / PA5
   Red probe:  Arduino D11 / PA7
   Red probe:  Arduino D7  / PA8
   ```

## Questions for support

1. Can `GPIOA_IDR` read high for `PA7/PA8` while the corresponding external
   connector points `CN10-15/CN10-23` measure `0 V`?
2. Is there any NUCLEO-G474RE solder bridge, jumper, board revision issue, or
   alternate routing that can disconnect `PA7/PA8` from `CN10-15/CN10-23` while
   leaving `PA5/CN10-11` normal?
3. Is the `STM32_Programmer_CLI -r32 0x48000000 24` read possibly returning a
   stale or debug-side view rather than the live GPIO peripheral state?
4. Could DMM measurement on these pins be affected by ST-LINK hotplug/debug
   state, reset state, boot state, or a hidden external load?
5. What independent check is recommended next: oscilloscope probe on the MCU
   package pin, direct register write through ST-LINK, full board reset/power
   cycle, or testing a second NUCLEO-G474RE board?

## Current recommended next checks

No power-board action should proceed until this contradiction is explained.

Suggested next diagnostic steps:

1. Fully power-cycle the NUCLEO by unplugging USB for at least 10 seconds, then
   replug and measure `PA5/PA7/PA8` before opening any debug connection.
2. Use STM32CubeProgrammer to write `GPIOA_BSRR` directly while connected, then
   measure immediately:

   ```text
   GPIOA_BSRR address = 0x48000018
   Set PA5/PA7/PA8   = 0x000001A0
   ```

3. If available, use an oscilloscope or logic probe on `CN10-11`, `CN10-15`,
   and `CN10-23` relative to the same NUCLEO GND.
4. If available, repeat the same firmware and DMM measurements on a second
   NUCLEO-G474RE.
5. Inspect the NUCLEO underside for solder-bridge modifications or visible
   damage around the Arduino/Morpho connector area.
