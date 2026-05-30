import json
import unittest
from pathlib import Path

from src.software_hall_model import SoftwareHallStateMachine, format_hall_state


ROOT = Path(__file__).resolve().parents[1]
VECTOR_PATH = ROOT / "tests" / "fixtures" / "software_hall_golden_vectors.json"


def _state_from_text(value):
    if value is None:
        return None
    return int(value, 2)


class SoftwareHallGoldenVectorTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.vectors = json.loads(VECTOR_PATH.read_text(encoding="utf-8"))

    def test_metadata_keeps_no_power_boundary(self):
        metadata = self.vectors["metadata"]

        self.assertEqual(
            metadata["decision"],
            "Host-side software Hall golden vectors / no firmware implementation / no MCSDK Hall integration / no Hall readiness",
        )
        self.assertEqual(
            metadata["route"],
            "HALL_A/B/C -> IA/IB/IC -> PA0/PA1/PB4",
        )
        self.assertIn("PB3=LIN1", metadata["pin_constraint"])
        self.assertIn("firmware implementation", metadata["not_evidence_for"])
        self.assertIn("MCSDK Hall integration", metadata["not_evidence_for"])
        self.assertIn("Gate PWM safety", metadata["not_evidence_for"])

    def test_vectors_replay_against_reference_model(self):
        for case in self.vectors["cases"]:
            with self.subTest(case=case["name"]):
                hall = SoftwareHallStateMachine(
                    min_edge_ticks=case["min_edge_ticks"]
                )

                for sample in case["samples"]:
                    with self.subTest(case=case["name"], sample=sample["raw"]):
                        decision = hall.process(
                            _state_from_text(sample["raw"]),
                            timestamp_ticks=sample["ticks"],
                        )

                        self.assertEqual(decision.decision, sample["decision"])
                        self.assertEqual(
                            format_hall_state(decision.accepted_state),
                            sample["accepted"] or "---",
                        )
                        self.assertEqual(
                            format_hall_state(decision.previous_state),
                            sample["previous"] or "---",
                        )
                        self.assertEqual(
                            decision.direction_candidate, sample["direction"]
                        )
                        self.assertEqual(
                            decision.counted_edge, sample["counted_edge"]
                        )
                        self.assertEqual(decision.abnormal, sample["abnormal"])

                        if "dt_ticks" in sample:
                            self.assertEqual(decision.dt_ticks, sample["dt_ticks"])

                        for counter_name in (
                            "edge_count",
                            "illegal_state_count",
                            "repeat_count",
                            "bounce_candidate_count",
                            "abnormal_jump_count",
                        ):
                            if counter_name in sample:
                                self.assertEqual(
                                    getattr(hall, counter_name),
                                    sample[counter_name],
                                    counter_name,
                                )


if __name__ == "__main__":
    unittest.main()
