## Syntax

`teffects psmatch (ovar) (tvar tmvarlist` \[`,`
`tmodel`\]`)` _\[`if`\] \[`in`\]_
\[`weight`\] \[`, stat options`\]

`ovar` is a binary, count, continuous, fractional, or nonnegative
outcome of interest.

`tvar` must contain integer values representing the treatment levels.

`tmvarlist` specifies the variables that predict treatment assignment in
the treatment model. Only two treatment levels are allowed.

| tmodel                                                   |                      | Description                            |
|----------------------------------------------------------|----------------------|----------------------------------------|
| Model                                                    |                      |                                        |
|                                                          | `logit`              | logistic treatment model; the default  |
|                                                          | `probit`             | probit treatment model                 |
|                                                          | `hetprobit(varlist)` | heteroskedastic probit treatment model |
| `tmodel` specifies the model for the treatment variable. |                      |                                        |

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

SE/Robust

`vce(vcetype)`

`vcetype` may be

\[ \]; use robust Abadie-Imbens standard errors with matches ; use
independent and identically distributed Abadie-Imbens standard errors

Reporting

`level(#)`

set confidence level; default is `level(95)`

`display_options`

control columns and column formats, row spacing, line width, display of
omitted variables and base and empty cells, and factor-variable labeling

Advanced

`caliper(#)`

specify the maximum distance for which two observations are potential
neighbors

`pstolerance(#)`

set tolerance for in overlap assumption

`osample(newvar)`

`newvar` identifies observations that violate the overlap assumption

`control(# , label)`

specify the level of `tvar` that is the control

`tlevel(# , label)`

specify the level of `tvar` that is the treatment

`generate(stub)`

generate variables containing the observation numbers of the nearest
neighbors

`coeflegend`

display legend instead of statistics

`tmvarlist` may contain factor variables; see
[<strong>fvvarlists</strong>](http://www.stata.com/help.cgi?fvvarlists).

`by` and `statsby` are allowed; see
[<strong>prefix</strong>](http://www.stata.com/help.cgi?prefix).

`fweight`s are allowed; see
[<strong>weight</strong>](http://www.stata.com/help.cgi?weight).

`coeflegend` does not appear in the dialog box.

See
[<strong>[TE]</strong> teffects postestimation](http://www.stata.com/help.cgi?teffects_postestimation)
for features available after estimation.
