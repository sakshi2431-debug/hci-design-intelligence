#!/usr/bin/env python3
"""Create a GitHub-ready ZIP from tracked repository files."""

from __future__ import annotations

import subprocess
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
OUTPUT = DIST / "hci-design-intelligence-repository.zip"
TOP = Path("hci-design-intelligence")


def main() -> None:
    subprocess.run(
        ["python3", str(ROOT / "scripts" / "validate_repo.py")], check=True
    )
    tracked = subprocess.run(
        ["git", "ls-files", "-z", "--cached", "--others", "--exclude-standard"],
        cwd=ROOT,
        check=True,
        capture_output=True,
    ).stdout.split(b"\0")
    paths = [ROOT / raw.decode("utf-8") for raw in tracked if raw]
    DIST.mkdir(exist_ok=True)
    with zipfile.ZipFile(OUTPUT, "w", zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(paths):
            if path.is_file() and "dist" not in path.relative_to(ROOT).parts:
                archive.write(path, TOP / path.relative_to(ROOT))
    print(f"Created {OUTPUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
