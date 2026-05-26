---
name: multilingual-translation-quality-check
description: Translation QA workflow for scoring multilingual output across adequacy, fluency, terminology, and cultural safety. Use when the user asks to review translation quality, compare candidate translations, perform final linguistic QA, or reduce risk before publishing localized content.
---

# Multilingual Translation Quality Check

## Goal

Audit multilingual translations with a repeatable scorecard and clear fix priorities.

## Workflow

1. Set evaluation context.
- Capture source text, candidate translation, target locale, domain, and publishing channel.
- Capture style constraints: formal/informal, legal precision, UI brevity, or marketing tone.

2. Score translation quality.
- Apply the rubric in `references/quality-scorecard.md`.
- Evaluate adequacy, fluency, terminology, and cultural safety separately.

3. Classify errors by severity.
- Use `references/error-taxonomy.md` to label issues as critical, major, or minor.
- Treat safety, compliance, and meaning-reversal errors as critical.

4. Produce repair guidance.
- Provide exact segment-level fixes, not generic advice.
- Prefer minimal edits that recover meaning while preserving natural flow.

5. Return a publication decision.
- Output one of: pass, pass-with-fixes, fail.
- Fail when any critical error exists or score is below threshold.

## Output Template

Use this structure unless the user requests another format:

```text
Decision: <pass | pass-with-fixes | fail>
Score: <0-100>

Findings:
- [Severity] <issue>

Required fixes:
1. <segment + correction>
2. <segment + correction>

Optional improvements:
- <style or fluency improvement>
```

## Reference Files

- Read `references/quality-scorecard.md` for weighted scoring.
- Read `references/error-taxonomy.md` for consistent severity labeling.
