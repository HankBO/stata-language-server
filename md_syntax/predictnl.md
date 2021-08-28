## Syntax

`predictnl` _\[`type`\] \[_
[newvar](http://www.stata.com/help.cgi?newvar)
= `pnl_exp` _\[`if`\] \[`in`\]_ \[`,`
`options`\]

| Options                                    |                    | Description                                                                                                     |
|--------------------------------------------|--------------------|-----------------------------------------------------------------------------------------------------------------|
| Main                                       |                    |                                                                                                                 |
|                                            | `se(newvar)`       | create `newvar` containing standard errors                                                                      |
|                                            | `variance(newvar)` | create `newvar` containing variances                                                                            |
|                                            | `wald(newvar)`     | create `newvar` containing the Wald test statistic                                                              |
|                                            | `p(newvar)`        | create `newvar` containing the p-value for the Wald test                                                        |
|                                            | `ci(newvars)`      | create `newvars` containing lower and upper confidence intervals                                                |
|                                            | `level(#)`         | set confidence level; default is `level(95)`                                                                    |
|                                            | `g(stub)`          | create `stub1`, `stub2`, ..., `stubk` variables containing observation-specific derivatives               |
| Advanced                                   |                    |                                                                                                                 |
|                                            | `iterate(#)`       | maximum iterations for finding optimal step size; default is 100                                                |
|                                            | `force`            | calculate standard errors, etc., even when possibly inappropriate                                               |
|                                            | `df(#)`            | use F distribution with `#` denominator degrees of freedom for the reference distribution of the test statistic |
| `df(#)` does not appear in the dialog box. |                    |                                                                                                                 |
