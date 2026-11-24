# Microsoft HAX design patterns

Use this catalog after selecting applicable HAX guidelines. The live library contains 34 patterns for guidelines 1, 2, 9, 10, 11, 14, 15, and 16. Each official pattern is structured around a problem, solution, use conditions, implementation guidance, user benefit, and common pitfalls. Treat the pattern as a candidate mechanism and test it in context.

## Provenance and use

`APPLIED` — Microsoft [HAX design patterns](https://www.microsoft.com/en-us/haxtoolkit/design-patterns/), retrieved 2026-08-24. This is an original, compact synthesis with original examples. Follow each link when exact wording, current examples, or updates matter. The live pages do not state an open-content license; do not copy their text or imagery into deliverables.

Read each entry as **purpose; example; guardrail**.

## Guideline 1: capability communication

- **[1A — Introductory blurb](https://www.microsoft.com/en-us/haxtoolkit/pattern/g1-a-introductory-blurb/):** Briefly name the capability for unfamiliar users. Example: “Summarizes the selected meeting transcript.” Keep it concrete, dismissible, and no more capable-sounding than the product.
- **[1B — Use explanation patterns](https://www.microsoft.com/en-us/haxtoolkit/pattern/g1-b-use-explanation-g11-patterns/):** Let explanations reveal capability boundaries through system-wide or instance-level behavior. Example: a ranking explanation exposes which inputs influence results. Explanations must be faithful and discoverable, not a substitute for a clear capability statement.
- **[1C — Expose system controls](https://www.microsoft.com/en-us/haxtoolkit/pattern/g1-c-expose-system-controls/):** Use visible controls and settings to reveal possible operations. Example: visible tone, length, and source controls show what a writing assistant can change. Do not rely on exploration alone for novices or hide key controls.
- **[1D — Demonstrate possible inputs](https://www.microsoft.com/en-us/haxtoolkit/pattern/g1-d-demonstrate-possible-system-inputs/):** Offer representative prompts or inputs that teach the supported range. Example: selectable “compare,” “extract,” and “rewrite” prompts. Samples must be diverse, reliably supported, contextually suitable, and free of biased assumptions.
- **[1E — Show a set of outputs](https://www.microsoft.com/en-us/haxtoolkit/pattern/g1-e-show-a-set-of-system-outputs/):** Teach by displaying representative output alternatives. Example: preview three crop suggestions for an image. Avoid cherry-picked examples that inflate expectations or overwhelm choice.

## Guideline 2: performance communication

- **[2A — Match language precision to performance](https://www.microsoft.com/en-us/haxtoolkit/pattern/g2-a-match-the-level-of-precision-in-ui-communication-with-the-system-performance-language/):** Use calibrated words such as “may,” “likely,” or “estimated.” Example: “This may be a duplicate” instead of “Duplicate.” Avoid vague hedging and test how users interpret the terms.
- **[2B — Match numeric precision to performance](https://www.microsoft.com/en-us/haxtoolkit/pattern/g2-b-match-the-level-of-precision-in-ui-communication-with-the-system-performance-numbers/):** Round, range, or qualify numbers to the evidence. Example: “about 20 minutes” rather than “19:47” when the estimate is noisy. Do not expose uncalibrated model scores as user confidence.
- **[2C — Report system performance information](https://www.microsoft.com/en-us/haxtoolkit/pattern/g2-c-report-system-performance-information/):** Provide task-relevant evaluation results and conditions. Example: show error rates by document quality when a reviewer chooses whether to adopt extraction software. Translate metrics into practical consequences and do not hide subgroup variation.
- **[2D — Provide low-performance alerts](https://www.microsoft.com/en-us/haxtoolkit/pattern/g2-d-provide-low-performance-alerts/):** Warn when a detectable context raises failure risk. Example: flag that glare makes a scanned ID unreliable and request a retake. Match urgency to harm and provide an actionable next step.

## Guideline 9: correction

- **[9A — Switch classification decisions](https://www.microsoft.com/en-us/haxtoolkit/pattern/g9-a-switch-classification-decisions/):** Let users flip a wrong label among a small set. Example: mark “not spam.” Make the states and effect clear; frequent correction signals that the feature or model needs redesign.
- **[9B — Rich and detailed edits](https://www.microsoft.com/en-us/haxtoolkit/pattern/g9-b-rich-and-detailed-edits/):** Make every relevant part of an output directly editable. Example: edit an AI-generated itinerary without regenerating the whole plan. Preserve provenance and user changes; do not overwrite them on refresh.
- **[9C — Undo automated actions](https://www.microsoft.com/en-us/haxtoolkit/pattern/g9-c-undo-automated-actions/):** Provide immediate reversal for completed automation. Example: restore messages moved by an automatic rule. Undo must cover the real consequence, remain available long enough, and disclose irreversible parts.
- **[9D — Combine correction through feedback (official title: “Do G9 through G15”)](https://www.microsoft.com/en-us/haxtoolkit/pattern/g9-d-do-g9-through-g15/):** When direct repair cannot fully correct the model, connect correction to feedback, learning, explanation, and control patterns. Example: correct a recommendation and state whether future recommendations will change. Do not imply that feedback retrains the model when it does not.
- **[9E — Batch-edit data](https://www.microsoft.com/en-us/haxtoolkit/pattern/g9-e-batch-editing-data/):** Allow efficient multi-item correction when errors repeat. Example: reclassify selected expenses together. Preview scope, support partial exceptions, and provide undo for high-volume changes.

## Guideline 10: uncertainty and scope

- **[10A — Disambiguate before acting](https://www.microsoft.com/en-us/haxtoolkit/pattern/g10-a-disambiguate-before-acting/):** Ask a focused question when multiple interpretations lead to different consequences. Example: “Cambridge, UK or Massachusetts?” Do not interrogate users when a harmless default or reversible preview is sufficient.
- **[10B — Avoid cold starts by eliciting preferences](https://www.microsoft.com/en-us/haxtoolkit/pattern/g10-b-avoid-cold-starts-by-eliciting-user-preferences/):** Collect a small set of meaningful preferences before personalization has evidence. Example: choose several topics to seed a news feed. Offer skip/reset, explain use, and do not overfit to provisional answers.
- **[10C — Fall back to other strategies](https://www.microsoft.com/en-us/haxtoolkit/pattern/g10-c-fall-back-to-other-strategies/):** Degrade to a safer method or conventional workflow. Example: offer filters when semantic search is uncertain. Keep the fallback useful and accessible; never conceal that capability has changed.

## Guideline 11: explanations

- **[11A — Local explanations](https://www.microsoft.com/en-us/haxtoolkit/pattern/g11-a-local-explanations/):** Explain one output or action. Example: list the factors that caused a specific transaction alert. Include only relevant, faithful factors and a path to challenge or correct them.
- **[11B — Global explanations](https://www.microsoft.com/en-us/haxtoolkit/pattern/g11-b-global-explanations/):** Explain the system’s general behavior and limits. Example: describe what a recommender uses across sessions. Avoid a generic model description that cannot help users predict practical behavior.
- **[11C — Present properties of outputs](https://www.microsoft.com/en-us/haxtoolkit/pattern/g11-c-present-properties-of-system-outputs/):** Expose useful attributes of the result. Example: show source date, provenance, and coverage beside a generated summary. Properties must be meaningful to the decision, not technical decoration.
- **[11D — Map input attributes to outputs](https://www.microsoft.com/en-us/haxtoolkit/pattern/g11-d-map-system-input-attributes-to-system-outputs/):** Show which input features influenced a result. Example: highlight clauses that contributed to a contract-risk flag. Do not present correlation or feature importance as a causal guarantee.
- **[11E — Map user behaviors to outputs](https://www.microsoft.com/en-us/haxtoolkit/pattern/g11-e-map-user-behaviors-to-system-outputs/):** Show how prior actions shaped personalization. Example: “Recommended because you saved three accessibility articles.” Respect privacy and let users remove signals or correct the inference.
- **[11F — Example-based explanations](https://www.microsoft.com/en-us/haxtoolkit/pattern/g11-f-example-based-explanations/):** Use comparable cases when examples communicate better than rules. Example: show similar approved applications and their relevant characteristics. Explain similarity, avoid privacy leakage, and represent meaningful diversity.
- **[11G — “What if?” explanations](https://www.microsoft.com/en-us/haxtoolkit/pattern/g11-g-what-if-explanations/):** Let users vary controllable inputs and inspect possible outcomes. Example: simulate how delivery time changes with a different address. Label estimates, avoid implying causality, and do not suggest manipulating protected or immutable attributes.

## Guideline 14: adaptation

- **[14A — Comprehensive updates](https://www.microsoft.com/en-us/haxtoolkit/pattern/g14-a-comprehensive-updates/):** Deliberately refresh the experience after sufficient new evidence. Example: rebuild a recommendation set after the user changes a major preference. Control rate and scale, communicate the change, and preserve orientation.
- **[14B — Immediate, partial, non-disruptive updates](https://www.microsoft.com/en-us/haxtoolkit/pattern/g14-b-immediate-partial-non-disruptive-updates/):** Locally update the affected part while retaining the prior context. Example: replace one rejected recommendation without reshuffling the page. Guard against cascading changes and make the update perceptible without stealing attention.

## Guideline 15: feedback

- **[15A — Encourage feedback on individual outputs](https://www.microsoft.com/en-us/haxtoolkit/pattern/g15-a-encourage-explicit-feedback-on-individual-system-outputs/):** Keep user-initiated feedback attached to the relevant item. Example: rate one generated answer and optionally explain why. Define how it will be used and account for self-selection bias.
- **[15B — Request feedback on selected outputs](https://www.microsoft.com/en-us/haxtoolkit/pattern/g15-b-request-explicit-feedback-on-selected-system-outputs/):** Ask at sampled, appropriate moments. Example: request a rating after a resolved support exchange. Avoid disruption, coercion, and sampling schemes that exclude important groups.
- **[15C — Report inappropriate content](https://www.microsoft.com/en-us/haxtoolkit/pattern/g15-c-reporting-inappropriate-content/):** Let users flag harmful, biased, wrong, or offensive output at item level. Example: report a generated image with a reason category. Establish review, urgency, abuse handling, and policy rather than treating every report as ground truth.
- **[15D — Use existing public ratings or interaction data](https://www.microsoft.com/en-us/haxtoolkit/pattern/g15-d-use-existing-public-rating-or-interaction-data-as-feedback-for-the-system/):** Reuse legitimate behavioral or rating signals when they fit the improvement goal. Example: use explicit “helpful” votes to evaluate retrieval quality. Confirm consent, representativeness, context, gaming resistance, and whether the signal measures what the team claims.

## Guideline 16: consequences

- **[16A — Feedforward before action](https://www.microsoft.com/en-us/haxtoolkit/pattern/g16-a-feedforward-convey-the-consequences-of-user-actions-before-the-user-takes-action/):** Preview what a user action will change. Example: “Disliking this removes similar items from this profile.” Be specific about scope, timing, and reversibility.
- **[16B — Feedback after action](https://www.microsoft.com/en-us/haxtoolkit/pattern/g16-b-feedback-convey-the-consequences-of-user-actions-after-the-user-takes-action/):** Confirm the actual effect immediately. Example: “Saved; future suggestions will use this preference.” Do not claim an effect the system cannot guarantee.
- **[16C — Reconfirm a past action’s consequences](https://www.microsoft.com/en-us/haxtoolkit/pattern/g16-c-remind-of-consequences-of-a-past-action-and-ask-for-reconfirmation/):** Re-surface a consequential prior choice when it becomes relevant again. Example: reconfirm that an old personalization preference should apply to a new workspace. Avoid repetitive prompts and preserve a clear change path.
- **[16D — Explain consequences in help and documentation](https://www.microsoft.com/en-us/haxtoolkit/pattern/g16-d-convey-the-consequences-of-user-action-in-help-and-documentation/):** Document persistent or complex effects that cannot fit inline. Example: explain how feedback enters review and model-improvement processes. Keep documentation discoverable, current, and consistent with actual behavior.

## Selection checklist

For any chosen pattern, document: guideline and user problem; applicability conditions; project evidence; UI/AI/data/engineering dependencies; accessibility; foreseeable misuse; failure and recovery; validation measure; source URL and retrieval date. Combine patterns only when the combined interaction remains understandable.
