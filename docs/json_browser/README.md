# The European Genome-phenome Archive (EGA) metadata standards: JSON Browser

In this directory you will find human-readable summaries of EGA's metadata schemas. The information codified within the JSON schemas can appear cryptic to the unaccustomed eye, hence the need for this markdown documents that easily summarize the information codified within the schemas (which are the ultimate source of truth). Such schemas can be found in their
[corresponding directory](../../schemas) within this repo, along with brief documentation.

Work inspired by [HCA's JSON Browser](https://github.com/HumanCellAtlas/metadata-schema/tree/master/docs/jsonBrowser).

## Where to start

Each **object** and **definition** within the JSON Schemas will have its own markdown file (``.md``). Given the amount of objects, the easiest path to follow is from top to bottom of the hierarchy.

Hence, take a look at the [markdown's summary](markdowns/README.md). There, you will find the section **Top-level Schemas**, which will list the main metadata objects (e.g. ``ArrayAssay``). If you click on any of these, you will be redirected to their corresponding records, with diverse details (such as ``title`` or ``description``) and, most importantly, a list with all their ``properties``
(with their details, constraints, etc.)

## How they are created
Markdown summaries constitute the JSON Browser and are automatically generated through the usage of **GitHub actions** ([``markdown_generation``](../../.github/workflows/markdown_creation.yml)) and the [**jsonschema2md**](https://github.com/adobe/jsonschema2md) tool. Every pull request merged into the ``main`` branch of this repository will trigger the workflow to automatically generate updated
documentation based on the JSON schemas. This workflow makes use of jsonschema2md, which parses the JSON schemas and creates markdown documentation based on them.