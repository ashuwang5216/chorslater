---
name: low-resource-translation
description: High-accuracy translation workflow for low-resource languages, code-switched text, and culturally dense content. Use when translating smaller-language pairs (for example Uyghur, Lao, Khmer, Amharic, Burmese, Nepali, Kazakh, Yoruba), when literal translation is risky, or when the user asks for higher fidelity and ambiguity handling.
---

# Low Resource Translation

## Goal

Produce faithful, context-aware translations for low-resource language pairs while reducing semantic drift and hallucinated meaning.

## Workflow

1. Lock translation constraints before drafting.
- Capture source language, target language, locale, audience, domain, and required tone.
- Ask for intended usage if unknown: legal, medical, product UI, marketing, or casual text.

2. Detect risk factors early.
- Scan for code-switching, named entities, idioms, cultural references, honorifics, and ambiguous pronouns.
- Read `references/language-risk-checklist.md` when high-risk patterns appear.

3. Build a small translation memory for this request.
- Extract terms, acronyms, product names, and numbers that must stay stable.
- Preserve names, units, IDs, URLs, and formatting unless the user asks otherwise.

4. Translate by meaning, not by token position.
- Prioritize semantic equivalence, then style equivalence.
- Keep sentence boundaries adjustable if the target language needs reordering for clarity.

5. Perform self-review and repair.
- Check omission, addition, polarity reversal, number mismatch, and register mismatch.
- Run a second pass focused only on mistranslation and ambiguity.

6. Return concise delivery plus uncertainty notes.
- Provide final translation first.
- Add a short "risk notes" block only when uncertainty remains or alternatives are plausible.

## Output Template

Use this structure unless the user requests a different format:

```text
Translation:
<final text>

Risk notes (only if needed):
- <term/phrase>: <reason it is ambiguous>
- Preferred rendering: <chosen option>
- Alternate rendering: <optional alternate>
```

## Reference Files

- Read `references/language-risk-checklist.md` for language-specific pitfalls and safeguards.
- Read `references/prompt-templates.md` for reusable prompt frames when the request is underspecified.
