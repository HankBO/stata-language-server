## Syntax

Derivatives of numeric functions

`dydx yvar xvar` _\[`if`\] \[`in`\]_ `,`
`generate(newvar)` \[`dydx_options`\]

Integrals of numeric functions

`integ yvar xvar` _\[`if`\] \[`in`\]_
\[`, integ_options`\]

| dydx\_options                                                                                                                                                                                                                                                                                                         |                    | Description                                                         |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------|---------------------------------------------------------------------|
| Main                                                                                                                                                                                                                                                                                                                  |                    |                                                                     |
| \*                                                                                                                                                                                                                                                                                                                    | `generate(newvar)` | create variable named `newvar`                                      |
|                                                                                                                                                                                                                                                                                                                       | `replace`          | overwrite the existing variable                                     |
|                                                                                                                                                                                                                                                                                                                       | `trapezoid`        | use trapezoidal rule to compute integrals; default is cubic splines |
|                                                                                                                                                                                                                                                                                                                       | `initial(#)`       | initial value of integral; default is `initial(0)`                  |
|                                                                                                                                                                                                                                                                                                                       | `replace`          | overwrite the existing variable                                     |
| \* `generate(newvar)` is required. <span options="20 tabbed">{synoptset 20 tabbed}_{nobreak None} <span options="integ_options">{marker integ\_options}_{nobreak None} {synopthdr None:integ\_options} {synoptline None} {syntab None:Main} {synopt None}`generate(newvar)`create variable named `newvar` |                    |                                                                     |

`by` is allowed with `dydx` and `integ`; see
[<strong>[D]</strong> by](http://www.stata.com/help.cgi?by).
