## Syntax

`tabulate varname1` \[`varname2`\] _\[`if`\]
\[`in`\]_ \[`weight`\] \[`, options`\]

| Options                                                                                                                                |                       | Description                                                     |
|----------------------------------------------------------------------------------------------------------------------------------------|-----------------------|-----------------------------------------------------------------|
| Main                                                                                                                                   |                       |                                                                 |
|                                                                                                                                        | `summarize(varname3)` | report summary statistics for `varname3`                        |
|                                                                                                                                        | \[`no`\]`means`       | include or suppress means                                       |
|                                                                                                                                        | \[`no`\]`standard`    | include or suppress standard deviations                         |
|                                                                                                                                        | \[`no`\]`freq`        | include or suppress frequencies                                 |
|                                                                                                                                        | \[`no`\]`obs`         | include or suppress number of observations                      |
|                                                                                                                                        | `nolabel`             | show numeric codes, not labels                                  |
|                                                                                                                                        | `wrap`                | do not break wide tables                                        |
|                                                                                                                                        | `missing`             | treat missing values of `varname1` and `varname2` as categories |
| `by` is allowed; see [<strong>[D]</strong> by](http://www.stata.com/help.cgi?by).                           |                       |                                                                 |
| `aweight`s and `fweight`s are allowed; see [<strong>weight</strong>](http://www.stata.com/help.cgi?weight). |                       |                                                                 |
