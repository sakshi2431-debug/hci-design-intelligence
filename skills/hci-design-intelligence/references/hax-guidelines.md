# Microsoft HAX: 18 guidelines

Use this reference to review an AI experience across its lifecycle. The guidelines are design prompts, not proof of safety, usability, fairness, or compliance. Validate them with users, system measurements, and domain experts.

## Provenance

- `ACADEMIC` — Amershi et al., [Guidelines for Human–AI Interaction](https://www.microsoft.com/en-us/research/publication/guidelines-for-human-ai-interaction/), CHI 2019.
- `APPLIED` — Microsoft, [HAX Guidelines](https://www.microsoft.com/en-us/haxtoolkit/ai-guidelines/) and the individual guideline pages linked below.
- This file is an original summary. Microsoft’s live HAX site does not state an open-content license; do not reproduce its page text or imagery.

## Initially

### HAX 1 — Make clear what the system can do

State the supported user goals, inputs, outputs, and boundaries in task language. Show representative examples without implying guarantees. Ask: can a new user predict which requests belong here and which do not?

Source: [HAX guideline 1](https://www.microsoft.com/en-us/haxtoolkit/guideline/make-clear-what-the-system-can-do/)

### HAX 2 — Make clear how well the system can do what it can do

Communicate expected performance, important failure conditions, and variation across contexts or groups. Match linguistic and numeric precision to calibrated evidence. Ask: can users decide how much review or reliance is appropriate?

Source: [HAX guideline 2](https://www.microsoft.com/en-us/haxtoolkit/guideline/make-clear-how-well-the-system-can-do-what-it-can-do/)

## During interaction

### HAX 3 — Time services based on context

Invoke, interrupt, or defer according to the user’s task, attention, environment, and stakes. Ask: is this the right moment, channel, and urgency?

Source: [HAX guideline 3](https://www.microsoft.com/en-us/haxtoolkit/guideline/time-services-based-on-context/)

### HAX 4 — Show contextually relevant information

Prioritize information that advances the current task and suppress irrelevant detail. Ask: does the system use context transparently, and can the user correct a wrong context assumption?

Source: [HAX guideline 4](https://www.microsoft.com/en-us/haxtoolkit/guideline/show-contextually-relevant-information/)

### HAX 5 — Match relevant social norms

Align tone, turn-taking, disclosure, politeness, and boundaries with the social and cultural setting. Avoid pretending the system is human. Ask: would the behavior be acceptable for this role, audience, and context?

Source: [HAX guideline 5](https://www.microsoft.com/en-us/haxtoolkit/guideline/match-relevant-social-norms/)

### HAX 6 — Mitigate social biases

Identify representation, allocation, quality-of-service, and stereotyping risks across affected groups. Test both data and interaction effects. Ask: who is more likely to be misrepresented, excluded, burdened, or harmed?

Source: [HAX guideline 6](https://www.microsoft.com/en-us/haxtoolkit/guideline/mitigate-social-biases/)

## When wrong

### HAX 7 — Support efficient invocation

Make it easy to deliberately start or request the AI service using accessible, predictable controls. Ask: can users invoke it without memorizing fragile syntax or relying on a single modality?

Source: [HAX guideline 7](https://www.microsoft.com/en-us/haxtoolkit/guideline/support-efficient-invocation/)

### HAX 8 — Support efficient dismissal

Let users ignore, close, reject, stop, or opt out of unwanted AI behavior without penalty. Ask: is dismissal discoverable, immediate, and persistent when appropriate?

Source: [HAX guideline 8](https://www.microsoft.com/en-us/haxtoolkit/guideline/support-efficient-dismissal/)

### HAX 9 — Support efficient correction

Make outputs editable and actions reversible; preserve user work and offer proportionate recovery. Ask: can the user correct the smallest wrong part rather than restart?

Source: [HAX guideline 9](https://www.microsoft.com/en-us/haxtoolkit/guideline/support-efficient-correction/)

### HAX 10 — Scope services when in doubt

When confidence or intent is unclear, ask, narrow, defer, or use a safe fallback. Do not silently take a high-impact action. Ask: does uncertainty reduce authority and consequence?

Source: [HAX guideline 10](https://www.microsoft.com/en-us/haxtoolkit/guideline/scope-services-when-in-doubt/)

### HAX 11 — Make clear why the system did what it did

Provide an explanation that supports the user’s next decision: relevant inputs, constraints, examples, or counterfactuals. Avoid false causal stories and decorative technical detail. Ask: is the explanation faithful, actionable, and understandable?

Source: [HAX guideline 11](https://www.microsoft.com/en-us/haxtoolkit/guideline/make-clear-why-the-system-did-what-it-did/)

## Over time

### HAX 12 — Remember recent interactions

Maintain short-term continuity where it benefits the task, while making retention and reset behavior clear. Ask: does the system remember enough to reduce repetition without surprising the user?

Source: [HAX guideline 12](https://www.microsoft.com/en-us/haxtoolkit/guideline/remember-recent-interactions/)

### HAX 13 — Learn from user behavior

Personalize only from meaningful signals with appropriate consent, controls, and safeguards. Ask: is the inferred preference valid, reversible, and distinct from accidental behavior?

Source: [HAX guideline 13](https://www.microsoft.com/en-us/haxtoolkit/guideline/learn-from-user-behavior/)

### HAX 14 — Update and adapt cautiously

Control the timing, scale, and visibility of adaptive changes so they do not erase context or destabilize learned workflows. Ask: will users notice, understand, and recover from the change?

Source: [HAX guideline 14](https://www.microsoft.com/en-us/haxtoolkit/guideline/update-and-adapt-cautiously/)

### HAX 15 — Encourage granular feedback

Collect feedback at the level where it can be interpreted and acted upon. Explain what feedback affects and account for reporting and sampling bias. Ask: is feedback useful to both the user and the improvement process?

Source: [HAX guideline 15](https://www.microsoft.com/en-us/haxtoolkit/guideline/encourage-granular-feedback/)

### HAX 16 — Convey the consequences of user actions

Show how a correction, rating, permission, or preference will affect current and future behavior. Ask: can the user foresee the effect before acting and verify it afterward?

Source: [HAX guideline 16](https://www.microsoft.com/en-us/haxtoolkit/guideline/convey-the-consequences-of-user-actions/)

### HAX 17 — Provide global controls

Offer understandable controls for monitoring, personalization, notifications, data use, and autonomy. Ask: can the user inspect and change system-wide behavior without hunting through individual outputs?

Source: [HAX guideline 17](https://www.microsoft.com/en-us/haxtoolkit/guideline/provide-global-controls/)

### HAX 18 — Notify users about changes

Communicate material changes to capabilities, limitations, data practices, or behavior at a useful time and level of detail. Ask: must the user revise a mental model, workflow, consent, or reliance decision?

Source: [HAX guideline 18](https://www.microsoft.com/en-us/haxtoolkit/guideline/notify-users-about-changes/)

## Review output

For each applicable guideline, record: evidence observed; lifecycle phase; affected users and task; failure or harm; proposed response; owner across UX/AI/data/engineering/policy; validation method; residual risk. Mark a guideline `not applicable` only with a reason.
