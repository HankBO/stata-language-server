## Syntax

`rocfit refvar classvar` _\[`if`\]
\[`in`\]_ \[`weight`\] \[`, rocfit_options`\]

| rocfit\_options                                                                                                                                                           |                    | Description                                                     |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------|-----------------------------------------------------------------|
| Model                                                                                                                                                                     |                    |                                                                 |
|                                                                                                                                                                           | `continuous(#)`    | divide `classvar` into `#` groups of approximately equal length |
|                                                                                                                                                                           | `generate(newvar)` | create `newvar` containing classification groups                |
| SE                                                                                                                                                                        |                    |                                                                 |
|                                                                                                                                                                           | `vce(vcetype)`     | `vcetype` may be `oim` or `opg`                                 |
| Reporting                                                                                                                                                                 |                    |                                                                 |
|                                                                                                                                                                           | `level(#)`         | set confidence level; default is `level(95)`                    |
| Maximization                                                                                                                                                              |                    |                                                                 |
|                                                                                                                                                                           | `maximize_options` | control the maximization process; seldom used                   |
| `fp` is allowed; see [<strong>prefix</strong>](http://www.stata.com/help.cgi?prefix).                                                          |                    |                                                                 |
| `fweight`s are allowed; see [<strong>weight</strong>](http://www.stata.com/help.cgi?weight).                                                   |                    |                                                                 |
| See [<strong>[R]</strong> rocfit postestimation](http://www.stata.com/help.cgi?rocfit_postestimation) for features available after estimation. |                    |                                                                 |
