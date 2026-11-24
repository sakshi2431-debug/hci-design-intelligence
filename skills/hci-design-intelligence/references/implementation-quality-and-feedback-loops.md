# Implementation quality and verified feedback loops

Use this reference after interaction requirements are sufficiently clear and when reviewing or implementing a product experience.

## Priority order

Review quality in this order:

1. task success, truthfulness, data integrity, and irreversible consequences;
2. performance, stability, and frequently used controls;
3. loading, empty, partial, error, offline, permission, cancellation, and recovery states;
4. accessibility and input-method support;
5. platform conventions, responsive behavior, and device realities;
6. content clarity, hierarchy, visual coherence, and product identity;
7. delight and decorative refinement.

A generic-looking interface can be a symptom, but visual novelty is not the product outcome. Diagnose whether the experience fits this product, these people, and their tasks. Do not replace one fashionable template with another or change a healthy flow merely to make it look different.

## Inspect before changing

- Identify the actual stack, platforms, package manager, design tokens, shared components, content rules, and established brand decisions.
- Inspect the running experience when possible. Code inspection alone cannot prove perceived performance, focus behavior, layout stability, touch quality, readability, or screen-reader usability.
- Scope the review to named screens or the smallest representative task flow. Do not sweep an entire product without agreement.
- Preserve established behavior and information architecture unless the decision explicitly includes changing them.
- Treat static analysis, automated accessibility scans, and pattern detectors as signals requiring contextual verification.

## Platform-realistic validation

For responsive web, check representative narrow, medium, and wide viewports; keyboard operation; visible focus; text resize or zoom; light/dark themes when supported; reduced motion; and common loading/error states.

For mobile or mobile web, verify on physical hardware when practical. Consider safe areas, on-screen keyboards, touch target size, input zoom, overscroll, long-press behavior, hover assumptions, orientation, network interruption, and assistive technology. A desktop browser emulation is useful but not final evidence of native-feeling behavior.

Never claim performance is healthy without measurement. Never claim accessibility conformance from an automated scan alone. State what was tested, what was inferred, and what remains unverified.

## Closed-loop visual feedback

Annotation or visual-feedback tools can shorten the path from observation to implementation. Treat them as optional adapters, not core dependencies.

A complete loop is:

1. capture the exact screen, state, viewport, actor, and comment;
2. confirm the implementation agent received that exact item—not merely that a server is reachable;
3. connect the item to a requirement, defect, or preference with owner and status;
4. change the source of truth where possible: token, shared component, content rule, or service behavior;
5. rebuild and reproduce the same state;
6. verify the intended outcome and check for regressions;
7. close the original item with evidence and note anything not tested.

A visible toolbar, successful installation, connection health, or nonzero annotation count does not prove the loop works. Verify an identifiable test item end to end.

## Implementation-system adapters

Component libraries, design-system tools, frontend-quality skills, native-platform checklists, and annotation services may be excellent execution aids. Keep their installation and stack-specific rules in separate adapters. The HCI core should define the human requirements, states, evaluation criteria, and evidence boundaries they must satisfy.

When a project already has a component system, prefer its accessible primitives and semantic tokens before adding custom markup. This is a maintainability heuristic, not permission to ignore a better interaction or an unmet access need.

## Report honestly

For each important issue include:

- observed evidence and state;
- affected people and task;
- consequence and priority;
- the requirement, standard, convention, or preference involved;
- proposed change and tradeoff;
- how it was or will be verified;
- what could not be checked.
