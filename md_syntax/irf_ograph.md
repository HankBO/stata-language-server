## Syntax

`irf ograph (spec_1)` \[`(spec_2)` ... \[`(spec_15)`\]\] \[`,`
`options`\]

where `(spec_k)` is

`(irfname impulsevar responsevar stat` \[`, spec_options`\]`)`

`irfname` is the name of a set of IRF results in the active IRF file or
"`.`", which means the first named result in the active IRF file.
`impulsevar` should be specified as an endogenous variable for all
statistics except `dm` and `cdm`; for those, specify as an exogenous
variable. `responsevar` is an endogenous variable name. `stat` is one or
more statistics from the list below:

|         |                                                                |
|---------|----------------------------------------------------------------|
| `stat`  | Description {p2line None} {syntab None:Main}                   |
| `irf`   | impulse-response function                                      |
| `oirf`  | orthogonalized impulse-response function                       |
| `dm`    | dynamic-multiplier function                                    |
| `cirf`  | cumulative impulse-response function                           |
| `coirf` | cumulative orthogonalized impulse-response function            |
| `cdm`   | cumulative dynamic-multiplier function                         |
| `fevd`  | Cholesky forecast-error variance decomposition                 |
| `sirf`  | structural impulse-response function                           |
| `sfevd` | structural forecast-error variance decomposition {p2line None} |

| options                                 |                  | Description                                                                                                                                                           |
|-----------------------------------------|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Plots                                   |                  |                                                                                                                                                                       |
|                                         | `plot_options`   | define the IRF plots                                                                                                                                                  |
|                                         | `set(filename)`  | make `filename` active                                                                                                                                                |
| Options                                 |                  |                                                                                                                                                                       |
|                                         | `common_options` | level and steps                                                                                                                                                       |
| Y axis, X axis, Titles, Legend, Overall |                  |                                                                                                                                                                       |
|                                         | `twoway_options` | any options other than `by()` documented in [<strong>[G-3]</strong> <em>twoway_options</em>](http://www.stata.com/help.cgi?twoway_options) |

| plot\_options |                            | Description                                    |
|---------------|----------------------------|------------------------------------------------|
| Main          |                            |                                                |
|               | `set(filename)`            | make `filename` active                         |
|               | `irf(irfnames)`        | use `irfnames` IRF result sets                 |
|               | `impulse(impulsevar)`      | use `impulsevar` as impulse variables          |
|               | `response:(endogvars)` | use endogenous variables as response variables |
|               | `ci`                       | add confidence bands to the graph              |

| spec\_options |                        | Description                                  |
|---------------|------------------------|----------------------------------------------|
| Options       |                        |                                              |
|               | `common_options`       | level and steps                              |
| Plot          |                        |                                              |
|               | `cline_options`        | affect rendition of the plotted lines        |
| CI plot       |                        |                                              |
|               | `ciopts(area_options)` | affect rendition of the confidence intervals |

| common\_options                                                                                                                                                                                                                                                                                                                                                       |            | Description                                  |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------|----------------------------------------------|
| Options                                                                                                                                                                                                                                                                                                                                                               |            |                                              |
|                                                                                                                                                                                                                                                                                                                                                                       | `level(#)` | set confidence level; default is `level(95)` |
|                                                                                                                                                                                                                                                                                                                                                                       | `lstep(#)` | use `#` for first step                       |
|                                                                                                                                                                                                                                                                                                                                                                       | `ustep(#)` | use `#` for maximum step                     |
| `common_options` may be specified within a plot specification, globally, or in both. When specified in a plot specification, the `common_options` affect only the specification in which they are used. When supplied globally, the `common_options` affect all plot specifications. When supplied in both places, options in the plot specification take precedence. |            |                                              |
