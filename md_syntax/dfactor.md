## Syntax

`dfactor obs_eq` \[`fac_eq`\] _\[`if`\]
\[`in`\]_ \[`,`
[<var class="command">options</var><strong></strong>](#table_options)\]

`obs_eq` specifies the equation for the observed dependent variables,
and it has the form

`(depvars =` \[`exog_d`\] \[`, sopts`\]`)`

`fac_eq` specifies the equation for the unobserved factors, and it has
the form

`(facvars =` \[`exog_f`\] \[`, sopts`\]`)`

`depvars` are the observed dependent variables. `exog_d` are the
exogenous variables that enter into the equations for the observed
dependent variables. (All factors are automatically entered into the
equations for the observed dependent variables.) `facvars` are the names
for the unobserved factors in the model. You may specify the names of
existing variables in `facvars`, but `dfactor` treats them only as names
and takes no notice that they are also variables. `exog_f` are the
exogenous variables that enter into the equations for the factors.

| Options      |                            | Description                                                                                                                          |
|--------------|----------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| Model        |                            |                                                                                                                                      |
|              | `constraints(constraints)` | apply specified linear constraints                                                                                                   |
| SE/Robust    |                            |                                                                                                                                      |
|              | `vce(vcetype)`             | `vcetype` may be `oim` or `robust`                                                                                                   |
| Reporting    |                            |                                                                                                                                      |
|              | `level(#)`                 | set confidence level; default is `level(95)`                                                                                         |
|              | `nocnsreport`              | do not display constraints                                                                                                           |
|              | `display_options`          | control columns and column formats, row spacing, display of omitted variables and base and empty cells, and factor-variable labeling |
| Maximization |                            |                                                                                                                                      |
|              | `maximize_options`         | control the maximization process; seldom used                                                                                        |
|              | `from(matname)`            | specify initial values for the maximization process; seldom used                                                                     |
| Advanced     |                            |                                                                                                                                      |
|              | `method(method)`       | specify the method for calculating the log likelihood; seldom used                                                                   |
|              | `coeflegend`               | display legend instead of statistics                                                                                                 |

| sopts |                                  | Description                                                        |
|-------|----------------------------------|--------------------------------------------------------------------|
| Model |                                  |                                                                    |
|       | `noconstant`                     | suppress constant term from the equation; allowed only in `obs_eq` |
|       | `ar(numlist)`                    | autoregressive terms                                               |
|       | `arstructure(arstructure)`   | structure of autoregressive coefficient matrices                   |
|       | `covstructure(covstructure)` | covariance structure                                               |

| arstructure |               | Description                  |
|-------------|---------------|------------------------------|
|             | `diagonal`    | diagonal matrix; the default |
|             | `ltriangular` | lower triangular matrix      |
|             | `general`     | general matrix               |

| covstructure |                | Description                         |
|--------------|----------------|-------------------------------------|
|              | `identity`     | identity matrix                     |
|              | `dscalar`      | diagonal scalar matrix              |
|              | `diagonal`     | diagonal matrix                     |
|              | `unstructured` | symmetric, positive-definite matrix |

| method |          | Description                                                                         |
|--------|----------|-------------------------------------------------------------------------------------|
|        | `hybrid` | use the stationary Kalman filter and the De Jong diffuse Kalman filter; the default |
|        | `dejong` | use the stationary De Jong method and the De Jong diffuse Kalman filter             |

You must `tsset` your data before using `dfactor`; see
[<strong>[TS]</strong> tsset](http://www.stata.com/help.cgi?tsset).

`exog_d` and `exog_f` may contain factor variables; see
[<strong>fvvarlist</strong>](http://www.stata.com/help.cgi?fvvarlist).

`depvars`, `exog_d`, and `exog_f` may contain time-series operators; see
[<strong>tsvarlist</strong>](http://www.stata.com/help.cgi?tsvarlist).

`by`, `fp`, `rolling`, and `statsby` are allowed; see
[<strong>prefix</strong>](http://www.stata.com/help.cgi?prefix).

`coeflegend` does not appear in the dialog box.

See
[<strong>[TS]</strong> dfactor postestimation](http://www.stata.com/help.cgi?dfactor_postestimation)
for features available after estimation.
