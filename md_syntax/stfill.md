## Syntax

`stfill`
[varlist](http://www.stata.com/help.cgi?varlist)
_\[`if`\] \[`in`\]_ `,` <span options="-(">{c
-(}_`baseline`\|`forward`}
\[`options`\]

| Options                                                                                                                                                                   |            | Description                        |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------|------------------------------------|
| Main                                                                                                                                                                      |            |                                    |
| \*                                                                                                                                                                        | `baseline` | replace with values at baseline    |
| \*                                                                                                                                                                        | `forward`  | carry forward values               |
|                                                                                                                                                                           | `noshow`   | do not show st setting information |
| \* Either `baseline` or `forward` is required.                                                                                                                            |            |                                    |
| You must `stset` your data before using `stfill`; see [<strong>[ST]</strong> stset](http://www.stata.com/help.cgi?stset).                      |            |                                    |
| `fweight`s, `iweight`s, and `pweights` may be specified using `stset`; see [<strong>[ST]</strong> stset](http://www.stata.com/help.cgi?stset). |            |                                    |
