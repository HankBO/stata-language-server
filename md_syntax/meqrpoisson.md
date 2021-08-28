## Syntax

`meqrpoisson`
[depvar](http://www.stata.com/help.cgi?depvar)
`fe_equation || re_equation` \[`|| re_equation` ...\] \[`,`
`options`\]

where the syntax of `fe_equation` is

\[[indepvars](http://www.stata.com/help.cgi?indepvars)\]
_\[`if`\] \[`in`\]_ \[`, fe_options`\]

and the syntax of `re_equation` is one of the following:

for random coefficients and intercepts

`levelvar:`
\[[varlist](http://www.stata.com/help.cgi?varlist)\]
\[`, re_options`\]

for random effects among the values of a factor variable

`levelvar:`
`R.`[varname](http://www.stata.com/help.cgi?varname)
\[`, re_options`\]

`levelvar` is a variable identifying the group structure for the random
effects at that level or is `_all` representing one group comprising all
observations.

| fe\_options |                       | Description                                                        |
|-------------|-----------------------|--------------------------------------------------------------------|
| Model       |                       |                                                                    |
|             | `noconstant`          | suppress constant term from the fixed-effects equation             |
|             | `exposure(varname_e)` | include ln(`varname_e`) in model with coefficient constrained to 1 |
|             | `offset(varname_o)`   | include `varname_o` in model with coefficient constrained to 1     |

| re\_options |                       | Description                                             |
|-------------|-----------------------|---------------------------------------------------------|
| Model       |                       |                                                         |
|             | `covariance(vartype)` | variance-covariance structure of the random effects     |
|             | `noconstant`          | suppress constant term from the random-effects equation |
|             | `collinear`           | keep collinear variables                                |

| options      |                                | Description                                                                                                                                      |
|--------------|--------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| Reporting    |                                |                                                                                                                                                  |
|              | `level(#)`                     | set confidence level; default is `level(95)`                                                                                                     |
|              | `irr`                          | report fixed-effects coefficients as incidence-rate ratios                                                                                       |
|              | `variance`                     | show random-effects parameter estimates as variances and covariances; the default                                                                |
|              | `stddeviations`                | show random-effects parameter estimates as standard deviations and correlations                                                                  |
|              | `noretable`                    | suppress random-effects table                                                                                                                    |
|              | `nofetable`                    | suppress fixed-effects table                                                                                                                     |
|              | `estmetric`                    | show parameter estimates as stored in `e(b)`                                                                                                     |
|              | `noheader`                     | suppress output header                                                                                                                           |
|              | `nogroup`                      | suppress table summarizing groups                                                                                                                |
|              | `display_options`              | control columns and column formats, row spacing, line width, display of omitted variables and base and empty cells, and factor-variable labeling |
| Integration  |                                |                                                                                                                                                  |
|              | `intpoints(# [# ...])`         | set the number of integration (quadrature) points; default is `intpoints(7)`                                                                     |
|              | `laplace`                      | use Laplacian approximation; equivalent to `intpoints(1)`                                                                                        |
| Maximization |                                |                                                                                                                                                  |
|              | `maximize_options`             | control the maximization process; seldom used                                                                                                    |
|              | `retolerance(#)`               | tolerance for random-effects estimates; default is `retolerance(1e-8)`; seldom used                                                              |
|              | `reiterate(#)`                 | maximum number of iterations for random-effects estimation; default is `reiterate(50)`; seldom used                                              |
|              | `matsqrt`                      | parameterize variance components using matrix square roots; the default                                                                          |
|              | `matlog`                       | parameterize variance components using matrix logarithms                                                                                         |
|              | `refineopts(maximize_options)` | control the maximization process during refinement of starting values                                                                            |
|              | `coeflegend`                   | display legend instead of statistics                                                                                                             |

| vartype |                | Description                                                                                                        |
|---------|----------------|--------------------------------------------------------------------------------------------------------------------|
|         | `independent`  | one unique variance parameter per random effect, all covariances 0; the default unless the **R.** notation is used |
|         | `exchangeable` | equal variances for random effects, and one common pairwise covariance                                             |
|         | `identity`     | equal variances for random effects, all covariances 0; the default if the **R.** notation is used                  |
|         | `unstructured` | all variances and covariances to be distinctly estimated                                                           |

`indepvars` may contain factor variables; see
[<strong>fvvarlist</strong>](http://www.stata.com/help.cgi?fvvarlist).

`indepvars` and `varlist` may contain time-series operators; see
[<strong>tsvarlist</strong>](http://www.stata.com/help.cgi?tsvarlist).

`bootstrap`, `by`, `jackknife`, `mi estimate`, `rolling`, and `statsby`
are allowed; see
[<strong>prefix</strong>](http://www.stata.com/help.cgi?prefix).

`coeflegend` does not appear in the dialog box.

See
[<strong>[ME]</strong> meqrpoisson postestimation](http://www.stata.com/help.cgi?meqrpoisson_postestimation)
for features available after estimation.
