# Laws of UX

Use the [Laws of UX index](https://lawsofux.com/) as an accessible psychology-oriented design reference. The site lists 30 laws; this file covers the ones most useful for design decisions. Treat each “law” as a lens with boundary conditions, not a universal prediction or standard. The project's [information page](https://lawsofux.com/info/) states a CC BY-NC-ND 4.0 license; summarize and link rather than reproducing the site.

## Route by design question

### Action and target acquisition

- **Fitts's law:** larger/nearer targets are faster to acquire under defined pointing conditions. Consider device, motor ability, edge effects, and competing targets.
- **Doherty threshold:** responsive feedback preserves interaction flow; use progress, optimistic UI, or staged results without disguising actual delay.

### Choice and cognitive demand

- **Hick's law:** decision time can rise with the number and complexity of alternatives. Improve meaning, grouping, defaults, search, and progressive disclosure; do not blindly remove necessary choices.
- **Chunking / working memory:** externalize state and group related information meaningfully.
- **Miller's law:** the “7±2” finding concerns short-term memory span in controlled tasks; do not cite it as a universal limit on menu items or options.
- **Cognitive load:** reduce effort not needed for the task (extraneous load) while keeping the effort that builds understanding; do not judge load from visual density alone.
- **Choice overload:** distinguish a genuinely difficult tradeoff from a merely long but scannable list.

### Familiarity and conceptual models

- **Jakob's law:** users transfer expectations from other products. Use conventions where transfer helps; make departures visible and learnable.
- **Mental model:** align structure and behavior with users' causal understanding or teach a better model through feedback.
- **Paradox of the active user:** provide learn-in-place support because many users start acting before reading documentation.

### Perception and grouping

- **Proximity, similarity, common region, and uniform connectedness:** use visual relationships to communicate semantic relationships; verify they do not create false grouping.
- **Prägnanz:** simple organization can aid perception, but “simple-looking” must not hide necessary distinctions.
- **Aesthetic-usability effect:** polish can increase perceived ease and tolerance, but can also mask usability problems.

### Attention and memory

- **Von Restorff effect:** distinctive items gain attention; reserve distinction for meaningful priority and avoid competing highlights.
- **Serial-position effect:** beginnings and endings may be more memorable; task relevance still controls ordering.
- **Peak-end rule:** salient peaks and endings shape retrospective evaluation; never manufacture harmful peaks or ignore the whole journey.
- **Selective attention:** align salience with user goals; beware banner blindness and manipulative attention capture.
- **Cognitive bias:** people use mental shortcuts that can be predictable; design to reduce harmful errors from them, never to exploit them.

### Complexity and system responsibility

- **Tesler's law:** some complexity remains; decide whether the system, organization, or user should bear it.
- **Occam's razor:** prefer the least complicated solution that explains and satisfies the requirements; do not sacrifice capability or accessibility for minimalism.
- **Postel's law:** accept reasonable input variation and produce predictable output, but do not use permissiveness to weaken security, validation, or accessibility.
- **Pareto principle:** a minority of causes often accounts for most effects; use it to prioritize investigation, not to ignore the people in the long tail.

### Motivation and progress

- **Goal-gradient effect:** visible progress can motivate completion; progress indicators must be truthful.
- **Zeigarnik effect:** unfinished tasks may stay cognitively active; use saved state and reminders without exploiting anxiety.
- **Flow:** absorbed engagement tends to need clear goals, immediate feedback, and challenge matched to skill; flow is a contested construct and not a synonym for ease.
- **Parkinson's law:** work tends to expand to fill the time available; realistic defaults and autofill can shorten tasks, but artificial time pressure is manipulation.

Assess ethical implications, consent, and user wellbeing before using any motivational mechanism.

## Application template

For each lens state:

1. Principle and proposed mechanism.
2. Evidence visible in this design.
3. Boundary conditions and alternative explanations.
4. Design implication.
5. Testable prediction and evaluation method.

Course-derived context: the Information Architecture synthesis treats design-psychology resources as prompts for investigation, not universal laws. See [coursework-information-architecture.md](coursework-information-architecture.md).
