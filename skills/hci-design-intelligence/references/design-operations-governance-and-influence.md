# Design operations, governance, influence, and impact

Use this reference for design debt, design-system governance, adoption, cross-functional tradeoffs, implementation handoff ownership, and reporting design impact.

## Treat design debt as an evidence-backed backlog

Classify debt without collapsing distinct problems:

- **Experience debt:** known task breakdowns, confusing mental models, missing recovery, or harmful friction.
- **Structural debt:** information architecture and workflows that no longer fit the product or service.
- **Accessibility debt:** identified barriers or unmet conformance criteria; do not label an untested suspicion as a confirmed violation.
- **System debt:** inconsistent components, tokens, behaviors, content patterns, or cross-platform divergence.
- **Documentation debt:** decisions, states, components, or ownership that cannot be reliably discovered.
- **Implementation debt:** hardcoded values, duplicated components, fragile exceptions, or design–code drift.
- **Research and measurement debt:** material assumptions with no evidence, invalid instrumentation, or missing outcome measures.

For each item record evidence, affected people and tasks, frequency or reach, persistence, consequence, dependencies, effort uncertainty, owner, status, and validation. Do not use a single arithmetic score as truth. Prioritize through explicit judgment: harm and rights first, then criticality, reach, persistence, dependency, opportunity cost, and feasible sequencing.

## Govern a design system as a product and service

Define:

1. consumers, contributors, maintainers, decision owners, and funding;
2. centralized, federated, or hybrid contribution boundaries;
3. proposal, triage, research, design, accessibility, engineering, content, security, and approval steps;
4. versioning, release notes, migration support, compatibility, deprecation, and retirement;
5. quality gates for states, semantics, keyboard behavior, responsive behavior, tokens, localization, documentation, tests, and ownership;
6. adoption support, office hours, contribution usability, and feedback routes;
7. measures for reuse, exceptions, defects, contribution time, migration burden, accessibility, and consumer success.

Semantic versioning can help when the system behaves like a versioned software dependency, but it is not automatically the right contract for every design library or platform. Choose a change-communication model that matches actual consumers and release mechanics.

## Negotiate through shared outcomes and explicit tradeoffs

Start from the user and product outcome, acknowledge delivery and technical constraints, and distinguish requirements from preferred solutions. Offer bounded alternatives:

- what can be delivered now;
- what is deferred or removed;
- which user, accessibility, security, quality, or evidence risk is accepted;
- who owns the decision;
- what would trigger reconsideration;
- how resulting debt will be recorded and addressed.

Use project evidence before appeals to taste or authority. Competitive precedent is context, not proof. Do not call a plausible accessibility concern a confirmed legal or WCAG failure without the necessary evaluation.

## Report impact without laundering attribution

Connect:

- **Intervention:** what changed and the causal mechanism proposed.
- **Human outcome:** effectiveness, effort, recovery, comprehension, access, confidence, agency, or wellbeing.
- **Product outcome:** activation, adoption, retention, conversion, contribution, support demand, or another legitimate result.
- **Business outcome:** revenue, cost, risk, speed, or capability.
- **Guardrails:** unequal outcomes, regret, complaints, accessibility regressions, privacy or safety incidents, unwanted engagement, or downstream burden.

State the design contribution separately from shared outcomes and causal proof. Report baselines, dates, populations, sample sizes, effect sizes or distributions, co-occurring changes, limitations, and failures. Outputs such as screens or components are delivery evidence, not impact by themselves.

## Decision record

| Decision | Evidence | Options considered | Human outcome | Product outcome | Tradeoff/risk | Owner | Revisit trigger | Validation |
|---|---|---|---|---|---|---|---|---|

For parallel concepts, fix evaluation criteria before selecting, keep fidelity comparable, make the concepts behaviorally distinct, and preserve what each rejected direction tested and the evidence that could revive it.

## Provenance

This is an original HCI synthesis informed by the MIT-licensed `design-debt-audit`, `design-system-governance`, `design-negotiation`, `design-impact-reporting`, and `explore-options` materials in MC Dean's [Designer Skills Pack](https://github.com/Owl-Listener/designer-skills). It corrects their useful operational patterns with this skill's evidence, accessibility, product-outcome, and causal-claim discipline. See `licenses/designer-skills-pack-MIT.txt`.
