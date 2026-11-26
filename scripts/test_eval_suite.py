"""Exercise the release gate through the public JSONL scoring command."""

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CASES = json.loads((ROOT / "evals" / "cases.json").read_text(encoding="utf-8"))[
    "cases"
]


def passing_rows(trials=1):
    return [
        {
            "case_id": case["id"],
            "trial": trial,
            "passed": True,
            "required": dict.fromkeys(case["required"], True),
            "prohibited": dict.fromkeys(case["prohibited"], False),
        }
        for case in CASES
        for trial in range(
            1, 1 + (max(3, trials) if case["risk"] == "safety-critical" else trials)
        )
    ]


class ReleaseGateTests(unittest.TestCase):
    def score(self, rows, trials=1):
        with tempfile.TemporaryDirectory() as directory:
            judgments = Path(directory) / "judgments.jsonl"
            judgments.write_text(
                "".join(json.dumps(row) + "\n" for row in rows), encoding="utf-8"
            )
            command = [sys.executable, str(ROOT / "scripts" / "eval_suite.py"), "score",
                       str(judgments)]
            if trials != 1:
                command.extend(["--trials", str(trials)])
            return subprocess.run(command, capture_output=True, text=True, check=False)

    def test_complete_passing_run_passes(self):
        result = self.score(passing_rows())
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_single_passing_case_cannot_pass(self):
        result = self.score(passing_rows()[:1])
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("missing judgment", result.stdout)

    def test_missing_entire_negative_case_cannot_pass(self):
        result = self.score([row for row in passing_rows() if row["case_id"] != "A90"])
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("A90 trial 1 missing judgment", result.stdout)

    def test_failed_negative_activation_cannot_pass(self):
        rows = passing_rows()
        for row in rows:
            if row["case_id"] == "A90":
                row["passed"] = False
        result = self.score(rows)
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("A90 trial 1 activation failed", result.stdout)

    def test_failed_positive_activation_below_floor_cannot_pass(self):
        rows = passing_rows()
        for row in rows:
            if row["case_id"] == "A01":
                row["passed"] = False
        result = self.score(rows)
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("Activation must_trigger: 2/3", result.stdout)

    def test_duplicate_trial_cannot_mask_missing_safety_critical_trial(self):
        rows = passing_rows()
        row = next(row for row in rows if row["case_id"] == "E04" and row["trial"] == 3)
        row["trial"] = 2
        result = self.score(rows)
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("E04 trial 2 duplicate judgment", result.stdout)
        self.assertIn("E04 trial 3 missing judgment", result.stdout)

    def test_custom_trial_count_requires_the_full_schedule(self):
        complete = self.score(passing_rows(2), trials=2)
        self.assertEqual(complete.returncode, 0, complete.stdout + complete.stderr)
        incomplete = self.score(passing_rows(), trials=2)
        self.assertEqual(incomplete.returncode, 1, incomplete.stdout + incomplete.stderr)
        self.assertIn("A90 trial 2 missing judgment", incomplete.stdout)


if __name__ == "__main__":
    unittest.main()
