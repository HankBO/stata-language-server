## Syntax

`varbasic`
[depvarlist](http://www.stata.com/help.cgi?depvarlist)
_\[`if`\] \[`in`\]_ \[`, options`\]

| Options                                                                                                                                                                        |                 | Description                                                                              |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------|------------------------------------------------------------------------------------------|
| Main                                                                                                                                                                           |                 |                                                                                          |
|                                                                                                                                                                                | `lags(numlist)` | use `numlist` lags in the model; default is `lags(1 2)`                                  |
|                                                                                                                                                                                | `irf`           | produce matrix graph of IRFs                                                             |
|                                                                                                                                                                                | `fevd`          | produce matrix graph of FEVDs                                                            |
|                                                                                                                                                                                | `nograph`       | do not produce a graph                                                                   |
|                                                                                                                                                                                | `step(#)`       | set forecast horizon `#` for estimating the OIRFs, IRFs, and FEVDs; default is `step(8)` |
| You must `tsset` your data before using `varbasic`; see [<strong>[TS] tsset</strong>](http://www.stata.com/help.cgi?tsset).                         |                 |                                                                                          |
| `depvarlist` may contain time-series operators; see [<strong>tsvarlist</strong>](http://www.stata.com/help.cgi?tsvarlist).                          |                 |                                                                                          |
| `rolling`, `statsby`, and `xi` are allowed; see [<strong>prefix</strong>](http://www.stata.com/help.cgi?prefix).                                    |                 |                                                                                          |
| See [<strong>[TS]</strong> varbasic postestimation](http://www.stata.com/help.cgi?varbasic_postestimation) for features available after estimation. |                 |                                                                                          |
