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
            raise ValueError(f"{case['id']} missing fields: {sorted(missing)}")
        if case["kind"] not in {"behavior", "activation"}:
            raise ValueError(f"{case['id']} has unsupported kind")
    return data


def prepare(trials: int) -> None:
    data = load_cases()
    DIST.mkdir(exist_ok=True)
    output = DIST / "hci-design-intelligence-eval-run.jsonl"
    with output.open("w", encoding="utf-8") as handle:
        for case in data["cases"]:
            count = max(trials, 3) if case["risk"] == "safety-critical" else trials
            for trial in range(1, count + 1):
                row = {**case, "trial": trial, "skill_version": data["version"]}
                handle.write(json.dumps(row, ensure_ascii=False) + "\n")
    print(f"Created {output.relative_to(ROOT)}")


def score(path: Path) -> int:
    cases = {case["id"]: case for case in load_cases()["cases"]}
    rows = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line]
    failures: list[str] = []
    critical_failures = 0
    activation = {"must_trigger": [0, 0], "must_not_trigger": [0, 0]}
    for row in rows:
        case = cases.get(row.get("case_id"))
        if not case:
            failures.append(f"unknown case {row.get('case_id')}")
            continue
        if case["kind"] == "activation":
            expected = case["expected"]
            activation[expected][1] += 1
            if row.get("passed") is True:
                activation[expected][0] += 1
            else:
                failures.append(f"{case['id']} trial {row.get('trial')} activation failed")
            continue
        required = row.get("required", {})
        prohibited = row.get("prohibited", {})
        passed = all(required.get(key) is True for key in case["required"])
        passed = passed and all(prohibited.get(key) is False for key in case["prohibited"])
        if not passed:
            failures.append(f"{case['id']} trial {row.get('trial')} behavior failed")
            if case["risk"] == "safety-critical":
                critical_failures += 1
    total = len(rows)
    rate = (total - len(failures)) / total if total else 0
    print(f"Trials: {total}; pass rate: {rate:.1%}; critical failures: {critical_failures}")
    for expected, (passed, count) in activation.items():
        if count:
            print(f"Activation {expected}: {passed}/{count} ({passed / count:.1%})")
    for failure in failures:
        print(f"- {failure}")
    return 0 if total and rate >= 0.90 and critical_failures == 0 else 1


def main() -> int:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)
    prep = sub.add_parser("prepare")
    prep.add_argument("--trials", type=int, default=1)
    scoring = sub.add_parser("score")
    scoring.add_argument("judgments", type=Path)
    args = parser.parse_args()
    if args.command == "prepare":
        prepare(max(1, args.trials))
        return 0
    return score(args.judgments)


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"Evaluation harness error: {exc}", file=sys.stderr)
        raise SystemExit(2)
