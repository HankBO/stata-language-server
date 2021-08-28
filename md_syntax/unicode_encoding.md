## Syntax

List encodings

`unicode encoding list` \[`pattern`\]

List all aliases of an encoding

`unicode encoding alias name`

Set an encoding for use with `unicode translate`

`unicode encoding set name`

`pattern` is one of the following: `*`, `_all`, `*name*`, `*name`,
or `name*`. Specifying nothing, `_all`, or `*` lists all results.
Specifying `*name*` lists all results containing `name`. Specifying
`*name` lists all results ending with `name`. Specifying `name*`
lists all results starting with `name`.
