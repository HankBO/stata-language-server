## Syntax

`xtmixed`
[depvar](http://www.stata.com/help.cgi?depvar)
\[`fe_equation`\] \[`|| re_equation`\] \[`|| re_equation` ...\]
\[`, options`\]

where the syntax of `fe_equation` is

\[[indepvars](http://www.stata.com/help.cgi?indepvars)\]
_\[`if`\] \[`in`\]_ <span
class="command">\[`weight`\]_ \[`, fe_options`\]

and the syntax of `re_equation` is one of the following:

for random coefficients and intercepts

`levelvar:`
\[[varlist](http://www.stata.com/help.cgi?varlist)\]
\[`, re_options`\]

for a random effect among the values of a factor variable

`levelvar:`
`R.`[varname](http://www.stata.com/help.cgi?varname)
\[`, re_options`\]

`levelvar` is a variable identifying the group structure for the random
effects at that level or `_all` representing one group comprising all
observations.

| fe\_options |              | Description                                            |
|-------------|--------------|--------------------------------------------------------|
| Model       |              |                                                        |
|             | `noconstant` | suppress constant term from the fixed-effects equation |

| re\_options |                       | Description                                             |
|-------------|-----------------------|---------------------------------------------------------|
| Model       |                       |                                                         |
|             | `covariance(vartype)` | variance-covariance structure of the random effects     |
|             | `noconstant`          | suppress constant term from the random-effects equation |
|             | `collinear`           | keep collinear variables                                |
|             | `fweight(exp)`        | frequency weights at higher levels                      |
|             | `pweight(exp)`        | sampling weights at higher levels                       |

| vartype |                | Description                                                                                                       |
|---------|----------------|-------------------------------------------------------------------------------------------------------------------|
|         | `independent`  | one variance parameter per random effect, all covariances zero; the default unless a factor variable is specified |
|         | `exchangeable` | equal variances for random effects, and one common pairwise covariance                                            |
|         | `identity`     | equal variances for random effects, all covariances zero; the default for factor variables                        |
|         | `unstructured` | all variances and covariances distinctly estimated                                                                |

| options      |                              | Description                                                                                    |
|--------------|------------------------------|------------------------------------------------------------------------------------------------|
| Model        |                              |                                                                                                |
|              | `mle`                        | fit model via maximum likelihood, the default                                                  |
|              | `reml`                       | fit model via restricted maximum likelihood                                                    |
|              | ` pwscale(scale_method)` | control scaling of sampling weights in two-level models                                        |
|              | `residuals(rspec)`       | structure of residual errors                                                                   |
| SE/Robust    |                              |                                                                                                |
|              | `vce(vcetype)`               | `vcetype` may be `oim`, `robust`, or `cluster clustvar`                                      |
| Reporting    |                              |                                                                                                |
|              | `level(#)`                   | set confidence level; default is `level(95)`                                                   |
|              | `variance`                   | show random-effects parameter estimates as variances and covariances                           |
|              | `noretable`                  | suppress random-effects table                                                                  |
|              | `nofetable`                  | suppress fixed-effects table                                                                   |
|              | `estmetric`                  | show parameter estimates in the estimation metric                                              |
|              | `noheader`                   | suppress output header                                                                         |
|              | `nogroup`                    | suppress table summarizing groups                                                              |
|              | `nostderr`                   | do not estimate standard errors of random-effects parameters                                   |
|              | `nolrtest`                   | do not perform LR test comparing to linear regression                                          |
|              | `display_options`            | control column formats, row spacing, and display of omitted variables and base and empty cells |
| EM options   |                              |                                                                                                |
|              | `emiterate(#)`               | number of EM iterations, default is 20                                                         |
|              | `emtolerance(#)`             | EM convergence tolerance, default is 1e-10                                                     |
|              | `emonly`                     | fit model exclusively using EM                                                                 |
|              | `emlog`                      | show EM iteration log                                                                          |
|              | `emdots`                     | show EM iterations as dots                                                                     |
| Maximization |                              |                                                                                                |
|              | `maximize_options`           | control the maximization process; seldom used                                                  |
|              | `matsqrt`                    | parameterize variance components using matrix square roots; the default                        |
|              | `matlog`                     | parameterize variance components using matrix logarithms                                       |
|              | `coeflegend`                 | display legend instead of statistics                                                           |

`indepvars` may contain factor variables; see
[<strong>fvvarlist</strong>](http://www.stata.com/help.cgi?fvvarlist).

`depvar`, `indepvars`, and `varlist` may contain time-series operators;
see
[<strong>tsvarlist</strong>](http://www.stata.com/help.cgi?tsvarlist).

`bootstrap`, `by`, `jackknife`, `mi estimate`, `rolling`, and `statsby`
are allowed; see
[<strong>prefix</strong>](http://www.stata.com/help.cgi?prefix).

`pweight`s and `fweight`s are allowed; see
[<strong>weight</strong>](http://www.stata.com/help.cgi?weight).

`coeflegend` does not appear in the dialog box.

See
[<strong>[XT]</strong> xtmixed postestimation](http://www.stata.com/help.cgi?xtmixed_postestimation)
for features available after estimation.
