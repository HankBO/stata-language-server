## Syntax

Maximum likelihood estimator

`ivprobit`
[depvar](http://www.stata.com/help.cgi?depvar)
\[`varlist1`\] `(varlist2 = varlist_iv)` <span
class="command">\[`if`\] \[`in`\]_ \[`weight`\] \[`,`
`mle_options`\]

Two-step estimator

`ivprobit`
[depvar](http://www.stata.com/help.cgi?depvar)
\[`varlist1`\] `(varlist2 = varlist_iv)` <span
class="command">\[`if`\] \[`in`\]_ \[`weight`\] `, twostep`
\[`tse_options`\]

`varlist1` is the list of exogenous variables.

`varlist2` is the list of endogenous variables.

`varlist_iv` is the list of exogenous variables used with `varlist1` as
instruments for `varlist2`.

| mle\_options |                                | Description                                                                                                                                      |
|--------------|--------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| Model        |                                |                                                                                                                                                  |
|              | `mle`                          | use conditional maximum-likelihood estimator; the default                                                                                        |
|              | `asis`                         | retain perfect predictor variables                                                                                                               |
|              | `constraints(constraints)` | apply specified linear constraints                                                                                                               |
| SE/Robust    |                                |                                                                                                                                                  |
|              | `vce(vcetype)`                 | `vcetype` may be `oim`, `robust`, `cluster clustvar`, `opg`, `bootstrap`, or `jackknife`                                                       |
| Reporting    |                                |                                                                                                                                                  |
|              | `level(#)`                     | set confidence level; default is `level(95)`                                                                                                     |
|              | `first`                        | report first-stage regression                                                                                                                    |
|              | `nocnsreport`                  | do not display constraints                                                                                                                       |
|              | `display_options`              | control columns and column formats, row spacing, line width, display of omitted variables and base and empty cells, and factor-variable labeling |
| Maximization |                                |                                                                                                                                                  |
|              | `maximize_options`             | control the maximization process                                                                                                                 |
|              | `coeflegend`                   | display legend instead of statistics                                                                                                             |

| tse\_options              |                   | Description                                                                                                                                      |
|---------------------------|-------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| Model                     |                   |                                                                                                                                                  |
| \*                        | `twostep`         | use Newey's two-step estimator; the default is `mle`                                                                                             |
|                           | `asis`            | retain perfect predictor variables                                                                                                               |
| SE/Robust                 |                   |                                                                                                                                                  |
|                           | `vce(vcetype)`    | `vcetype` may be `twostep`, `bootstrap`, or `jackknife`                                                                                          |
| Reporting                 |                   |                                                                                                                                                  |
|                           | `level(#)`        | set confidence level; default is `level(95)`                                                                                                     |
|                           | `first`           | report first-stage regression                                                                                                                    |
|                           | `display_options` | control columns and column formats, row spacing, line width, display of omitted variables and base and empty cells, and factor-variable labeling |
|                           | `coeflegend`      | display legend instead of statistics                                                                                                             |
| \* `twostep` is required. |                   |                                                                                                                                                  |

`varlist1` and `varlist_iv` may contain factor variables; see
[<strong>fvvarlist</strong>](http://www.stata.com/help.cgi?fvvarlist).

`depvar`, `varlist1`, `varlist2`, and `varlist_iv` may contain
time-series operators; see
[<strong>tsvarlist</strong>](http://www.stata.com/help.cgi?tsvarlist).

`bootstrap`, `by`, `jackknife`, `rolling`, `statsby`, and `svy` are
allowed; see
[<strong>prefix</strong>](http://www.stata.com/help.cgi?prefix).
`fp` is allowed with the maximum likelihood estimator.

Weights are not allowed with the
[<strong>bootstrap</strong>](http://www.stata.com/help.cgi?bootstrap)
prefix.

`vce()`, `first`, `twostep`, and weights are not allowed with the
[<strong>svy</strong>](http://www.stata.com/help.cgi?svy)
prefix.

`fweight`s, `iweight`s, and `pweight`s are allowed with the maximum
likelihood estimator. `fweight`s are allowed with Newey's two-step
estimator. See
[<strong>weight</strong>](http://www.stata.com/help.cgi?weight).

`coeflegend` does not appear in the dialog box.

See
[<strong>[R]</strong> ivprobit postestimation](http://www.stata.com/help.cgi?ivprobit_postestimation)
for features available after estimation.
