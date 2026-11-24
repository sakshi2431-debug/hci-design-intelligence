# HCI Design Intelligence

A model-agnostic, people-centered HCI and product-design skill for designing useful, viable, accessible, responsible products—including AI and agentic systems.

Created and maintained by **Sakshir**.

## What this repository does

The repository keeps one canonical body of HCI knowledge and exposes it through platform adapters. It helps an AI collaborator:

- frame products around people's goals, context, rights, and wellbeing;
- balance human value with legitimate growth, engagement, and business outcomes;
- reason from HCI theory, research evidence, accessibility standards, and product constraints;
- use original interactive discovery prompts informed by Microsoft HAX and Google PAIR;
- allocate work and authority between people and agents action by action;
- design research, critique experiences, define guardrails, and evaluate behavior;
- distinguish observations, evidence, heuristics, assumptions, and recommendations.

It does **not** bundle UI/UX Pro Max, private course archives, or course-derived notes. Visual-design and implementation systems can be used separately after human, interaction, and system requirements are established.

## Repository structure

```text
skills/hci-design-intelligence/  Canonical Agent Skill and public references
adapters/generic/                Bootstrap prompt for other LLM products
docs/                            Architecture, provenance, and platform notes
scripts/                         Validation and packaging helpers
gemini-extension.json            Gemini CLI extension manifest
plugin.json                      Portable agent-plugin manifest
```

## Install

### Codex

```bash
gh skill install sakshi2431-debug/hci-design-intelligence hci-design-intelligence --agent codex --scope user
```

### Claude Code

```bash
gh skill install sakshi2431-debug/hci-design-intelligence hci-design-intelligence --agent claude-code --scope user
```

### Gemini CLI

Install the repository as an extension:

```bash
gemini extensions install https://github.com/sakshi2431-debug/hci-design-intelligence
```

Or install only the skill through the Agent Skills installer:

```bash
gh skill install sakshi2431-debug/hci-design-intelligence hci-design-intelligence --agent gemini-cli --scope user
```

### ChatGPT / API agents

Create a portable skill ZIP, then upload the result wherever Agent Skills are accepted:

```bash
python3 scripts/package_skill.py
```

The artifact is written to `dist/hci-design-intelligence.zip` with one top-level skill directory.

### Other LLM products

Build a compact core bundle, or a domain profile for a host without file retrieval:

```bash
python3 scripts/build_generic_bundle.py
python3 scripts/build_generic_bundle.py --profile ai
```

Profiles are `core`, `ai`, `research`, `accessibility`, `product`, and `all`. Use the generated bundle as project knowledge alongside `adapters/generic/SYSTEM-PROMPT.md`. Prefer the canonical `SKILL.md` with progressive reference retrieval whenever the host supports files.

## Invoke it

On skill-aware platforms, ask naturally or invoke `$hci-design-intelligence` explicitly. Examples:

- “Use HCI Design Intelligence to pressure-test this onboarding idea.”
- “Help me decide what the agent may do automatically and when it must ask.”
- “Run the AI product discovery questions with me, one at a time.”
- “Critique this flow for accessibility, human control, growth ethics, and failure recovery.”

## Validate

```bash
python3 scripts/validate_repo.py
```

The validation checks the skill manifest, manifests for supported hosts, forbidden private/bundled material, broken local links, and package structure.

Prepare the model-agnostic behavioral evaluation run file with:

```bash
python3 scripts/eval_suite.py prepare
```

See `evals/README.md` for scoring and release gates.

## Build the GitHub-ready repository

```bash
python3 scripts/package_repository.py
```

The result is `dist/hci-design-intelligence-repository.zip`. It contains the tracked repository files without Git history or generated artifacts and can be uploaded into a new GitHub repository.

## Provenance and licensing

Every source family has an explicit epistemic role and provenance. See [docs/provenance.md](docs/provenance.md), [NOTICE.md](NOTICE.md), and [LICENSE.md](LICENSE.md).

Original prose is CC BY 4.0 and scripts/configuration are MIT licensed. PAIR is cited as an influence; this release does not redistribute or adapt PAIR text or worksheets. Preserved upstream notices remain applicable to the specific derived material they identify.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Additions must improve people-centered product reasoning, preserve source provenance, and pass validation.
