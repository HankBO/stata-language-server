## Syntax

`adjust` \[`var`\[`= #`\] `...`\] _\[`if`\]
\[`in`\]_ \[`, options`\]

|                               |                                                                         |
|-------------------------------|-------------------------------------------------------------------------|
| `options`                     | Description {p2line None}                                               |
| Main                          |                                                                         |
| `by(varlist)`                 | compute and display predictions for each level of variables             |
| Options                       |                                                                         |
| `xb`                          | linear prediction; the default                                          |
| `pr`                          | predicted probabilities                                                 |
| `exp`                         | exponentiated linear prediction                                         |
| `se`                          | display standard error of the prediction; default is none               |
| `stdf`                        | display standard error of the forecast; default is none                 |
| `ci`                          | display confidence or prediction intervals                              |
| `level(#)`                    | set confidence level; default is `level(95)`                            |
| `vertical`                    | stack confidence intervals                                              |
| `equation(eqno)`              | use `eqno` equation in a multiple-equation system                       |
| `nooffset`                    | ignore `offset` or `exposure` variable (if any) when making predictions |
| `generate(newvar1 [newvar2])` | generate prediction variable, error variable                            |
| More options                  |                                                                         |
| `replace`                     | replace data in memory with table                                       |
| `label(text)`                 | prediction label                                                        |
| `selabel(text)`               | error-term label                                                        |
| `cilabel(text)`               | confidence interval label                                               |
| `format(%fmt)`                | display format for numbers in table                                     |
| `nokey`                       | suppress table key                                                      |
| `noheader`                    | suppress table header                                                   |
| `center`                      | center numbers in cells; default is to right-align                      |
| `left`                        | left-align column labels; default is to right-align                     |
| `cellwidth(#)`                | cell width                                                              |
| `csepwidth(#)`                | column separation                                                       |
| `scsepwidth(#)`               | supercolumn separation                                                  |
| `stubwidth(#)`                | left stub width {p2line None}                                           |
