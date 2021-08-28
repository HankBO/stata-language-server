## Syntax

`oneway response_var factor_var` _\[`if`\]
\[`in`\]_ \[`weight`\] \[`, options`\]

| Options                                                                                                                                |                    | Description                                                              |
|----------------------------------------------------------------------------------------------------------------------------------------|--------------------|--------------------------------------------------------------------------|
| Main                                                                                                                                   |                    |                                                                          |
|                                                                                                                                        | `bonferroni`       | Bonferroni multiple-comparison test                                      |
|                                                                                                                                        | `scheffe`          | Scheffe multiple-comparison test                                         |
|                                                                                                                                        | `sidak`            | Sidak multiple-comparison test                                           |
|                                                                                                                                        | `tabulate`         | produce summary table                                                    |
|                                                                                                                                        | \[`no`\]`means`    | include or suppress means; default is `means`                            |
|                                                                                                                                        | \[`no`\]`standard` | include or suppress standard deviations; default is `standard`           |
|                                                                                                                                        | \[`no`\]`freq`     | include or suppress frequencies; default is `freq`                       |
|                                                                                                                                        | \[`no`\]`obs`      | include or suppress number of obs; default is `obs` if data are weighted |
|                                                                                                                                        | `noanova`          | suppress the ANOVA table                                                 |
|                                                                                                                                        | `nolabel`          | show numeric codes, not labels                                           |
|                                                                                                                                        | `wrap`             | do not break wide tables                                                 |
|                                                                                                                                        | `missing`          | treat missing values as categories                                       |
| `by` is allowed; see [<strong>[D]</strong> by](http://www.stata.com/help.cgi?by).                           |                    |                                                                          |
| `aweight`s and `fweight`s are allowed; see [<strong>weight</strong>](http://www.stata.com/help.cgi?weight). |                    |                                                                          |
