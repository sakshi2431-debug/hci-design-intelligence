# AI-agent evaluation

Use this reference when defining, prototyping, comparing, releasing, or monitoring an AI agent or multi-turn AI workflow. It turns product requirements, PAIR findings, HAX risks, and observed failures into evaluation tasks and release evidence.

## Provenance and role

Primary applied source: `ENGINEERING/PRACTITIONER` — Anthropic, [Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents), published 2026-01-09 and accessed 2026-08-31. This file is an original HCI-oriented synthesis; it does not reproduce the article.

Anthropic's guidance reflects experience building and supporting agent systems. Treat it as strong applied engineering guidance, not a normative standard or proof that an evaluation transfers unchanged to another domain. Combine automated evaluation with user research, production monitoring, accessibility evaluation, manual trace review, and domain expertise.

## Define the evaluation object

Do not evaluate “the model” as if it were the whole product. An agent's behavior arises from the model plus its scaffold: instructions, tools, retrieval, memory, permissions, environment, UI, and control policy.

Use these terms consistently:

- **Task:** one test case with inputs, environment, and success criteria.
- **Trial:** one attempt at a task. Run multiple trials when behavior is stochastic.
- **Grader:** logic or judgment scoring one dimension; it may contain several assertions.
- **Trace/transcript:** the complete interaction record, including messages, tool calls, intermediate states, and results.
- **Outcome:** the final state that matters. Prefer verifying it over trusting the agent's claim.
- **Agent harness/scaffold:** the system that lets the model act.
- **Eval harness:** infrastructure that executes isolated trials, records traces, grades results, and aggregates evidence.
- **Suite:** a maintained collection of tasks measuring named capabilities or behaviors.

## Start from the human and product contract

Before writing tasks, specify:

1. people, goals, contexts, accessibility needs, and affected non-users;
2. the end-to-end outcome the agent must produce or preserve;
3. what remains the person's responsibility and what the agent may do;
4. important errors, hidden failures, reliance risks, and recovery expectations;
5. product constraints such as latency, cost, privacy, security, and operational load;
6. evidence required to release, expand autonomy, change a model, or roll back.

PAIR supplies the product fit, data, mental-model, reliance, control, and failure questions. HAX supplies lifecycle interaction requirements. Convert each material requirement or failure into one or more observable eval assertions.

## Build two complementary suites

- **Capability/quality suite:** asks what the agent can do well. Include difficult, valuable tasks with room for improvement. Low initial pass rates can be useful if tasks are valid and solvable.
- **Regression suite:** protects behavior already expected to work. It should be stable and approach consistent passing. Promote mature capability tasks into regression coverage.

Averages can hide severe failures. Report task-level results, distributions across trials, important user segments and contexts, failure clusters, and uncertainty. Include cases where a behavior should occur and matched cases where it should not, so optimization does not create over-triggering.

## Design useful tasks

Source tasks from real workflows, manual checks, prototypes, support incidents, user research, HAX failure scenarios, AI product discovery lenses, accessibility barriers, and production traces that can be used lawfully and safely.

For every task define:

- user situation, goal, starting state, and relevant constraints;
- tools, permissions, data, and environment;
- observable outcome and unacceptable side effects;
- task-completion, interaction-quality, accessibility, reliance, and recovery criteria as relevant;
- reference solution or known-valid path proving the task and graders are workable;
- variation dimensions and number of trials;
- privacy, safety, and data-handling requirements.

Two qualified reviewers should be able to understand the task and reach a compatible judgment. A persistent zero score can indicate a broken task, grader, or harness rather than an incapable agent. Do not hide required paths or assumptions from the agent while grading against them.

## Choose graders by claim

Combine only the graders that change a decision:

- **Deterministic/code-based:** state checks, unit tests, schema validation, static analysis, required or forbidden effects, tool parameters, latency, tokens, and cost. Fast and reproducible, but potentially brittle.
- **Model-based:** structured rubrics, assertions, pairwise comparisons, reference comparisons, groundedness, coverage, coherence, and interaction quality. Useful for open-ended work, but stochastic and dependent on calibration.
- **Human/domain expert:** subjective quality, high-stakes correctness, cultural or contextual judgment, product taste, and calibration of model graders. High-quality but slower and more expensive.
- **User evidence:** task success, comprehension, appropriate reliance, accessibility, recovery, satisfaction with consequences, and downstream outcomes. Essential when the claim concerns people rather than output form alone.

