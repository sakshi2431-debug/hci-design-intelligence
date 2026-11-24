# AI interaction pattern index

Use this index when you know the problem an AI experience has and need candidate design mechanisms. Each entry names a problem, mechanisms that often help, the main way they go wrong, and related HAX patterns from [hax-design-patterns.md](hax-design-patterns.md). A pattern is a hypothesis to test in context, not evidence that a design works. Original material for this skill; see "Influences" at the end.

## Deciding whether AI belongs

| Problem | Mechanisms that often help | Common failure | Related HAX |
|---|---|---|---|
| The team cannot say why AI beats a simpler approach | Compare against a rules, search, or human service baseline on the same tasks; prototype both | Comparing against a strawman baseline | (none) |
| People expect magic | State the job the feature does and the conditions where it struggles, at the moment of use | Limits buried in a help page | 1A, 2C |
| The technology is described instead of the benefit | Lead with what the person gets; add mechanism only when it changes consent or checking | Removing the mechanism when people need it to judge risk | 1A, 11B |

## Data and evaluation

| Problem | Mechanisms that often help | Common failure | Related HAX |
|---|---|---|---|
| Errors cost different groups differently | Separate false positive and false negative costs by group and set thresholds from them | One global threshold tuned on an average | 2C |
| Training or evaluation data is thin for some people | Targeted collection with consent, subgroup evaluation, and an explicit "not supported" state | Shipping anyway with no warning | 2D, 10C |
| Labelers disagree | Treat disagreement as information: review the task definition and keep uncertainty labels | Majority vote that hides a real ambiguity | (none) |
| Data goes stale | Named owner, refresh triggers, drift monitoring, and retirement criteria | Data treated as a one time input | 14A |
| Privacy and learning settings are unclear | Plain statements of what is collected, kept, shared, and learned, next to the controls | A settings page nobody can find | 11E, 16D |

## Understanding and onboarding

| Problem | Mechanisms that often help | Common failure | Related HAX |
|---|---|---|---|
| New users do not know what to try | Representative example inputs and outputs that the system reliably handles | Cherry picked examples that inflate expectations | 1D, 1E |
| People fear breaking something | Previews, sandboxes, drafts, and undo so exploration is cheap | Undo that does not cover the real consequence | 9C, 16A |
| The new behavior clashes with a familiar workflow | Attach the AI step to a known workflow and point out where it differs | Hiding the difference so people misread results | 1C |

## Explanation and reliance

| Problem | Mechanisms that often help | Common failure | Related HAX |
|---|---|---|---|
| People cannot check an output quickly | Show sources, dates, and the inputs that mattered next to the output | Showing everything, so nothing is checked | 11A, 11C, 11D |
| Confidence is shown but not meaningful | Show confidence only if calibrated and tested; otherwise use categories, ranked options, or nothing | Raw model scores presented as certainty | 2A, 2B |
| Explanations are too complete to use | Give the smallest faithful reason that supports the next decision; offer more on request | Decorative technical detail | 11A, 11B |
| People need to learn the system over time | System level explanations in onboarding, history, and documentation, not only in the moment | Explanations that disappear after first use | 11B, 16D |
| Human expertise should sit beside the model | Attach human authored context, citations, or expert review to outputs | Implying a human checked what nobody checked | 11C |

## Control, feedback, and automation level

| Problem | Mechanisms that often help | Common failure | Related HAX |
|---|---|---|---|
| Unclear how much to automate | Automate more where stakes are low and errors reversible; keep review where they are not | One autonomy level for the whole product | 10A, 16A |
| Automation should grow over time | Increase scope in stages, each gated by evidence, with rollback | Expanding scope because nothing visibly broke | 14A, 14B |
| People need to supervise ongoing automation | Status, activity history, pause, and override at useful points | A log nobody can act on | 9C, 16B |
| Feedback has no clear purpose | Define what each signal changes and tell people the effect and timing | Implying feedback retrains the model when it does not | 9D, 15A, 15B, 16B |
| Harmful or wrong content needs reporting | Item level reporting with reasons, review, and abuse handling | Treating every report as ground truth | 15C |

## Failure and recovery

| Problem | Mechanisms that often help | Common failure | Related HAX |
|---|---|---|---|
| The system fails and the person is stuck | Return control with work preserved, a non AI route, and a path to a human | Error message with no next step | 9C, 10C |
| The product must own its mistakes | Acknowledge the error, state impact and recovery, and name who fixes it | Blaming the user or the model | 16B |
| The system is unsure what was meant | Ask one focused question when interpretations lead to different consequences | Interrogating people about harmless details | 10A |
| Repeated errors of the same kind | Batch correction with preview and undo | Batch changes that cannot be reviewed | 9E |

## How to use an entry

1. Confirm the problem with evidence from research, logs, or failure testing.
2. Pick the smallest mechanism that addresses it.
3. Note the common failure and design against it.
4. Define how you will know it worked: a comprehension, reliance, recovery, or task measure.
5. Record the decision in the canvas in [ai-facilitation-and-decision-canvas.md](ai-facilitation-and-decision-canvas.md).

## Influences

The problem areas overlap with Google's [People + AI Guidebook pattern collection](https://pair.withgoogle.com/guidebook-v2/patterns) and its [case studies](https://pair.withgoogle.com/guidebook-v2/case-studies), which are worth reading for worked examples. This index is newly written for this skill, organized by problem, and does not reproduce or adapt PAIR's pattern text or case summaries. Google does not endorse this skill. HAX pattern identifiers refer to the synthesis in [hax-design-patterns.md](hax-design-patterns.md) of Microsoft's [HAX design patterns](https://www.microsoft.com/en-us/haxtoolkit/design-patterns/).
