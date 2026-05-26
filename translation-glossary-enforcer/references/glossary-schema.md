# Glossary Schema

Use JSON format for deterministic checks with `scripts/glossary_guard.py`.

## Supported Structure

```json
{
  "entries": [
    {
      "source": "cloud service",
      "preferred": "cloud platform",
      "forbidden": ["cloud solution", "cloud stack"]
    }
  ]
}
```

## Field Rules

- `preferred` (required): final term that must appear in translated output.
- `forbidden` (optional): list of banned variants that should trigger violations.
- `source` (optional): original language reference term for translator context.

## Normalization Guidance

- Keep one concept per entry.
- Separate near-synonyms into `forbidden` only when policy requires strict lock.
- Keep capitalization style exactly as user policy requires.

## Review Checklist

- Ensure each required concept has a preferred term.
- Ensure forbidden variants do not include the preferred term itself.
- Ensure product names and legal phrases are included before translation starts.
