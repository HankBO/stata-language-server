## Syntax

Generalized spatial two-stage least squares

`spregress`
[depvar](http://www.stata.com/help.cgi?depvar)
\[[indepvars](http://www.stata.com/help.cgi?indepvars)\]
_\[`if`\] \[`in`\]_`, gs2sls`
\[[<var class="command">gs2sls_options</var><strong></strong>](#gs2sls_options)\]

Maximum likelihood

`spregress`
[depvar](http://www.stata.com/help.cgi?depvar)
\[[indepvars](http://www.stata.com/help.cgi?indepvars)\]
_\[`if`\] \[`in`\]_`, ml`
\[[<var class="command">ml_options</var><strong></strong>](#ml_options)\]

| gs2sls\_options |                                                                                                                   | Description                                                                                                                                      |
|-----------------|-------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| Model           |                                                                                                                   |                                                                                                                                                  |
| \*              | `gs2sls`                                                                                                          | use generalized spatial two-stage least-squares estimator                                                                                        |
|                 | `dvarlag(spmatname)`                                                                                              | spatially lagged dependent variable; repeatable                                                                                                  |
|                 | `errorlag(spmatname)`                                                                                             | spatially lagged errors; repeatable                                                                                                              |
|                 | `ivarlag(spmatname :` [varlist](http://www.stata.com/help.cgi?varlist)`)`          | spatially lagged independent variables; repeatable                                                                                               |
|                 | `noconstant`                                                                                                      | suppress constant term                                                                                                                           |
|                 | `heteroskedastic`                                                                                                 | treat errors as heteroskedastic                                                                                                                  |
|                 | `force`                                                                                                           | allow estimation when estimation sample is a subset of the sample used to create the spatial weighting matrix                                    |
|                 | `impower(#)`                                                                                                      | order of instrumental-variable approximation                                                                                                     |
| Reporting       |                                                                                                                   |                                                                                                                                                  |
|                 | `level(#)`                                                                                                        | set confidence level; default is `level(95)`                                                                                                     |
|                 | [<var class="command">display_options</var><strong></strong>](#gs2sls_display_options) | control columns and column formats, row spacing, line width, display of omitted variables and base and empty cells, and factor-variable labeling |
| Optimization    |                                                                                                                   |                                                                                                                                                  |
|                 | [<var class="command">optimization_options</var><strong></strong>](#optimopts)         | control the optimization process; seldom used                                                                                                    |
|                 | `coeflegend`                                                                                                      | display legend instead of statistics                                                                                                             |

| ml\_options  |                                                                                                               | Description                                                                                                                                      |
|--------------|---------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| Model        |                                                                                                               |                                                                                                                                                  |
| \*           | `ml`                                                                                                          | use maximum likelihood estimator                                                                                                                 |
|              | `dvarlag(spmatname)`                                                                                          | spatially lagged dependent variable; not repeatable                                                                                              |
|              | `errorlag(spmatname)`                                                                                         | spatially lagged errors; not repeatable                                                                                                          |
|              | `ivarlag(spmatname :` [varlist](http://www.stata.com/help.cgi?varlist)`)`      | spatially lagged independent variables; repeatable                                                                                               |
|              | `noconstant`                                                                                                  | suppress constant term                                                                                                                           |
|              | `constraints(estimation_options##constraints()`                                                               | apply specified linear constraints                                                                                                               |
|              | `force`                                                                                                       | allow estimation when estimation sample is a subset of the sample used to create the spatial weighting matrix                                    |
|              | `gridsearch(#)`                                                                                               | resolution of the initial-value search grid; seldom used                                                                                         |
| SE/Robust    |                                                                                                               |                                                                                                                                                  |
|              | `vce(vcetype)`                                                                                                | `vcetype` may be `oim` or `robust`                                                                                                               |
| Reporting    |                                                                                                               |                                                                                                                                                  |
|              | `level(#)`                                                                                                    | set confidence level; default is `level(95)`                                                                                                     |
|              | `nocnsreport`                                                                                                 | do not display constraints                                                                                                                       |
|              | [<var class="command">display_options</var><strong></strong>](#ml_display_options) | control columns and column formats, row spacing, line width, display of omitted variables and base and empty cells, and factor-variable labeling |
| Maximization |                                                                                                               |                                                                                                                                                  |
|              | [<var class="command">maximize_options</var><strong></strong>](#maxopts)           | control the maximization process; seldom used {synopt None}`coeflegend`display legend instead of statistics                                      |

\* You must specify either `gs2sls` or `ml`.

`indepvars` and `varlist` specified in `ivarlag()` may contain factor
variables; see
[<strong>fvvarlist</strong>](http://www.stata.com/help.cgi?fvvarlist).

`coeflegend` does not appear in the dialog box.

See
[<strong>[SP]</strong> spregress postestimation](http://www.stata.com/help.cgi?spregress_postestimation)
for features available after estimation.
