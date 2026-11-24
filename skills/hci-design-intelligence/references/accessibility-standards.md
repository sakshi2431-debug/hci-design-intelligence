# Accessibility standards and inclusive practice

## Source authority

- Use [WCAG 2.2](https://www.w3.org/TR/WCAG22/) success criteria for normative web-content conformance. The [W3C overview](https://www.w3.org/WAI/standards-guidelines/wcag/) explains versions and supporting documents.
- Use [WAI-ARIA](https://www.w3.org/WAI/standards-guidelines/aria/) for accessibility semantics in dynamic content and custom controls.
- Use the [ARIA Authoring Practices Guide](https://www.w3.org/WAI/ARIA/apg/) for informative patterns and keyboard models. APG is not itself a normative standard.
- Use [WCAG-EM](https://www.w3.org/WAI/test-evaluate/conformance/wcag-em/) for an evaluation methodology and [W3C Cognitive Accessibility](https://www.w3.org/WAI/cognitive/) for supplemental guidance. Preserve their current publication status and do not silently present informative or draft material as normative.
- Prefer native HTML behavior and semantics. Incorrect ARIA can make the non-visual experience worse.
- Accessibility conformance is not the same as legal compliance or usable inclusion. Do not give legal conclusions.

## Disability framing

Distinguish models:

- **Medical model:** locates disability primarily in individual impairment; useful in some clinical/benefits contexts but can encourage “fix the person” framing.
- **Social model:** locates disability in barriers and mismatched environments; directs design toward removing exclusion.
- **Charity/tragedy model:** frames disabled people through pity or inspiration; avoid this representational pattern.
- **Interaction/mismatch framing:** disability occurs at the interaction between a person's capabilities and environmental demands.

Account for permanent, temporary, situational, visible, and non-visible disability and intersectional context. Ask rather than assume. Use identity- or person-first language according to individual/community preference.

Course provenance: `COURSE — Digital Accessibility.zip / Week 2 - Understanding Disability.pdf, pp. 39–57`.

## WCAG structure

WCAG 2.2 organizes testable success criteria under four principles:

1. **Perceivable:** alternatives, adaptable structure, distinguishable presentation, accessible media.
2. **Operable:** keyboard access, enough time, seizure/physical-reaction safety, navigation, input modalities.
3. **Understandable:** readable/predictable interfaces and error/input assistance.
4. **Robust:** compatible semantics and status communication across user agents and assistive technologies.

Conformance levels are A, AA, and AAA. Cite the exact success criterion and level. Do not call all Level A items “mandatory” without stating the chosen conformance target and jurisdiction/context.

## Design and test checklist

### Structure and semantics

- Logical headings and landmarks.
- Native elements for controls.
- Accurate accessible names, roles, values, descriptions, and states.
- Programmatic labels and instructions.
- Page language and meaningful reading order.

### Keyboard and focus

- All functionality operable without a pointer.
- Logical tab order, no trap, visible focus, and focus not obscured.
- Managed focus after dialogs, route changes, errors, deletion, and dynamic updates.
- Skip mechanisms and predictable composite-widget keyboard behavior.

### Visual and motion

- Text and non-text contrast at applicable WCAG thresholds.
- Meaning not conveyed by color alone.
- Reflow, zoom, text spacing, orientation, and responsive adaptation.
- Adequate target size and spacing.
- Reduced motion and no seizure-triggering flashes.

### Content and cognition

- Clear purpose, familiar hierarchy, consistent design, explicit steps, plain language.
- Do not rely unnecessarily on memory; preserve entered data and prevent redundant entry.
- Helpful, specific errors and recovery.
- Consistent help and accessible authentication.
- Support adaptation and personalization when appropriate.

### Media and non-text content

- Purpose-appropriate alt text; empty alternatives for decorative images.
- Captions, transcripts, and audio description as applicable.
- Text alternatives for charts that preserve the intended information and relationships.

### Screen readers

Users often navigate by headings, landmarks, links, controls, tables, and search—not by listening top-to-bottom. Test name/role/state, sequence, announcements, and efficient navigation. Distinguish visible keyboard focus from the screen reader's virtual or accessibility focus.

## Integrated product practice

Accessibility is shared responsibility. Establish policy, ownership, training, accessible authoring tools, design-system patterns, annotations, QA gates, bug tracking, and maintenance. Include disabled people in research and usability testing. Combine:

1. automated tools for detectable rules;
2. manual code/design review;
3. keyboard and assistive-technology testing;
4. usability research with disabled participants.

No single layer proves accessibility. Course provenance: `COURSE — Digital Accessibility.zip / Week 11 - Accessibility in Product Development.pdf, pp. 10–29, 41–50`.

For a formal audit scope, representative sampling, assistive-technology matrix, evidence record, and remediation retest, read [accessibility-evaluation.md](accessibility-evaluation.md).

## Universal and inclusive design

Universal design seeks broadly usable products/environments through equitable use, flexibility, simplicity, perceptible information, tolerance for error, low effort, and adequate size/space. Inclusive design explicitly asks who is excluded, learns with diversity, and “solves for one, extends to many.” Do not claim one solution literally works for everyone; support adaptation and alternatives.

Course provenance: `COURSE — Digital Accessibility.zip / Week 10 - Universal _ Inclusive Design.pdf, pp. 7–38`.
