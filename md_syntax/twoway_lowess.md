## Syntax

`twoway lowess yvar xvar` _\[`if`\]
\[`in`\]_ \[`, options`\]

|                       |                                                                                                  |
|-----------------------|--------------------------------------------------------------------------------------------------|
| `options`             | Description {p2line None}                                                                        |
| `bwidth:(#)`      | smoothing parameter                                                                              |
| `mean`                | use running-mean smoothing                                                                       |
| `noweight`            | use unweighted smoothing                                                                         |
| `logit`               | transform the smooth to logits                                                                   |
| `adjust`              | adjust smooth's mean to equal `yvar`'s mean                                                      |
| `cline_options`       | change look of the line                                                                          |
| `axis_choice_options` | associate plot with alternative axis                                                             |
| `twoway_options`      | titles, legends, axes, added lines and text, by, regions, name, aspect ratio, etc. {p2line None} |
