## Syntax

Random-effects (RE) model

`xtlogit`
[depvar](http://www.stata.com/help.cgi?depvar)
\[[indepvars](http://www.stata.com/help.cgi?indepvars)\]
_\[`if`\] \[`in`\]_ \[`weight`\] \[`, re`
`RE_options`\]

Conditional fixed-effects (FE) model

`xtlogit`
[depvar](http://www.stata.com/help.cgi?depvar)
\[[indepvars](http://www.stata.com/help.cgi?indepvars)\]
_\[`if`\] \[`in`\]_ \[`weight`\] `, fe`
\[`FE_options`\]

Population-averaged (PA) model

`xtlogit`
[depvar](http://www.stata.com/help.cgi?depvar)
\[[indepvars](http://www.stata.com/help.cgi?indepvars)\]
_\[`if`\] \[`in`\]_ \[`weight`\] `, pa`
\[`PA_options`\]

| RE\_options  |                                                 | Description                                                                                                                                      |
|--------------|-------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| Model        |                                                 |                                                                                                                                                  |
|              | `noconstant`                                    | suppress constant term                                                                                                                           |
|              | `re`                                            | use random-effects estimator; the default                                                                                                        |
|              | `offset(varname)`                               | include `varname` in model with coefficient constrained to 1                                                                                     |
|              | `constraints(estimation options##constraints()` | apply specified linear constraints                                                                                                               |
|              | `collinear`                                     | keep collinear variables                                                                                                                         |
|              | `asis`                                          | retain perfect predictor variables                                                                                                               |
| SE/Robust    |                                                 |                                                                                                                                                  |
|              | `vce(vcetype)`                                  | `vcetype` may be `oim`, `robust`, `cluster clustvar`, `bootstrap`, or `jackknife`                                                              |
| Reporting    |                                                 |                                                                                                                                                  |
|              | `level(#)`                                      | set confidence level; default is `level(95)`                                                                                                     |
|              | `or`                                            | report odds ratios                                                                                                                               |
|              | `lrmodel`                                       | perform the likelihood-ratio model test instead of the default Wald test                                                                         |
|              | `nocnsreport`                                   | do not display constraints                                                                                                                       |
|              | `display_options`                               | control columns and column formats, row spacing, line width, display of omitted variables and base and empty cells, and factor-variable labeling |
| Integration  |                                                 |                                                                                                                                                  |
|              | `intmethod(intmethod)`                          | integration method; `intmethod` may be `mvaghermite` (the default) or `ghermite`                                                                 |
|              | `intpoints(#)`                                  | use \# quadrature points; default is `intpoints(12)`                                                                                             |
| Maximization |                                                 |                                                                                                                                                  |
|              | `maximize_options`                              | control the maximization process; seldom used                                                                                                    |
|              | `nodisplay`                                     | suppress display of header and coefficients                                                                                                      |
|              | `coeflegend`                                    | display legend instead of statistics                                                                                                             |

| FE\_options  |                                                 | Description                                                                                                                                      |
|--------------|-------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| Model        |                                                 |                                                                                                                                                  |
|              | `fe`                                            | use fixed-effects estimator                                                                                                                      |
|              | `offset(varname)`                               | include `varname` in model with coefficient constrained to 1                                                                                     |
|              | `constraints(estimation options##constraints()` | apply specified linear constraints                                                                                                               |
|              | `collinear`                                     | keep collinear variables                                                                                                                         |
| SE           |                                                 |                                                                                                                                                  |
|              | `vce(vcetype)`                                  | `vcetype` may be `oim`, `bootstrap`, or `jackknife`                                                                                              |
| Reporting    |                                                 |                                                                                                                                                  |
|              | `level(#)`                                      | set confidence level; default is `level(95)`                                                                                                     |
|              | `or`                                            | report odds ratios                                                                                                                               |
|              | `lrmodel`                                       | perform the likelihood-ratio model test instead of the default Wald test                                                                         |
|              | `nocnsreport`                                   | do not display constraints                                                                                                                       |
|              | `display_options`                               | control columns and column formats, row spacing, line width, display of omitted variables and base and empty cells, and factor-variable labeling |
| Maximization |                                                 |                                                                                                                                                  |
|              | `maximize_options`                              | control the maximization process; seldom used                                                                                                    |
|              | `nodisplay`                                     | suppress display of header and coefficients                                                                                                      |
|              | `coeflegend`                                    | display legend instead of statistics                                                                                                             |

| PA\_options  |                         | Description                                                                                                                                      |
|--------------|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| Model        |                         |                                                                                                                                                  |
|              | `noconstant`            | suppress constant term                                                                                                                           |
|              | `pa`                    | use population-averaged estimator                                                                                                                |
|              | `offset(varname)`       | include `varname` in model with coefficient constrained to 1                                                                                     |
|              | `asis`                  | retain perfect predictor variables                                                                                                               |
| Correlation  |                         |                                                                                                                                                  |
|              | `corr(correlation)` | within-panel correlation structure                                                                                                               |
|              | `force`                 | estimate even if observations unequally spaced in time                                                                                           |
| SE/Robust    |                         |                                                                                                                                                  |
|              | `vce(vcetype)`          | `vcetype` may be `conventional`, `robust`, `bootstrap`, or `jackknife`                                                                           |
|              | `nmp`                   | use divisor N-P instead of the default N                                                                                                         |
|              | `scale(parm)`           | override the default scale parameter; `parm` may be `x2`, `dev`, `phi`, or `#`                                                                   |
| Reporting    |                         |                                                                                                                                                  |
|              | `level(#)`              | set confidence level; default is `level(95)`                                                                                                     |
|              | `or`                    | report odds ratios                                                                                                                               |
|              | `display_options`       | control columns and column formats, row spacing, line width, display of omitted variables and base and empty cells, and factor-variable labeling |
| Optimization |                         |                                                                                                                                                  |
|              | `optimize_options`      | control the optimization process; seldom used                                                                                                    |
|              | `nodisplay`             | suppress display of header and coefficients                                                                                                      |
|              | `coeflegend`            | display legend instead of statistics                                                                                                             |

| correlation |                     | Description                 |
|-------------|---------------------|-----------------------------|
|             | `exchangeable`      | exchangeable                |
|             | `independent`       | independent                 |
|             | `unstructured`      | unstructured                |
|             | `fixed matname`   | user-specified              |
|             | `ar #`            | autoregressive of order `#` |
|             | `stationary #`    | stationary of order `#`     |
|             | `nonstationary #` | nonstationary of order `#`  |

A panel variable must be specified. For `xtlogit, pa`, correlation
structures other than `exchangeable` and `independent` require that a
time variable also be specified. Use
[<strong>xtset</strong>](http://www.stata.com/help.cgi?xtset).

`indepvars` may contain factor variables; see
[<strong>fvvarlist</strong>](http://www.stata.com/help.cgi?fvvarlist).

`depvar` and `indepvars` may contain time-series operators; see
[<strong>tsvarlist</strong>](http://www.stata.com/help.cgi?tsvarlist).

`by`, `mi estimate`, and `statsby` are allowed; see
[<strong>prefix</strong>](http://www.stata.com/help.cgi?prefix).
`fp` is allowed for the random-effects and fixed-effects models.

`vce(bootstrap)` and `vce(jackknife)` are not allowed with the
[<strong>mi estimate</strong>](http://www.stata.com/help.cgi?mi%20estimate)
prefix.

`iweight`s, `fweight`s, and `pweight`s are allowed for the
population-averaged model, and `iweight`s are allowed for the
fixed-effects and random-effects models; see
[<strong>weight</strong>](http://www.stata.com/help.cgi?weight).
Weights must be constant within panel.

`nodisplay` and `coeflegend` do not appear in the dialog box.

See
[<strong>[XT]</strong> xtlogit postestimation](http://www.stata.com/help.cgi?xtlogit_postestimation)
for features available after estimation.
