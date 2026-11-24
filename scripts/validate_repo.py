#!/usr/bin/env python3
"""Validate repository structure, portability, provenance boundaries, and links."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "hci-design-intelligence"
MAIN = SKILL / "SKILL.md"

REQUIRED = [
    ROOT / "README.md",
    ROOT / "LICENSE.md",
    ROOT / "NOTICE.md",
    ROOT / "plugin.json",
    ROOT / "gemini-extension.json",
    MAIN,
    SKILL / "agents" / "openai.yaml",
    SKILL / "licenses" / "ACKNOWLEDGEMENTS.md",
    ROOT / "evals" / "cases.json",
    ROOT / "evals" / "README.md",
    ROOT / "scripts" / "eval_suite.py",
    ROOT / "scripts" / "package_repository.py",
]

FORBIDDEN = [
    re.compile(r"course-[a-z0-9-]+\.md", re.I),
    re.compile(r"Pratt Material", re.I),
    re.compile(r"vendor/ui-ux-pro-max", re.I),
    re.compile(r"Human Clarity Institute", re.I),
    re.compile(r"masteraba\.academy", re.I),
    re.compile(r"passagehealth\.com", re.I),
    re.compile(r"aiuxplayground\.com", re.I),
]

LEGACY_PAIR_FILES = {
    "pair-guidebook.md",
    "pair-patterns-and-cases.md",
    "pair-worksheets.md",
    "hax-pair-interactive-facilitation.md",
    "PAIR-ATTRIBUTION.md",
}

LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")


def frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        raise ValueError("SKILL.md must begin with YAML frontmatter")
    try:
        raw = text.split("---\n", 2)[1]
    except IndexError as exc:
        raise ValueError("SKILL.md frontmatter is not closed") from exc
    result: dict[str, str] = {}
    for line in raw.splitlines():
        if line and not line.startswith((" ", "\t")) and ":" in line:
            key, value = line.split(":", 1)
            result[key.strip()] = value.strip().strip('"')
    return result


def main() -> int:
    errors: list[str] = []

    for path in REQUIRED:
        if not path.is_file():
            errors.append(f"missing required file: {path.relative_to(ROOT)}")

    if not MAIN.is_file():
        print("\n".join(errors), file=sys.stderr)
        return 1

    text = MAIN.read_text(encoding="utf-8")
    try:
        meta = frontmatter(text)
    except ValueError as exc:
        errors.append(str(exc))
        meta = {}

    if meta.get("name") != SKILL.name:
        errors.append("frontmatter name must equal the parent skill directory")
    if not meta.get("description"):
        errors.append("frontmatter description is required")
    if len(text.splitlines()) > 500:
        errors.append("SKILL.md must stay at or below 500 lines")

    version_match = re.search(r'^\s+version:\s*["\']?([^"\'\s]+)', text, re.M)
    version = version_match.group(1) if version_match else None
    if not version:
        errors.append("metadata.version is required in SKILL.md")
    for manifest in (ROOT / "plugin.json", ROOT / "gemini-extension.json"):
        try:
            data = json.loads(manifest.read_text(encoding="utf-8"))
            if data.get("name") != "hci-design-intelligence":
                errors.append(f"incorrect name in {manifest.name}")
            if data.get("version") != version:
                errors.append(f"version mismatch in {manifest.name}")
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"invalid {manifest.name}: {exc}")

    text_files = [
        path
        for path in list(ROOT.rglob("*.md")) + list(ROOT.rglob("*.yaml"))
        if "dist" not in path.relative_to(ROOT).parts
    ]
    for path in text_files:
        body = path.read_text(encoding="utf-8")
        if "references/course-" not in body and path.name != "CONTRIBUTING.md":
            for pattern in FORBIDDEN:
                if pattern.search(body):
                    errors.append(
                        f"forbidden private or bundled dependency reference in {path.relative_to(ROOT)}: {pattern.pattern}"
                    )
        for target in LINK.findall(body):
            clean = target.split("#", 1)[0].strip()
            if not clean or re.match(r"^(https?://|mailto:|#)", clean):
                continue
            clean = clean.strip("<>")
            resolved = (path.parent / clean).resolve()
            if not resolved.exists():
                errors.append(
                    f"broken local link in {path.relative_to(ROOT)}: {target}"
                )

    for path in SKILL.rglob("*"):
        if path.name in LEGACY_PAIR_FILES:
            errors.append(f"legacy PAIR adaptation remains: {path.relative_to(ROOT)}")

    try:
        cases = json.loads((ROOT / "evals" / "cases.json").read_text(encoding="utf-8"))
        if cases.get("version") != version:
            errors.append("evaluation suite version must match SKILL.md")
        ids = [case.get("id") for case in cases.get("cases", [])]
        if not ids or len(ids) != len(set(ids)):
            errors.append("evaluation cases must exist and have unique IDs")
        for case in cases.get("cases", []):
            for field in ("id", "kind", "risk", "prompt", "required", "prohibited"):
                if field not in case:
                    errors.append(f"evaluation case missing {field}: {case.get('id', 'unknown')}")
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"invalid evals/cases.json: {exc}")

    try:
        citation = (ROOT / "CITATION.cff").read_text(encoding="utf-8")
        if f'version: "{version}"' not in citation:
            errors.append("version mismatch in CITATION.cff")
    except OSError as exc:
        errors.append(f"invalid CITATION.cff: {exc}")

    if not any((SKILL / "references").glob("*.md")):
        errors.append("skill must contain progressive reference files")

    if errors:
        print("Validation failed:", file=sys.stderr)
        for error in sorted(set(errors)):
            print(f"- {error}", file=sys.stderr)
        return 1

    print(
        f"Validated {SKILL.name}: {len(text.splitlines())} SKILL.md lines, "
        f"{len(list((SKILL / 'references').glob('*.md')))} references."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
