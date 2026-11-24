# Interaction states, errors, recovery, and handoff

Use this reference when an interaction has several states, async work, validation, permissions, retries, partial completion, cross-channel transitions, or implementation ambiguity.

## Model behavior explicitly

For each interaction, define:

- **States:** mutually meaningful conditions such as idle, editing, validating, submitting, waiting, partially complete, successful, empty, unavailable, blocked, cancelled, failed, and recovering.
- **Events:** user actions, system responses, timeouts, permission changes, connectivity changes, external updates, and lifecycle changes.
- **Transitions:** valid movement between states.
- **Guards:** permissions, validation, prerequisites, safety conditions, and business rules.
- **Actions and side effects:** data reads/writes, messages, charges, navigation, logging, or external changes.
- **Entry and exit behavior:** focus placement, announcements, saved state, cleanup, and persistence.

Do not force independent concerns into one overloaded state machine. Use related state models when visual state, network state, authorization, and long-running job state can vary independently. Identify impossible combinations and race conditions explicitly.

## State-transition specification

| Current state | Event | Guard | Next state | Visible response | Side effect | Accessible announcement | Recovery/escape |
|---|---|---|---|---|---|---|---|

Every reachable state needs an understandable presentation and a viable exit, even when that exit is cancellation, escalation, or safe abandonment.

## Design errors as part of the task

Use this hierarchy:

1. **Prevent:** constraints, safe defaults, examples, previews, dependency checks, and reversible staging.
2. **Detect:** validation, monitoring, conflict detection, timeouts, stale-state checks, and verified external outcomes.
3. **Explain:** what happened, what remains unchanged, why it matters, and what the person can do next.
4. **Recover:** preserve work, retry safely, edit, undo, roll back, switch channels, contact support, or escalate.
5. **Learn:** record the failure without exposing sensitive data and use recurrent failures to improve the system.

Avoid unnecessary confirmation dialogs. Use confirmation when consequence, irreversibility, scope, or uncertainty makes review valuable. Never use a reassuring message to conceal partial completion or an unverified outcome.

## Accessibility contract for dynamic states

Specify:

- focus movement and restoration;
- keyboard actions and escape behavior;
- semantic role, name, state, and value;
- live-region or status announcements without excessive interruption;
- error association and a navigable error summary when appropriate;
- preservation of entered data;
- reduced-motion behavior;
- time-limit extension or removal;
- alternatives for gesture, drag, hover, vision, hearing, speech, or fine-motor demands.

## Implementation handoff

A handoff must explain behavior, not only appearance. Include:

- user goal, requirements, assumptions, and unresolved questions;
- component or flow states and transition table;
- content rules, min/max cases, truncation, localization, RTL, and empty/loading/error content;
- responsive and cross-platform behavior;
- token references rather than unexplained raw values;
- keyboard, screen-reader, focus, contrast, target-size, and motion requirements;
- data and API assumptions, permissions, latency expectations, offline behavior, and idempotency where relevant;
- analytics definitions tied to verified states rather than visual renders;
- testable acceptance criteria and design-QA plan;
- ownership for open decisions and post-release monitoring.

Do not present implementation assumptions as decided requirements. Walk through consequential or novel behavior with engineering, content, research, accessibility, security, or operations partners as appropriate.

## Provenance

This is an original HCI synthesis informed by the MIT-licensed `state-machine`, `error-handling-ux`, and `handoff-spec` skills in MC Dean's [Designer Skills Pack](https://github.com/Owl-Listener/designer-skills), expanded with accessibility, agent-state, verification, and evidence safeguards. See `licenses/designer-skills-pack-MIT.txt`.
