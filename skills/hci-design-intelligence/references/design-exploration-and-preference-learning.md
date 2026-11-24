# Design exploration, decision dialogue, and preference learning

Use this reference when a team is converging too quickly, wants to stress-test a direction, or wants an AI collaborator to learn durable design preferences without inventing them.

## Explore the problem, not cosmetic variants

Generate at least three meaningfully different concepts when the solution shape is consequential or still uncertain. Difference should appear in the conceptual model, information architecture, division of responsibility, interaction pattern, service process, or authority model—not merely color, typography, or layout.

For each concept state:

1. the view of the problem it assumes;
2. the people and situations it serves best;
3. the core interaction and important states;
4. what complexity it hides and what it exposes;
5. accessibility, error, recovery, trust, and agency implications;
6. organizational value, dependencies, and operational burden;
7. evidence supporting it and the assumption most likely to break it.

Hosts may generate concepts sequentially or in parallel. Parallel agents are an optional execution technique, never a requirement of the skill. Enforce conceptual difference in the brief; multiple generators otherwise tend to converge on the same familiar pattern.

Compare the concepts against the actual decision criteria. Do not select a winner by visual novelty alone. Synthesis is allowed, but name which tension each borrowed element resolves so the result does not become an incoherent collection of features.

## Decision-tree dialogue

When the user asks to be challenged, grilled, or interviewed:

- map the unresolved decision branches and their dependencies;
- answer questions from available artifacts or evidence before asking the user;
- ask one decision-changing question at a time;
- include a recommended answer with reasoning, not a neutral question dump;
- follow the consequence of the answer before opening an unrelated branch;
- periodically recap decisions, assumptions, disagreements, and remaining branches;
- stop when the decision is sufficiently specified, not when every imaginable question has been asked.

Use care with “relentless” questioning. Productive rigor preserves the person's agency, cognitive bandwidth, psychological safety, and right to defer or decline.

## Learn design preferences responsibly

Treat user corrections and selections as evidence of project intent, not automatically as universal design truth.

For each possible preference:

1. retain the original correction, selection, or observable change;
2. distinguish a functional fix, one-off content choice, contextual compromise, and reusable preference;
3. find the narrowest useful scope: instance, component class, product, brand, or organization;
4. capture the user's reason; label any proposed rationale as inferred;
5. check existing principles for duplication or conflict;
6. propose the rule and scope before persisting it;
7. store only after approval, with date, provenance, exceptions, and owner;
8. convert mechanically detectable rules into tokens, tests, or lint checks where appropriate;
9. revisit rules when the product, audience, evidence, or platform changes.

Do not infer personal, demographic, emotional, health, or other sensitive attributes from design feedback. Do not silently create long-term memory. A user must be able to inspect, correct, export, and delete persisted preferences.

## Keep three layers distinct

- **Evidence-backed requirement:** needed for a human goal, standard, safety constraint, or observed behavior.
- **Project or brand convention:** chosen for coherence, voice, or maintainability.
- **Taste preference:** a defensible aesthetic judgment that may still be subjective.

All three can matter. Problems begin when taste is presented as research, a local convention is presented as universal HCI, or a standard is waived as mere preference.

## Validation

Test whether the learned rule improves consistency without erasing contextual judgment. Test whether the exploration produced materially different choices. Test whether the dialogue changed or clarified a decision rather than only increasing documentation.
