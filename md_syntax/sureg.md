## Syntax

Basic syntax

`sureg`
`(`[depvar1](http://www.stata.com/help.cgi?depvar)
[varlist1](http://www.stata.com/help.cgi?varlist)`)`
`(`[depvar2](http://www.stata.com/help.cgi?depvar)
[varlist2](http://www.stata.com/help.cgi?varlist)`)`
`...`
`(`[depvarN](http://www.stata.com/help.cgi?depvar)
[varlistN](http://www.stata.com/help.cgi?varlist)`)`
_\[`if`\] \[`in`\]_ \[`weight`\]

Full syntax

`sureg (`\[`eqname1:`\]
[depvar1a](http://www.stata.com/help.cgi?depvar)
\[[depvar1b](http://www.stata.com/help.cgi?depvar)
... `=`\]
[varlist1](http://www.stata.com/help.cgi?varlist)
\[`, noconstant`\]`)`

`(`\[`eqname2:`\]
[depvar2a](http://www.stata.com/help.cgi?depvar)
\[[depvar2b](http://www.stata.com/help.cgi?depvar)
... `=`\]
[varlist2](http://www.stata.com/help.cgi?varlist)
\[`, noconstant`\]`)`

`...`

`(`\[`eqnameN:`\]
[depvarNa](http://www.stata.com/help.cgi?depvar)
\[[depvarNb](http://www.stata.com/help.cgi?depvar)
... `=`\]
[varlistN](http://www.stata.com/help.cgi?varlist)
\[`, noconstant`\]`)` _\[`if`\] \[`in`\]_
\[`weight`\] \[`, options`\]

Explicit equation naming (`eqname:`) cannot be combined with multiple
dependent variables in an equation specification.

| Options                                                                                                                                                                                                                                                        |                                | Description                                                                                                                                      |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| Model                                                                                                                                                                                                                                                          |                                |                                                                                                                                                  |
|                                                                                                                                                                                                                                                                | `isure`                        | iterate until estimates converge                                                                                                                 |
|                                                                                                                                                                                                                                                                | `constraints(constraints)` | apply specified linear constraints                                                                                                               |
| df adj.                                                                                                                                                                                                                                                        |                                |                                                                                                                                                  |
|                                                                                                                                                                                                                                                                | `small`                        | report small-sample statistics                                                                                                                   |
|                                                                                                                                                                                                                                                                | `dfk`                          | use small-sample adjustment                                                                                                                      |
|                                                                                                                                                                                                                                                                | `dfk2`                         | use alternate adjustment                                                                                                                         |
| Reporting                                                                                                                                                                                                                                                      |                                |                                                                                                                                                  |
|                                                                                                                                                                                                                                                                | `level(#)`                     | set confidence level; default is `level(95)`                                                                                                     |
|                                                                                                                                                                                                                                                                | `corr`                         | perform Breusch-Pagan test                                                                                                                       |
|                                                                                                                                                                                                                                                                | `nocnsreport`                  | do not display constraints                                                                                                                       |
|                                                                                                                                                                                                                                                                | `display_options`              | control columns and column formats, row spacing, line width, display of omitted variables and base and empty cells, and factor-variable labeling |
| Optimization                                                                                                                                                                                                                                                   |                                |                                                                                                                                                  |
|                                                                                                                                                                                                                                                                | `optimization_options`         | control the optimization process; seldom used                                                                                                    |
|                                                                                                                                                                                                                                                                | `noheader`                     | suppress header table from above coefficient table                                                                                               |
|                                                                                                                                                                                                                                                                | `notable`                      | suppress coefficient table                                                                                                                       |
|                                                                                                                                                                                                                                                                | `coeflegend`                   | display legend instead of statistics                                                                                                             |
| `varlist1`, ..., `varlistN` may contain factor variables; see [<strong>fvvarlist</strong>](http://www.stata.com/help.cgi?fvvarlist). You must have the same levels of factor variables in all equations that have factor variables. |                                |                                                                                                                                                  |
| `depvar` and the `varlists` may contain time-series operators; see [<strong>tsvarlist</strong>](http://www.stata.com/help.cgi?tsvarlist).                                                                                           |                                |                                                                                                                                                  |
| `bootstrap`, `by`, `fp`, `jackknife`, `rolling`, and `statsby` are allowed; see [<strong>prefix</strong>](http://www.stata.com/help.cgi?prefix).                                                                                    |                                |                                                                                                                                                  |
| Weights are not allowed with the [<strong>bootstrap</strong>](http://www.stata.com/help.cgi?bootstrap) prefix.                                                                                                                      |                                |                                                                                                                                                  |
| `aweight`s are not allowed with the [<strong>jackknife</strong>](http://www.stata.com/help.cgi?jackknife) prefix.                                                                                                                   |                                |                                                                                                                                                  |
| `aweight`s and `fweight`s are allowed, see [<strong>weight</strong>](http://www.stata.com/help.cgi?weight).                                                                                                                         |                                |                                                                                                                                                  |
| `noheader`, `notable`, and `coeflegend` do not appear in the dialog box.                                                                                                                                                                                       |                                |                                                                                                                                                  |
| See [<strong>[R]</strong> sureg postestimation](http://www.stata.com/help.cgi?sureg_postestimation) for features available after estimation.                                                                                        |                                |                                                                                                                                                  |
