## Syntax

`loneway response_var group_var` _\[`if`\]
\[`in`\]_ \[`weight`\] \[`, options`\]

| Options                                                                                                                 |            | Description                                                       |
|-------------------------------------------------------------------------------------------------------------------------|------------|-------------------------------------------------------------------|
| Main                                                                                                                    |            |                                                                   |
|                                                                                                                         | `mean`     | expected value of F distribution; default is 1                    |
|                                                                                                                         | `median`   | median of F distribution; default is 1                            |
|                                                                                                                         | `exact`    | exact confidence intervals (groups must be equal with no weights) |
|                                                                                                                         | `level(#)` | set confidence level; default is `level(95)`                      |
| `by` is allowed; see [<strong>[D]</strong> by](http://www.stata.com/help.cgi?by).            |            |                                                                   |
| `aweight`s are allowed; see [<strong>weight</strong>](http://www.stata.com/help.cgi?weight). |            |                                                                   |
