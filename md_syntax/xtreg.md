## Syntax

GLS random-effects (RE) model

`xtreg`
[depvar](http://www.stata.com/help.cgi?depvar)
\[[indepvars](http://www.stata.com/help.cgi?indepvars)\]
_\[`if`\] \[`in`\]_ \[`, re RE_options`\]

Between-effects (BE) model

`xtreg`
[depvar](http://www.stata.com/help.cgi?depvar)
\[[indepvars](http://www.stata.com/help.cgi?indepvars)\]
_\[`if`\] \[`in`\]_ `, be` \[`BE_options`\]

Fixed-effects (FE) model

`xtreg`
[depvar](http://www.stata.com/help.cgi?depvar)
\[[indepvars](http://www.stata.com/help.cgi?indepvars)\]
_\[`if`\] \[`in`\]_ \[`weight`\] `, fe`
\[`FE_options`\]

ML random-effects (MLE) model

`xtreg`
[depvar](http://www.stata.com/help.cgi?depvar)
\[[indepvars](http://www.stata.com/help.cgi?indepvars)\]
_\[`if`\] \[`in`\]_ \[`weight`\] `, mle`
\[`MLE_options`\]

Population-averaged (PA) model

`xtreg`
[depvar](http://www.stata.com/help.cgi?depvar)
\[[indepvars](http://www.stata.com/help.cgi?indepvars)\]
_\[`if`\] \[`in`\]_ \[`weight`\] `, pa`
\[`PA_options`\]

| RE\_options |                   | Description                                                                                                                                      |
|-------------|-------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| Model       |                   |                                                                                                                                                  |
|             | `re`              | use random-effects estimator; the default                                                                                                        |
|             | `sa`              | use Swamy-Arora estimator of the variance components                                                                                             |
| SE/Robust   |                   |                                                                                                                                                  |
|             | `vce(vcetype)`    | `vcetype` may be `conventional`, `robust`, `cluster clustvar`, `bootstrap`, or `jackknife`                                                     |
| Reporting   |                   |                                                                                                                                                  |
|             | `level(#)`        | set confidence level; default is `level(95)`                                                                                                     |
|             | `theta`           | report theta                                                                                                                                     |
|             | `display_options` | control columns and column formats, row spacing, line width, display of omitted variables and base and empty cells, and factor-variable labeling |
|             | `coeflegend`      | display legend instead of statistics                                                                                                             |

| BE\_options |                   | Description                                                                                                                                      |
|-------------|-------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| Model       |                   |                                                                                                                                                  |
|             | `be`              | use between-effects estimator                                                                                                                    |
|             | `wls`             | use weighted least squares                                                                                                                       |
| SE          |                   |                                                                                                                                                  |
|             | `vce(vcetype)`    | `vcetype` may be `conventional`, `bootstrap`, or `jackknife`                                                                                     |
| Reporting   |                   |                                                                                                                                                  |
|             | `level(#)`        | set confidence level; default is `level(95)`                                                                                                     |
|             | `display_options` | control columns and column formats, row spacing, line width, display of omitted variables and base and empty cells, and factor-variable labeling |
|             | `coeflegend`      | display legend instead of statistics                                                                                                             |

| FE\_options |                   | Description                                                                                                                                      |
|-------------|-------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| Model       |                   |                                                                                                                                                  |
|             | `fe`              | use fixed-effects estimator                                                                                                                      |
| SE/Robust   |                   |                                                                                                                                                  |
|             | `vce(vcetype)`    | `vcetype` may be `conventional`, `robust`, `cluster clustvar`, `bootstrap`, or `jackknife`                                                     |
| Reporting   |                   |                                                                                                                                                  |
|             | `level(#)`        | set confidence level; default is `level(95)`                                                                                                     |
|             | `display_options` | control columns and column formats, row spacing, line width, display of omitted variables and base and empty cells, and factor-variable labeling |
|             | `coeflegend`      | display legend instead of statistics                                                                                                             |

| MLE\_options |                    | Description                                                                                                                                      |
|--------------|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| Model        |                    |                                                                                                                                                  |
|              | `noconstant`       | suppress constant term                                                                                                                           |
|              | `mle`              | use ML random-effects estimator                                                                                                                  |
| SE           |                    |                                                                                                                                                  |
|              | `vce(vcetype)`     | `vcetype` may be `oim`, `bootstrap`, or `jackknife`                                                                                              |
| Reporting    |                    |                                                                                                                                                  |
|              | `level(#)`         | set confidence level; default is `level(95)`                                                                                                     |
|              | `display_options`  | control columns and column formats, row spacing, line width, display of omitted variables and base and empty cells, and factor-variable labeling |
| Maximization |                    |                                                                                                                                                  |
|              | `maximize_options` | control the maximization process; seldom used                                                                                                    |
|              | `coeflegend`       | display legend instead of statistics                                                                                                             |

| PA\_options  |                         | Description                                                                                                                                      |
|--------------|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| Model        |                         |                                                                                                                                                  |
|              | `noconstant`            | suppress constant term                                                                                                                           |
|              | `pa`                    | use population-averaged estimator                                                                                                                |
|              | `offset(varname)`       | include `varname` in model with coefficient constrained to 1                                                                                     |
| Correlation  |                         |                                                                                                                                                  |
|              | `corr(correlation)` | within-panel correlation structure                                                                                                               |
|              | `force`                 | estimate even if observations unequally spaced in time                                                                                           |
| SE/Robust    |                         |                                                                                                                                                  |
|              | `vce(vcetype)`          | `vcetype` may be `conventional`, `robust`, `bootstrap`, or `jackknife`                                                                           |
|              | `nmp`                   | use divisor N-P instead of the default N                                                                                                         |
|              | `rgf`                   | multiply the robust variance estimate by (N-1)/(N-P)                                                                                             |
|              | `scale(parm)`           | override the default scale parameter; `parm` may be `x2`, `dev`, `phi`, or `#`                                                                   |
| Reporting    |                         |                                                                                                                                                  |
|              | `level(#)`              | set confidence level; default is `level(95)`                                                                                                     |
|              | `display_options`       | control columns and column formats, row spacing, line width, display of omitted variables and base and empty cells, and factor-variable labeling |
| Optimization |                         |                                                                                                                                                  |
|              | `optimize_options`      | control the optimization process; seldom used                                                                                                    |
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

A panel variable must be specified. For `xtreg, pa`, correlation
structures other than `exchangeable` and `independent` require that a
time variable also be specified. Use
[<strong>xtset</strong>](http://www.stata.com/help.cgi?xtset).

`indepvars` may contain factor variables; see
[<strong>fvvarlist</strong>](http://www.stata.com/help.cgi?fvvarlist).

`depvar` and `indepvars` may contain time-series operators; see
[<strong>tsvarlist</strong>](http://www.stata.com/help.cgi?tsvarlist).

`by`, `mi estimate`, and `statsby` are allowed; see
[<strong>prefix</strong>](http://www.stata.com/help.cgi?prefix).
`fp` is allowed for the between-effects, fixed-effects, and
maximum-likelihood random-effects models.

`vce(bootstrap)` and `vce(jackknife)` are not allowed with the
[<strong>mi estimate</strong>](http://www.stata.com/help.cgi?mi%20estimate)
prefix.

`aweight`s, `fweight`s, and `pweight`s are allowed for the fixed-effects
model. `iweight`s, `fweight`s, and `pweight`s are allowed for the
population-averaged model. `iweight`s are allowed for the
maximum-likelihood random-effects (MLE) model.
[<strong>Weights</strong>](http://www.stata.com/help.cgi?weight)
must be constant within panel.

`coeflegend` does not appear in the dialog box.

See
[<strong>[XT]</strong> xtreg postestimation](http://www.stata.com/help.cgi?xtreg_postestimation)
for features available after estimation.
