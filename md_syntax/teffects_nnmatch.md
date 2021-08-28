## Syntax

`teffects nnmatch (ovar omvarlist) (tvar)` <span
class="command">\[`if`\] \[`in`\]_ \[`weight`\] \[`, stat`
`options`\]

`ovar` is a binary, count, continuous, fractional, or nonnegative
outcome of interest.

`omvarlist` specifies the covariates in the outcome model.

`tvar` must contain integer values representing the treatment levels.
Only two treatment levels are allowed.

| stat |        | Description                                                  |
|------|--------|--------------------------------------------------------------|
| Stat |        |                                                              |
|      | `ate`  | estimate average treatment effect in population; the default |
|      | `atet` | estimate average treatment effect on the treated             |

Options

Description

Model

`nneighbor(#)`

specify number of matches per observation; default is `nneighbor(1)`

`biasadj(varlist)`

correct for large-sample bias using specified variables

`ematch(varlist)`

match exactly on specified variables

SE/Robust

`vce(vcetype)`

`vcetype` may be

\[ \]; use robust Abadie-Imbens standard errors with matches ; use
default Abadie-Imbens standard errors

Reporting

`level(#)`

set confidence level; default is `level(95)`

`dmvariables`

display names of matching variables

`display_options`

control columns and column formats, row spacing, line width, display of
omitted variables and base and empty cells, and factor-variable labeling

Advanced

`caliper(#)`

specify the maximum distance for which two observations are potential
neighbors

`dtolerance(#)`

set maximum distance between individuals considered equal

`osample(newvar)`

`newvar` identifies observations that violate the overlap assumption

`control(# , label)`

specify the level of `tvar` that is the control

`tlevel(# , label)`

specify the level of `tvar` that is the treatment

`generate(stub)`

generate variables containing the observation numbers of the nearest
neighbors

`metric(metric)`

select distance metric for covariates

`coeflegend`

display legend instead of statistics

| metric |                    | Description                                      |
|--------|--------------------|--------------------------------------------------|
|        | `mahalanobis`      | inverse sample covariate covariance; the default |
|        | `ivariance`        | inverse diagonal sample covariate covariance     |
|        | `euclidean`        | identity                                         |
|        | `matrix matname` | user-supplied scaling matrix                     |

`omvarlist` may contain factor variables; see
[<strong>fvvarlists</strong>](http://www.stata.com/help.cgi?fvvarlists).

`by` and `statsby` are allowed; see
[<strong>prefix</strong>](http://www.stata.com/help.cgi?prefix).

`fweight`s are allowed; see
[<strong>weight</strong>](http://www.stata.com/help.cgi?weight).

`coeflegend` does not appear in the dialog box.

See
[<strong>[TE]</strong> teffects postestimation](http://www.stata.com/help.cgi?teffects_postestimation)
for features available after estimation.
