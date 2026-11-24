# Learning, skill, and behavioral assessment

Use this reference when a product teaches a human skill, assesses performance, supports simulation or practice, claims to improve capability, measures how people use AI, or evaluates an AI agent as a behavioral system. Keep the evaluation object explicit: a person's skill, an interface's usability, self-reported behavior, and an AI system's behavior are different constructs requiring different evidence.

## Choose the right evaluation object

| Question | Appropriate evidence | Common misuse |
|---|---|---|
| Can a person perform a target skill? | Observable task performance, defined criteria, repeated opportunities, transfer and retention | Treating confidence, completion, or content exposure as mastery |
| Is the product usable? | Representative participants performing realistic tasks while a researcher observes behavior | Calling opinions, simulated personas, or staff demonstrations usability testing |
| How does a person describe using or relating to AI? | Clearly bounded self-report instrument plus stated benchmark and limitations | Inferring ability, mental health, causation, or a fixed identity |
| How does an AI system behave? | Repeated trials, controlled environments, perturbations, action traces, outcomes, and strategy-sensitive tests | Grading only final answers or anthropomorphizing behavior as inner intent |
| Does training improve real-world capability? | Baseline, intervention, authentic performance, generalization, retention, comparison where appropriate | Measuring only immediate rehearsal in the training context |

Do not use one evidence type to answer a different question. A usable training interface does not prove learning; a learner's score does not prove the interface caused improvement; an AI-use questionnaire does not establish whether AI output was correct; an agent's correct outcome does not reveal a stable strategy.

## Design a human skill-learning loop

For procedural or interpersonal skills, consider a four-part practice loop:

1. **Instruction:** define the target behavior, purpose, conditions, important steps, examples, and criteria in accessible language.
2. **Modeling:** demonstrate competent performance, including difficult cases, decision points, and recoverable mistakes.
3. **Rehearsal:** let the learner practice in a safe, representative setting with support that can be faded.
4. **Feedback:** give timely, specific, behavior-linked feedback and another opportunity to improve.

This sequence is one applied training pattern, not a universal learning theory. Adapt it to the skill, learner, culture, disability, stakes, and setting. Do not equate compliance with learning, reward rote performance over understanding, or train behavior that violates dignity or autonomy.

When AI provides a model, simulated partner, adaptive difficulty, or feedback:

- establish expert-reviewed criteria and source material;
- disclose AI involvement and limitations;
- prevent confident but incorrect instruction from becoming practice;
- let learners inspect why feedback was given and contest or escalate it;
- protect psychological safety, privacy, and sensitive performance data;
- preserve instructor or domain-expert oversight for consequential skills;
- assess unaided performance so the product does not mistake dependence on scaffolding for learning.

## Assess human skill responsibly

1. Define the construct and why it matters in the person's life or work.
2. Translate it into observable tasks without collapsing a complex capability into one proxy.
3. Establish a baseline using appropriate, accessible conditions.
4. Sample different examples, people, settings, tools, time pressure, and support levels when transfer matters.
5. Define criteria for accuracy, quality, independence, safety, fluency, recovery, and explanation as relevant.
6. Record prompts and assistance; prompted completion is not independent mastery.
7. Check generalization, retention, and maintenance after practice.
8. Include self-report for experience or confidence only as a complementary measure.
9. Reassess when context, task, health, tools, or support changes—not on an arbitrary cadence alone.
10. Use findings to change instruction and support, not to label the person permanently.

For clinical, educational, employment, eligibility, or diagnostic decisions, use validated instruments, qualified professionals, informed consent, governance, accommodation, and the applicable legal/ethical requirements. Do not repurpose narrow ABA assessment tools as general UX measures. Avoid deficit framing, forced normalization, and goals chosen without the person's meaningful participation.

## Conduct usability testing without confusing it with training

In formative usability testing, recruit people representative of the intended audience, give realistic task scenarios without teaching the interface, observe behavior, and use neutral follow-up questions. The core elements are the participant, realistic tasks, and facilitator. If participants must first receive training because that matches real deployment, separate onboarding/training performance from subsequent product usability and later real-world proficiency.

Qualitative usability studies identify problems and mechanisms; they do not estimate prevalence or prove learning. Use [research-and-evaluation.md](research-and-evaluation.md) and [research-rigor.md](research-rigor.md) for sampling, method, validity, and causal claims.

## Use AI-use self-report cautiously

Self-report instruments about AI use may cover reported trust, reliance, verification, decision delegation, agency, or disclosure. If the user explicitly wants such an instrument or those constructs:

