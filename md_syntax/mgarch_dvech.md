## Syntax

`mgarch dvech eq` \[`eq` ... `eq`\] _\[`if`\]
\[`in`\]_ \[`, options`\]

where each `eq` has the form

`(`[depvarlist](http://www.stata.com/help.cgi?depvarlist)
`=`
\[[indepvars](http://www.stata.com/help.cgi?indepvars)\]
\[`, noconstant`\]`)`

| Options                                                                                                                                                                                |                               | Description                                                                                                                                      |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| Model                                                                                                                                                                                  |                               |                                                                                                                                                  |
|                                                                                                                                                                                        | `arch(numlist)`               | ARCH terms                                                                                                                                       |
|                                                                                                                                                                                        | `garch(numlist)`              | GARCH terms                                                                                                                                      |
|                                                                                                                                                                                        | `distribution(dist [#])`      | use `dist` distribution for errors \[may be `gaussian` (synonym `normal`) or `t`; default is `gaussian`\]                                        |
|                                                                                                                                                                                        | `constraints(numlist)`        | apply linear constraints                                                                                                                         |
| SE/Robust                                                                                                                                                                              |                               |                                                                                                                                                  |
|                                                                                                                                                                                        | `vce(vcetype)`                | `vcetype` may be `oim` or `robust`                                                                                                               |
| Reporting                                                                                                                                                                              |                               |                                                                                                                                                  |
|                                                                                                                                                                                        | `level(#)`                    | set confidence level; default is `level(95)`                                                                                                     |
|                                                                                                                                                                                        | `nocnsreport`                 | do not display constraints                                                                                                                       |
|                                                                                                                                                                                        | `display_options`             | control columns and column formats, row spacing, line width, display of omitted variables and base and empty cells, and factor-variable labeling |
| Maximization                                                                                                                                                                           |                               |                                                                                                                                                  |
|                                                                                                                                                                                        | `maximize_options`            | control the maximization process; seldom used                                                                                                    |
|                                                                                                                                                                                        | `from(matname)`               | initial values for the coefficients; seldom used                                                                                                 |
|                                                                                                                                                                                        | `svtechnique(algorithm_spec)` | starting-value maximization algorithm                                                                                                            |
|                                                                                                                                                                                        | `sviterate(#)`                | number of starting-value iterations; default is `sviterate(25)`                                                                                  |
|                                                                                                                                                                                        | `coeflegend`                  | display legend instead of statistics                                                                                                             |
| You must `tsset` your data before using `mgarch dvech`; see [<strong>[TS]</strong> tsset](http://www.stata.com/help.cgi?tsset).                             |                               |                                                                                                                                                  |
| `indepvars` may contain factor variables; see [<strong>fvvarlist</strong>](http://www.stata.com/help.cgi?fvvarlist).                                        |                               |                                                                                                                                                  |
| `depvars` and `indepvars` may contain time-series operators; see [<strong>tsvarlist</strong>](http://www.stata.com/help.cgi?tsvarlist).                     |                               |                                                                                                                                                  |
| `by`, `fp`, `rolling`, and `statsby` are allowed; see [<strong>prefix</strong>](http://www.stata.com/help.cgi?prefix).                                      |                               |                                                                                                                                                  |
| `coeflegend` does not appear in the dialog box.                                                                                                                                        |                               |                                                                                                                                                  |
| See [<strong>[TS]</strong> mgarch dvech postestimation](http://www.stata.com/help.cgi?mgarch_dvech_postestimation) for features available after estimation. |                               |                                                                                                                                                  |
