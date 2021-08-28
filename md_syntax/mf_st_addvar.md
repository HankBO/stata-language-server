## Syntax

`real rowvector`<span class="nowrap"> _ `st_addvar(type,`
`name)`

`real rowvector`<span class="nowrap"> _ `st_addvar(type,`
`name, nofill)`

`real rowvector _st_addvar(type, name)`

`real rowvector _st_addvar(type, name, nofill)`

where

`type`: `string scalar` or `rowvector` containing `"byte"`, `"int"`,
`"long"`, `"float"`, `"double"`, `"str#"`, or `"strL"`

or

`real scalar` or `rowvector` containing `#` (interpreted as `str#`)

`name`: `string rowvector` containing new variable names

`nofill`: `real scalar` containing 0 or non-0
