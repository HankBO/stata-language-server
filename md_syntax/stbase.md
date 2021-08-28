## Syntax

`stbase` _\[`if`\] \[`in`\]_ \[`,`
`options`\]

| Options                                                                                                                                                                   |               | Description                                                                   |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|-------------------------------------------------------------------------------|
| Main                                                                                                                                                                      |               |                                                                               |
|                                                                                                                                                                           | `at(#)`       | convert single/multiple-record st data to cross-sectional dataset at time `#` |
|                                                                                                                                                                           | `gap(newvar)` | name of variable containing gap time; default is `gap` or `gaptime`           |
|                                                                                                                                                                           | `replace`     | overwrite current data in memory                                              |
|                                                                                                                                                                           | `noshow`      | do not show st setting information                                            |
|                                                                                                                                                                           | `nopreserve`  | programmer's option; see `Options` below                                      |
| You must `stset` your data before using `stbase`; see [<strong>[ST]</strong> stset](http://www.stata.com/help.cgi?stset).                      |               |                                                                               |
| `fweight`s, `iweight`s, and `pweight`s may be specified using `stset`; see [<strong>[ST]</strong> stset](http://www.stata.com/help.cgi?stset). |               |                                                                               |
| `nopreserve` does not appear in the dialog box.                                                                                                                           |               |                                                                               |
