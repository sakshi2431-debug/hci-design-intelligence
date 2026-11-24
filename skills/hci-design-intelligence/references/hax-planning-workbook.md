# HAX planning workbook

Use this original worksheet early in requirements definition with UX, AI/ML, data, engineering, product, accessibility, safety, and policy partners. It follows the five-stage logic of Microsoft’s [HAX Workbook](https://www.microsoft.com/en-us/haxtoolkit/workbook/) without reproducing the workbook.

## 1. Select relevant guidelines

For each HAX guideline, record:

| Field | Prompt |
|---|---|
| Applicability | Relevant, uncertain, or not relevant—and why? |
| User situation | Which user, task, context, and lifecycle phase? |
| Failure or need | What could go wrong, or what must users understand/control? |
| Evidence | Research, system evaluation, domain evidence, or assumption? |
| Impact | Harm, task failure, reliance error, exclusion, or recoverability? |

Read [hax-guidelines.md](hax-guidelines.md) and retain uncertain items until the team resolves them.

## 2. Estimate requirements

For every high-impact guideline, draft requirements in four lanes:

- **UI/interaction:** messages, controls, states, explanations, correction, feedback, accessibility.
- **AI/model:** confidence or failure signals, supported inputs, thresholds, explanations, learning behavior.
- **Data:** source, labels, coverage, consent, provenance, subgroup evaluation, retention, monitoring.
- **Engineering/operations:** logging, latency, fallbacks, rollback, escalation, release controls, incident response.

Use [hax-design-patterns.md](hax-design-patterns.md) only where a listed pattern addresses the need. A guideline without an official pattern still requires a project-specific response.

## 3. Size and test the requirement

| Requirement | Owner | Dependencies | Size (S/M/L/unknown) | Acceptance signal | Failure test | Residual risk |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |

Do not use size as a proxy for importance. Mark technical unknowns explicitly rather than forcing a false estimate.

## 4. Prioritize impact against cost

Place requirements in an impact/cost matrix, then apply constraints:

- Address severe, irreversible, rights-affecting, or safety-related harms even when expensive.
- Prefer high-impact, low-cost work for early delivery.
- Research high-uncertainty items before committing to expensive implementation.
- Record deferred items, rationale, owner, trigger for reconsideration, and interim mitigation.

## 5. Track through release

| Requirement | Status | Design evidence | Model/data evidence | Test result | Decision | Recheck trigger |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |

Re-open the workbook when the model, prompt, retrieval source, threshold, training data, user group, task, autonomy, or policy changes materially.

## Workshop agenda

1. Align on users, goals, exclusions, stakes, and known system limits.
2. Independently mark the 18 guidelines, then discuss disagreements.
3. Select high-impact needs and candidate design patterns.
4. Draft UI/AI/data/engineering requirements together.
5. Size, prioritize, name owners, and define evidence needed for release.
6. End with open risks and decisions—not only a feature list.

Provenance: `APPLIED` Microsoft HAX Workbook, retrieved 2026-08-24. This file is an original worksheet and is not an official Microsoft template.
