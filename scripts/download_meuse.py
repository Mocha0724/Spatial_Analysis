#!/usr/bin/env python3
"""Download the Meuse soil sample dataset (tabular copy derived from R `sp::meuse`) as CSV."""

from __future__ import annotations

import argparse
import hashlib
import urllib.request
from pathlib import Path

# Gist-hosted CSV mirror (columns match common R `meuse` exports: x,y in Dutch RD / EPSG:28992).
DEFAULT_URL = (
    "https://gist.githubusercontent.com/essicolo/"
    "91a2666f7c5972a91bca763daecdc5ff/raw/meuse.csv"
)

# Optional integrity check (SHA-256 of file as of vendoring); update if upstream gist changes.
EXPECTED_SHA256: str | None = (
    "aca2070a2dfaa9590cadbf9dde3ecec230882b7682dc3f910091a21c0e51f0c2"
)


def download(url: str, dest: Path) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    with urllib.request.urlopen(url, timeout=120) as resp:
        data = resp.read()
    if EXPECTED_SHA256 is not None:
        digest = hashlib.sha256(data).hexdigest()
        if digest != EXPECTED_SHA256:
            raise RuntimeError(
                f"SHA-256 mismatch: got {digest}, expected {EXPECTED_SHA256}"
            )
    dest.write_bytes(data)
    print(f"Wrote {dest} ({len(data)} bytes)")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--url",
        default=DEFAULT_URL,
        help="Source URL for meuse.csv",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default=Path(__file__).resolve().parent.parent / "data" / "processed" / "meuse.csv",
        help="Output CSV path",
    )
    args = parser.parse_args()
    download(args.url, args.output)


if __name__ == "__main__":
    main()
