# Coursework synthesis: Conversational UX

Public-safe original synthesis derived from user-supplied graduate coursework. It does not reproduce readings, assignments, rubrics, private examples, or participant data. Treat it as a course-informed lens, not as independent empirical authority.

## Use this reference when

Designing voice, chat, multimodal, or agent conversations; mapping intents; handling uncertainty; establishing personality; or testing dialogue behavior.

## Working model

- Conversation is coordinated action, not a sequence of polished messages.
- Begin with the user's goal and task flow. Map intents, entities or slots, context, system capabilities, and recovery paths before writing final dialogue.
- Design multiple natural utterances for the same intent and account for ambiguity, interruption, repair, topic shifts, and incomplete information.
- Treat confidence as uncertain evidence, not permission to act.
- Make system state, limits, data use, and consequences legible at the moment they matter.
- Personality should clarify the product relationship and remain consistent across success, waiting, error, refusal, and escalation.

## Conversation footprint

Inspect six connected layers:

- **Skeleton:** goals, turns, intents, entities, states, and branching.
- **Spirit:** voice, tone, social role, and boundaries.
- **State:** memory, context, progress, and what the system believes.
- **Screen:** visual or multimodal support for comprehension and control.
- **Section:** where the conversation sits in the larger journey and service.
- **Stealth:** background automation, data access, and actions not visible in the dialogue.

## Decision prompts

1. Why is conversation preferable to a form, menu, direct manipulation, or mixed interface?
2. What can the system reliably understand, remember, retrieve, and do?
3. What should it ask, confirm, summarize, or refuse?
4. How can the person correct a misunderstanding or leave the conversation?
5. Which failures need graceful recovery or human escalation?
6. How will different speech, language, disability, culture, and privacy needs affect use?

## Validation

Test the dialogue as behavior, not prose alone: varied utterances, ambiguous requests, interruptions, corrections, latency, tool failure, sensitive contexts, multimodal transitions, and takeover.
