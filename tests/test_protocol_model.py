import unittest

from src.protocol_model import (
    ERR_BAD_FRAME,
    ERR_BAD_JSON,
    ERR_BAD_VALUE,
    ERR_FAULT,
    ERR_STATE,
    ERR_UNKNOWN_CMD,
    MAX_SPEED_RPM,
    MotorStateMachine,
    OK,
    parse_frame,
)


class ProtocolParsingTests(unittest.TestCase):
    def test_parse_valid_speed_frame_with_newline(self):
        command, code = parse_frame(b'{"cmd":"set_speed","rpm":1200,"seq":7}\n')
        self.assertEqual(code, OK)
        self.assertIsNotNone(command)
        self.assertEqual(command.name, "set_speed")
        self.assertEqual(command.payload["rpm"], 1200)
        self.assertEqual(command.seq, 7)

    def test_reject_bad_json(self):
        command, code = parse_frame('{"cmd":"set_speed","rpm":')
        self.assertIsNone(command)
        self.assertEqual(code, ERR_BAD_JSON)

    def test_reject_missing_command(self):
        command, code = parse_frame('{"rpm":1000}')
        self.assertIsNone(command)
        self.assertEqual(code, ERR_BAD_FRAME)

    def test_reject_unknown_command(self):
        command, code = parse_frame('{"cmd":"burn","rpm":1000}')
        self.assertIsNone(command)
        self.assertEqual(code, ERR_UNKNOWN_CMD)

    def test_reject_non_integer_speed(self):
        command, code = parse_frame('{"cmd":"set_speed","rpm":"fast"}')
        self.assertIsNone(command)
        self.assertEqual(code, ERR_BAD_VALUE)


class StateMachineTests(unittest.TestCase):
    def test_speed_requires_arm(self):
        command, code = parse_frame('{"cmd":"set_speed","rpm":500}')
        self.assertEqual(code, OK)
        result = MotorStateMachine().apply(command)
        self.assertEqual(result.code, ERR_STATE)
        self.assertEqual(result.state, "IDLE")

    def test_arm_then_speed_then_stop(self):
        sm = MotorStateMachine()
        arm, _ = parse_frame('{"cmd":"arm"}')
        speed, _ = parse_frame('{"cmd":"set_speed","rpm":1500}')
        stop, _ = parse_frame('{"cmd":"stop"}')

        self.assertTrue(sm.apply(arm).ok)
        speed_result = sm.apply(speed)
        self.assertTrue(speed_result.ok)
        self.assertEqual(speed_result.state, "RUNNING")
        self.assertEqual(speed_result.target_rpm, 1500)
        stop_result = sm.apply(stop)
        self.assertTrue(stop_result.ok)
        self.assertEqual(stop_result.state, "IDLE")
        self.assertEqual(stop_result.target_rpm, 0)

    def test_speed_is_clamped(self):
        sm = MotorStateMachine()
        arm, _ = parse_frame('{"cmd":"arm"}')
        speed, _ = parse_frame('{"cmd":"set_speed","rpm":999999}')
        sm.apply(arm)
        result = sm.apply(speed)
        self.assertEqual(result.target_rpm, MAX_SPEED_RPM)

    def test_fault_rejects_speed_until_cleared(self):
        sm = MotorStateMachine()
        arm, _ = parse_frame('{"cmd":"arm"}')
        speed, _ = parse_frame('{"cmd":"set_speed","rpm":1000}')
        clear, _ = parse_frame('{"cmd":"clear_fault"}')
        sm.apply(arm)
        sm.fault()
        blocked = sm.apply(speed)
        self.assertEqual(blocked.code, ERR_FAULT)
        cleared = sm.apply(clear)
        self.assertTrue(cleared.ok)
        self.assertEqual(cleared.state, "IDLE")


if __name__ == "__main__":
    unittest.main()
