# XM - Molecule type: mRNA Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/curieRefseqPattern/oneOf/7
```



| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## 7 Type

unknown ([XM - Molecule type: mRNA](ega-4-definitions-refseq-accessions-data1098-curie-pattern-oneof-xm---molecule-type-mrna.md))

## 7 Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^[^:]+:XM_\d+(\.\d+)?$
```

[try pattern](https://regexr.com/?expression=%5E%5B%5E%3A%5D%2B%3AXM_%5Cd%2B\(%5C.%5Cd%2B\)%3F%24 "try regular expression with regexr.com")