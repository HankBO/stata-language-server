## Syntax

Maximum likelihood estimation

`hetregress`
[depvar](http://www.stata.com/help.cgi?depvar)
\[[indepvars](http://www.stata.com/help.cgi?indepvars)\]
_\[`if`\] \[`in`\]_ \[`weight`\] \[`,`
`ml_options`\]

Two-step GLS estimation

`hetregress`
[depvar](http://www.stata.com/help.cgi?depvar)
\[[indepvars](http://www.stata.com/help.cgi?indepvars)\]
_\[`if`\] \[`in`\]_`, twostep`
`het(`[varlist](http://www.stata.com/help.cgi?varlist)`)`
\[`ts_options`\]

| ml\_options  |                                                                                      | Description                                                                                                                                      |
|--------------|--------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| Model        |                                                                                      |                                                                                                                                                  |
|              | `mle`                                                                                | use maximum likelihood estimator; the default                                                                                                    |
|              | `het(`[varlist](http://www.stata.com/help.cgi?varlist)`)` | independent variables to model the variance                                                                                                      |
|              | `noconstant`                                                                         | suppress constant term                                                                                                                           |
|              | `constraints(constraints)`                                                       | apply specified linear constraints                                                                                                               |
|              | `collinear`                                                                          | keep collinear variables                                                                                                                         |
| SE/Robust    |                                                                                      |                                                                                                                                                  |
|              | `vce(vcetype)`                                                                       | `vcetype` may be `oim`, `robust`, `cluster clustvar`, `opg`, `bootstrap`, or `jackknife`                                                       |
| Reporting    |                                                                                      |                                                                                                                                                  |
|              | `level(#)`                                                                           | set confidence level; default is `level(95)`                                                                                                     |
|              | `lrmodel`                                                                            | perform the LR model test instead of the default Wald model test                                                                                 |
|              | `waldhet`                                                                            | perform Wald test on variance instead of LR test                                                                                                 |
|              | `nocnsreport`                                                                        | do not display constraints                                                                                                                       |
|              | `display_options`                                                                    | control columns and column formats, row spacing, line width, display of omitted variables and base and empty cells, and factor-variable labeling |
| Maximization |                                                                                      |                                                                                                                                                  |
|              | `maximize_options`                                                                   | control the maximization process; seldom used                                                                                                    |
|              | `coeflegend`                                                                         | display legend instead of statistics                                                                                                             |

| ts\_options                            |                                                                                      | Description                                                                                                                                      |
|----------------------------------------|--------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| Model                                  |                                                                                      |                                                                                                                                                  |
| \*                                     | `twostep`                                                                            | use two-step GLS estimator; default is maximum likelihood                                                                                        |
| \*                                     | `het(`[varlist](http://www.stata.com/help.cgi?varlist)`)` | independent variables to model the variance                                                                                                      |
|                                        | `noconstant`                                                                         | suppress constant term                                                                                                                           |
| SE                                     |                                                                                      |                                                                                                                                                  |
|                                        | `vce(vcetype)`                                                                       | `vcetype` may be `conventional`, `bootstrap`, or `jackknife`                                                                                     |
| Reporting                              |                                                                                      |                                                                                                                                                  |
|                                        | `level(#)`                                                                           | set confidence level; default is `level(95)`                                                                                                     |
|                                        | `display_options`                                                                    | control columns and column formats, row spacing, line width, display of omitted variables and base and empty cells, and factor-variable labeling |
|                                        | `coeflegend`                                                                         | display legend instead of statistics                                                                                                             |
| \* `twostep` and `het()` are required. |                                                                                      |                                                                                                                                                  |

`indepvars` and `varlist` may contain factor variables; see
[<strong>fvvarlist</strong>](http://www.stata.com/help.cgi?fvvarlist).

`depvar`, `indepvars`, and `varlist` may contain time-series operators;
see
[<strong>tsvarlist</strong>](http://www.stata.com/help.cgi?tsvarlist).

`bayes`, `bootstrap`, `by`, `fp`, `jackknife`, `rolling`, `statsby`, and
`svy` are allowed; see
[<strong>prefix</strong>](http://www.stata.com/help.cgi?prefix).
For more details, see
[<strong>[BAYES]</strong> bayes: hetregress](http://www.stata.com/help.cgi?bayes_hetregress).

Weights are not allowed with the
[<strong>bootstrap</strong>](http://www.stata.com/help.cgi?bootstrap)
prefix.

`aweight`s are not allowed with the
[<strong>jackknife</strong>](http://www.stata.com/help.cgi?jackknife)
prefix.

`vce()`, `lrmodel`, `twostep`, and weights are not allowed with the
[<strong>svy</strong>](http://www.stata.com/help.cgi?svy)
prefix.

`aweight`s, `fweight`s, `iweight`s, and `pweight`s are allowed with
maximum likelihood estimation; see
[<strong>weight</strong>](http://www.stata.com/help.cgi?weight).

`coeflegend` does not appear in the dialog box.

See
[<strong>[R]</strong> hetregress postestimation](http://www.stata.com/help.cgi?hetregress_postestimation)
for features available after estimation.
