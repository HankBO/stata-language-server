## Syntax

`summarize`
\[[varlist](http://www.stata.com/help.cgi?varlist)\]
_\[`if`\] \[`in`\]_ \[`weight`\] \[`,`
`options`\]

| Options |                   | Description                                                              |
|---------|-------------------|--------------------------------------------------------------------------|
| Main    |                   |                                                                          |
|         | `detail`          | display additional statistics                                            |
|         | `meanonly`        | suppress the display; calculate only the mean; programmer's option       |
|         | `format`          | use variable's display format                                            |
|         | `separator(#)`    | draw separator line after every `#` variables; default is `separator(5)` |
|         | `display_options` | control spacing, line width, and base and empty cells                    |

|                                                                                                                                                                                                                   |     |     |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|-----|
| `varlist` may contain factor variables; see [<strong>fvvarlist</strong>](http://www.stata.com/help.cgi?fvvarlist).                                                                     |     |     |
| `varlist` may contain time-series operators; see [<strong>tsvarlist</strong>](http://www.stata.com/help.cgi?tsvarlist).                                                                |     |     |
| `by`, `rolling`, and `statsby` are allowed; see [<strong>prefix</strong>](http://www.stata.com/help.cgi?prefix).                                                                       |     |     |
| `aweight`s, `fweight`s, and `iweight`s are allowed. However, `iweight`s may not be used with the `detail` option; see [<strong>weight</strong>](http://www.stata.com/help.cgi?weight). |     |     |
