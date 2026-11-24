# HCI foundations

For original works, model boundaries, and academic provenance, also read [foundational-source-guide.md](foundational-source-guide.md).

## Frame HCI broadly

Treat HCI as the study and design of interactions among people, technologies, tasks, organizations, and environments. Avoid reducing it to interface aesthetics or isolated screen behavior. Use context of use: users, goals, tasks, equipment, physical/social environment, and consequences.

## Core models

### Human-centred design lifecycle

Use ISO 9241-210 as the lifecycle anchor: understand context, specify user requirements, produce design solutions, evaluate against requirements, and iterate with multidisciplinary participation. Treat the process as iterative and evidence-driven.

### Usability

Use ISO 9241-11's context-specific framing: effectiveness, efficiency, and satisfaction for specified users pursuing specified goals in a specified context. Add learnability, error tolerance, accessibility, trust, and experience qualities when the product demands them, but do not silently redefine the metric.

### Norman's action cycle

Diagnose both gulfs:

- **Execution:** Can users form an intention, discover possible actions, and map a control to the desired action?
- **Evaluation:** Can users perceive system state, interpret feedback, and determine whether the goal was achieved?

Use signifiers, mapping, constraints, feedback, visibility, conceptual models, and error support as design levers. Distinguish an affordance (possible action) from a signifier (perceivable cue).

### Mental and conceptual models

Users act through incomplete, context-dependent mental models. Designers provide a conceptual model through structure, terminology, behavior, and explanation. Diagnose mismatches rather than blaming users. Familiar conventions can transfer useful expectations but can also import the wrong model.

### Distributed and situated cognition

Do not place all cognition inside one user. Inspect what information is carried by artifacts, collaborators, spatial arrangement, history, and workflow. Plans are resources for action; real behavior adapts to local circumstances. Evaluate in realistic contexts when environmental dependencies matter.

### Predictive performance models

- **GOMS/KLM:** Estimate skilled, routine, error-free task performance; do not use for novices, discovery, emotion, or complex collaboration.
- **Fitts's law:** Model rapid aimed movement as a function of target distance and size; define the actual motor task and input device.
- **Hick-Hyman law:** Model choice reaction under controlled alternatives; do not translate it mechanically into “fewer options is always better.” Organization, familiarity, search, and meaning matter.

### Attention, memory, and learning

- Working memory is limited and task-dependent; externalize state and reduce recall requirements.
- Recognition often reduces retrieval demand, but recognition sets can still become visually or semantically difficult.
- Selective attention follows goals and salience; visual prominence can help or manipulate.
- Chunking works only when groups are meaningful to the audience.
- Expertise changes behavior: support novices without blocking efficient expert paths.

### Error and resilience

Separate slips (execution failures despite a correct goal) from mistakes (goal or model failures). Prefer prevention for severe harm, constraints for impossible states, reversible actions, clear recovery, preserved user work, and explanations that help users repair their model.

## Interaction-quality checklist

Assess:

1. Goal clarity and value.
2. Discoverability and action mapping.
3. System status, latency, and feedback.
4. Consistency with user and platform expectations.
5. Information scent, hierarchy, and navigation.
6. Cognitive, perceptual, and motor demand.
7. Error prevention, recovery, and reversibility.
8. Accessibility and adaptable use.
9. Trust, privacy, consent, representation, and agency.
10. Cross-channel continuity and organizational feasibility.

## Use theory responsibly

Name the construct, explain its mechanism, connect it to observable design evidence, and state the boundary conditions. A theory-backed concern is still a hypothesis about a particular product until project evidence supports it.
