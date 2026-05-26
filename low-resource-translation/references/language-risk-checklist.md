# Language Risk Checklist

Use this checklist before finalizing a translation for low-resource or mixed-language content.

## Meaning Risks

- Pronoun ambiguity: clarify gender, number, or politeness when source pronouns are underspecified.
- Negation scope: verify that "not", "never", and exception clauses stay intact.
- Temporal ambiguity: preserve tense and event order, especially in procedural text.
- Modality drift: distinguish must/should/may and avoid softening hard requirements.

## Cultural and Pragmatic Risks

- Idioms: convert to natural target-language meaning, not literal words.
- Honorifics and formality: align with social hierarchy and user intent.
- Religious and historical references: avoid over-normalizing culturally loaded terms.
- Speech-level mismatch: check for too formal or too casual rendering.

## Named Entity and Format Risks

- Person and place names: keep canonical spelling or accepted local transliteration.
- Product terms: keep official brand casing and punctuation.
- Numbers, dates, units, currency: preserve values; localize presentation only when requested.
- Links, IDs, code snippets: keep exact tokens unchanged.

## Quality Gate

Block release and rework when any of the following appear:

- Critical content omitted or added.
- Reversed meaning (for example permission becomes prohibition).
- Unsafe mistranslation in legal, medical, financial, or policy text.
- Terminology inconsistency across repeated mentions.
