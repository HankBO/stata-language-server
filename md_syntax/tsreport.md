## Syntax

`tsreport`
\[[varlist](http://www.stata.com/help.cgi?varlist)\]
_\[`if`\] \[`in`\]_ \[`, options`\]

| options                                                                                                                                            |            | Description                                                           |
|----------------------------------------------------------------------------------------------------------------------------------------------------|------------|-----------------------------------------------------------------------|
| Main                                                                                                                                               |            |                                                                       |
|                                                                                                                                                    | `detail`   | list periods for each gap                                             |
|                                                                                                                                                    | `casewise` | treat a period as a gap if any of the specified variables are missing |
|                                                                                                                                                    | `panel`    | do not count panel changes as gaps                                    |
| `varlist` may contain time-series operators; see [<strong>tsvarlist</strong>](http://www.stata.com/help.cgi?tsvarlist). |            |                                                                       |
