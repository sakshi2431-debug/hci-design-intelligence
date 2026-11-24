# Architecture

## One source of truth

`skills/hci-design-intelligence/` is the canonical, model-neutral skill. Platform manifests point to or discover that same directory; they do not fork its HCI logic.

The main `SKILL.md` is the control and routing layer. References hold deeper knowledge and are loaded progressively. Licenses live beside the material they govern.

## Adapter boundary

- `agents/openai.yaml` supplies OpenAI/Codex interface metadata only.
- `gemini-extension.json` makes the repository installable by Gemini CLI, which discovers `skills/`.
- `plugin.json` identifies the repository as a portable agent plugin.
- `adapters/generic/SYSTEM-PROMPT.md` bootstraps products that do not implement Agent Skills.

Adapters must not redefine HCI behavior. A platform-specific improvement belongs in an adapter only when it concerns discovery, installation, invocation, or interface metadata.

## Deliberate exclusions

This public core includes original, public-safe coursework syntheses but no private course files, student work, licensed course archives, or embedded copy of UI/UX Pro Max. Private layers and separate tools may be used locally, but the public skill remains usable and attributable on its own.

Visual-design and implementation tools are optional downstream capabilities. They do not outrank people-centered requirements, research evidence, accessibility, or system safeguards.
