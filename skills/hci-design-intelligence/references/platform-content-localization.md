# Platform guidance, content, and localization

Read this reference when a recommendation depends on operating system, device family, input method, language, region, or interface copy.

## First-party platform sources

- Apple: [Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/)
- Android and Material: [Material Design](https://m3.material.io/)
- Microsoft: [Fluent 2](https://fluent2.microsoft.design/)
- Web semantics: [HTML Living Standard](https://html.spec.whatwg.org/)

Platform guidance changes. Verify the current page and supported OS/framework version before implementation. Do not transfer an Apple, Android, Fluent, or web convention to another platform without explaining why it remains appropriate.

## Platform adaptation

Identify device, viewport, posture, input, output, interruption model, permissions, navigation conventions, system settings, and assistive technologies. Preserve the product's conceptual model and brand while respecting native expectations for controls, navigation, selection, dialogs, menus, back behavior, keyboard shortcuts, notifications, and destructive actions.

Responsive design is not only resizing. Reevaluate information priority, input effort, reach, focus order, content density, environmental use, latency, and continuity across devices.

## Content design

- Start from the user task and information need.
- Give controls specific labels that describe their action or outcome.
- Place instructions before the action they govern and errors near the cause.
- Use plain, direct language without erasing necessary technical or legal precision.
- Keep terminology consistent with the user's domain and conceptual model.
- Make status, waiting, risk, consequences, and recovery explicit.
- Test copy inside complete states and flows, not in a spreadsheet alone.

Voice and tone may vary with context; terminology and factual meaning should remain stable. Urgent, destructive, financial, health, privacy, and safety interactions need especially clear consequences and recovery.

## Internationalization and localization

Design source content and components for translation, expansion, contraction, plurals, grammatical gender, names, addresses, numbers, currencies, dates, calendars, time zones, units, sorting, search, and bidirectional text. Do not concatenate fragments that translators cannot reorder.

Test:

- long and compact translations;
- right-to-left layout and mixed-direction content;
- user-entered names and addresses without culturally narrow validation;
- locale-specific formatting and time-zone boundaries;
- icons, color, examples, humor, imagery, gestures, and metaphors across cultures;
- screen-reader language changes and pronunciation;
- truncation, wrapping, tables, charts, filters, and error messages.

Localization quality requires native-language review in context. Automatic translation can support exploration but is not final evidence of correctness or cultural suitability.

