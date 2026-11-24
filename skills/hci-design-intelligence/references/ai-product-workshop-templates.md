# AI product workshop templates

Fill-in templates for the six lenses in [ai-product-discovery.md](ai-product-discovery.md). Use only the templates the current decision needs. A filled template is a record of decisions and open questions, not proof that the design works. Original material for this skill; see "Influences" at the end.

## T1. Fit brief

```text
Person and situation:
Job they are trying to get done:
What they do today without help:
Simpler alternative considered (no model):
Why the alternative falls short:
Role for AI: does it / drafts for review / advises / not at all
Parts the person keeps, and why:
Human outcome we will measure:
Product outcome we will measure:
Signal that would make us drop the AI role:
```

## T2. Task allocation

| Step in the job | Who does it today | Proposed role (person / AI drafts / AI does / rule) | Why | Cost if AI is wrong | How the person reviews or reverses it |
|---|---|---|---|---|---|

## T3. Error cost

| Error type | Example in this product | Who is affected | Cost to them | How often acceptable | Mitigation |
|---|---|---|---|---|---|
| Says yes when the answer is no |  |  |  |  |  |
| Says no when the answer is yes |  |  |  |  |  |
| Right answer, wrong moment |  |  |  |  |  |

Choose thresholds from the costs in this table, not from a single accuracy number.

## T4. Data readiness

| Input needed | Source | Rights and consent | Coverage gaps | How correctness is judged | Refresh owner |
|---|---|---|---|---|---|

Add a short "headline test": for each of privacy, exclusion, labor, misuse outside the intended context, and drift, write the worst plausible news headline, then one prevention, one detection signal, and one owner.

## T5. Understanding map

| Audience | What they assume now | Belief we need them to hold | Risky mistaken belief | Where we teach or correct it | How we check they understood |
|---|---|---|---|---|---|
| First time |  |  |  |  |  |
| Regular |  |  |  |  |  |
| After a model or policy change |  |  |  |  |  |

Check understanding by asking people to predict what the system will do, not by asking whether they read the explanation.

## T6. Reliance spec

```text
Decision the output supports:
Target behavior: accept / verify first / human decides
Overreliance looks like:
Underuse looks like:
What we show to support checking (sources, key inputs, examples, range):
Confidence signal: none / categories / ranking / number, and why
Evidence the signal is calibrated:
How we test that people rely appropriately:
How we rebuild reliance after a visible error:
```

## T7. Control matrix

| System action | Preview | Approve | Edit | Pause | Undo | Reset | Turn off | Escalate to a human |
|---|---|---|---|---|---|---|---|---|

Mark each cell yes, no, or not needed, with a reason for every "no" on a high stakes action.

## T8. Feedback statement

```text
We collect [signal] from [who] at [moment].
It changes [this output / this person's settings / the shared system] within [time].
The person sees [acknowledgement and expected effect].
It can be biased or gamed by [risk]; we handle that by [plan].
The person can stop giving it or undo its effect by [control].
```

## T9. Failure register

| Failure | Where in the journey | Likelihood | Cost | Would the person notice? | Reversible? | What they see | Recovery path | Owner |
|---|---|---|---|---|---|---|---|---|

Include at least one failure the person would not notice and one deliberate misuse. Use [hax-playbook-failures.md](hax-playbook-failures.md) to generate realistic failure types.

## Workshop agenda (90 to 120 minutes)

1. **Ground (15 min):** the person, the job, today's workaround, the simpler alternative. Fill T1.
2. **Allocate (20 min):** split the job into steps and assign roles. Fill T2 and T3.
3. **Check the inputs (15 min):** data, rights, gaps, correctness. Fill T4.
4. **Shape understanding and reliance (20 min):** T5 and T6.
5. **Give control back (15 min):** T7 and T8.
6. **Break it (15 min):** inject realistic failures. Fill T9.
7. **Commit (10 min):** decisions, owners, evidence still needed, release gate, and what change reopens the review.

Invite only the roles the decision needs: product, design or research, ML, data, engineering, accessibility, privacy or safety, support, a domain expert, and someone who represents affected people. End with a decision log and an open risk list, not with every cell filled.

## Influences

The topics follow the questions raised in Google's [People + AI Guidebook](https://pair.withgoogle.com/guidebook-v2/), which also publishes its own worksheets. These templates are newly written for this skill and do not reproduce or adapt PAIR's worksheets. Google does not endorse this skill.
