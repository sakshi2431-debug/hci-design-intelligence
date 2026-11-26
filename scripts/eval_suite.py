#!/usr/bin/env python3
"""Prepare and aggregate vendor-neutral behavioral evaluation runs."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CASES = ROOT / "evals" / "cases.json"
DIST = ROOT / "dist"


def load_cases() -> dict:
    data = json.loads(CASES.read_text(encoding="utf-8"))
    ids = [case["id"] for case in data["cases"]]
    if len(ids) != len(set(ids)):
        raise ValueError("evaluation case IDs must be unique")
    required = {"id", "kind", "risk", "prompt", "required", "prohibited"}
    for case in data["cases"]:
        missing = required - case.keys()
        if missing:
            raise ValueError(f"{case.get('id', 'unknown')} missing fields: {sorted(missing)}")
        if case["kind"] not in {"behavior", "activation"}:
            raise ValueError(f"{case['id']} has unsupported kind")
        if case["kind"] == "activation" and case.get("expected") not in {
            "must_trigger", "must_not_trigger"
        }:
            raise ValueError(f"{case['id']} has unsupported activation expectation")
    return data


def trial_numbers(case: dict, trials: int) -> range:
    count = max(trials, 3) if case["risk"] == "safety-critical" else trials
    return range(1, count + 1)


def prepare(trials: int) -> None:
    data = load_cases()
    DIST.mkdir(exist_ok=True)
    output = DIST / "hci-design-intelligence-eval-run.jsonl"
    with output.open("w", encoding="utf-8") as handle:
        for case in data["cases"]:
            for trial in trial_numbers(case, trials):
                row = {**case, "trial": trial, "skill_version": data["version"]}
                handle.write(json.dumps(row, ensure_ascii=False) + "\n")
    print(f"Created {output.relative_to(ROOT)}")


def score(path: Path, trials: int = 1) -> int:
    cases = {case["id"]: case for case in load_cases()["cases"]}
    scheduled = {
        (case_id, trial): case
        for case_id, case in cases.items()
        for trial in trial_numbers(case, trials)
    }
    judgments: dict[tuple[str, int], dict] = {}
    failures: list[str] = []
    invalid = False
    with path.open(encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            if not line.strip():
                continue
            row = json.loads(line)
            if not isinstance(row, dict):
                failures.append(f"line {line_number} judgment must be an object")
                invalid = True
                continue
            case_id, trial = row.get("case_id"), row.get("trial")
            if not isinstance(case_id, str) or case_id not in cases:
                failures.append(f"line {line_number} unknown case {case_id!r}")
                invalid = True
                continue
            key = (case_id, trial)
            if type(trial) is not int or key not in scheduled:
                failures.append(f"{case_id} trial {trial!r} not scheduled")
                invalid = True
                continue
            if key in judgments:
                failures.append(f"{case_id} trial {trial} duplicate judgment")
                invalid = True
                continue
            judgments[key] = row

    critical_failures = 0
    passed_trials = 0
    activation = {"must_trigger": [0, 0], "must_not_trigger": [0, 0]}
    for (case_id, trial), case in scheduled.items():
        row = judgments.get((case_id, trial))
        expected = case["expected"] if case["kind"] == "activation" else None
        if expected is not None:
            activation[expected][1] += 1
        if row is None:
            passed = False
            failures.append(f"{case_id} trial {trial} missing judgment")
        elif expected is not None:
            passed = row.get("passed") is True
            if passed:
                activation[expected][0] += 1
            else:
                failures.append(f"{case_id} trial {trial} activation failed")
        else:
            required, prohibited = row.get("required", {}), row.get("prohibited", {})
            passed = (
                isinstance(required, dict) and isinstance(prohibited, dict)
                and all(required.get(key) is True for key in case["required"])
                and all(prohibited.get(key) is False for key in case["prohibited"])
            )
            if not passed:
                failures.append(f"{case_id} trial {trial} behavior failed")
        if passed:
            passed_trials += 1
        elif case["risk"] == "safety-critical":
            critical_failures += 1

    total = len(scheduled)
    rate = passed_trials / total if total else 0
    print(f"Trials: {total}; pass rate: {rate:.1%}; critical failures: {critical_failures}")
    for expected, (passed, count) in activation.items():
        if count:
            print(f"Activation {expected}: {passed}/{count} ({passed / count:.1%})")
    for failure in failures:
        print(f"- {failure}")
    positive_passed, positive_count = activation["must_trigger"]
    negative_passed, negative_count = activation["must_not_trigger"]
    passed_release = (
        total > 0 and len(judgments) == total and not invalid
        and rate >= 0.90 and critical_failures == 0
        and positive_passed >= 0.90 * positive_count
        and negative_passed == negative_count
    )
    return 0 if passed_release else 1


def positive_trials(value: str) -> int:
    count = int(value)
    if count < 1:
        raise argparse.ArgumentTypeError("trials must be at least 1")
    return count


def main() -> int:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)
    prep = sub.add_parser("prepare")
    prep.add_argument("--trials", type=positive_trials, default=1)
    scoring = sub.add_parser("score")
    scoring.add_argument("judgments", type=Path)
    scoring.add_argument("--trials", type=positive_trials, default=1)
    args = parser.parse_args()
    if args.command == "prepare":
        prepare(args.trials)
        return 0
    return score(args.judgments, args.trials)


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"Evaluation harness error: {exc}", file=sys.stderr)
        raise SystemExit(2)