- preserve the instrument's official names and interpretation rules;
- describe results as comparative self-report at one point in time;
- do not infer a profile from conversation or product telemetry;
- do not treat a percentile as quality, health, correctness, or an ideal target;
- do not make clinical, diagnostic, ability, population, causal, hiring, education, or eligibility claims;
- cite the specific methodology, benchmark, dataset, or report behind a claim;
- verify independent psychometric evidence before treating it as a validated research instrument.

Prefer direct task evidence for capability and appropriate reliance. Self-report can reveal perceptions and reported habits, not whether verification succeeded or judgment was sound.

## Evaluate AI as a behavioral system

Add behavioral tests when an agent's decision process, adaptation, or multi-agent dynamics matter—not only its final score.

- **Observe:** record action sequences, tool choices, timing, state changes, and outcomes across repeated trials.
- **Perturb:** vary task framing, irrelevant cues, order, defaults, incentives, uncertainty, social signals, available tools, and environmental state while preserving the construct of interest.
- **Isolate:** design environments where competing strategies predict different actions.
- **Interpret cautiously:** infer a decision strategy only when alternative explanations have been tested; do not claim inner beliefs or motives.
- **Test stability:** compare across model, prompt, scaffold, memory, tool, user group, and time.
- **Probe interaction:** test coordination, conflict, duplication, specialization, cascades, and emergent failures in multi-agent systems.
- **Connect to consequences:** pair process evidence with verified outcomes, human impact, accessibility, security, cost, and recovery.

Behavioral tests complement the capability and regression suites in [ai-agent-evaluation.md](ai-agent-evaluation.md). They are especially useful when two agents achieve the same outcome through strategies with different safety, reliability, or human-control implications.

## Use extended-mind claims as a lens, not proof

Extended Mind Theory asks when tools and environments participate in cognition rather than merely delivering information. For AI or mixed-reality learning products, use it to examine where memory, planning, feedback, authorship, and agency are distributed across person and system. It can generate design questions about cognitive offloading, scaffold dependence, transparency, and responsibility; it does not itself prove clinical effectiveness or learning benefit.

For healthcare or mental-health training, require clinical oversight, safety and efficacy evidence, informed consent, privacy, psychological safety, accessibility, representative evaluation, and a clear boundary between educational simulation and treatment.

## Interactive questions

- What observable performance matters outside the product, and how will we distinguish independent skill from successful scaffolding?
- Which variation of person, setting, materials, or time would demonstrate transfer rather than memorization?
- Are we measuring behavior, self-report, usability, system outcome, or a proxy—and what claim can that evidence support?
- Which controlled perturbation would reveal whether the agent uses the intended strategy rather than a shortcut?
- What evidence would show that AI support strengthens human capability instead of increasing dependence?

## Provenance and source roles

- `PEER-REVIEWED PRACTICE GUIDE` — Parsons, Rollyson, and Reid, “Evidence-Based Staff Training: A Guide for Practitioners,” *Behavior Analysis in Practice* 5(2), 2–11, 2012, [DOI 10.1007/BF03391819](https://doi.org/10.1007/BF03391819). Used for the instruction–modeling–rehearsal–feedback sequence in staff training; transfer to other learners and settings must be tested.
- `ORIGINAL SYNTHESIS` — The skill assessment steps (baseline, multiple contexts, observable criteria, generalization, retention, ongoing review) are general measurement practice written for this skill, not drawn from a single source.
- `NNG/APPLIED METHOD` — [NN/g, Usability (User) Testing 101](https://www.nngroup.com/articles/usability-testing-101/), reviewed 2026-07-15. Used for the applied definition and core participant–task–facilitator structure, not as proof for a specific product.
- `OPEN-ACCESS EDITORIAL` — Jacobs et al., [Human–Computer Interaction and Artificial Intelligence: Advancing Care Through Extended Mind Theory](https://pmc.ncbi.nlm.nih.gov/articles/PMC11691189/), 2024, CC BY 4.0. Used as an editorial lens for AI/MR training and extended cognition, not as an empirical effectiveness study.
- `WORKSHOP POSITION PAPER` — Cherep, Singh, and Maes, [Behavioral Systems Require Behavioral Tests](https://www.media.mit.edu/publications/behavioral-tests/), NeurIPS LAW Workshop, 2025. Used for the observation–perturbation–interpretation research agenda; it proposes a direction rather than a validated universal test protocol.
