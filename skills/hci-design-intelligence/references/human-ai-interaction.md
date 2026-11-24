# Human–AI interaction

Use this reference for AI-assisted, predictive, conversational, generative, autonomous, or agentic product behavior. AI interaction is probabilistic system design, not ordinary content decoration.

## Source anchors

- `ACADEMIC/APPLIED` — [Microsoft HAX Guidelines for Human–AI Interaction](https://www.microsoft.com/en-us/haxtoolkit/ai-guidelines/) and the [CHI 2019 research paper](https://www.microsoft.com/en-us/research/publication/guidelines-for-human-ai-interaction/).
- `APPLIED` — [Microsoft HAX Toolkit](https://www.microsoft.com/en-us/haxtoolkit/), including its design library and failure-oriented playbook. For full coverage, route to [hax-guidelines.md](hax-guidelines.md), [hax-design-patterns.md](hax-design-patterns.md), [hax-planning-workbook.md](hax-planning-workbook.md), or [hax-playbook-failures.md](hax-playbook-failures.md).
- `APPLIED` — [Google People + AI Guidebook](https://pair.withgoogle.com/guidebook-v2/) (PAIR), an influence and recommended reading. This skill's own discovery guidance is in [ai-product-discovery.md](ai-product-discovery.md), [ai-product-workshop-templates.md](ai-product-workshop-templates.md), [ai-interaction-pattern-index.md](ai-interaction-pattern-index.md), and [ai-facilitation-and-decision-canvas.md](ai-facilitation-and-decision-canvas.md); none of it adapts PAIR text.
- `RISK FRAMEWORK` — [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework).

Use the research paper for provenance, the toolkits for design prompts, and product evidence for final decisions. Do not present a toolkit guideline as proof that a particular design is safe or understood.

## Interaction contract

Define before designing the interface:

1. Intended users, goals, exclusions, and material stakes.
2. What the AI can and cannot do, including unsupported inputs and contexts.
3. Data sources, freshness, privacy boundaries, and whether user content is retained or used for training.
4. Expected errors, uncertainty, unequal performance, and foreseeable misuse.
5. What the user controls, reviews, edits, reverses, exports, or escalates.
6. When the system acts, recommends, interrupts, asks, waits, or hands off.
7. How quality, safety, accessibility, and reliance will be evaluated over time.

## Experience phases

### Initially

- Communicate capabilities and important limitations in task language.
- Show representative inputs and outputs without implying guaranteed performance.
- Set accurate expectations about automation, review, latency, cost, and data use.
- Do not imply a human identity, consciousness, professional qualification, or certainty the system does not have.

### During interaction

- Provide status for long or multistep work and preserve user context.
- Make generated, retrieved, transformed, and user-authored material distinguishable when that distinction matters.
- Present uncertainty in a form that helps the decision; avoid decorative confidence scores without calibration.
- Support correction, regeneration, comparison, editing, undo, and stopping.
- Time proactive behavior to the user's task and attention; provide global controls for notifications and autonomy.

### When the system is wrong

- Make failure visible without blaming the user.
- Preserve work, explain recoverable causes when known, and offer actionable next steps.
- Provide a non-AI route or human escalation for consequential tasks when feasible.
- Capture feedback with consent; do not force users to become unpaid model evaluators.

### Over time

- Let users inspect and change personalization.
- Communicate material capability, policy, or data-use changes.
- Monitor overreliance, disuse, error concentration, accessibility regressions, and distributional harms.
- Revalidate the experience when models, prompts, retrieval sources, thresholds, or autonomy change.

## Generative and agentic systems

For generated content, specify provenance, citation behavior, freshness, uncertainty, editing, and responsibility for verification. For an agent that can act:

- show the proposed plan and affected resources when consequences are material;
- use preview and confirmation at the point of consequence;
- apply least privilege and scoped authorization;
- expose progress, logs, changes, partial completion, and failures;
- make cancellation effective and rollback available when technically possible;
- require renewed approval when scope expands;
- never equate fluent output with correctness.

## Evaluation

Test calibrated understanding rather than asking only whether users “trust” the system. Measure whether users can identify capabilities, limitations, uncertainty, source quality, required review, available controls, and recovery routes. Include realistic successes, ambiguous outputs, partial failures, confident errors, stale information, latency, interruptions, and accessibility conditions.

Report task quality, appropriate reliance, correction success, recovery time, user control, mental-model accuracy, and disparate failure patterns. High satisfaction does not establish safety or appropriate reliance.
