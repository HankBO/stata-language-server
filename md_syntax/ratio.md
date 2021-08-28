## Syntax

Basic syntax

`ratio` \[`name:`\]
[varname](http://www.stata.com/help.cgi?varname)
\[`/`\]
[varname](http://www.stata.com/help.cgi?varname)

Full syntax

`ratio (`\[`name:`\]
[varname](http://www.stata.com/help.cgi?varname)
\[`/`\]
[varname](http://www.stata.com/help.cgi?varname)`)`  
\[`(`\[`name:`\]
[varname](http://www.stata.com/help.cgi?varname)
\[`/`\]
[varname](http://www.stata.com/help.cgi?varname)`)`
...\] _\[`if`\] \[`in`\]_ \[`weight`\] \[`,`
`options`\]

| Options                                                                                                                                                                               |                                      | Description                                                                       |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------|-----------------------------------------------------------------------------------|
| Model                                                                                                                                                                                 |                                      |                                                                                   |
|                                                                                                                                                                                       | `stdize(varname)`                    | variable identifying strata for standardization                                   |
|                                                                                                                                                                                       | `stdweight(varname)`                 | weight variable for standardization                                               |
|                                                                                                                                                                                       | `nostdrescale`                       | do not rescale the standard weight variable                                       |
| if/in/over                                                                                                                                                                            |                                      |                                                                                   |
|                                                                                                                                                                                       | `over(varlist`\[`, nolabel`\]`)` | group over subpopulations defined by `varlist`; optionally, suppress group labels |
| SE/Cluster                                                                                                                                                                            |                                      |                                                                                   |
|                                                                                                                                                                                       | `vce(vcetype)`                       | `vcetype` may be `linearized`, `cluster clustvar`, `bootstrap`, or `jackknife`  |
| Reporting                                                                                                                                                                             |                                      |                                                                                   |
|                                                                                                                                                                                       | `level(#)`                           | set confidence level; default is `level(95)`                                      |
|                                                                                                                                                                                       | `noheader`                           | suppress table header                                                             |
|                                                                                                                                                                                       | `nolegend`                           | suppress table legend                                                             |
|                                                                                                                                                                                       | `display_options`                    | control column formats and line width                                             |
|                                                                                                                                                                                       | `coeflegend`                         | display legend instead of statistics                                              |
| `bootstrap`, `jackknife`, `mi estimate`, `rolling`, `statsby`, and `svy` are allowed; see [<strong>prefix</strong>](http://www.stata.com/help.cgi?prefix). |                                      |                                                                                   |
| `vce(bootstrap)` and `vce(jackknife)` are not allowed with the [<strong>mi estimate</strong>](http://www.stata.com/help.cgi?mi%20estimate) prefix.         |                                      |                                                                                   |
| Weights are not allowed with the [<strong>bootstrap</strong>](http://www.stata.com/help.cgi?bootstrap) prefix.                                             |                                      |                                                                                   |
| `vce()` and weights are not allowed with the [<strong>svy</strong>](http://www.stata.com/help.cgi?svy) prefix.                                             |                                      |                                                                                   |
| `fweight`s, `iweight`s, and `pweight`s are allowed; see [<strong>weight</strong>](http://www.stata.com/help.cgi?weight).                                   |                                      |                                                                                   |
| `coeflegend` does not appear in the dialog box.                                                                                                                                       |                                      |                                                                                   |
| See [<strong>[R]</strong> ratio postestimation](http://www.stata.com/help.cgi?ratio_postestimation) for features available after estimation.               |                                      |                                                                                   |
