## Syntax

`irf ctable (spec_1)` \[`(spec_2)` ... \[`(spec_N)`\]\] \[`,`
`options`\]

where `(spec_k)` is

`(irfname impulsevar responsevar stat` \[`, spec_options`\]`)`

`irfname` is the name of a set of IRF results in the active IRF file.
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

| options |                     | Description                                   |
|---------|---------------------|-----------------------------------------------|
|         | `set(filename)`     | make `filename` active                        |
|         | `noci`              | do not report confidence intervals            |
|         | `stderror`          | include standard errors for each statistic    |
|         | `individual`        | make an individual table for each combination |
|         | `title("text")` | use `text` as overall table title             |
|         | `step(#)`           | set common maximum set                        |
|         | `level(#)`          | set confidence level; default is `level(95)`  |

| spec\_options                                                                                                                                                                                                                                                                                                                                                        |                      | Description                                          |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------|------------------------------------------------------|
|                                                                                                                                                                                                                                                                                                                                                                      | `noci`               | do not report confidence intervals                   |
|                                                                                                                                                                                                                                                                                                                                                                      | `stderror`           | include standard errors for each statistic           |
|                                                                                                                                                                                                                                                                                                                                                                      | `level(#)`           | set confidence level; default is `level(95)`         |
|                                                                                                                                                                                                                                                                                                                                                                      | `ititle("text")` | use `text` as individual subtitle for specific table |
| `spec_options` may be specified within a table specification, globally, or in both. When specified in a table specification, the `spec_options` affect only the specification in which they are used. When supplied globally, the `spec_options` affect all table specifications. When supplied in both places, options for the table specification take precedence. |                      |                                                      |
| `ititle()` does not appear in the dialog box.                                                                                                                                                                                                                                                                                                                        |                      |                                                      |
