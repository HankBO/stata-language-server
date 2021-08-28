## Syntax

`mixed`
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
\[`, re_options`\]

`levelvar` is a variable identifying the group structure for the random
effects at that level or is `_all` representing one group comprising all
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

| options      |                              | Description                                                                                                                                      |
|--------------|------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| Model        |                              |                                                                                                                                                  |
|              | `mle`                        | fit model via maximum likelihood (ML); the default                                                                                               |
|              | `reml`                       | fit model via restricted maximum likelihood (REML)                                                                                               |
|              | `dfmethod(df_method)`    | specify method for computing degrees of freedom (DF) of a t distribution                                                                         |
|              | ` pwscale(scale_method)` | control scaling of sampling weights in two-level models                                                                                          |
|              | `residuals(rspec)`       | structure of residual errors                                                                                                                     |
| SE/Robust    |                              |                                                                                                                                                  |
|              | `vce(vcetype)`               | `vcetype` may be `oim`, `robust`, or `cluster clustvar`; types other than `oim` may not be combined with `dfmethod()`                          |
| Reporting    |                              |                                                                                                                                                  |
|              | `level(#)`                   | set confidence level; default is `level(95)`                                                                                                     |
|              | `variance`                   | show random-effects and residual-error parameter estimates as variances and covariances; the default                                             |
|              | `stddeviations`              | show random-effects and residual-error parameter estimates as standard deviations and correlations                                               |
|              | `dftable(dftable)`       | specify contents of fixed-effects table; requires `dfmethod()` at estimation                                                                     |
|              | `noretable`                  | suppress random-effects table                                                                                                                    |
|              | `nofetable`                  | suppress fixed-effects table                                                                                                                     |
|              | `estmetric`                  | show parameter estimates as stored in `e(b)`                                                                                                     |
|              | `noheader`                   | suppress output header                                                                                                                           |
|              | `nogroup`                    | suppress table summarizing groups                                                                                                                |
|              | `nostderr`                   | do not estimate standard errors of random-effects parameters                                                                                     |
|              | `display_options`            | control columns and column formats, row spacing, line width, display of omitted variables and base and empty cells, and factor-variable labeling |
| EM options   |                              |                                                                                                                                                  |
|              | `emiterate(#)`               | number of EM iterations; default is `emiterate(20)`                                                                                              |
|              | `emtolerance(#)`             | EM convergence tolerance; default is `emtolerance(1e-10)`                                                                                        |
|              | `emonly`                     | fit model exclusively using EM                                                                                                                   |
|              | `emlog`                      | show EM iteration log                                                                                                                            |
|              | `emdots`                     | show EM iterations as dots                                                                                                                       |
| Maximization |                              |                                                                                                                                                  |
|              | `maximize_options`           | control the maximization process; seldom used                                                                                                    |
|              | `matsqrt`                    | parameterize variance components using matrix square roots; the default                                                                          |
|              | `matlog`                     | parameterize variance components using matrix logarithms                                                                                         |
|              | `small`                      | replay small-sample inference results                                                                                                            |
|              | `coeflegend`                 | display legend instead of statistics                                                                                                             |

| vartype |                | Description                                                                                                        |
|---------|----------------|--------------------------------------------------------------------------------------------------------------------|
|         | `independent`  | one unique variance parameter per random effect, all covariances 0; the default unless the **R.** notation is used |
|         | `exchangeable` | equal variances for random effects, and one common pairwise covariance                                             |
|         | `identity`     | equal variances for random effects, all covariances 0; the default if the **R.** notation is used                  |
|         | `unstructured` | all variances and covariances to be distinctly estimated                                                           |

| df\_method |                                 | Description                                                   |
|------------|---------------------------------|---------------------------------------------------------------|
|            | `residual`                      | residual degrees of freedom, n - rank(X)                      |
|            | `repeated`                      | repeated-measures ANOVA                                       |
|            | `anova`                         | ANOVA                                                         |
|            | `satterthwaite`\[`, dfopts`\] | generalized Satterthwaite approximation; REML estimation only |
|            | `kroger`\[`, dfopts`\]        | Kenward-Roger; REML estimation only                           |

| dftable |           | Description                                                      |
|---------|-----------|------------------------------------------------------------------|
|         | `default` | test statistics, p-values, and confidence intervals; the default |
|         | `ci`      | DFs and confidence intervals                                     |
|         | `pvalue`  | DFs, test statistics, and p-values                               |

`indepvars` may contain factor variables; see
[<strong>fvvarlist</strong>](http://www.stata.com/help.cgi?fvvarlist).

`depvar`, `indepvars`, and `varlist` may contain time-series operators;
see
[<strong>tsvarlist</strong>](http://www.stata.com/help.cgi?tsvarlist).

`bayes`, `bootstrap`, `by`, `jackknife`, `mi estimate`, `rolling`, and
`statsby` are allowed; see
[<strong>prefix</strong>](http://www.stata.com/help.cgi?prefix).
For more details, see
[<strong>[BAYES]</strong> bayes: mixed](http://www.stata.com/help.cgi?bayes_mixed).

`mi estimate` is not allowed if `dfmethod()` is specified.

Weights are not allowed with the
[<strong>bootstrap</strong>](http://www.stata.com/help.cgi?bootstrap)
prefix.

`pweight`s and `fweight`s are allowed; see
[<strong>weight</strong>](http://www.stata.com/help.cgi?weight).
However, no weights are allowed if either option `reml` or option
`dfmethod()` is specified.

`small` and `coeflegend` do not appear in the dialog box.

See
[<strong>[ME]</strong> mixed postestimation](http://www.stata.com/help.cgi?mixed_postestimation)
for features available after estimation.
