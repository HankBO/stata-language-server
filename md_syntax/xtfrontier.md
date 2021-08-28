## Syntax

Time-invariant model

`xtfrontier`
[depvar](http://www.stata.com/help.cgi?depvar)
\[[indepvars](http://www.stata.com/help.cgi?indepvars)\]
_\[`if`\] \[`in`\]_ \[`weight`\] `, ti`
\[`ti_options`\]

Time-varying decay model

`xtfrontier`
[depvar](http://www.stata.com/help.cgi?depvar)
\[[indepvars](http://www.stata.com/help.cgi?indepvars)\]
_\[`if`\] \[`in`\]_ \[`weight`\] `, tvd`
\[`tvd_options`\]

| ti\_options  |                                | Description                                                                                                                                      |
|--------------|--------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| Model        |                                |                                                                                                                                                  |
|              | `noconstant`                   | suppress constant term                                                                                                                           |
|              | `ti`                           | use time-invariant model                                                                                                                         |
|              | `cost`                         | fit cost frontier model                                                                                                                          |
|              | `constraints(constraints)` | apply specified linear constraints                                                                                                               |
|              | `collinear`                    | keep collinear variables                                                                                                                         |
| SE           |                                |                                                                                                                                                  |
|              | `vce(vcetype)`                 | `vcetype` may be `oim`, `bootstrap`, or `jackknife`                                                                                              |
| Reporting    |                                |                                                                                                                                                  |
|              | `level(#)`                     | set confidence level; default is `level(95)`                                                                                                     |
|              | `nocnsreport`                  | do not display constraints                                                                                                                       |
|              | `display_options`              | control columns and column formats, row spacing, line width, display of omitted variables and base and empty cells, and factor-variable labeling |
| Maximization |                                |                                                                                                                                                  |
|              | `maximize_options`             | control the maximization process; seldom used                                                                                                    |
|              | `coeflegend`                   | display legend instead of statistics                                                                                                             |

| tvd\_options |                                | Description                                                                                                                                      |
|--------------|--------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| Model        |                                |                                                                                                                                                  |
|              | `noconstant`                   | suppress constant term                                                                                                                           |
|              | `tvd`                          | use time-varying decay model                                                                                                                     |
|              | `cost`                         | fit cost frontier model                                                                                                                          |
|              | `constraints(constraints)` | apply specified linear constraints                                                                                                               |
|              | `collinear`                    | keep collinear variables                                                                                                                         |
| SE           |                                |                                                                                                                                                  |
|              | `vce(vcetype)`                 | `vcetype` may be `oim`, `bootstrap`, or `jackknife`                                                                                              |
| Reporting    |                                |                                                                                                                                                  |
|              | `level(#)`                     | set confidence level; default is `level(95)`                                                                                                     |
|              | `nocnsreport`                  | do not display constraints                                                                                                                       |
|              | `display_options`              | control columns and column formats, row spacing, line width, display of omitted variables and base and empty cells, and factor-variable labeling |
| Maximization |                                |                                                                                                                                                  |
|              | `maximize_options`             | control the maximization process; seldom used                                                                                                    |
|              | `coeflegend`                   | display legend instead of statistics                                                                                                             |

A panel variable must be specified. For `xtfrontier, tvd`, a time
variable must also be specified. Use
[<strong>xtset</strong>](http://www.stata.com/help.cgi?xtset).

`indepvars` may contain factor variables; see
[<strong>fvvarlist</strong>](http://www.stata.com/help.cgi?fvvarlist).

`depvars` and `indepvars` may contain time-series operators; see
[<strong>tsvarlist</strong>](http://www.stata.com/help.cgi?tsvarlist).

`by`, `fp`, and `statsby` are allowed; see
[<strong>prefix</strong>](http://www.stata.com/help.cgi?prefix).

`fweight`s and `iweight`s are allowed; see
[<strong>weight</strong>](http://www.stata.com/help.cgi?weight).
Weights must be constant within panel.

`coeflegend` does not appear in the dialog box.

See
[<strong>[XT]</strong> xtfrontier postestimation](http://www.stata.com/help.cgi?xtfrontier_postestimation)
for features available after estimation.
