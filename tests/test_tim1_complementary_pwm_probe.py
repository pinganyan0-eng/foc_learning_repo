import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = (
    ROOT
    / "apps"
    / "stm32_g474_foc"
    / "tim1_complementary_pwm_probe"
    / "Core"
    / "Src"
    / "main.c"
)


def macro_int(text: str, name: str) -> int:
    match = re.search(
        rf"^#define\s+{re.escape(name)}\s+(0x[0-9A-Fa-f]+|\d+)(?:U?L)?\s*$",
        text,
        re.MULTILINE,
    )
    if not match:
        raise AssertionError(f"Missing integer macro: {name}")
    return int(match.group(1), 0)


def deadtime_ticks(dtg: int) -> int:
    if dtg < 0x80:
        return dtg
    if dtg < 0xC0:
        return (64 + (dtg & 0x3F)) * 2
    if dtg < 0xE0:
        return (32 + (dtg & 0x1F)) * 8
    return (32 + (dtg & 0x1F)) * 16


class Tim1ComplementaryPwmProbeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text = SOURCE.read_text(encoding="utf-8")

    def test_logic_only_timing_contract(self):
        clock_hz = macro_int(self.text, "TIM1_INPUT_CLOCK_HZ")
        frequency_hz = macro_int(self.text, "PWM_TEST_FREQUENCY_HZ")
        duty_percent = macro_int(self.text, "PWM_TEST_DUTY_PERCENT")
        dtg = macro_int(self.text, "PWM_TEST_DEADTIME_DTG")

        period_counts = clock_hz // (2 * frequency_hz)
        self.assertEqual(period_counts, 8500)
        self.assertEqual((period_counts * duty_percent) // 100, 2125)
        self.assertEqual(deadtime_ticks(dtg), 336)
        self.assertAlmostEqual(deadtime_ticks(dtg) / clock_hz, 1.976e-6, places=9)

    def test_all_three_main_and_complementary_outputs_are_enabled(self):
        for token in (
            "TIM_CCER_CC1E",
            "TIM_CCER_CC1NE",
            "TIM_CCER_CC2E",
            "TIM_CCER_CC2NE",
            "TIM_CCER_CC3E",
            "TIM_CCER_CC3NE",
        ):
            self.assertIn(token, self.text)

        for token in (
            "TIM_CCER_CC1NP",
            "TIM_CCER_CC2NP",
            "TIM_CCER_CC3NP",
        ):
            self.assertNotIn(token, self.text)

    def test_exact_alternate_function_mapping_is_present(self):
        self.assertIn("PWM_OUTPUTS_PORT_A", self.text)
        self.assertIn("GPIO_PIN_7 | GPIO_PIN_8 | GPIO_PIN_9 | GPIO_PIN_10", self.text)
        self.assertIn("GPIO_InitStruct.Pin = GPIO_PIN_14;", self.text)
        self.assertIn("GPIO_InitStruct.Pin = GPIO_PIN_15;", self.text)
        self.assertIn("GPIO_InitStruct.Alternate = GPIO_AF4_TIM1;", self.text)
        self.assertGreaterEqual(self.text.count("GPIO_AF6_TIM1"), 3)

    def test_startup_and_break_do_not_auto_enable_outputs(self):
        self.assertNotIn("TIM_BDTR_AOE", self.text)
        self.assertEqual(self.text.count("TIM1->BDTR |= TIM_BDTR_MOE;"), 1)
        self.assertGreaterEqual(self.text.count("TIM1->BDTR &= ~TIM_BDTR_MOE;"), 2)
        self.assertIn("TIM_BDTR_BKE", self.text)
        self.assertIn("TIM1->AF1 = TIM1_AF1_BKINE;", self.text)
        self.assertIn("PWM_STATE_BREAK_LATCHED", self.text)
        self.assertIn("TIM1->DIER &= ~TIM_DIER_BIE;", self.text)
        self.assertIn("require a reset before another arm", self.text)

    def test_center_aligned_and_debug_freeze_are_enabled(self):
        self.assertIn("TIM_CR1_CMS_0", self.text)
        self.assertIn("TIM_CR1_CMS_1", self.text)
        self.assertIn("__HAL_DBGMCU_FREEZE_TIM1();", self.text)

    def test_button_held_during_reset_does_not_arm(self):
        self.assertIn("static uint8_t initialized = 0U;", self.text)
        self.assertIn("last_state = state;\n    initialized = 1U;\n    return;", self.text)


if __name__ == "__main__":
    unittest.main()
