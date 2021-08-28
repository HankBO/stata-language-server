## Syntax

Many `mata` commands allow or require a `namelist`, such as

: `mata describe` \[`namelist`\] \[`, all`\]

A `namelist` is defined as a list of matrix and/or function names, such
as

`alpha beta foo()`

The above `namelist` refers to the matrices `alpha` and `beta` along
with the function named `foo()`.

Function names always end in `()`, hence

`alphaalphaalpha()`

Names may also be specified using the `*` and `?` wildcard characters:

`*?`

hence,

`**()* *()s*ss*()s*ee*e()es*eses*e()ses?eses?e()se`
