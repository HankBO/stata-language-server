## Syntax

`xtmepoisson`
[depvar](http://www.stata.com/help.cgi?depvar)
\[`fe_equation`\] `|| re_equation` \[`|| re_equation` ...\] \[`,`
`options`\]

where the syntax of `fe_equation` is

\[[indepvars](http://www.stata.com/help.cgi?indepvars)\]
_\[`if`\] \[`in`\]_ \[`, fe_options`\]

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

| fe\_options |                       | Description                                                        |
|-------------|-----------------------|--------------------------------------------------------------------|
| Model       |                       |                                                                    |
|             | `noconstant`          | suppress constant term from the fixed-effects equation             |
|             | `exposure(varname_e)` | include ln(`varname_e`) in model with coefficient constrained to 1 |
|             | `offset(varname_o)`   | include `varname_o` in model with coefficient constrained to 1     |

| re\_options |                       | Description                                            |
|-------------|-----------------------|--------------------------------------------------------|
| Model       |                       |                                                        |
|             | `covariance(vartype)` | variance-covariance structure of the random effects    |
|             | `noconstant`          | suppress the constant from the random-effects equation |
|             | `collinear`           | keep collinear variables                               |

| options      |                                      | Description                                                                                         |
|--------------|--------------------------------------|-----------------------------------------------------------------------------------------------------|
| Integration  |                                      |                                                                                                     |
|              | `laplace`                            | use Laplacian approximation; equivalent to `intpoints(1)`                                           |
|              | `intpoints(#` \[`#` ...\]`)`     | set the number of integration (quadrature) points; default is 7                                     |
| Reporting    |                                      |                                                                                                     |
|              | `level(#)`                           | set confidence level; default is `level(95)`                                                        |
|              | `irr`                                | report fixed-effects coefficients as incidence-rate ratios                                          |
|              | `variance`                           | show random-effects parameter estimates as variances and covariances                                |
|              | `noretable`                          | suppress random-effects table                                                                       |
|              | `nofetable`                          | suppress fixed-effects table                                                                        |
|              | `estmetric`                          | show parameter estimates in the estimation metric                                                   |
|              | `noheader`                           | suppress output header                                                                              |
|              | `nogroup`                            | suppress table summarizing groups                                                                   |
|              | `nolrtest`                           | do not perform LR test comparing to Poisson regression                                              |
|              | `display_options`                    | control column formats, row spacing, and display of omitted variables and base and empty cells      |
| Maximization |                                      |                                                                                                     |
|              | `maximize_options`                   | control the maximization process during gradient-based optimization; seldom used                    |
|              | `retolerance(#)`                     | tolerance for random-effects estimates; default is `retolerance(1e-8)`; seldom used                 |
|              | `reiterate(#)`                       | maximum number of iterations for random-effects estimation; default is `reiterate(50)`; seldom used |
|              | `matsqrt`                            | parameterize variance components using matrix square roots; the default                             |
|              | `matlog`                             | parameterize variance components using matrix logarithms                                            |
|              | `refineopts(maximize_options)` | control the maximization process during refinement of starting values                               |
|              | `coeflegend`                         | display legend instead of statistics                                                                |

| vartype |                | Description                                                                                                       |
|---------|----------------|-------------------------------------------------------------------------------------------------------------------|
|         | `independent`  | one variance parameter per random effect, all covariances zero; the default unless a factor variable is specified |
|         | `exchangeable` | equal variances for random effects, and one common pairwise covariance                                            |
|         | `identity`     | equal variances for random effects, all covariances zero; the default if factor variables are specified           |
|         | `unstructured` | all variances-covariances distinctly estimated                                                                    |

`indepvars` may contain factor variables; see
[<strong>fvvarlist</strong>](http://www.stata.com/help.cgi?fvvarlist).

`indepvars` and `varlist` may contain time-series operators; see
[<strong>tsvarlist</strong>](http://www.stata.com/help.cgi?tsvarlist).

`bootstrap`, `by`, `jackknife`, `mi estimate`, `rolling`, and `statsby`
are allowed; see
[<strong>prefix</strong>](http://www.stata.com/help.cgi?prefix).

`coeflegend` does not appear in the dialog box.

See
[<strong>[XT]</strong> xtmepoisson postestimation](http://www.stata.com/help.cgi?xtmepoisson_postestimation)
for features available after estimation.
