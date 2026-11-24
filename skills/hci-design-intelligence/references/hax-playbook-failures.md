# HAX Playbook failure taxonomy

Use this reference to design failure scenarios for natural-language and adjacent AI systems before usability testing. Include normal operation as a baseline. Simulate failures safely; never expose participants to real harmful content when placeholders or controlled prototypes answer the question.

## Provenance

- `RESEARCH/APPLIED` — Hong, Fourney, DeBellis, and Amershi, [Planning for Natural Language Failures with the AI Playbook](https://doi.org/10.1145/3411764.3445735), CHI 2021.
- `SOURCE DATA` — Microsoft, [HAXPlaybook](https://github.com/microsoft/HAXPlaybook), commit `fe264d5b286993572604526c32424123476605dc`, archived 2026-06-11, MIT licensed.
- This is an original synthesis of the repository’s `src/data/content.json` and survey branching. Preserve the source attribution when reusing the taxonomy.

## Routing dimensions

The original playbook branches by system domain, primary input, trigger, input delimiter, ambiguity, response type, response mechanism, and classification type.

- **Domains:** search, recommendation, conversational AI, text prediction/assistance, classification.
- **Primary input:** typed text or documents, speech/audio, or an action sequence.
- **Trigger:** explicit/unambiguous or inferred under uncertainty.
- **Delimiter:** clear input boundaries or inferred start/end.
- **Interpretation:** one clear interpretation or multiple plausible interpretations.
- **Response type:** one response, ranked list, or action execution.
- **Response mechanism:** generated content or selection from an existing corpus.
- **Classification:** binary or multiclass.

## Complete failure inventory

### Input errors

- **Text corruption:** deletion/truncation, substitution, insertion, or adjacent-character swap changes meaning.
- **Speech transcription:** omitted endings/articles, homophone substitution, insertion, or segmentation/extension error.
- **Noisy channel:** background speech or noise adds unrelated content or removes intended content.
- **Spurious action-sequence events:** misclicks, similar controls, or undo/recovery actions become misleading model input.

### Trigger errors

- **Missed trigger:** a valid activation is not detected; vary the false-negative rate.
- **Spurious trigger:** activation occurs without user intent; vary the false-positive rate.
- **Delayed trigger:** activation arrives after the useful moment; vary delay to study confidence/latency tradeoffs.

### Delimiter errors

- **Truncation:** capture starts late or ends early, so the system receives partial input.
- **Overcapture:** capture starts early or ends late, so unrelated content becomes input.

### Interpretation and action errors

- **Ambiguity resolved incorrectly:** the system chooses the wrong valid interpretation of an underspecified input.
- **No understanding:** a well-formed request maps to no known response or action.
- **Misunderstanding:** the request maps to the wrong intent or action category.
- **Partial understanding:** the intent is right but an entity, attribute, unit, time zone, or other detail is wrong.

### Generated-output errors

- **Implausible or incoherent response:** output is visibly nonsensical or internally inconsistent.
- **Plausible but incorrect response:** fluent output contains false facts or fabricated details.
- **Inappropriate response:** content violates relevant social norms or safety expectations; test with neutral placeholders where possible.
- **Implausible/incoherent list items:** a ranked result set includes nonsensical items.
- **Plausible-but-incorrect list items:** a ranked result set includes convincing falsehoods.
- **Inappropriate list items:** a ranked result set includes unsafe, biased, or offensive content.
- **Poor ranking:** relevant items appear in an order that conflicts with the task’s intended criterion.
- **Low result diversity:** near-duplicates crowd out meaningfully different choices.

### Selected-output errors

- **Wrong item:** the system retrieves or selects an unrelated corpus item.
- **Poor precision:** many irrelevant items are included.
- **Poor recall:** important relevant items are omitted, potentially blocking task completion.
- **Poor ranking:** ordering does not match relevance, probability, importance, or the declared criterion.
- **Low result diversity:** the set is dominated by similar items.

### Classification errors

- **False negative:** a positive case receives the negative label.
- **False positive:** a negative case receives the positive label.
- **Confusion among close categories:** similar categories are collapsed or swapped.
- **Confusion among distant categories:** clearly different categories receive the same label.

## Scenario card

For each relevant failure, write:

| Field | Content |
|---|---|
| User and goal | Who is doing what, under which conditions? |
| Normal baseline | What should happen? |
| Injected failure | Which taxonomy item, at what severity or rate? |
| Observable behavior | What exactly will the prototype do? |
| Stakes | What is frustrating, costly, exclusionary, unsafe, or irreversible? |
| User path | Detect, understand, correct, retry, undo, bypass, or escalate? |
| Recovery criterion | What counts as successful recovery? |
| Measures | Task success, reliance, time, errors, correction, comprehension, affect? |
| Safeguards | Debrief, placeholders, stop rules, privacy, vulnerable-participant protections? |

## Test design

Select failures from each applicable stage of the interaction pipeline rather than only model-output errors. Include realistic frequency and severity, compare against normal operation, randomize carefully when experimental claims are intended, and test recovery as a first-class task. Pair this taxonomy with [hax-guidelines.md](hax-guidelines.md), especially HAX 2, 7–11, and 15–18.
