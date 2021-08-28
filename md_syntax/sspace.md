## Syntax

Covariance-form syntax

`sspace state_ceq` \[`state_ceq` ... `state_ceq`\] `obs_ceq`
\[`obs_ceq` ... `obs_ceq`\] _\[`if`\]
\[`in`\]_ \[`, options`\]

where each `state_ceq` is of the form

(`statevar` \[`lagged_statevars`\]
\[[indepvars](http://www.stata.com/help.cgi?indepvars)\]`, state`
\[`noerror noconstant`\])

and each `obs_ceq` is of the form

`(`[depvar](http://www.stata.com/help.cgi?depvar)
\[`statevars`\]
\[[indepvars](http://www.stata.com/help.cgi?indepvars)\]
\[`, noerror noconstant`\]`)`

Error-form syntax

`sspace state_efeq` \[`state_efeq` ... `state_efeq`\] `obs_efeq`
\[`obs_efeq` ... `obs_efeq`\] _\[`if`\]
\[`in`\]_ \[`, options`\]

where each `state_efeq` is of the form

`(statevar` \[`lagged_statevars`\]
\[[indepvars](http://www.stata.com/help.cgi?indepvars)\]
\[`state_errors`\]`, state` \[`noconstant`\]`)`

and each `obs_efeq` is of the form

{cmd
None}([depvar](http://www.stata.com/help.cgi?depvar)
\[`statevars`\]
\[[indepvars](http://www.stata.com/help.cgi?indepvars)\]
\[`obs_errors`\] \[`, noconstant`\]`)`

`statevar` is the name of an unobserved state, not a variable. If there
happens to be a variable of the same name, the variable is ignored and
plays no role in the estimation.

`lagged_statevars` is a list of lagged `statevar`s. Only first lags are
allowed.

`state_errors` is a list of state-equation errors that enter a state
equation. Each state error has the form `e.statevar`, where `statevar`
is the name of a state in the model.

`obs_errors` is a list of observation-equation errors that enter an
equation for an observed variable. Each error has the form
`e.`[depvar](http://www.stata.com/help.cgi?depvar),
where `depvar` is an observed dependent variable in the model.

| equation-level options |              | Description                                           |
|------------------------|--------------|-------------------------------------------------------|
| Model                  |              |                                                       |
|                        | `state`      | specifies that the equation is a state equation       |
|                        | `noerror`    | specifies that there is no error term in the equation |
|                        | `noconstant` | suppresses the constant term from the equation        |

| Options      |                                | Description                                                                                                                          |
|--------------|--------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| Model        |                                |                                                                                                                                      |
|              | `covstate(covform)`            | specifies the covariance structure for the errors in the state variables                                                             |
|              | `covobserved(covform)`         | specifies the covariance structure for the errors in the observed dependent variables                                                |
|              | `constraints(constraints)` | apply specified linear constraints                                                                                                   |
| SE/Robust    |                                |                                                                                                                                      |
|              | `vce(vcetype)`                 | `vcetype` may be `oim` or `robust`                                                                                                   |
| Reporting    |                                |                                                                                                                                      |
|              | `level(#)`                     | set confidence level; default is `level(95)`                                                                                         |
|              | `nocnsreport`                  | do not display constraints                                                                                                           |
|              | `display_options`              | control columns and column formats, row spacing, display of omitted variables and base and empty cells, and factor-variable labeling |
| Maximization |                                |                                                                                                                                      |
|              | `maximize_options`             | control the maximization process; seldom used                                                                                        |
| Advanced     |                                |                                                                                                                                      |
|              | `method(method)`               | specify the method for calculating the log likelihood; seldom used                                                                   |
|              | `coeflegend`                   | display legend instead of statistics                                                                                                 |

| covform |                | Description                                                             |
|---------|----------------|-------------------------------------------------------------------------|
|         | `identity`     | identity matrix; the default for error-form syntax                      |
|         | `dscalar`      | diagonal scalar matrix                                                  |
|         | `diagonal`     | diagonal matrix; the default for covariance-form syntax                 |
|         | `unstructured` | symmetric, positive-definite matrix; not allowed with error-form syntax |

| method |            | Description                                                                                           |
|--------|------------|-------------------------------------------------------------------------------------------------------|
|        | `hybrid`   | use the stationary Kalman filter and the De Jong diffuse Kalman filter; the default                   |
|        | `dejong`   | use the stationary De Jong Kalman filter and the De Jong diffuse Kalman filter                        |
|        | `kdiffuse` | use the stationary Kalman filter and the nonstationary large-kappa diffuse Kalman filter; seldom used |

You must `tsset` your data before using `sspace`; see
[<strong>[TS]</strong> tsset](http://www.stata.com/help.cgi?tsset).

`indepvars` may contain factor variables; see
[<strong>fvvarlist</strong>](http://www.stata.com/help.cgi?fvvarlist).

`indepvars` and `depvar` may contain time-series operators; see
[<strong>tsvarlist</strong>](http://www.stata.com/help.cgi?tsvarlist).

`by`, `rolling`, and `statsby` are allowed; see
[<strong>prefix</strong>](http://www.stata.com/help.cgi?prefix).

`coeflegend` does not appear in the dialog box.

See
[<strong>[TS]</strong> sspace postestimation](http://www.stata.com/help.cgi?sspace_postestimation)
for features available after estimation.
