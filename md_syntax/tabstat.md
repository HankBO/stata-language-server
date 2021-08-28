## Syntax

`tabstat`
[varlist](http://www.stata.com/help.cgi?varlist)
_\[`if`\] \[`in`\]_ \[`weight`\] \[`,`
`options`\]

| Options                                                                                                                                |                                       | Description                                                   |
|----------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------|---------------------------------------------------------------|
| Main                                                                                                                                   |                                       |                                                               |
|                                                                                                                                        | `by(varname)`                         | group statistics by variable                                  |
|                                                                                                                                        | `statistics:(statname` \[`...`\]`)` | report specified statistics                                   |
| Options                                                                                                                                |                                       |                                                               |
|                                                                                                                                        | `labelwidth(#)`                       | width for `by()` variable labels; default is `labelwidth(16)` |
|                                                                                                                                        | `varwidth(#)`                         | variable width; default is `varwidth(12)`                     |
|                                                                                                                                        | `columns(variables)`              | display variables in table columns; the default               |
|                                                                                                                                        | `columns(statistics)`             | display statistics in table columns                           |
|                                                                                                                                        | `format`\[`(%fmt)`\]              | display format for statistics; default format is `%9.0g`      |
|                                                                                                                                        | `casewise`                            | perform casewise deletion of observations                     |
|                                                                                                                                        | `nototal`                             | do not report overall statistics; use with `by()`             |
|                                                                                                                                        | `missing`                             | report statistics for missing values of `by()` variable       |
|                                                                                                                                        | `noseparator`                         | do not use separator line between `by()` categories           |
|                                                                                                                                        | `longstub`                            | make left table stub wider                                    |
|                                                                                                                                        | `save`                                | store summary statistics in `r()`                             |
| `by` is allowed; see [<strong>[D]</strong> by](http://www.stata.com/help.cgi?by).                           |                                       |                                                               |
| `aweight`s and `fweight`s are allowed; see [<strong>weight</strong>](http://www.stata.com/help.cgi?weight). |                                       |                                                               |
