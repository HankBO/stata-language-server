## Syntax

`spivregress`
[depvar](http://www.stata.com/help.cgi?depvar)
\[[varlist](http://www.stata.com/help.cgi?varlist)\_1\]
`(varlist`\_2 `= varlist`\_iv`)` _\[`if`\]
\[`in`\]_ \[`, options`\]

`varlist`\_1 is the list of included exogenous regressors.

`varlist`\_2 is the list of endogenous regressors.

`varlist`\_iv is the list of excluded exogenous regressors used with
`varlist`\_1 as instruments for `varlist`\_2.

| Options      |                                                                                                            | Description                                                                                                                                      |
|--------------|------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| Model        |                                                                                                            |                                                                                                                                                  |
|              | `dvarlag(spmatname)`                                                                                       | spatially lagged dependent variable; repeatable                                                                                                  |
|              | `errorlag(spmatname)`                                                                                      | spatially lagged errors; repeatable                                                                                                              |
|              | `ivarlag(spmatname :` [varlist](http://www.stata.com/help.cgi?varlist)`)`   | spatially lagged exogenous variables from `varlist`\_1; repeatable                                                                               |
|              | `noconstant`                                                                                               | suppress constant term                                                                                                                           |
|              | `heteroskedastic`                                                                                          | treat errors as heteroskedastic                                                                                                                  |
|              | `force`                                                                                                    | allow estimation when estimation sample is a subset of the sample used to create the spatial weighting matrix                                    |
|              | `impower(#)`                                                                                               | order of instrumental-variable approximation                                                                                                     |
| Reporting    |                                                                                                            |                                                                                                                                                  |
|              | `level(#)`                                                                                                 | set confidence level; default is `level(95)`                                                                                                     |
|              | [<var class="command">display_options</var><strong></strong>](#display_options) | control columns and column formats, row spacing, line width, display of omitted variables and base and empty cells, and factor-variable labeling |
| Optimization |                                                                                                            |                                                                                                                                                  |
|              | [<var class="command">optimization_options</var><strong></strong>](#optimopts)  | control the optimization process; seldom used                                                                                                    |
|              | `coeflegend`                                                                                               | display legend instead of statistics                                                                                                             |

`varlist`\_1, `varlist`\_2, `varlist`\_iv, and `varlist` specified in
`ivarlag()` may contain factor variables; see
[<strong>fvvarlist</strong>](http://www.stata.com/help.cgi?fvvarlist).

`coeflegend` does not appear in the dialog box.

See
[<strong>[SP]</strong> spivregress postestimation](http://www.stata.com/help.cgi?spivregress_postestimation)
for features available after estimation.
