# AI product discovery: six lenses

Use this reference when a team is deciding whether, where, and how AI should take part in a product or feature. It turns a vague "add AI" idea into decisions about fit, evidence, understanding, reliance, control, and failure. It is original guidance for this skill. It is informed by, but does not adapt, Google's People + AI Guidebook; see "Influences" at the end.

Work through the lenses as the conversation reaches them, not as a form. One lens is often enough for the decision at hand.

## Lens 1: Fit

**The decision:** is AI the right tool for this person's problem, and if so, in what role?

Ask:

- What is the person trying to get done, and what do they do today when the product does not help?
- What would a version with no model look like (rules, search, a better form, a human service)? Why is it not enough?
- Which part of the job does the person want to keep because it carries judgment, identity, enjoyment, or accountability?
- Which part would they gladly hand off because it is tedious, risky, or beyond human scale?
- If the model is wrong one time in ten, is the feature still worth having? One time in a hundred?
- What will the team measure to know the feature helped the person, not only that it was used?

Produce: a one paragraph fit statement naming the person, the job, the simpler alternative, the role AI plays (does the task, drafts for review, advises, or stays out), and the human outcome measure.

Warning signs: the AI role was chosen before the job was described; the only success measure is usage; nobody can name the simpler alternative.

## Lens 2: Evidence and data

**The decision:** can the system learn or retrieve what it needs, legitimately, for the people and conditions it will actually meet?

Ask:

- What exactly must the system produce, and what inputs would a skilled human need to produce it?
- Where will those inputs come from, who owns them, and did the people they describe agree to this use?
- Which people, languages, devices, environments, or edge conditions are missing or thin in the data?
- Who decides what a correct output is? What happens when qualified people disagree?
- If labels or judgments are produced by people, what are their working conditions, instructions, and pay?
- How will the data and the evaluation set be kept current as the world and the user base change?

Produce: a data readiness note listing required inputs, sources and rights, known coverage gaps, how correctness is defined, and the refresh owner.

Warning signs: "we will use whatever we have"; correctness defined by another model with no human check; no plan for the groups the data underrepresents.

## Lens 3: Understanding

**The decision:** what must people believe about the system to use it well, and how will they come to believe it?

Ask:

- Before using the feature, what will a first time user assume it can do, sees, remembers, or decides?
- Which of those assumptions, if wrong, would cause real harm or wasted effort?
- How does the experienced user's picture differ from the newcomer's?
- At which moments does the person need to learn something new (first use, first error, after an update)?
- Do any cues (a name, a voice, warmth, confident phrasing) suggest more capability or care than the system has?

Produce: a short list of the beliefs people need, the mistaken beliefs to prevent, and where in the journey each is taught or corrected.

Warning signs: onboarding explains the technology rather than what the person can expect; the system sounds certain where it is not.

## Lens 4: Reliance

**The decision:** when should people act on the output, check it, or ignore it, and what helps them tell the difference?

Ask:

- What decision or action follows from the output?
- What does too much reliance look like here? What does too little look like?
- What would the person need to see to check an output quickly: the sources, the inputs that mattered, similar cases, or a range?
- Is any confidence signal actually calibrated for this task and population? Would people read it the same way?
- After the system makes a visible mistake, how is appropriate reliance rebuilt rather than lost entirely?

Produce: a reliance specification naming the decision, the target behavior (accept, verify, or override), the information shown to support it, and how comprehension will be tested.

Warning signs: the goal is stated as "increase trust"; a confidence number appears because the model emits one; explanations describe the model instead of helping the decision.

## Lens 5: Control and feedback

**The decision:** what can people steer, correct, stop, or refuse, and what happens to the signals they give?

Ask:

- For each thing the system does, can the person preview it, approve it, edit it, pause it, undo it, reset it, or turn it off?
- Which of those controls matter most given the stakes and how hard the action is to reverse?
- What feedback will the product collect, explicitly or by observing behavior, and what will it change: this output, this person's settings, or the system for everyone?
- How will the person know their feedback was received and what effect to expect, and when?
- Could feedback be gamed, biased by who bothers to give it, or misread?

Produce: a control matrix (action by available control) and a feedback statement naming what is collected, why, what it changes, and what the person sees.

Warning signs: feedback buttons with no defined use; implying feedback retrains the model when it does not; no way to turn a learned behavior off.

## Lens 6: Failure and recovery

**The decision:** what goes wrong, who notices, and how does the person get back to a good state?

Ask:

- List the realistic failures across the journey: bad input, wrong interpretation, plausible but false output, missed action, action at the wrong time, upstream outage.
- Which failure would the person be least likely to notice? Which would cost the most?
- When a failure is detected, what does the person see, and what can they do next without losing work?
- Is there a route that does not depend on the model at all? Can they reach a human?
- How does the team learn from failures, and who owns that loop?
- How might someone misuse the feature on purpose?

Produce: a failure register ranking failures by likelihood, cost, detectability, and reversibility, each with its message, recovery path, and owner.

Warning signs: only the happy path is designed; errors blame the user; failures are logged but nobody reviews them.

## Before release

A team should be able to answer, in plain words:

1. Why AI here, and what was the simpler alternative?
2. Who is missing from the data and the evaluation?
3. What should people believe about the system, and how do we know they do?
4. What reliance does each explanation or signal support?
5. What can people control, correct, undo, or refuse?
6. Which failures did we test, and what does the person experience when the system gets it wrong?

Turn unresolved answers into evaluation tasks with [ai-agent-evaluation.md](ai-agent-evaluation.md) and interaction requirements with [hax-guidelines.md](hax-guidelines.md).

## Influences

Google's [People + AI Guidebook](https://pair.withgoogle.com/guidebook-v2/) (PAIR) shaped the topics this reference covers. Its chapters remain the recommended reading for each lens: [User Needs + Defining Success](https://pair.withgoogle.com/guidebook-v2/chapter/user-needs/), [Data Collection + Evaluation](https://pair.withgoogle.com/guidebook-v2/chapter/data-collection/), [Mental Models](https://pair.withgoogle.com/guidebook-v2/chapter/mental-models/), [Explainability + Trust](https://pair.withgoogle.com/guidebook-v2/chapter/explainability-trust/), [Feedback + Control](https://pair.withgoogle.com/guidebook-v2/chapter/feedback-controls/), and [Errors + Graceful Failure](https://pair.withgoogle.com/guidebook-v2/chapter/errors-failing/). The guidebook was published in 2019 and updated in 2021; PAIR has since announced generative AI updates, so check the live site for newer guidance. This file does not reproduce or adapt PAIR text or worksheets. Google does not endorse this skill.
