# Design-token standards

Use the [Design Tokens Format Module 2025.10](https://www.designtokens.org/TR/2025.10/format/) as the stable interchange reference. It is a Final Community Group Report intended for implementation, not a W3C Recommendation. Do not implement from a preview editor's draft when a stable published version is required.

## Core format rules

- Use JSON token files with token names mapped to objects containing `$value`.
- Provide or inherit an unambiguous `$type`; tools must not guess a type from a value.
- Use `$description` for purpose and usage, not merely the visual value.
- Preserve unknown `$extensions` data across round trips.
- Use `$deprecated` with a replacement or migration reason when applicable.
- Prevent circular references and validate aliases before transforming tokens.
- Treat groups as organization, not evidence of token type or semantic purpose.

Before generating a file, verify the exact published version and any target-tool compatibility requirements.

## Architecture

The DTCG format defines exchange semantics; it does not require a particular organizational taxonomy. Use primitive → semantic → component layers when they improve governance and theming, but avoid component layers that merely duplicate semantic values without a maintenance benefit.

For each token record purpose, modes/themes, accessibility constraints, owner, lifecycle status, and downstream mappings. Keep behavior, content, anatomy, states, and accessibility specifications in component documentation rather than forcing them into visual tokens.

## Validation

Validate schema/structure, types, references, cycles, allowed units, color representation, naming, deprecation, mode completeness, and round-trip preservation. Then validate product outcomes: contrast, legibility, forced colors, dark mode, text scaling, motion preferences, localization, platform adaptation, and component states.

