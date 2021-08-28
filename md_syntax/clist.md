## Syntax

`clist`
\[[varlist](http://www.stata.com/help.cgi?varlist)\]
_\[`if`\] \[`in`\]_ \[`, options`\]

| options                                                                                                                                            |                   | Description                                                                                        |
|----------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|----------------------------------------------------------------------------------------------------|
|                                                                                                                                                    | \[`no`\]`display` | format into display or tabular nodisplay format                                                    |
|                                                                                                                                                    | `noheader`        | omit variable or observation number header information                                             |
|                                                                                                                                                    | `nolabel`         | display numeric codes; default displays label values                                               |
|                                                                                                                                                    | `noobs`           | suppress printing of observation numbers                                                           |
|                                                                                                                                                    | `doublespace`     | insert a blank line between each observation when in nodisplay mode; has no effect in display mode |
| `varlist` may contain time-series operators; see [<strong>tsvarlist</strong>](http://www.stata.com/help.cgi?tsvarlist). |                   |                                                                                                    |
| `by` is allowed with `clist`; see [<strong>[D]</strong> by](http://www.stata.com/help.cgi?by).                          |                   |                                                                                                    |
