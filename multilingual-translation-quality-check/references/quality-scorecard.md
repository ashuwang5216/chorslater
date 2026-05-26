# Quality Scorecard

Use a 100-point weighted score.

## Dimension Weights

- Adequacy (40): preserve source meaning, logic, and intent.
- Fluency (20): read naturally in target language.
- Terminology (20): follow glossary and domain terms.
- Cultural and safety fit (20): avoid offensive, unsafe, or context-breaking phrasing.

## Scoring Rules

- Start at full points in each dimension.
- Subtract based on issue severity and frequency.
- Cap each dimension at a minimum of 0.

## Suggested Deductions

- Critical issue: minus 15 to 25 per issue.
- Major issue: minus 6 to 12 per issue.
- Minor issue: minus 1 to 5 per issue.

## Decision Thresholds

- `pass`: score >= 90 and no critical issue.
- `pass-with-fixes`: score 75-89 and no unresolved critical issue.
- `fail`: score < 75 or at least one unresolved critical issue.
