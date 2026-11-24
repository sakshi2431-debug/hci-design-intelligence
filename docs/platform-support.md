# Platform support

| Platform | Native path | Repository support |
|---|---|---|
| Codex | Agent Skills | Canonical skill plus `agents/openai.yaml` |
| ChatGPT/API agents | Uploaded Agent Skill | `scripts/package_skill.py` creates a portable ZIP |
| Claude Code | Agent Skills | Canonical skill follows the open Agent Skills specification |
| Gemini CLI | Extensions and Agent Skills | Root extension manifest plus canonical `skills/` directory |
| Other LLM products | Project knowledge/system instructions | Generic bootstrap and generated Markdown bundle |

The canonical skill uses only portable Markdown and relative links. Optional packaging scripts use the Python standard library.

Platform behavior and installation commands can change. Validate against the official host documentation before a release.
