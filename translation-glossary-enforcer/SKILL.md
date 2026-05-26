---
name: translation-glossary-enforcer
description: Glossary-driven translation enforcement workflow that keeps preferred terms consistent across multilingual output. Use when a user provides terminology rules, style guides, or forbidden variants and asks for stricter translation consistency in product, legal, technical, or localization content.
---

# Translation Glossary Enforcer

## Goal

Enforce terminology consistency so translated output follows preferred terms and avoids banned variants.

## Workflow

1. Ingest terminology policy.
- Read glossary, style guide, or terminology spreadsheet from the user.
- Normalize into the schema documented in `references/glossary-schema.md`.

2. Translate with glossary lock.
- Apply preferred terms deterministically when semantic context matches.
- Keep brand names, feature names, and legal terms identical across all segments.

3. Run mechanical consistency checks.
- Execute `scripts/glossary_guard.py` against the translated text.
- Treat every forbidden-variant hit as a blocking issue.

4. Repair and recheck.
- Replace forbidden terms with preferred terms.
- Rerun the check until no blocking issue remains.

5. Deliver final output plus a change log.
- Return cleaned translation.
- Add a short list of enforced terms that were corrected.

## Quick Command

Use this pattern to run the checker:

```text
python scripts/glossary_guard.py --glossary <path-to-glossary.json> --translation <path-to-translation.txt>
```

## Reference Files

- Read `references/glossary-schema.md` before building or converting glossary files.
