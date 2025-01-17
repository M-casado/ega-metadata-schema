# Single sequence position Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/sequenceCoordinates/properties/sequenceInterval/properties/start
```

A single 1-based (first base of the assembly unit is 1, not 0) sequence coordinate, inclusive. It can be used to describe the start or end coordinates of a sequence interval, or directly a single coordinate within a sequence.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## start Type

`number` ([Single sequence position](ega-4-definitions-sequence-coordinates-properties-sequence-interval-properties-single-sequence-position.md))

## start Examples

```json
71366222
```

```json
36592394
```

```json
1
```
