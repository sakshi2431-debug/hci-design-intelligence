# Output patterns

## People-centered product decision

For product, feature, growth, engagement, retention, or monetization work, include only the sections useful to the decision:

1. People's intended progress and context.
2. Legitimate product or business outcome.
3. Value-exchange hypothesis and candidate behavior.
4. Evidence, assumptions, affected groups, and possible non-user effects.
5. Experience concept, alternatives, and important states or failure paths.
6. Human-outcome, product-outcome, experience-quality, and guardrail metrics.
7. Agency, accessibility, privacy, safety, equity, and long-term wellbeing tradeoffs.
8. Cheapest useful validation, decision criterion, and reversal plan.

Do not treat more activity as proof of more value. Recommend a healthy stopping point when successful use should naturally end.

## Interactive HAX–PAIR recap

When an AI-product conversation benefits from a checkpoint, provide a compact living record:

- **Decision in progress**
- **What we know** — supplied or external evidence
- **What we are assuming**
- **PAIR diagnosis** — relevant need, data, mental-model, reliance, control, or failure finding
- **HAX implications** — initially, during interaction, when wrong, or over time
- **Requirements changed** — UI, model, data, engineering/operations, accessibility, or evaluation
- **Highest-impact open question**
- **Next evidence or decision**

Do not display this recap after every conversational turn. Use it when the discussion changes phase, several decisions accumulate, ambiguity appears, or the user asks for a summary.

## AI-agent evaluation plan

1. User goal, agent capability, boundaries, and consequential failures.
2. Agent/scaffold versions, tools, permissions, data, and environment.
3. Capability suite and regression suite.
4. Representative tasks, matched negative cases, reference solutions, and repeated trials.
5. Outcome, trace, interaction-quality, accessibility, reliance, safety, cost, and latency measures as relevant.
6. Deterministic, model-based, expert, and user graders with calibration and partial-credit logic.
7. Task-level results, distributions, segments, uncertainty, and observed failure clusters.
8. Production monitoring, user research, trace review, and human-study layers.
9. Release threshold, guardrails, owner, rollback, maintenance, and recheck triggers.

Do not reduce evaluation to one aggregate score or grade only whether the agent says it succeeded. Verify the state that matters to the person and inspect representative traces.

## Agent authority and orchestration map

1. User goal, non-agent baseline, and reason flexible agency is justified.
2. Actor/owner, agent roles, tools, data, resources, recipients, and environments.
3. Proposed, preparatory, executable, prohibited, and human-only actions.
4. Limits on scope, time, cost, volume, privacy, and downstream delegation.
5. Preview, confirmation, re-authentication, expert review, and takeover checkpoints.
6. Status, provenance, handoffs, conflicts, cancellation, rollback, and escalation.
7. Verified success, forbidden side effects, matched do-not-act cases, and residual responsibility.
8. Evaluation, monitoring, rollout, suspension, retirement, owners, and recheck triggers.

## Secure AI interaction review

1. People, assets, consequences, likely threats, trust boundaries, and responsible owners.
2. Human, application, workload, model/profile, tool, and operator identities.
3. Authorization rules and independent enforcement points outside the model.
4. Permission experience: actor, action, resource, reason, duration, scope, consequence, and revocation.
5. Proposed/approved/running/blocked/partial/completed/rolled-back states and recovery.
6. Operator information architecture, evidence, verification, prioritization, and handoffs.
7. Audit events, correlation, policy versions, sensitive-field handling, access, and retention.
8. Security tests, usability/accessibility tasks, release gates, incident response, and recheck triggers.

## Interface critique

Lead with the top risks. For each issue use:

```markdown
### [Severity] Issue title
- Evidence: What is visible or observed.
- Affected users/tasks: Who and when.
- Lens: Standard, HCI model, research finding, heuristic, or psychology lens.
- Consequence: Likely task/accessibility/trust effect.
- Confidence: Observed / strongly supported / plausible risk.
- Recommendation: Specific change and preserved tradeoff.
- Validate: Method, participant/task, and success signal.
- Provenance: Source links, standard identifiers, or supplied evidence.
```

Suggested severity:

- **Critical:** blocks or seriously harms a critical task, safety, rights, or access.
- **High:** major failure with poor recovery or broad reach.
- **Medium:** meaningful friction, misunderstanding, or inefficiency.
- **Low:** localized polish/consistency issue with limited task impact.

## Whole-product critique

1. Product thesis: people, context, progress, promise, and business outcome.
2. Artifact maturity, critique decision, constraints, and comparison set.
3. Strengths to preserve and the evidence supporting them.
4. Findings across value, end-to-end experience, interaction, system, and craft.
5. For each finding: observation, interpretation, evidence, taste judgment if any, consequence, and confidence.
6. Priorities by human harm/value, product impact, reach, persistence, and dependency.
7. Decisions, unresolved disagreements, owners, and intentionally deferred work.
8. Validation and the evidence that would change the decision.

Do not disguise taste as user evidence or let a list of visual issues stand in for product critique.

## AI personality contract

1. Role, audience, task, stakes, and reason social cues help.
2. Desired traits expressed as behaviors and counter-behaviors.
3. Voice and adaptation rules across tasks, locales, access needs, and user choice.
4. Uncertainty, disagreement, correction, initiative, refusal, failure, and recovery behavior.
5. Capability, authority, memory, identity, and relational boundaries.
6. HAX–PAIR implications for mental models, reliance, control, failure, and change over time.
7. Sycophancy, false intimacy, attachment, manipulation, bias, and cultural safeguards.
8. Multi-turn capability and regression scenarios, measures, release criteria, and monitoring.

## HCI explanation

1. Plain-language definition.
2. Mechanism.
3. Example and counterexample.
4. Boundary conditions/misuses.
5. How to test it in practice.
6. Source type and provenance.

## Research plan

1. Decision context and objectives.
2. Research questions/hypotheses.
3. Method rationale.
4. Participants and recruitment.
5. Procedure and materials.
6. Measures and analysis.
7. Ethics, privacy, and accessibility.
8. Timeline/roles/dependencies.
9. Limitations and decision criteria.

## Human skill-learning and assessment plan

1. Meaningful target skill, context, learner participation, and affected groups.
2. Observable construct, baseline, current supports, and evidence boundaries.
3. Instruction, modeling, rehearsal, feedback, and support-fading plan as relevant.
4. Authentic tasks, performance criteria, prompts/assistance, and evaluator competence.
5. Accessibility, dignity, consent, privacy, psychological safety, and contestability.
6. Generalization across people/settings/materials, retention, and maintenance.
7. Usability, self-report, independent performance, and system measures kept separate.
8. Decision criteria, adaptation, expert oversight, limitations, and recheck triggers.

## Accessibility evaluation

Separate:

- standards findings with exact WCAG criterion/level;
- implementation observations;
- usability findings from disabled participants;
- automated-tool signals requiring manual confirmation;
- inclusive-design opportunities beyond conformance.

Never write “WCAG compliant” without defined scope, target version/level, complete evidence, and appropriate authority.

## Redesign brief

Include user/problem framing, requirements, conceptual model, IA/task flow, components/states, content, error recovery, accessibility contract, responsive/cross-channel behavior, analytics/research instrumentation, visual direction, implementation constraints, and acceptance/validation checks.

