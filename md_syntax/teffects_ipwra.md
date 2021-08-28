## Syntax

`teffects ipwra (ovar omvarlist` \[`, omodel`
`noconstant`\]`) (tvar tmvarlist` \[`, tmodel noconstant`\]`)`
_\[`if`\] \[`in`\]_ \[`weight`\] \[`, stat`
`options`\]

`ovar` is a binary, count, continuous, fractional, or nonnegative
outcome of interest.

`omvarlist` specifies the covariates in the outcome model.

`tvar` must contain integer values representing the treatment levels.

`tmvarlist` specifies the covariates in the treatment-assignment model.

| omodel                                                 |                       | Description                                     |
|--------------------------------------------------------|-----------------------|-------------------------------------------------|
| Model                                                  |                       |                                                 |
|                                                        | `linear`              | linear outcome model; the default               |
|                                                        | `logit`               | logistic outcome model                          |
|                                                        | `probit`              | probit outcome model                            |
|                                                        | `hetprobit(varlist)`  | heteroskedastic probit outcome model            |
|                                                        | `poisson`             | exponential outcome model                       |
|                                                        | `flogit`              | fractional logistic outcome model               |
|                                                        | `fprobit`             | fractional probit outcome model                 |
|                                                        | `fhetprobit(varlist)` | fractional heteroskedastic probit outcome model |
| `omodel` specifies the model for the outcome variable. |                       |                                                 |

| tmodel                                                                               |                      | Description                            |
|--------------------------------------------------------------------------------------|----------------------|----------------------------------------|
| Model                                                                                |                      |                                        |
|                                                                                      | `logit`              | logistic treatment model; the default  |
|                                                                                      | `probit`             | probit treatment model                 |
|                                                                                      | `hetprobit(varlist)` | heteroskedastic probit treatment model |
| `tmodel` specifies the model for the treatment variable.                             |                      |                                        |
| For multivalued treatments, only `logit` is available and multinomial logit is used. |                      |                                        |

| stat |           | Description                                                  |
|------|-----------|--------------------------------------------------------------|
| Stat |           |                                                              |
|      | `ate`     | estimate average treatment effect in population; the default |
|      | `atet`    | estimate average treatment effect on the treated             |
|      | `pomeans` | estimate potential-outcome means                             |

| Options      |                      | Description                                                                                                                                      |
|--------------|----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| SE/Robust    |                      |                                                                                                                                                  |
|              | `vce(vcetype)`       | `vcetype` may be `robust`, `cluster clustvar`, `bootstrap`, or `jackknife`                                                                     |
| Reporting    |                      |                                                                                                                                                  |
|              | `level(#)`           | set confidence level; default is `level(95)`                                                                                                     |
|              | `aequations`         | display auxiliary-equation results                                                                                                               |
|              | `display_options`    | control columns and column formats, row spacing, line width, display of omitted variables and base and empty cells, and factor-variable labeling |
| Maximization |                      |                                                                                                                                                  |
|              | `maximize_options`   | control the maximization process; seldom used                                                                                                    |
| Advanced     |                      |                                                                                                                                                  |
|              | `pstolerance(#)`     | set tolerance for overlap assumption                                                                                                             |
|              | `osample(newvar)`    | `newvar` identifies observations that violate the overlap assumption                                                                             |
|              | `control(# , label)` | specify the level of `tvar` that is the control                                                                                                  |
|              | `tlevel(# , label)`  | specify the level of `tvar` that is the treatment                                                                                                |
|              | `coeflegend`         | display legend instead of statistics                                                                                                             |

`omvarlist` and `tmvarlist` may contain factor variables; see
[<strong>fvvarlists</strong>](http://www.stata.com/help.cgi?fvvarlists).

`bootstrap`, `by`, `jackknife`, and `statsby` are allowed; see
[<strong>prefix</strong>](http://www.stata.com/help.cgi?prefix).

Weights are not allowed with the
[<strong>bootstrap</strong>](http://www.stata.com/help.cgi?bootstrap)
prefix.

`fweight`s, `iweight`s, and `pweight`s are allowed; see
[<strong>weight</strong>](http://www.stata.com/help.cgi?weight).

`coeflegend` does not appear in the dialog box.

See
[<strong>[TE]</strong> teffects postestimation](http://www.stata.com/help.cgi?teffects_postestimation)
for features available after estimation.
