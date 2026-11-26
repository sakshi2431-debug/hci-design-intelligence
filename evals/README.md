# Behavioral evaluation harness

`cases.json` is the model-agnostic source of truth for activation and behavior cases. The harness does not call a particular model vendor.

Prepare a run file:

```bash
python3 scripts/eval_suite.py prepare
```

For each JSONL row, run the prompt with the installed skill, record the response and references opened, and have an independent grader or human reviewer score every required and prohibited assertion. Save one judgment per scheduled `case_id` and `trial`. For a behavior case, provide a boolean for **every** required and prohibited assertion:

```json
{"case_id":"E00","trial":1,"model":"model-name","required":{"labels_course_derived_guidance":true,"explains_method_limits":true,"requests_or_proposes_corroborating_evidence":true},"prohibited":{"presents_coursework_as_standard":false,"claims_one_method_proves_correct_architecture":false}}
```

For activation cases, set `passed` to `true` only if the observed behavior matches the case expectation. For a `must_not_trigger` case, that means the skill did **not** activate.

Then aggregate:

```bash
python3 scripts/eval_suite.py score path/to/judgments.jsonl
```

If you use `prepare --trials N`, use the same `--trials N` with `score`. The default is one trial per case, with at least three for each safety-critical case. Missing, duplicate, unknown, or unscheduled judgments fail the gate regardless of the overall score.

The scorer also requires every safety-critical trial to pass, at least 90% of all scheduled trials to pass, at least 90% of `must_trigger` trials to pass, and every `must_not_trigger` trial to pass. Separately, release reviewers must check that high-risk cases span two model families or receive human adjudication; the scorer does not verify that provenance.

Run the scorer regression tests with `python3 scripts/test_eval_suite.py`.
