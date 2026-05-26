#!/usr/bin/env python3
"""Check translated text for glossary violations."""

from __future__ import annotations

import argparse
from collections.abc import Iterable
import json
import re
import sys
from pathlib import Path


def load_glossary(path: Path) -> list[dict]:
    data = json.loads(path.read_text(encoding="utf-8-sig"))
    if isinstance(data, dict):
        entries = data.get("entries", [])
    elif isinstance(data, list):
        entries = data
    else:
        raise ValueError("Glossary JSON must be a list or an object with 'entries'.")

    normalized = []
    for index, item in enumerate(entries, start=1):
        if not isinstance(item, dict):
            raise ValueError(f"Entry #{index} must be an object.")
        preferred = str(item.get("preferred", "")).strip()
        if not preferred:
            raise ValueError(f"Entry #{index} is missing 'preferred'.")
        forbidden_raw = item.get("forbidden", [])
        if isinstance(forbidden_raw, str):
            forbidden = [forbidden_raw.strip()] if forbidden_raw.strip() else []
        elif isinstance(forbidden_raw, Iterable):
            forbidden = [str(x).strip() for x in forbidden_raw if str(x).strip()]
        else:
            raise ValueError(f"Entry #{index} has invalid 'forbidden' value.")
        forbidden = [term for term in forbidden if term != preferred]
        normalized.append(
            {
                "preferred": preferred,
                "forbidden": forbidden,
                "source": str(item.get("source", "")).strip(),
            }
        )
    return normalized


def find_violations(text: str, glossary: list[dict]) -> list[dict]:
    violations = []
    lines = text.splitlines()
    for line_no, line in enumerate(lines, start=1):
        for entry in glossary:
            preferred = entry["preferred"]
            for forbidden in entry["forbidden"]:
                pattern = re.escape(forbidden)
                for match in re.finditer(pattern, line, flags=re.IGNORECASE):
                    start = max(match.start() - 24, 0)
                    end = min(match.end() + 24, len(line))
                    snippet = line[start:end]
                    violations.append(
                        {
                            "line": line_no,
                            "forbidden": forbidden,
                            "preferred": preferred,
                            "snippet": snippet,
                        }
                    )
    return violations


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Detect forbidden glossary variants in translated text."
    )
    parser.add_argument("--glossary", required=True, help="Path to glossary JSON")
    parser.add_argument("--translation", required=True, help="Path to translated text file")
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output JSON report instead of plain text",
    )
    args = parser.parse_args()

    glossary_path = Path(args.glossary).resolve()
    translation_path = Path(args.translation).resolve()

    if not glossary_path.exists():
        print(f"[ERROR] Glossary file not found: {glossary_path}", file=sys.stderr)
        return 1
    if not translation_path.exists():
        print(f"[ERROR] Translation file not found: {translation_path}", file=sys.stderr)
        return 1

    try:
        glossary = load_glossary(glossary_path)
    except Exception as exc:
        print(f"[ERROR] Failed to load glossary: {exc}", file=sys.stderr)
        return 1

    text = translation_path.read_text(encoding="utf-8-sig")
    violations = find_violations(text, glossary)

    report = {
        "glossary_file": str(glossary_path),
        "translation_file": str(translation_path),
        "violation_count": len(violations),
        "violations": violations,
    }

    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        if not violations:
            print("No glossary violations found.")
        else:
            print(f"Found {len(violations)} violation(s):")
            for item in violations:
                print(
                    f"- line {item['line']}: forbidden '{item['forbidden']}' -> use '{item['preferred']}'"
                )

    return 0 if not violations else 2


if __name__ == "__main__":
    raise SystemExit(main())
