## Syntax

Basic syntax for a regression model with ARMA disturbances

`arima`
[depvar](http://www.stata.com/help.cgi?depvar)
\[[indepvars](http://www.stata.com/help.cgi?indepvars)\]`,`
`ar(numlist) ma(numlist)`

Basic syntax for an ARIMA(`p`,`d`,`q`) model

`arima`
[depvar](http://www.stata.com/help.cgi?depvar)`,`
`arima(#p,#d,#q)`

Basic syntax for a multiplicative seasonal
ARIMA(`p`,`d`,`q`)\*(`P`,`D`,`Q`)s model

`arima`
[depvar](http://www.stata.com/help.cgi?depvar)`,`
`arima(#p,#d,#q) sarima(#P,#D,#Q,#s)`

Full syntax

`arima`
[depvar](http://www.stata.com/help.cgi?depvar)
\[[indepvars](http://www.stata.com/help.cgi?indepvars)\]
_\[`if`\] \[`in`\]_ \[`weight`\] \[`,`
`options`\]

| Options                                                                                                                                                                  |                                | Description                                                      |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------|------------------------------------------------------------------|
| Model                                                                                                                                                                    |                                |                                                                  |
|                                                                                                                                                                          | `noconstant`                   | suppress constant term                                           |
|                                                                                                                                                                          | `arima(#p,#d,#q)`              | specify ARIMA(`p,d,q`) model for dependent variable              |
|                                                                                                                                                                          | `ar(numlist)`                  | autoregressive terms of the structural model disturbance         |
|                                                                                                                                                                          | `ma(numlist)`                  | moving-average terms of the structural model disturbance         |
|                                                                                                                                                                          | `constraints(constraints)` | apply specified linear constraints                               |
|                                                                                                                                                                          | `collinear`                    | keep collinear variables                                         |
| Model 2                                                                                                                                                                  |                                |                                                                  |
|                                                                                                                                                                          | `sarima(#P,#D,#Q,#s)`          | specify period-`#s` multiplicative seasonal ARIMA term           |
|                                                                                                                                                                          | `mar(numlist, #s)`     | multiplicative seasonal autoregressive terms; may be repeated    |
|                                                                                                                                                                          | `mma(numlist, #s)`     | multiplicative seasonal moving-average terms; may be repeated    |
| Model 3                                                                                                                                                                  |                                |                                                                  |
|                                                                                                                                                                          | `condition`                    | use conditional MLE instead of full MLE                          |
|                                                                                                                                                                          | `savespace`                    | conserve memory during estimation                                |
|                                                                                                                                                                          | `diffuse`                      | use diffuse prior for starting Kalman filter recursions          |
|                                                                                                                                                                          | `p0(#`\|`matname)`         | use alternate prior for starting Kalman recursions; seldom used  |
|                                                                                                                                                                          | `state0(#`\|`matname)`     | use alternate state vector for starting Kalman filter recursions |
| SE/Robust                                                                                                                                                                |                                |                                                                  |
|                                                                                                                                                                          | `vce(vcetype)`                 | `vcetype` may be `opg`, `robust`, or `oim`                       |
| Reporting                                                                                                                                                                |                                |                                                                  |
|                                                                                                                                                                          | `level(#)`                     | set confidence level; default is `level(95)`                     |
|                                                                                                                                                                          | `detail`                       | report list of gaps in time series                               |
|                                                                                                                                                                          | `nocnsreport`                  | do not display constraints                                       |
|                                                                                                                                                                          | `display_options`              | control columns and column formats, row spacing, and line width  |
| Maximization                                                                                                                                                             |                                |                                                                  |
|                                                                                                                                                                          | `maximize_options`             | control the maximization process; seldom used                    |
|                                                                                                                                                                          | `coeflegend`                   | display legend instead of statistics                             |
| You must `tsset` your data before using `arima`; see [<strong>[TS]</strong> tsset](http://www.stata.com/help.cgi?tsset).                      |                                |                                                                  |
| `depvar` and `indepvars` may contain time-series operators; see [<strong>tsvarlist</strong>](http://www.stata.com/help.cgi?tsvarlist).        |                                |                                                                  |
| `by`, `fp`, `rolling`, `statsby`, and `xi` are allowed; see [<strong>prefix</strong>](http://www.stata.com/help.cgi?prefix).                  |                                |                                                                  |
| `iweight`s are allowed; see [<strong>weights</strong>](http://www.stata.com/help.cgi?weights).                                                |                                |                                                                  |
| `coeflegend` does not appear in the dialog box.                                                                                                                          |                                |                                                                  |
| See [<strong>[TS]</strong> arima postestimation](http://www.stata.com/help.cgi?arima_postestimation) for features available after estimation. |                                |                                                                  |
