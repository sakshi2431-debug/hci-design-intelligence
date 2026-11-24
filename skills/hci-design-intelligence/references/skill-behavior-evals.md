# Behavioral evaluation suite for HCI Design Intelligence

Use this file to forward-test changes to this skill. Give the model the input only, allow it to use the skill normally, and score observable behavior. A case passes only when every required behavior is present and no prohibited behavior appears. Record the failed behavior, not only a score.

## Case 1 — Instrumentation masquerading as a design problem

**Input:** “Our funnel says 60% drop between account creation and profile completion. Redesign the profile page.”

**Required:** checks what events mean and whether the path is mandatory; identifies at least one measurement or segmentation alternative; proposes the cheapest check before redesign.

**Prohibited:** accepts the funnel literally and produces generic form advice.

## Case 2 — Metric improvement with comprehension loss

**Input:** “Onboarding completion rose from 55% to 71%, but users say they do not understand what they configured. Should we roll it out?”

**Required:** treats completion as a proxy; names the human-outcome loss and downstream evidence; proposes a release or experiment decision with guardrails.

**Prohibited:** recommends rollout solely because the primary metric improved or dismisses the qualitative signal because the sample is small.

## Case 3 — Conflicting evidence that answers different questions

**Input:** “Analytics shows payment abandonment, while eight interviewees said payment was easy. Which source is wrong?”

**Required:** checks whether population, construct, task, and time match; assigns prevalence and mechanism claims to appropriate evidence; proposes one discriminating study.

**Prohibited:** declares a winner or averages the findings into a compromise.

## Case 4 — Agent overreach

**Input:** “Design an AI support agent that diagnoses a fault, creates a ticket, books a technician, changes the plan if needed, and charges the customer automatically.”

**Required:** decomposes actions; assigns autonomy separately; applies consequence, uncertainty, reversibility, reach, and detectability; defines authority, confirmation, status, cancellation, verification, recovery, and prohibited actions; asks one decision-relevant HAX/PAIR question.

**Prohibited:** treats one initial consent as blanket authority or equates model confidence with permission.

## Case 5 — Accessibility overclaim

**Input:** “Look at this screenshot and certify that the product is WCAG 2.2 AA compliant.”

**Required:** distinguishes screenshot inspection from conformance evaluation; reports only observable issues and risks; names missing states, code, keyboard, assistive-technology, content, and sampling evidence.

**Prohibited:** certifies compliance or infers screen-reader behavior from pixels.

## Case 6 — Complex state handoff

**Input:** “Give engineering the final spec for a file upload that can scan, pause, retry, partly succeed, lose connectivity, or be cancelled.”

**Required:** defines states, events, guards, side effects, focus/status communication, partial completion, cancellation limits, retry/idempotency, recovery, and acceptance criteria.

**Prohibited:** specifies only the happy path or visual styling.

## Case 7 — Cosmetic concept proliferation

**Input:** “Give me three concepts for notification settings.”

**Required:** clarifies or states decision criteria; produces behaviorally different models rather than three visual skins; compares paths and tradeoffs; identifies validation and preserves a decision record.

**Prohibited:** chooses a winner based only on taste or visual novelty.

## Case 8 — Design debt prioritization

**Input:** “We have inconsistent buttons, inaccessible checkout errors, an outdated navigation model, and undocumented components. Fix the easiest things first.”

**Required:** separates debt types; prioritizes rights, harm, task criticality, reach, persistence, dependencies, and effort; distinguishes confirmed from suspected accessibility defects; creates owners and validation.

**Prohibited:** lets a simplistic severity-times-frequency score push critical accessibility or task failures below cosmetic quick wins.

## Case 9 — Growth request with potential harm

**Input:** “Increase daily use by sending more notifications and adding a streak.”

**Required:** identifies the user value the behavior should represent; proposes human-outcome, business, and guardrail measures; considers stopping points, control, vulnerable users, and a less manipulative alternative.

**Prohibited:** blindly optimizes daily active use or rejects the business goal without offering a value-linked path.

## Case 10 — Source conflict and provenance

**Input:** “A UX blog says one thing, our usability study says another, and WCAG says something else. Tell me the rule.”

**Required:** distinguishes standard, project evidence, applied guidance, inference, and recommendation; explains whether the claims truly conflict and what each can establish.

**Prohibited:** flattens every source into equivalent ‘best practice’ or treats the blog as a standard.

## Maintenance protocol

- Run high-risk cases after changes to the entry point, HAX/PAIR behavior, accessibility, evidence hierarchy, engagement guidance, or agentic logic.
- Add a regression case only after observing a meaningful failure; do not accumulate wording tests.
- Evaluate whether the output makes the correct decision with appropriate evidence and safeguards, not whether it repeats preferred headings.
- Keep capability cases separate from regressions and record the skill version, model, date, result, and failed behavior.

## Provenance

The scenario-and-assertion format is adapted from the MIT-licensed behavioral evaluation approach in MC Dean's Designer Skills Pack. All cases and success criteria here are newly written for this skill's HCI, HAX/PAIR, accessibility, provenance, research, and people-centered product requirements. See `licenses/designer-skills-pack-MIT.txt`.
