## Syntax

Fixed-effects maximum likelihood

`spxtregress`
[depvar](http://www.stata.com/help.cgi?depvar)
\[[indepvars](http://www.stata.com/help.cgi?indepvars)\]
_\[`if`\] \[`in`\]_`, fe`
\[[<var class="command">fe_options</var><strong></strong>](#fe_options)\]

Random-effects maximum likelihood

`spxtregress`
[depvar](http://www.stata.com/help.cgi?depvar)
\[[indepvars](http://www.stata.com/help.cgi?indepvars)\]
_\[`if`\] \[`in`\]_`, re`
\[[<var class="command">re_options</var><strong></strong>](#re_options)\]

| fe\_options  |                                                                                                               | Description                                                                                                                                      |
|--------------|---------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| Model        |                                                                                                               |                                                                                                                                                  |
| \*           | `fe`                                                                                                          | use fixed-effects estimator                                                                                                                      |
|              | `dvarlag(spmatname)`                                                                                          | spatially lagged dependent variable                                                                                                              |
|              | `errorlag(spmatname)`                                                                                         | spatially lagged errors                                                                                                                          |
|              | `ivarlag(spmatname :` [varlist](http://www.stata.com/help.cgi?varlist)`)`      | spatially lagged independent variables; repeatable                                                                                               |
|              | `force`                                                                                                       | allow estimation when estimation sample is a subset of the sample used to create the spatial weighting matrix                                    |
|              | `gridsearch(#)`                                                                                               | resolution of the initial-value search grid; seldom used                                                                                         |
| Reporting    |                                                                                                               |                                                                                                                                                  |
|              | `level(#)`                                                                                                    | set confidence level; default is `level(95)`                                                                                                     |
|              | [<var class="command">display_options</var><strong></strong>](#fe_display_options) | control columns and column formats, row spacing, line width, display of omitted variables and base and empty cells, and factor-variable labeling |
| Maximization |                                                                                                               |                                                                                                                                                  |
|              | [<var class="command">maximize_options</var><strong></strong>](#fe_maxopts)        | control the maximization process; seldom used                                                                                                    |
|              | `coeflegend`                                                                                                  | display legend instead of statistics                                                                                                             |

| re\_options  |                                                                                                               | Description                                                                                                                                      |
|--------------|---------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| Model        |                                                                                                               |                                                                                                                                                  |
| \*           | `re`                                                                                                          | use random-effects estimator                                                                                                                     |
|              | `dvarlag(spmatname)`                                                                                          | spatially lagged dependent variable                                                                                                              |
|              | `errorlag(spmatname)`                                                                                         | spatially lagged errors                                                                                                                          |
|              | `ivarlag(spmatname :` [varlist](http://www.stata.com/help.cgi?varlist)`)`      | spatially lagged independent variables; repeatable                                                                                               |
|              | `sarpanel`                                                                                                    | alternative formulation of the estimator in which the panel effects follow the same spatial process as the errors                                |
|              | `noconstant`                                                                                                  | suppress constant term                                                                                                                           |
|              | `force`                                                                                                       | allow estimation when estimation sample is a subset of the sample used to create the spatial weighting matrix                                    |
| Reporting    |                                                                                                               |                                                                                                                                                  |
|              | `level(#)`                                                                                                    | set confidence level; default is `level(95)`                                                                                                     |
|              | [<var class="command">display_options</var><strong></strong>](#re_display_options) | control columns and column formats, row spacing, line width, display of omitted variables and base and empty cells, and factor-variable labeling |
| Maximization |                                                                                                               |                                                                                                                                                  |
|              | [<var class="command">maximize_options</var><strong></strong>](#re_maxopts)        | control the maximization process; seldom used                                                                                                    |
|              | `coeflegend`                                                                                                  | display legend instead of statistics                                                                                                             |

\* You must specify either `fe` or `re`.

`indepvars` and `varlist` specified in `ivarlag()` may contain factor
variables; see
[<strong>fvvarlist</strong>](http://www.stata.com/help.cgi?fvvarlist).

`coeflegend` does not appear in the dialog box.

See
[<strong>[SP]</strong> spxtregress postestimation](http://www.stata.com/help.cgi?spxtregress_postestimation)
for features available after estimation.
