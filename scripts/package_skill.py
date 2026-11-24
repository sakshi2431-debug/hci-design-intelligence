#!/usr/bin/env python3
"""Package the canonical Agent Skill as a portable ZIP."""

from __future__ import annotations

import subprocess
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "hci-design-intelligence"
DIST = ROOT / "dist"
OUTPUT = DIST / "hci-design-intelligence.zip"


def main() -> None:
    subprocess.run(
        ["python3", str(ROOT / "scripts" / "validate_repo.py")], check=True
    )
    DIST.mkdir(exist_ok=True)
    with zipfile.ZipFile(OUTPUT, "w", zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(SKILL.rglob("*")):
            if path.is_file():
                archive.write(path, Path(SKILL.name) / path.relative_to(SKILL))
        for notice in ("LICENSE.md", "NOTICE.md"):
            archive.write(ROOT / notice, Path(SKILL.name) / notice)
    print(f"Created {OUTPUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
