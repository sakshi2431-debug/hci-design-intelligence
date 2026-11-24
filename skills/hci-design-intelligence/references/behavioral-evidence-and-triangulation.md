# Behavioral evidence and qual–quant triangulation

Use this reference when interpreting funnels, retention, event streams, time-on-task distributions, product metrics, or apparent disagreement between behavioral data and qualitative research. The objective is a decision-ready diagnosis and the cheapest evidence that could disconfirm it—not a confident story attached to a chart.

## Validate the measurement before diagnosing the experience

Check:

1. **Event semantics:** what condition actually emits each event; whether it fires once, repeatedly, on render, on attempt, or on verified completion.
2. **Denominators and exposure:** who could have taken the action, who was included, and whether acquisition or eligibility changed.
3. **Path assumptions:** whether the supposed funnel is required, ordered, skippable, revisitable, or entered midway.
4. **Instrumentation and time:** missing events, duplicate events, late data, definition changes, and analytics releases.
5. **External changes:** product releases, incidents, campaigns, pricing, seasonality, policy, or audience shifts on the same timeline.
6. **Segmentation:** platform, geography, accessibility needs, experience level, acquisition source, cohort, task intent, and other differences that an aggregate may conceal.

If the number does not survive these checks, report a measurement question rather than inventing a design problem.

## Read shapes as hypotheses, not conclusions

- A sharp discontinuity can indicate a block, requirement, error, missing information, or instrumentation boundary.
- A gradual decline can indicate accumulated cost, but verify whether later steps are optional and whether remaining users differ from earlier users.
- Retention that stabilizes can suggest a durable cohort; continued decline can suggest weak recurring value, mismatch, or a changing population.
- A multimodal distribution means the mean may describe nobody. Identify the populations or task types before optimizing it.
- A metric change with a stable numerator can be denominator or mix-shift behavior rather than a product effect.

For each explanation, record the affected segment, competing explanations, confidence, the observation that would weaken or falsify it, and the cheapest suitable evidence. Rank next steps by decision value, risk, and cost—not narrative attractiveness.

## Reconcile qualitative and quantitative evidence

First determine whether the sources describe the same:

- population and segment;
- task and context;
- product version and time period;
- construct and outcome;
- stage of the journey.

Then give each source only the claims it can support:

- Behavioral data can estimate what happened, where, how often, and for whom when instrumentation and sampling are sound. It rarely establishes intent or mechanism by itself.
- Qualitative research can reveal goals, interpretations, strategies, breakdown mechanisms, and unmet needs. A small purposive sample does not estimate population prevalence.
- Self-report describes remembered or stated experience under the conditions in which it was asked; it is not interchangeable with observed behavior.
- Experiments can estimate a causal difference only when assignment, exposure, analysis, and interference assumptions are defensible.

An apparent conflict may expose a category error, different populations, a hidden segment, an unmeasured mechanism, or a proxy that improved while the broader experience worsened. Do not average incompatible findings into a compromise claim.

## Design the resolving study

Write:

1. the exact disputed claim;
2. the decision it affects;
3. what each existing source can and cannot establish;
4. the result that would change each interpretation;
5. the smallest method that discriminates between explanations;
6. the stopping rule and remaining uncertainty.

A targeted instrumentation check, segmented query, session replay with consent safeguards, brief task observation, intercept question, or mixed-method session may be more useful than repeating the larger study. Add the missing form of evidence instead of rerunning the source that supports the preferred answer.

## Output pattern

| Observation | Measurement validity | Candidate explanation | Segment | Disconfirming evidence | Confidence | Next check | Decision implication |
|---|---|---|---|---|---|---|---|

Keep observation, inference, and recommendation separate. Report effect magnitude and uncertainty alongside statistical significance. Pair product outcomes with human-outcome and guardrail measures.

## Provenance

This is an original HCI synthesis informed by the MIT-licensed `behavioural-analytics` and `qual-quant-triangulation` skills in MC Dean's [Designer Skills Pack](https://github.com/Owl-Listener/designer-skills), strengthened with this skill's research-rigor, evidence-role, ethics, and people-centered product requirements. See `licenses/designer-skills-pack-MIT.txt`.
