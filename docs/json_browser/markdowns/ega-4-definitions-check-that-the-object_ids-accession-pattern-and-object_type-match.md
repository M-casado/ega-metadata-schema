# Check that the object_id's accession pattern and object_type match Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/one-relationship-end/allOf/0
```

This object exists with the only purpose of being a reference as a pattern check of a given object_id and object_type. The constraint consists in asserting that, if the object identifier is an EGA accession, its pattern matches the object type (e.g. if object_type is 'sample', its EGA accession needs to match '^EGAN\[0-9]{11}$')

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :---------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.common-definitions.json*](../out/EGA.common-definitions.json "open original schema") |

## 0 Type

`object` ([Check that the object_id's accession pattern and object_type match](ega-4-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match.md))

any of

*   [Alias and Centername: object_id and object_type check](ega-4-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-alias-and-centername-object_id-and-object_type-check.md "check type definition")

*   [External accession: object_id and object_type check](ega-4-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-external-accession-object_id-and-object_type-check.md "check type definition")

*   [Experiment: object_id and object_type check](ega-4-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-experiment-object_id-and-object_type-check.md "check type definition")

*   [Study: object_id and object_type check](ega-4-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-study-object_id-and-object_type-check.md "check type definition")

*   [Sample: object_id and object_type check](ega-4-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-sample-object_id-and-object_type-check.md "check type definition")

*   [Submission: object_id and object_type check](ega-4-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-submission-object_id-and-object_type-check.md "check type definition")

*   [Run: object_id and object_type check](ega-4-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-run-object_id-and-object_type-check.md "check type definition")

*   [Dataset: object_id and object_type check](ega-4-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-dataset-object_id-and-object_type-check.md "check type definition")

*   [Analysis: object_id and object_type check](ega-4-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-analysis-object_id-and-object_type-check.md "check type definition")

*   [Policy: object_id and object_type check](ega-4-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-policy-object_id-and-object_type-check.md "check type definition")

*   [DAC: object_id and object_type check](ega-4-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-dac-object_id-and-object_type-check.md "check type definition")

*   [ArrayExperiment: object_id and object_type check](ega-4-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-arrayexperiment-object_id-and-object_type-check.md "check type definition")

*   [ArrayAssay: object_id and object_type check](ega-4-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-arrayassay-object_id-and-object_type-check.md "check type definition")

*   [Individual: object_id and object_type check](ega-4-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-individual-object_id-and-object_type-check.md "check type definition")