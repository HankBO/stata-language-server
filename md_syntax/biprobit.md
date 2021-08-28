## Syntax

Bivariate probit regression

`biprobit depvar1 depvar2`
\[[indepvars](http://www.stata.com/help.cgi?indepvars)\]
_\[`if`\] \[`in`\]_ \[`weight`\] \[`,`
`options`\]

Seemingly unrelated bivariate probit regression

`biprobit equation1 equation2` _\[`if`\]
\[`in`\]_ \[`weight`\] \[`, su_options`\]

where `equation1` and `equation2` are specified as

`(` \[`eqname: `\]
[depvar](http://www.stata.com/help.cgi?depvar)
\[`=`\]
\[[indepvars](http://www.stata.com/help.cgi?indepvars)\]
\[`, noconstant offset(varname)` \] `)`

| Options      |                                | Description                                                                                                                                      |
|--------------|--------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| Model        |                                |                                                                                                                                                  |
|              | `noconstant`                   | suppress constant term                                                                                                                           |
|              | `partial`                      | fit partial observability model                                                                                                                  |
|              | `offset1(varname)`             | offset variable for first equation                                                                                                               |
|              | `offset2(varname)`             | offset variable for second equation                                                                                                              |
|              | `constraints(constraints)` | apply specified linear constraints                                                                                                               |
|              | `collinear`                    | keep collinear variables                                                                                                                         |
| SE/Robust    |                                |                                                                                                                                                  |
|              | `vce(vcetype)`                 | `vcetype` may be `oim`, `robust`, `cluster clustvar`, `opg`, `bootstrap`, or `jackknife`                                                       |
| Reporting    |                                |                                                                                                                                                  |
|              | `level(#)`                     | set confidence level; default is `level(95)`                                                                                                     |
|              | `lrmodel`                      | perform likelihood-ratio model test instead of the default Wald test                                                                             |
|              | `nocnsreport`                  | do not display constraints                                                                                                                       |
|              | `display_options`              | control columns and column formats, row spacing, line width, display of omitted variables and base and empty cells, and factor-variable labeling |
| Maximization |                                |                                                                                                                                                  |
|              | `maximize_options`             | control the maximization process; seldom used                                                                                                    |
|              | `coeflegend`                   | display legend instead of statistics                                                                                                             |

| su\_options  |                                | Description                                                                                                                                      |
|--------------|--------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| Model        |                                |                                                                                                                                                  |
|              | `partial`                      | fit partial observability model                                                                                                                  |
|              | `constraints(constraints)` | apply specified linear constraints                                                                                                               |
|              | `collinear`                    | keep collinear variables                                                                                                                         |
| SE/Robust    |                                |                                                                                                                                                  |
|              | `vce(vcetype)`                 | `vcetype` may be `oim`, `robust`, `cluster clustvar`, `opg`, `bootstrap`, or `jackknife`                                                       |
| Reporting    |                                |                                                                                                                                                  |
|              | `level(#)`                     | set confidence level; default is `level(95)`                                                                                                     |
|              | `lrmodel`                      | perform the likelihood-ratio model test instead of the default Wald test                                                                         |
|              | `nocnsreport`                  | do not display constraints                                                                                                                       |
|              | `display_options`              | control columns and column formats, row spacing, line width, display of omitted variables and base and empty cells, and factor-variable labeling |
| Maximization |                                |                                                                                                                                                  |
|              | `maximize_options`             | control the maximization process; seldom used                                                                                                    |
|              | `coeflegend`                   | display legend instead of statistics                                                                                                             |

`indepvars` may contain factor variables; see
[<strong>fvvarlist</strong>](http://www.stata.com/help.cgi?fvvarlist).

`depvar1`, `depvar2`, `indepvars`, and `depvar` may contain time-series
operators; see
[<strong>tsvarlist</strong>](http://www.stata.com/help.cgi?tsvarlist).

`bayes`, `bootstrap`, `by`, `fp`, `jackknife`, `rolling`, `statsby`, and
`svy` are allowed; see
[<strong>prefix</strong>](http://www.stata.com/help.cgi?prefix).
For more details, see
[<strong>[BAYES]</strong> bayes: biprobit](http://www.stata.com/help.cgi?bayes_biprobit).

Weights are not allowed with the
[<strong>bootstrap</strong>](http://www.stata.com/help.cgi?bootstrap)
prefix.

`vce()`, `lrmodel`, and weights are not allowed with the
[<strong>svy</strong>](http://www.stata.com/help.cgi?svy)
prefix.

`pweight`s, `fweight`s, and `iweight`s are allowed; see
[<strong>weight</strong>](http://www.stata.com/help.cgi?weight).

`coeflegend` does not appear in the dialog box.

See
[<strong>[R]</strong> biprobit postestimation](http://www.stata.com/help.cgi?biprobit_postestimation)
for features available after estimation.
