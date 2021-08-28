## Syntax

`meprobit`
[depvar](http://www.stata.com/help.cgi?depvar)
`fe_equation` \[`|| re_equation`\] \[`|| re_equation` ...\] \[`,`
`options`\]

where the syntax of `fe_equation` is

\[[indepvars](http://www.stata.com/help.cgi?indepvars)\]
_\[`if`\] \[`in`\]_ \[`weight`\] \[`,`
`fe_options`\]

and the syntax of `re_equation` is one of the following:

for random coefficients and intercepts

`levelvar:`
\[[varlist](http://www.stata.com/help.cgi?varlist)\]
\[`, re_options`\]

for random effects among the values of a factor variable

`levelvar:`
`R.`[varname](http://www.stata.com/help.cgi?varname)

`levelvar` is a variable identifying the group structure for the random
effects at that level or is `_all` representing one group comprising all
observations.

| fe\_options |                   | Description                                                  |
|-------------|-------------------|--------------------------------------------------------------|
| Model       |                   |                                                              |
|             | `noconstant`      | suppress constant term from the fixed-effects equation       |
|             | `offset(varname)` | include `varname` in model with coefficient constrained to 1 |
|             | `asis`            | retain perfect predictor variables                           |

| re\_options |                       | Description                                             |
|-------------|-----------------------|---------------------------------------------------------|
| Model       |                       |                                                         |
|             | `covariance(vartype)` | variance-covariance structure of the random effects     |
|             | `noconstant`          | suppress constant term from the random-effects equation |
|             | `fweight(varname)`    | frequency weights at higher levels                      |
|             | `iweight(varname)`    | importance weights at higher levels                     |
|             | `pweight(varname)`    | sampling weights at higher levels                       |

| options      |                                    | Description                                                                                                                                      |
|--------------|------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| Model        |                                    |                                                                                                                                                  |
|              | `binomial(varname`\|`#)`     | set binomial trials if data are in binomial form                                                                                                 |
|              | `constraints(constraints)`     | apply specified linear constraints                                                                                                               |
|              | `collinear`                        | keep collinear variables                                                                                                                         |
| SE/Robust    |                                    |                                                                                                                                                  |
|              | `vce(vcetype)`                     | `vcetype` may be `oim`, `robust`, or `cluster clustvar`                                                                                        |
| Reporting    |                                    |                                                                                                                                                  |
|              | `level(#)`                         | set confidence level; default is `level(95)`                                                                                                     |
|              | `nocnsreport`                      | do not display constraints                                                                                                                       |
|              | `notable`                          | suppress coefficient table                                                                                                                       |
|              | `noheader`                         | suppress output header                                                                                                                           |
|              | `nogroup`                          | suppress table summarizing groups                                                                                                                |
|              | `display_options`                  | control columns and column formats, row spacing, line width, display of omitted variables and base and empty cells, and factor-variable labeling |
| Integration  |                                    |                                                                                                                                                  |
|              | `intmethod(intmethod)`             | integration method                                                                                                                               |
|              | `intpoints(#)`                     | set the number of integration (quadrature) points for all levels; default is `intpoints(7)`                                                      |
| Maximization |                                    |                                                                                                                                                  |
|              | `maximize_options`                 | control the maximization process; seldom used                                                                                                    |
|              | `startvalues(meglm##startvalues()` | method for obtaining starting values                                                                                                             |
|              | `startgrid`\[`(gridspec)`\]    | perform a grid search to improve starting values                                                                                                 |
|              | `noestimate`                       | do not fit the model; show starting values instead                                                                                               |
|              | `dnumerical`                       | use numerical derivative techniques                                                                                                              |
|              | `coeflegend`                       | display legend instead of statistics                                                                                                             |

| vartype |                    | Description                                                                                                                   |
|---------|--------------------|-------------------------------------------------------------------------------------------------------------------------------|
|         | `independent`      | one unique variance parameter per random effect, all covariances 0; the default unless the `R.` notation is used              |
|         | `exchangeable`     | equal variances for random effects, and one common pairwise covariance                                                        |
|         | `identity`         | equal variances for random effects, all covariances 0; the default if the `R.` notation is used                               |
|         | `unstructured`     | all variances and covariances to be distinctly estimated                                                                      |
|         | `fixed(matname)`   | user-selected variances and covariances constrained to specified values; the remaining variances and covariances unrestricted |
|         | `pattern(matname)` | user-selected variances and covariances constrained to be equal; the remaining variances and covariances unrestricted         |

| intmethod |               | Description                                                                                               |
|-----------|---------------|-----------------------------------------------------------------------------------------------------------|
|           | `mvaghermite` | mean-variance adaptive Gauss-Hermite quadrature; the default unless a crossed random-effects model is fit |
|           | `mcaghermite` | mode-curvature adaptive Gauss-Hermite quadrature                                                          |
|           | `ghermite`    | nonadaptive Gauss-Hermite quadrature                                                                      |
|           | `laplace`     | Laplacian approximation; the default for crossed random-effects models                                    |

`indepvars` may contain factor variables; see
[<strong>fvvarlist</strong>](http://www.stata.com/help.cgi?fvvarlist).

`depvar`, `indepvars`, and `varlist` may contain time-series operators;
see
[<strong>tsvarlist</strong>](http://www.stata.com/help.cgi?tsvarlist).

`bayes`, `by`, and `svy` are allowed; see
[<strong>prefix</strong>](http://www.stata.com/help.cgi?prefix).
For more details, see
[<strong>[BAYES]</strong> bayes: meprobit](http://www.stata.com/help.cgi?bayes_meprobit).

`vce()` and weights are not allowed with the
[<strong>svy</strong>](http://www.stata.com/help.cgi?svy)
prefix.

`fweight`s, `iweight`s, and `pweight`s are allowed; see
[<strong>weight</strong>](http://www.stata.com/help.cgi?weight).
Only one type of weight may be specified. Weights are not supported
under the Laplacian approximation or for crossed models.

`startvalues()`, `startgrid`, `noestimate`, `dnumerical`, and
`coeflegend` do not appear in the dialog box.

See
[<strong>[ME]</strong> meprobit postestimation](http://www.stata.com/help.cgi?meprobit_postestimation)
for features available after estimation.
