# AI facilitation and decision canvas

Reach for this reference when a conversation is exploring, designing, diagnosing, or planning an AI powered product, feature, or agent. Its job is to make the discovery lenses and HAX guidelines part of the thinking while the concept is still forming, instead of a checklist run after it is fixed. Original material for this skill.

Detailed material lives in: [ai-product-discovery.md](ai-product-discovery.md) (six lenses), [ai-product-workshop-templates.md](ai-product-workshop-templates.md) (templates), [ai-interaction-pattern-index.md](ai-interaction-pattern-index.md) (mechanisms), [hax-guidelines.md](hax-guidelines.md), [hax-design-patterns.md](hax-design-patterns.md), [hax-planning-workbook.md](hax-planning-workbook.md), and [hax-playbook-failures.md](hax-playbook-failures.md).

## How to facilitate

Behave like a colleague who knows the material, not a form.

1. Work out which decision the conversation is heading toward.
2. Respond to the idea itself first: answer, extend, or challenge it so the turn is useful on its own.
3. Find the open assumption that would most change value, feasibility, reliance, control, harm, or evaluation if it turned out wrong.
4. Pick the one lens and HAX guideline that address it.
5. Ask one concrete question about it, with your recommended answer and why.
6. When the person answers, say what changed: decision, assumption, risk, or requirement.
7. Hold the next question until the conversation reaches the decision it belongs to.

Infer low stakes details and label them as assumptions. Ask only when different answers would change the concept, a requirement, a risk, a metric, or a test. Never turn one person's answer into evidence about a population.

## Question router

| When the conversation reaches | Lens | HAX | A question that tends to move the decision |
|---|---|---|---|
| A new AI idea | Fit | 1, 2 | What does the person do today without this, and what would a version with no model look like? |
| Which steps the AI should do | Fit | 1, 2, 7 to 10 | Which step would the person refuse to hand over, and why? |
| Success metrics or rewards | Fit | 2, 6, 10 | What behavior would this metric reward that we would not want, and who pays for each kind of error? |
| Training, retrieval, personalization, or evaluation data | Evidence and data | 2, 6, 10, 13, 14 | Whose situations are missing from the data, and what happens to them? |
| Onboarding or expectations | Understanding | 1, 2 | What will a first time user assume this can do that it cannot? |
| Personality, voice, or social role | Understanding, reliance | 1, 2, 5, 6, 11, 14, 18 | Which recurring behavior helps the task without implying more capability, care, or authority than exists? |
| Transparency, confidence, or trust | Reliance | 2, 11 | What decision does this explanation support, and what would overreliance look like? |
| Feedback, editing, or autonomy | Control and feedback | 7 to 9, 12 to 17 | For this action, what can the person preview, undo, or turn off? |
| An agent's authority or several agents working together | Fit, control, failure | 1, 2, 7 to 10, 12 to 18 | What is the most consequential thing the agent may do without a person checking, and what evidence justifies that? |
| Permissions, identity, or security sensitive tools | Understanding, control, failure | 1, 2, 7 to 11, 15 to 18 | If someone tricks the model or it simply errs, what control outside the model caps the damage, and what does the person see? |
| Errors and recovery | Failure and recovery | 7 to 11 | Which failure would the person be least likely to notice, and how would they recover without losing work? |
| Whether an agent works | Fit, failure | All that apply | What observable end state proves the goal was met, and which failure should become a test before release? |
| AI supported learning or assessment | Fit, understanding, reliance, control, failure | 1, 2, 6, 10 to 18 | What must the learner manage alone once the support is gone, and how will we check it? |
| Adaptation and long term use | Understanding, control, failure | 12 to 18 | What changes over time, how do people find out, and when must we revalidate? |
| Turning the concept into requirements | All | Planning workbook | Which findings become UI, model, data, engineering, operations, accessibility, and evaluation requirements, and who owns each? |
| Release or a major change | Before release checks | All that apply | What evidence supports release, what risk remains, and what change reopens the review? |

The questions are starting points. Rewrite them in the product's own terms and at the person's level of detail.

## Decision canvas

Keep this record as the conversation goes. Show it when a recap would help, when the phase changes, or when asked. Keep it compact enough to paste into another session to continue the work.

```text
Decision in progress:
People and goals (users, affected non users, context):
Product outcome and candidate metric:
AI role and simpler alternative:
Evidence (what we know and where it came from):
Assumptions (plausible, not yet checked):
Understanding and reliance (beliefs needed, reliance risks):
Data and performance (sources, gaps, error costs):
Control and feedback (preview, undo, opt out, escalation):
Failures and recovery (expected, hidden, fallback):
Requirements (UI / model / data / engineering and ops / accessibility / evaluation):
Open questions, most consequential first:
Next evidence (smallest study, prototype, or test):
Evaluation contract (end state, tasks, graders, trials, release gate, regression trigger):
```

Tag each entry as one of: **supplied** (the person told us or we observed it), **external** (a named source supports it), **inference**, **assumption**, **decision** (agreed, with reason), or **open risk**.

## Turning lenses into requirements

1. A lens surfaces the issue (for example: people need to compare options, and a confident wrong recommendation is costly).
2. Record what appropriate reliance looks like, tagged as evidence or assumption.
3. HAX 2, 10, and 11 turn it into requirements: stated limits, narrower output when unsure, reasons that support the decision.
4. HAX 7 to 9 add how the person invokes, dismisses, and corrects it.
5. The failure register and [hax-playbook-failures.md](hax-playbook-failures.md) generate realistic breakdowns.
6. The [HAX planning workbook](hax-planning-workbook.md) assigns owners across UI, model, data, engineering, and operations.
7. [ai-agent-evaluation.md](ai-agent-evaluation.md) turns requirements and failures into tasks, graders, repeated trials, and release evidence.

Frameworks structure questions and requirements. Research and system evaluation supply the evidence; never cite a framework as proof that a design works.

## Pacing

- **Casual brainstorm:** answer substantively; ask one short lens question only when it unlocks the next step.
- **Focused problem solving:** one question, its implication, then continue.
- **Workshop:** announce the lenses and HAX phases you will cover, work through them in order, and keep the canvas visible.
- **Quick recommendation:** state assumptions, recommend, and name the single open question most likely to reverse the recommendation.
- **Audit:** check every relevant lens and HAX guideline, and report only what matters: findings, gaps in evidence, requirements, and risks to release.

Stop asking when the evidence matches the stakes, when the next uncertainty needs research rather than opinion, or when the person wants to move on. End with the decision, remaining assumptions, and the next piece of evidence.

## Influences

Microsoft's [HAX Toolkit](https://www.microsoft.com/en-us/haxtoolkit/) and Google's [People + AI Guidebook](https://pair.withgoogle.com/guidebook-v2/) (PAIR) are the main influences on this facilitation approach. No Microsoft or Google text, worksheets, or assets are reproduced or adapted here. Neither Microsoft nor Google endorses this skill.
