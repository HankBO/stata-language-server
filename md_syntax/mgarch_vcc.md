## Syntax

`mgarch vcc eq` \[`eq` ... `eq`\] _\[`if`\]
\[`in`\]_ \[`, options`\]

where each `eq` has the form

`(`[depvarlist](http://www.stata.com/help.cgi?depvarlist)
`=`
\[[indepvars](http://www.stata.com/help.cgi?indepvars)\]
\[`, eqoptions`\]`)`

| Options      |                          | Description                                                                                                                                      |
|--------------|--------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| Model        |                          |                                                                                                                                                  |
|              | `arch(numlist)`          | ARCH terms for all equations                                                                                                                     |
|              | `garch(numlist)`         | GARCH terms for all equations                                                                                                                    |
|              | `het(varlist)`           | include `varlist` in the specification of the conditional variance for all equations                                                             |
|              | `distribution(dist [#])` | use `dist` distribution for errors \[may be `gaussian` (synonym `normal`) or `t`; default is `gaussian`\]                                        |
|              | `constraints(numlist)`   | apply linear constraints                                                                                                                         |
| SE/Robust    |                          |                                                                                                                                                  |
|              | `vce(vcetype)`           | `vcetype` may be `oim` or `robust`                                                                                                               |
| Reporting    |                          |                                                                                                                                                  |
|              | `level(#)`               | set confidence level; default is `level(95)`                                                                                                     |
|              | `nocnsreport`            | do not display constraints                                                                                                                       |
|              | `display_options`        | control columns and column formats, row spacing, line width, display of omitted variables and base and empty cells, and factor-variable labeling |
| Maximization |                          |                                                                                                                                                  |
|              | `maximize_options`       | control the maximization process; seldom used                                                                                                    |
|              | `from(matname)`          | initial values for the coefficients; seldom used                                                                                                 |
|              | `coeflegend`             | display legend instead of statistics                                                                                                             |

| eqoptions                                                                                                                                                                          |                  | Description                                                        |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------|--------------------------------------------------------------------|
| Model                                                                                                                                                                              |                  |                                                                    |
|                                                                                                                                                                                    | `noconstant`     | suppress constant term in the mean equation                        |
|                                                                                                                                                                                    | `arch(numlist)`  | ARCH terms                                                         |
|                                                                                                                                                                                    | `garch(numlist)` | GARCH terms                                                        |
|                                                                                                                                                                                    | `het(varlist)`   | include `varlist` in the specification of the conditional variance |
| You must `tsset` your data before using `mgarch vcc`; see [<strong>[TS]</strong> tsset](http://www.stata.com/help.cgi?tsset).                           |                  |                                                                    |
| `indepvars` and `varlist` may contain factor variables; see [<strong>fvvarlist</strong>](http://www.stata.com/help.cgi?fvvarlist).                      |                  |                                                                    |
| `depvars`, `indepvars`, and `varlist` may contain time-series operators; see [<strong>tsvarlist</strong>](http://www.stata.com/help.cgi?tsvarlist).     |                  |                                                                    |
| `by`, `fp`, `rolling`, and `statsby` are allowed; see [<strong>prefix</strong>](http://www.stata.com/help.cgi?prefix).                                  |                  |                                                                    |
| `coeflegend` does not appear in the dialog box.                                                                                                                                    |                  |                                                                    |
| See [<strong>[TS]</strong> mgarch vcc postestimation](http://www.stata.com/help.cgi?mgarch_vcc_postestimation) for features available after estimation. |                  |                                                                    |
