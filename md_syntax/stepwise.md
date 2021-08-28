## Syntax

`stepwise` \[`, options`\] `: command`

| Options                                                                                                                                            |                   | Description                                        |
|----------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|----------------------------------------------------|
| Model                                                                                                                                              |                   |                                                    |
| \*                                                                                                                                                 | `pr(#)`           | significance level for removal from the model      |
| \*                                                                                                                                                 | `pe(#)`           | significance level for addition to the model       |
| Model2                                                                                                                                             |                   |                                                    |
|                                                                                                                                                    | `forward`         | perform forward-stepwise selection                 |
|                                                                                                                                                    | `hierarchical`    | perform hierarchical selection                     |
|                                                                                                                                                    | `lockterm1`       | keep the first term                                |
|                                                                                                                                                    | `lr`              | perform likelihood-ratio test instead of Wald test |
| Reporting                                                                                                                                          |                   |                                                    |
|                                                                                                                                                    | `display_options` | control columns and column formats and line width  |
| \* At least one of `pr(#)` or `pe(#)` must be specified.                                                                                           |                   |                                                    |
| `by` and `xi` are allowed; see [<strong>prefix</strong>](http://www.stata.com/help.cgi?prefix).                         |                   |                                                    |
| Weights are allowed if `command` allows them; see [<strong>weight</strong>](http://www.stata.com/help.cgi?weight).      |                   |                                                    |
| All postestimation commands behave as they would after `command` without the `stepwise` prefix; see the postestimation manual entry for `command`. |                   |                                                    |
