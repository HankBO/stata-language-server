## Syntax

`xtstreg`
\[[indepvars](http://www.stata.com/help.cgi?indepvars)\]
_\[`if`\] \[`in`\]_ <span
class="command">\[`weight`\]_`, distribution(distname)`
\[`options`\]

| options                                  |                                                 | Description                                                                                                                                      |
|------------------------------------------|-------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| Model                                    |                                                 |                                                                                                                                                  |
|                                          | `noconstant`                                    | suppress constant term                                                                                                                           |
| \*                                       | `distribution(distname)`                    | specify survival distribution                                                                                                                    |
|                                          | `time`                                          | use accelerated failure-time metric                                                                                                              |
|                                          | `offset(varname)`                               | include `varname` in model with coefficient constrained to 1                                                                                     |
|                                          | `constraints(estimation options##constraints()` | apply specified linear constraints                                                                                                               |
|                                          | `collinear`                                     | keep collinear variables                                                                                                                         |
| SE/Robust                                |                                                 |                                                                                                                                                  |
|                                          | `vce(vcetype)`                                  | `vcetype` may be `oim`, `robust`, `cluster clustvar`, `bootstrap`, or `jackknife`                                                              |
| Reporting                                |                                                 |                                                                                                                                                  |
|                                          | `level(#)`                                      | set confidence level; default is `level(95)`                                                                                                     |
|                                          | `nohr`                                          | do not report hazard ratios                                                                                                                      |
|                                          | `noshow`                                        | do not show st setting information                                                                                                               |
|                                          | `lrmodel`                                       | perform the likelihood-ratio model test instead of the default Wald test                                                                         |
|                                          | `nocnsreport`                                   | do not display constraints                                                                                                                       |
|                                          | `tratio`                                        | report time ratios                                                                                                                               |
|                                          | `display_options`                               | control columns and column formats, row spacing, line width, display of omitted variables and base and empty cells, and factor-variable labeling |
| Integration                              |                                                 |                                                                                                                                                  |
|                                          | `intmethod(intmethod)`                          | integration method; `intmethod` may be `mvaghermite` (the default) or `ghermite`                                                                 |
|                                          | `intpoints(#)`                                  | use \# quadrature points; default is `intpoints(12)`                                                                                             |
| Maximization                             |                                                 |                                                                                                                                                  |
|                                          | `maximize_options`                              | control the maximization process; seldom used                                                                                                    |
|                                          | `startgrid(numlist)`                            | improve starting value of the random-intercept parameter by performing a grid search                                                             |
|                                          | `nodisplay`                                     | suppress display the header and coefficients                                                                                                     |
|                                          | `coeflegend`                                    | display legend instead of statistics                                                                                                             |
| \* `distribution(distname)` is required. |                                                 |                                                                                                                                                  |

| distname |               | Description                       |
|----------|---------------|-----------------------------------|
|          | `exponential` | exponential survival distribution |
|          | `loglogistic` | loglogistic survival distribution |
|          | `llogistic`   | synonym for `loglogistic`         |
|          | `weibull`     | Weibull survival distribution     |
|          | `lognormal`   | lognormal survival distribution   |
|          | `lnormal`     | synonym for `lognormal`           |
|          | `gamma`       | gamma survival distribution       |

You must `stset` your data before using `xtstreg`; see
[<strong>[ST]</strong> stset](http://www.stata.com/help.cgi?stset).

A panel variable must be specified; see
[<strong>xtset</strong>](http://www.stata.com/help.cgi?xtset).

`indepvars` may contain factor variables; see
[<strong>fvvarlist</strong>](http://www.stata.com/help.cgi?fvvarlist).

`varlist` may contain time-series operators; see
[<strong>tsvarlist</strong>](http://www.stata.com/help.cgi?tsvarlist).

`by`, `fp`, and `statsby` are allowed; see
[<strong>prefix</strong>](http://www.stata.com/help.cgi?prefix).

`fweight`s, `iweight`s, and `pweight`s are allowed; see
[<strong>weight</strong>](http://www.stata.com/help.cgi?weight).
Weights must be constant within panel.

`startgrid()`, `nodisplay`, and `coeflegend` do not appear in the dialog
box.

See
[<strong>[XT]</strong> xtstreg postestimation](http://www.stata.com/help.cgi?xtstreg_postestimation)
for features available after estimation.
