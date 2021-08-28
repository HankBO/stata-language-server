## Syntax

Standard estimation command syntax

`nestreg` \[`, options` \] `: command_name`
[depvar](http://www.stata.com/help.cgi?depvar)
`(varlist)` \[`(varlist)` ...\] _\[`if`\]
\[`in`\]_ \[`weight`\] \[`, command_options`\]

Survey estimation command syntax

`nestreg` \[`, options`\] `: svy` \[`vcetype`\] \[`,`
`svy_options`\] `: command_name`
[depvar](http://www.stata.com/help.cgi?depvar)
`(varlist)` \[`(varlist)` ...\] _\[`if`\]
\[`in`\]_ \[`, command_options`\]

| Options                                                                                                                                                                                  |               | Description                                       |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|---------------------------------------------------|
| Reporting                                                                                                                                                                                |               |                                                   |
|                                                                                                                                                                                          | `waldtable`   | report Wald test results; the default             |
|                                                                                                                                                                                          | `lrtable`     | report likelihood-ratio test results              |
|                                                                                                                                                                                          | `quietly`     | suppress any output from `command_name`           |
|                                                                                                                                                                                          | `store(stub)` | store nested estimation results in `_est_stub#` |
| `by` is allowed; see [<strong>prefix</strong>](http://www.stata.com/help.cgi?prefix).                                                                         |               |                                                   |
| Weights are allowed if `command_name` allows them; see [<strong>weight</strong>](http://www.stata.com/help.cgi?weight).                                       |               |                                                   |
| A `varlist` in parentheses indicates that this list of variables is to be considered as a block. Each variable in a `varlist` not bound in parentheses will be treated as its own block. |               |                                                   |
| All postestimation commands behave as they would after `command_name` without the `nestreg` prefix; see the postestimation manual entry for `command_name`.                              |               |                                                   |