Prefer deterministic verification for objective outcomes and model graders only where nuance requires them. Calibrate model graders against independent human judgment. Give graders an “insufficient information” route. Grade separate dimensions separately when a single holistic score would hide disagreement.

Grade outcomes more heavily than a prescribed path. Verify tool use or sequence only when the path itself is a safety, rights, compliance, or process requirement. Allow legitimate alternative solutions and partial credit where partial completion has meaningful value.

## Evaluate the complete experience

An agent can reach the correct backend state while providing a poor or harmful experience. When relevant, evaluate:

- comprehension of capability, limitations, data use, and responsibility;
- appropriate reliance rather than maximum trust;
- invocation, interruption, dismissal, correction, undo, and escalation;
- preservation of user work and recovery from partial failure;
- accessible dynamic updates, focus, alternatives, and cognitive load;
- tone, social expectations, and personality without false certainty or intimacy;
- unequal error patterns and consequences across groups or contexts;
- end-to-end completion rather than an attractive intermediate response.

When the strategy, adaptation, or multi-agent dynamics matter, also apply [learning-skill-and-behavioral-assessment.md](learning-skill-and-behavioral-assessment.md): observe action sequences, perturb controlled variables, construct environments that distinguish competing strategies, and interpret behavior without claiming hidden beliefs or motives. Pair these process tests with verified outcomes.

For a conversational agent, pair outcome/state verification with a rubric for interaction quality and realistic multi-turn user behavior. For a research agent, evaluate claim support, coverage, source authority, freshness, and synthesis. For a computer-use agent, verify application or backend state and detect unintended side effects. For any consequential action, test permissions, preview, confirmation, cancellation, and rollback.

## Control noise and non-determinism

- Run repeated trials and report success frequency rather than treating one run as representative.
- Start each trial from a clean, stable, production-representative environment.
- Prevent shared state, cached artifacts, resource limits, or prior trial history from contaminating results.
- Separate agent failure from environment, task, grader, and harness failure.
- Track model, prompt, retrieval, tool, policy, and dataset versions.
- Read representative passing and failing traces; scores alone cannot show whether grading is fair.
- Inspect whether the agent can exploit the task or grader without solving the intended problem.

## Eval-driven product development

1. Convert intended capabilities and important failures into tasks before implementation when possible.
2. Establish a baseline across repeated trials.
3. Read traces and revise ambiguous tasks or invalid graders.
4. Improve the product, scaffold, prompts, tools, data, or interaction.
5. Run capability and regression suites together.
6. Pair automated results with dogfooding, user research, accessibility testing, production monitoring, A/B tests, feedback, and periodic expert review.
7. Define release thresholds, guardrails, owners, rollback criteria, and recheck triggers.
8. Add real failures to the suite and refresh saturated or outdated capability tasks.

Treat the suite as a living product artifact with ownership. Re-run it after meaningful changes to the model, system prompt, retrieval sources, tools, autonomy, interface, user group, task, data, or policy.

## Interactive questions

During ideation, ask only the question that unlocks the current decision. Useful prompts include:

- What observable end state would prove that the agent completed the person's goal rather than merely claimed success?
- What difficult or harmful failure should become a task before this feature is built?
- Where may two valid solutions differ, and how should the grader avoid penalizing creativity?
- Which dimension requires a human or domain expert because code or a model judge cannot establish it?
- What matched negative case tests that the agent does **not** act when it should not?
- What change would trigger re-running this suite or block release?

## Eval-plan output

Produce a compact decision artifact containing:

1. capability and user-outcome contract;
2. evaluation scope, versions, and environment;
3. capability and regression suites;
4. task schema and representative cases;
5. graders, assertions, calibration, and partial-credit logic;
6. trials, aggregation, segments, and uncertainty;
7. human, accessibility, production, and monitoring layers;
8. release gates, owners, rollback, and maintenance plan;
9. known blind spots and residual risk.
