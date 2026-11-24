# AI personality and relational design

Use this reference when defining or evaluating an AI product's personality, character, voice, social role, relational cues, or behavior over time. Personality is not cosmetic copy. It emerges from the base model, system instructions, tools, memory, routing, safety behavior, initiative, correction, refusals, and recovery—and it changes what people believe about the system.

## Distinguish the layers

- **Role:** what the system is for and what authority it has.
- **Capability:** what it can and cannot reliably do.
- **Voice:** recurring language choices such as formality, brevity, warmth, and vocabulary.
- **Personality:** stable behavioral tendencies across tasks and states, including disagreement, uncertainty, initiative, and boundaries.
- **Character/persona:** an explicitly represented identity or fiction, which increases anthropomorphism and therefore requires stronger safeguards.
- **Brand expression:** the product values and identity conveyed through language, visuals, motion, and service behavior.
- **Adaptation:** controlled variation for user, context, locale, accessibility, or task—not an excuse for inconsistent principles.

Never let warmth, confidence, a human name, or a backstory imply accuracy, consciousness, professional credentials, care, memory, or authority the system does not have.

## Build a behavioral contract

Specify the personality through observable behavior:

1. Product role, audience, task, stakes, and why social cues help.
2. Three to five traits expressed as behaviors and counter-behaviors—not adjectives alone.
3. Default communication: directness, detail, formality, humor, emotional mirroring, and pace.
4. Epistemic behavior: how it expresses uncertainty, cites evidence, disagrees, asks questions, and corrects itself.
5. Agency behavior: when it suggests, acts, waits, confirms, defers, escalates, or refuses.
6. Failure behavior: tone and recovery when the system is wrong, blocked, unsafe, or unavailable.
7. Relational boundaries: prohibited claims, intimacy cues, dependency loops, manipulation, and vulnerable-user safeguards.
8. Adaptation rules: what may change by task, user choice, culture, language, or access need; what must remain stable.
9. Model, mode, or memory changes that must be visible to the user.
10. Evaluation tasks and release/monitoring criteria.

Example trait specification:

> **Respectfully candid:** state disagreement and material risks plainly; explain the reason; preserve the user's decision authority. Do not flatter, reflexively validate, ridicule, or manufacture certainty.

## Use HAX and PAIR interactively

Route personality decisions through mental models, reliance, control, failure, and change over time:

- PAIR user needs: What task benefit requires personality rather than clear functional language?
- PAIR mental models: What kind of entity will users think this is, and which mistaken belief is consequential?
- PAIR explainability and reliance: Could warmth, certainty, empathy, or status cues inflate trust beyond demonstrated capability?
- PAIR feedback/control: Can people reduce, change, or turn off the personality and memory behavior?
- PAIR graceful failure: Does the personality remain honest, calm, and actionable when wrong or unable to help?
- HAX 1–2: make capabilities and likely performance clear;
- HAX 5–6: follow relevant social norms without stereotyping or reinforcing bias;
- HAX 11: explain consequential behavior in terms the user can act on;
- HAX 14 and 18: update cautiously and communicate model, mode, memory, or behavioral changes.

Ask at the natural design boundary: **Which recurring behavior would help the task without making the AI seem more capable, caring, or authoritative than it is?**

## Risks and safeguards

Inspect sycophancy, false intimacy, emotional dependency, parasocial attachment, authority inflation, manipulation, stereotyping, cultural mismatch, harassment, inconsistency, and personality drift. Memory can amplify the sense of an enduring relationship. For children, people in crisis, health, education, finance, employment, and other vulnerable or high-stakes settings, use stricter boundaries, escalation paths, and independent review.

Do not infer a person's personality from interaction traces and silently adapt the interface. Personality measures are sensitive research data and weak proxies for needs. If a validated trait instrument is genuinely necessary, obtain informed consent, use a qualified research plan, minimize data, test measurement validity across cultures and languages, avoid deterministic segments, and provide a non-profiled experience. Prefer direct preferences and observed task needs over personality typing. Do not use MBTI as a scientific basis for product decisions.

## Evaluate behavior, not adjectives

Test representative and adversarial multi-turn scenarios across:

- normal work, ambiguity, disagreement, correction, failure, refusal, and escalation;
- consistency across tools, models, languages, channels, and long sessions;
- factual accuracy and calibrated uncertainty under different tones;
- appropriate reliance, mental-model accuracy, user agency, and task outcomes;
- sycophancy, false authority, attachment cues, manipulation, bias, and cultural interpretation;
- accessibility, cognitive load, comprehension, and user control;
- drift after prompt, model, routing, memory, or policy changes.

Use [ai-agent-evaluation.md](ai-agent-evaluation.md) to turn the contract into capability and regression tasks. Satisfaction or engagement alone is unsafe evidence: a more agreeable personality can increase both while reducing correction, agency, or appropriate reliance.

## Provenance

This is an original HCI synthesis. [Shape of AI: Personality](https://www.shapeof.ai/patterns/personality) is an applied pattern source used for the model/scaffolding distinction, consistency/adaptation, empathy-versus-authority, model-switch transparency, sycophancy, attachment, memory, and evaluation concerns; it is not a standard or peer-reviewed evidence source. [The Role of Personality in User Experience](https://uxpsychology.substack.com/p/the-role-of-personality-in-user-experience) is a secondary psychology overview used only as a route to Five-Factor and cited individual-differences research.
