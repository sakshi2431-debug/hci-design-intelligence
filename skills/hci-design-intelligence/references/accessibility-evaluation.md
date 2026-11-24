# Accessibility evaluation

Use this reference for an audit plan, conformance evaluation, assistive-technology test, accessibility research study, or remediation verification. Read [accessibility-standards.md](accessibility-standards.md) first for standards and disability framing.

## Status-aware sources

- Use [WCAG 2.2](https://www.w3.org/TR/WCAG22/) as the normative web-content baseline unless the task names another required version.
- Use [WCAG-EM 2.0](https://www.w3.org/TR/wcag-em-2/) for the evaluation process. It became a W3C Group Note on 23 July 2026: informative guidance endorsed by the Accessibility Guidelines Working Group, not a W3C Recommendation. Use WCAG-EM 1.0 (2014) only when an audit was contracted against it. Status checked 2026-11-23.
- Use [ARIA Authoring Practices Guide](https://www.w3.org/WAI/ARIA/apg/) as informative pattern guidance, not proof of conformance.
- Use [W3C Cognitive Accessibility](https://www.w3.org/WAI/cognitive/) as supplemental guidance beyond the minimum WCAG requirements; label it informative.

Verify current document status at the time of a formal audit.

## Evaluation protocol

1. Define product, pages/views, states, flows, technologies, languages, platforms, conformance target, exceptions, and evidence required.
2. Explore the product to identify templates, critical paths, components, dynamic states, authentication, errors, documents, media, and third-party content.
3. Select a representative sample plus complete critical processes and randomly selected material when appropriate.
4. Evaluate each applicable criterion using documented techniques, manual judgment, and the relevant assistive technologies.
5. Record reproducible evidence: environment, steps, expected result, actual result, criterion, impact, affected users, screenshots/code where permitted, and remediation guidance.
6. Retest the repaired component and adjacent variants; do not close a defect from code inspection alone.
7. Report scope and limitations. Never extrapolate an evaluated sample into an unqualified whole-product claim.

## Minimum manual matrix

Adapt to the actual audience and platform:

| Modality | Representative checks |
|---|---|
| Keyboard | complete flows, order, traps, shortcuts, visible/unobscured focus, skip paths, drag alternatives |
| Screen reader | names, roles, states, reading order, headings/landmarks, errors, status updates, tables, dialogs |
| Vision | zoom, text resize/spacing, reflow, contrast, non-color cues, magnification, forced colors |
| Motor/touch | target size and spacing, pointer alternatives, path gestures, timing, orientation, accidental activation |
| Hearing/media | captions, transcripts, audio description, visual equivalents, media controls |
| Cognitive/language | purpose, consistency, plain language, error prevention, saved progress, authentication, help |
| Motion | reduced-motion preference, pause/stop, flashing, vestibular triggers |

Use combinations representative of the supported environment—for example VoiceOver/Safari, NVDA/Firefox or Chrome, JAWS/Chrome or Edge, and TalkBack/Chrome—but treat this as a maintained test matrix, not a timeless universal list.

## Automated testing

Automated tools can find only machine-detectable conditions. Record the tool, ruleset, configuration, browser, date, and false-positive/false-negative review. Automated success does not establish WCAG conformance, accessible interaction, or usability.

## Research with disabled participants

Recruit for relevant access needs and technology experience without treating one participant as representative of a disability. Make recruitment, consent, scheduling, prototypes, remote platforms, tasks, compensation, and reporting accessible. Allow personal assistive technology and preferred communication. Distinguish a prototype limitation from a participant difficulty and avoid asking participants to disclose unnecessary medical information.

## Severity

Prioritize by blocked or degraded critical task, safety or rights impact, absence of workaround, reach across templates/components, frequency, persistence, and remediation dependency. Conformance level alone is not a complete severity model.

