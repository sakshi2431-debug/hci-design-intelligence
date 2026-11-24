#!/usr/bin/env python3
"""Build compact Markdown bundles for hosts without Agent Skills support."""

from __future__ import annotations

import argparse
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "hci-design-intelligence"
DIST = ROOT / "dist"
PROFILES = {
    "core": [
        "hci-foundations.md",
        "people-centered-product-design.md",
        "output-patterns.md",
    ],
    "ai": [
        "human-ai-interaction.md",
        "ai-product-discovery.md",
        "ai-facilitation-and-decision-canvas.md",
        "agentic-workflows-and-human-control.md",
        "ai-security-and-secure-interaction.md",
        "ai-agent-evaluation.md",
    ],
    "research": [
        "research-and-evaluation.md",
        "research-rigor.md",
        "behavioral-evidence-and-triangulation.md",
        "learning-skill-and-behavioral-assessment.md",
    ],
    "accessibility": [
        "accessibility-standards.md",
        "accessibility-evaluation.md",
        "interaction-state-error-and-handoff.md",
    ],
    "product": [
        "people-centered-product-design.md",
        "product-critique-and-design-judgment.md",
        "design-exploration-and-preference-learning.md",
        "design-operations-governance-and-influence.md",
        "ethics-privacy-deceptive-design.md",
    ],
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--profile", choices=[*PROFILES, "all"], default="core")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    subprocess.run(
        ["python3", str(ROOT / "scripts" / "validate_repo.py")], check=True
    )
    DIST.mkdir(exist_ok=True)
    reference_dir = SKILL / "references"
    names = (
        [path.name for path in sorted(reference_dir.glob("*.md"))]
        if args.profile == "all"
        else PROFILES[args.profile]
    )
    files = [
        ROOT / "adapters" / "generic" / "SYSTEM-PROMPT.md",
        SKILL / "SKILL.md",
        *(reference_dir / name for name in names),
    ]
    suffix = "" if args.profile == "core" else f"-{args.profile}"
    output = DIST / f"hci-design-intelligence-bundle{suffix}.md"
    sections = [
        f"# HCI Design Intelligence — {args.profile} bundle\n",
        "> Generated from the canonical skill. Preserve source headings and provenance. Load only for relevant tasks.\n",
    ]
    for path in files:
        label = path.relative_to(ROOT)
        sections.append(f"\n---\n\n<!-- SOURCE: {label} -->\n\n")
        sections.append(path.read_text(encoding="utf-8").rstrip() + "\n")
    output.write_text("".join(sections), encoding="utf-8")
    print(f"Created {output.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
