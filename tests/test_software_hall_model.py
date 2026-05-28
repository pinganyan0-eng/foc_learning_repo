import unittest

from src.software_hall_model import (
    DECISION_ABNORMAL_JUMP,
    DECISION_BOUNCE_CANDIDATE,
    DECISION_FIRST_VALID,
    DECISION_FORWARD_STEP,
    DECISION_ILLEGAL_STATE,
    DECISION_REPEAT_STATE,
    DECISION_REVERSE_STEP,
    DIRECTION_FORWARD,
    DIRECTION_REVERSE,
    DIRECTION_UNKNOWN,
    SoftwareHallStateMachine,
    format_hall_state,
    is_forward_adjacent,
    is_reverse_adjacent,
    is_valid_state,
)


class SoftwareHallRuleTests(unittest.TestCase):
    def test_valid_states_exclude_000_and_111(self):
        for state in (0b001, 0b010, 0b011, 0b100, 0b101, 0b110):
            self.assertTrue(is_valid_state(state), format_hall_state(state))

        self.assertFalse(is_valid_state(0b000))
        self.assertFalse(is_valid_state(0b111))

    def test_candidate_adjacency_uses_locked_sequence(self):
        self.assertTrue(is_forward_adjacent(0b100, 0b110))
        self.assertTrue(is_reverse_adjacent(0b100, 0b101))
        self.assertFalse(is_forward_adjacent(0b100, 0b011))
        self.assertFalse(is_reverse_adjacent(0b100, 0b011))


class SoftwareHallStateMachineTests(unittest.TestCase):
    def test_first_valid_state_sets_baseline_without_counting_edge(self):
        hall = SoftwareHallStateMachine()

        decision = hall.process(0b100, timestamp_ticks=10)

        self.assertEqual(decision.decision, DECISION_FIRST_VALID)
        self.assertEqual(decision.accepted_state, 0b100)
        self.assertEqual(decision.direction_candidate, DIRECTION_UNKNOWN)
        self.assertFalse(decision.counted_edge)
        self.assertEqual(hall.edge_count, 0)

    def test_rejects_illegal_state_without_replacing_last_valid_state(self):
        hall = SoftwareHallStateMachine()
        hall.process(0b100, timestamp_ticks=10)

        decision = hall.process(0b000, timestamp_ticks=20)

        self.assertEqual(decision.decision, DECISION_ILLEGAL_STATE)
        self.assertTrue(decision.abnormal)
        self.assertFalse(decision.counted_edge)
        self.assertEqual(decision.accepted_state, 0b100)
        self.assertEqual(hall.illegal_state_count, 1)
        self.assertEqual(hall.last_accepted_state, 0b100)

    def test_repeated_state_does_not_count_edge(self):
        hall = SoftwareHallStateMachine()
        hall.process(0b100, timestamp_ticks=10)

        decision = hall.process(0b100, timestamp_ticks=20)

        self.assertEqual(decision.decision, DECISION_REPEAT_STATE)
        self.assertFalse(decision.counted_edge)
        self.assertFalse(decision.abnormal)
        self.assertEqual(hall.repeat_count, 1)
        self.assertEqual(hall.edge_count, 0)

    def test_forward_step_counts_edge_and_updates_direction(self):
        hall = SoftwareHallStateMachine()
        hall.process(0b100, timestamp_ticks=10)

        decision = hall.process(0b110, timestamp_ticks=30)

        self.assertEqual(decision.decision, DECISION_FORWARD_STEP)
        self.assertTrue(decision.counted_edge)
        self.assertFalse(decision.abnormal)
        self.assertEqual(decision.direction_candidate, DIRECTION_FORWARD)
        self.assertEqual(decision.dt_ticks, 20)
        self.assertEqual(hall.edge_count, 1)
        self.assertEqual(hall.last_accepted_state, 0b110)

    def test_reverse_step_counts_edge_and_updates_direction(self):
        hall = SoftwareHallStateMachine()
        hall.process(0b100, timestamp_ticks=10)

        decision = hall.process(0b101, timestamp_ticks=30)

        self.assertEqual(decision.decision, DECISION_REVERSE_STEP)
        self.assertTrue(decision.counted_edge)
        self.assertFalse(decision.abnormal)
        self.assertEqual(decision.direction_candidate, DIRECTION_REVERSE)
        self.assertEqual(hall.edge_count, 1)
        self.assertEqual(hall.last_accepted_state, 0b101)

    def test_legal_but_non_adjacent_state_is_abnormal_jump(self):
        hall = SoftwareHallStateMachine()
        hall.process(0b100, timestamp_ticks=10)

        decision = hall.process(0b011, timestamp_ticks=30)

        self.assertEqual(decision.decision, DECISION_ABNORMAL_JUMP)
        self.assertTrue(decision.abnormal)
        self.assertFalse(decision.counted_edge)
        self.assertEqual(hall.abnormal_jump_count, 1)
        self.assertEqual(hall.last_accepted_state, 0b100)

    def test_configurable_bounce_threshold_does_not_accept_fast_edge(self):
        hall = SoftwareHallStateMachine(min_edge_ticks=10)
        hall.process(0b100, timestamp_ticks=100)

        decision = hall.process(0b110, timestamp_ticks=105)

        self.assertEqual(decision.decision, DECISION_BOUNCE_CANDIDATE)
        self.assertEqual(decision.dt_ticks, 5)
        self.assertFalse(decision.counted_edge)
        self.assertFalse(decision.abnormal)
        self.assertEqual(hall.bounce_candidate_count, 1)
        self.assertEqual(hall.last_accepted_state, 0b100)

    def test_forward_sequence_counts_six_edges_around_cycle(self):
        hall = SoftwareHallStateMachine()
        sequence = (0b001, 0b101, 0b100, 0b110, 0b010, 0b011, 0b001)

        decisions = [
            hall.process(state, timestamp_ticks=index * 10)
            for index, state in enumerate(sequence)
        ]

        self.assertEqual(decisions[0].decision, DECISION_FIRST_VALID)
        self.assertTrue(all(decision.counted_edge for decision in decisions[1:]))
        self.assertEqual(hall.edge_count, 6)
        self.assertEqual(hall.direction_candidate, DIRECTION_FORWARD)
        self.assertEqual(hall.abnormal_jump_count, 0)


if __name__ == "__main__":
    unittest.main()
