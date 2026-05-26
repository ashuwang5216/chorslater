# Prompt Templates

Use these templates when translation requests lack structure.

## Template: High-Fidelity Translation

```text
Translate the following text from <source_language> to <target_language>.
Requirements:
1) Preserve meaning exactly; do not add new facts.
2) Keep names, numbers, units, and URLs unchanged.
3) Use natural <target_language> phrasing for a <audience> audience.
4) If a phrase is ambiguous, choose the safest interpretation and list one alternative briefly.
Text:
<source_text>
```

## Template: Low-Resource Pair With Domain Context

```text
Translate from <source_language> to <target_language> for the <domain> domain.
Priorities:
1) Terminology consistency
2) Instructional clarity
3) Cultural appropriateness
Output:
- Final translation
- Optional risk notes only for unresolved ambiguity
Text:
<source_text>
```

## Template: Code-Switched Input

```text
The input mixes multiple languages. Translate to <target_language>.
Rules:
1) Detect and preserve embedded entities (product names, IDs, code tokens).
2) Normalize only language content, not technical tokens.
3) Keep sentence intent and politeness level consistent.
Text:
<source_text>
```
