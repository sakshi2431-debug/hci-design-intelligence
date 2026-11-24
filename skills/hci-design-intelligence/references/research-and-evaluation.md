# Research and evaluation

For consequential, academic, causal, survey, or population-level claims, apply the additional validity, sampling, analysis, ethics, and reporting controls in [research-rigor.md](research-rigor.md).

## Select methods from decisions

| Decision need | Useful methods | Main limitation |
|---|---|---|
| Discover needs and context | contextual inquiry, observation, interviews, diary study | self-report and observer effects; limited prevalence claims |
| Organize information | open/closed card sorting, tree testing, search-log analysis | categories do not alone define task flows or labels |
| Find interaction problems | moderated/unmoderated usability testing, cognitive walkthrough, heuristic evaluation | inspection is not user evidence; small tests do not estimate prevalence |
| Measure perceived usability | SUS or task-specific satisfaction measures | a score does not explain causes |
| Measure task performance | success, time, errors, assists, abandonment | operational definitions and task realism determine validity |
| Understand visual attention | eye tracking, gaze replay, fixation/AOI measures | gaze is not thought; calibration and sample choices matter |
| Understand live behavior | analytics, funnels, path analysis, search logs | usually explains what, not why; instrumentation and selection bias matter |
| Compare variants causally | randomized A/B or multivariate tests | requires adequate traffic, stable assignment, correct metrics, and guardrails |
| Evaluate accessibility | standards review, keyboard/screen-reader/manual testing, disabled-participant research | automated scans cover only a subset and cannot prove conformance |

## Research plan

Include:

1. Decision and stakeholder context.
2. Objectives and research questions.
3. Hypotheses only when a testable prediction serves the study.
4. Method rationale and triangulation plan.
5. Participant criteria, exclusions, sample rationale, recruitment, compensation.
6. Tasks/scenarios, data collection, measures, instrumentation.
7. Consent, privacy, recording, retention, and accessibility.
8. Analysis plan, quality checks, and stopping rule.
9. Risks, limitations, dependencies, and communication cadence.

Do not confuse objectives, questions, hypotheses, tasks, and metrics.

## Moderated usability testing

- Make the participant comfortable and clarify that the design—not the participant—is being tested.
- Use realistic scenarios without embedding the answer.
- Remain a neutral observer; avoid praise, defense, leading prompts, and premature rescue.
- Use think-aloud when its reactivity is acceptable. Consider retrospective or gaze-cued review when concurrent verbalization would distort eye-tracking behavior.
- Record observable behavior separately from interpretation.
- Define success, error, assist, abandonment, and severity before analysis.
- Debrief, invite participant explanation, and protect sensitive data.

Prioritize findings by evidence strength, task criticality, frequency/reach, user harm, persistence, and recovery cost. Do not convert a few observations into percentages.

For inspection workflows, remote testing, and reporting, define the decision, participant context, task evidence, limitations, and criteria for action explicitly rather than relying on a template alone.

## Quantitative UX metrics

Operationalize measures before collection:

- completion/success rate;
- time on task;
- error, assist, backtrack, or abandonment counts;
- conversion or funnel progression;
- perceived ease, confidence, satisfaction, or SUS;
- eye-tracking measures such as time to first fixation, fixation duration/count, and AOI transitions.

Report denominator, missing data, uncertainty, sample definition, and practical significance. A metric becomes meaningful only through a decision threshold or comparison.

## Eye tracking

Use eye tracking for questions about visual attention and scan behavior. Plan calibration, device/context, stimulus fidelity, areas of interest, tasks, and participant inclusion. Inspect gaze replays for qualitative mechanisms; use heatmaps and gaze plots carefully; calculate metrics only when the design and sample support aggregation. Avoid the eye-mind fallacy: fixation does not prove comprehension, preference, or intent.

Course-derived emphasis: fixations are pauses, saccades are rapid movements between them; gaze replay, gaze plots, heatmaps, and AOI metrics answer different questions. See [coursework-advanced-usability.md](coursework-advanced-usability.md).

## Analytics and experiments

Use analytics to define paths, segments, scale, and drop-off, then pair it with qualitative work for mechanisms. Validate instrumentation and avoid treating absence of an event as user intent.

For A/B tests:

1. Define a falsifiable hypothesis grounded in prior evidence.
2. Specify control, treatment, assignment unit, population, duration, primary metric, guardrails, and stopping rule.
3. Avoid changing multiple uncontrolled elements if attribution matters.
4. Check novelty, seasonality, sample ratio mismatch, interference, and multiple-comparison risk.
5. Report uncertainty and practical impact, not only statistical significance.

Multivariate tests isolate combinations of selected variables but require substantially more traffic. This limitation is also reflected in [coursework-advanced-usability.md](coursework-advanced-usability.md).

## Synthesis and storytelling

Triangulate sources, preserve contradictions, distinguish observations from themes, and connect findings to decisions. A strong story has audience, context, tension/problem, evidence, consequence, and action; it does not hide uncertainty. Tailor detail to stakeholder authority and needs. Show quick wins without suppressing structural problems.
