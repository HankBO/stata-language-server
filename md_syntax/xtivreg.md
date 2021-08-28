## Syntax

GLS random-effects (RE) model

`xtivreg`
[depvar](http://www.stata.com/help.cgi?depvar)
\[`varlist_1`\] `(varlist_2 = varlist_iv)` <span
class="command">\[`if`\] \[`in`\]_ \[`, re RE_options`\]

Between-effects (BE) model

`xtivreg`
[depvar](http://www.stata.com/help.cgi?depvar)
\[`varlist_1`\] `(varlist_2 = varlist_iv)` <span
class="command">\[`if`\] \[`in`\]_ `, be` \[`BE_options`\]

Fixed-effects (FE) model

`xtivreg`
[depvar](http://www.stata.com/help.cgi?depvar)
\[`varlist_1`\] `(varlist_2 = varlist_iv)` <span
class="command">\[`if`\] \[`in`\]_ `, fe` \[`FE_options`\]

First-differenced (FD) estimator

`xtivreg`
[depvar](http://www.stata.com/help.cgi?depvar)
\[`varlist_1`\] `(varlist_2 = varlist_iv)` <span
class="command">\[`if`\] \[`in`\]_ `, fd` \[`FD_options`\]

| RE\_options |                   | Description                                                                                                                                      |
|-------------|-------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| Model       |                   |                                                                                                                                                  |
|             | `re`              | use random-effects estimator; the default                                                                                                        |
|             | `ec2sls`          | use Baltagi's EC2SLS random-effects estimator                                                                                                    |
|             | `nosa`            | use the Baltagi-Chang estimators of the variance components                                                                                      |
|             | `regress`         | treat covariates as exogenous and ignore instrumental variables                                                                                  |
| SE/Robust   |                   |                                                                                                                                                  |
|             | `vce(vcetype)`    | `vcetype` may be `conventional`, `robust`, `cluster clustvar`, `bootstrap`, or `jackknife`                                                     |
| Reporting   |                   |                                                                                                                                                  |
|             | `level(#)`        | set confidence level; default is `level(95)`                                                                                                     |
|             | `first`           | report first-stage estimates                                                                                                                     |
|             | `small`           | report t and F statistics instead of Z and chi-squared statistics                                                                                |
|             | `theta`           | report theta                                                                                                                                     |
|             | `display_options` | control columns and column formats, row spacing, line width, display of omitted variables and base and empty cells, and factor-variable labeling |
|             | `coeflegend`      | display legend instead of statistics                                                                                                             |

| BE\_options |                   | Description                                                                                                                                      |
|-------------|-------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| Model       |                   |                                                                                                                                                  |
|             | `be`              | use between-effects estimator                                                                                                                    |
|             | `regress`         | treat covariates as exogenous and ignore instrumental variables                                                                                  |
| SE/Robust   |                   |                                                                                                                                                  |
|             | `vce(vcetype)`    | `vcetype` may be `conventional`, `robust`, `cluster clustvar`, `bootstrap`, or `jackknife`                                                     |
| Reporting   |                   |                                                                                                                                                  |
|             | `level(#)`        | set confidence level; default is `level(95)`                                                                                                     |
|             | `first`           | report first-stage estimates                                                                                                                     |
|             | `small`           | report `t` and `F` statistics instead of `Z` and chi-squared statistics                                                                          |
|             | `display_options` | control columns and column formats, row spacing, line width, display of omitted variables and base and empty cells, and factor-variable labeling |
|             | `coeflegend`      | display legend instead of statistics                                                                                                             |

| FE\_options |                   | Description                                                                                                                                      |
|-------------|-------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| Model       |                   |                                                                                                                                                  |
|             | `fe`              | use fixed-effects estimator                                                                                                                      |
|             | `regress`         | treat covariates as exogenous and ignore instrumental variables                                                                                  |
| SE/Robust   |                   |                                                                                                                                                  |
|             | `vce(vcetype)`    | `vcetype` may be `conventional`, `robust`, `cluster clustvar`, `bootstrap`, or `jackknife`                                                     |
| Reporting   |                   |                                                                                                                                                  |
|             | `level(#)`        | set confidence level; default is `level(95)`                                                                                                     |
|             | `first`           | report first-stage estimates                                                                                                                     |
|             | `small`           | report `t` and `F` statistics instead of `Z` and chi-squared statistics                                                                          |
|             | `display_options` | control columns and column formats, row spacing, line width, display of omitted variables and base and empty cells, and factor-variable labeling |
|             | `coeflegend`      | display legend instead of statistics                                                                                                             |

| FD\_options |                   | Description                                                                                   |
|-------------|-------------------|-----------------------------------------------------------------------------------------------|
| Model       |                   |                                                                                               |
|             | `noconstant`      | suppress constant term                                                                        |
|             | `fd`              | use first-differenced estimator                                                               |
|             | `regress`         | treat covariates as exogenous and ignore instrumental variables                               |
| SE/Robust   |                   |                                                                                               |
|             | `vce(vcetype)`    | `vcetype` may be `conventional`, `robust`, `cluster clustvar`, `bootstrap`, or `jackknife`  |
| Reporting   |                   |                                                                                               |
|             | `level(#)`        | set confidence level; default is `level(95)`                                                  |
|             | `first`           | report first-stage estimates                                                                  |
|             | `small`           | report `t` and `F` statistics instead of `Z` and chi-squared statistics                       |
|             | `display_options` | control columns and column formats, row spacing, line width, and display of omitted variables |
|             | `coeflegend`      | display legend instead of statistics                                                          |

A panel variable must be specified. For `xtivreg, fd`, a time variable
must also be specified. Use
[<strong>xtset</strong>](http://www.stata.com/help.cgi?xtset).

`varlist_1` and `varlist_iv` may contain factor variables, except for
the `fd` estimator; see
[<strong>fvvarlist</strong>](http://www.stata.com/help.cgi?fvvarlist).

`depvar`, `varlist_1`, `varlist_2`, and `varlist_iv` may contain
time-series operators; see
[<strong>tsvarlist</strong>](http://www.stata.com/help.cgi?tsvarlist).

`by` and `statsby` are allowed; see
[<strong>prefix</strong>](http://www.stata.com/help.cgi?prefix).

`coeflegend` does not appear in the dialog box.

See
[<strong>[XT]</strong> xtivreg postestimation](http://www.stata.com/help.cgi?xtivreg_postestimation)
for features available after estimation.
