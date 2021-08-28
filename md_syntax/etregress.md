## Syntax

Basic syntax

`etregress`
[depvar](http://www.stata.com/help.cgi?depvar)
\[[indepvars](http://www.stata.com/help.cgi?indepvars)\]`,`
`treat:(`[depvar_t](http://www.stata.com/help.cgi?depvar)
`=`
[indepvars_t](http://www.stata.com/help.cgi?indepvars)`)`
\[`twostep`|`cfunction`\]

Full syntax for maximum likelihood estimates only

`etregress`
[depvar](http://www.stata.com/help.cgi?depvar)
\[[indepvars](http://www.stata.com/help.cgi?indepvars)\]
_\[`if`\] \[`in`\]_ \[`weight`\]`,`
`treat:(`[depvar_t](http://www.stata.com/help.cgi?depvar)
`=`
[indepvars_t](http://www.stata.com/help.cgi?indepvars)
\[`, noconstant`\]`)` \[`etregress_ml_options`\]

Full syntax for two-step consistent estimates only

`etregress`
[depvar](http://www.stata.com/help.cgi?depvar)
\[[indepvars](http://www.stata.com/help.cgi?indepvars)\]
_\[`if`\] \[`in`\]_`,`
`treat:(`[depvar_t](http://www.stata.com/help.cgi?depvar)
`=`
[indepvars_t](http://www.stata.com/help.cgi?indepvars)
\[`, noconstant`\]`) twostep` \[`etregress_ts_options`\]

Full syntax for control-function estimates only

`etregress`
[depvar](http://www.stata.com/help.cgi?depvar)
\[[indepvars](http://www.stata.com/help.cgi?indepvars)\]
_\[`if`\] \[`in`\]_`,`
`treat:(`[depvar_t](http://www.stata.com/help.cgi?depvar)
`=`
[indepvars_t](http://www.stata.com/help.cgi?indepvars)
\[`, noconstant`\]`) cfunction` \[`etregress_cf_options`\]

| etregress\_ml\_options                                                        |                                | Description                                                                                                                                      |
|-------------------------------------------------------------------------------|--------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| Model                                                                         |                                |                                                                                                                                                  |
| \*                                                                            | `treat()`                      | equation for treatment effects                                                                                                                   |
|                                                                               | `noconstant`                   | suppress constant term                                                                                                                           |
|                                                                               | `poutcomes`                    | use potential-outcome model with separate treatment and control group variance and correlation parameters                                        |
|                                                                               | `constraints(constraints)` | apply specified linear constraints                                                                                                               |
|                                                                               | `collinear`                    | keep collinear variables                                                                                                                         |
| SE/Robust                                                                     |                                |                                                                                                                                                  |
|                                                                               | `vce(vcetype)`                 | `vcetype` may be `oim`, `robust`, `cluster clustvar`, `opg`, `bootstrap`, or `jackknife`                                                       |
| Reporting                                                                     |                                |                                                                                                                                                  |
|                                                                               | `level(#)`                     | set confidence level; default is `level(95)`                                                                                                     |
|                                                                               | `first`                        | report first-step probit estimates                                                                                                               |
|                                                                               | `hazard(newvar)`               | create `newvar` containing hazard from treatment equation                                                                                        |
|                                                                               | `lrmodel`                      | perform the likelihood-ratio model test instead of the default Wald test                                                                         |
|                                                                               | `nocnsreport`                  | do not display constraints                                                                                                                       |
|                                                                               | `display_options`              | control columns and column formats, row spacing, line width, display of omitted variables and base and empty cells, and factor-variable labeling |
| Maximization                                                                  |                                |                                                                                                                                                  |
|                                                                               | `maximize_options`             | control maximization process; seldom used                                                                                                        |
|                                                                               | `coeflegend`                   | display legend instead of statistics                                                                                                             |
| \* `treat(depvar_t = indepvars_t`\[`, noconstant`\]`)` is required. |                                |                                                                                                                                                  |

| etregress\_ts\_options                                                                       |                   | Description                                                                                                                                      |
|----------------------------------------------------------------------------------------------|-------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| Model                                                                                        |                   |                                                                                                                                                  |
| \*                                                                                           | `treat()`         | equation for treatment effects                                                                                                                   |
| \*                                                                                           | `twostep`         | produce two-step consistent estimate                                                                                                             |
|                                                                                              | `noconstant`      | suppress constant term                                                                                                                           |
| SE                                                                                           |                   |                                                                                                                                                  |
|                                                                                              | `vce(vcetype)`    | `vcetype` may be `conventional`, `bootstrap`, or `jackknife`                                                                                     |
| Reporting                                                                                    |                   |                                                                                                                                                  |
|                                                                                              | `level(#)`        | set confidence level; default is `level(95)`                                                                                                     |
|                                                                                              | `first`           | report first-step probit estimates                                                                                                               |
|                                                                                              | `hazard(newvar)`  | create `newvar` containing hazard from treatment equation                                                                                        |
|                                                                                              | `display_options` | control columns and column formats, row spacing, line width, display of omitted variables and base and empty cells, and factor-variable labeling |
|                                                                                              | `coeflegend`      | display legend instead of statistics                                                                                                             |
| \* `treat(depvar_t = indepvars_t`\[`, noconstant`\]`)` and `twostep` are required. |                   |                                                                                                                                                  |

| etregress\_cf\_options                                                                         |                    | Description                                                                                                                                      |
|------------------------------------------------------------------------------------------------|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| Model                                                                                          |                    |                                                                                                                                                  |
| \*                                                                                             | `treat()`          | equation for treatment effects                                                                                                                   |
| \*                                                                                             | `cfunction`        | produce control-function estimate                                                                                                                |
|                                                                                                | `noconstant`       | suppress constant term                                                                                                                           |
|                                                                                                | `poutcomes`        | use potential-outcome model with separate treatment and control group variance and correlation parameters                                        |
| SE                                                                                             |                    |                                                                                                                                                  |
|                                                                                                | `vce(vcetype)`     | `vcetype` may be `robust`, `bootstrap`, or `jackknife`                                                                                           |
| Reporting                                                                                      |                    |                                                                                                                                                  |
|                                                                                                | `level(#)`         | set confidence level; default is `level(95)`                                                                                                     |
|                                                                                                | `first`            | report first-step probit estimates                                                                                                               |
|                                                                                                | `hazard(newvar)`   | create `newvar` containing hazard from treatment equation                                                                                        |
|                                                                                                | `display_options`  | control columns and column formats, row spacing, line width, display of omitted variables and base and empty cells, and factor-variable labeling |
| Maximization                                                                                   |                    |                                                                                                                                                  |
|                                                                                                | `maximize_options` | control maximization process; seldom used                                                                                                        |
|                                                                                                | `coeflegend`       | display legend instead of statistics                                                                                                             |
| \* `treat(depvar_t = indepvars_t`\[`, noconstant`\]`)` and `cfunction` are required. |                    |                                                                                                                                                  |

`indepvars` and `indepvars_t` may contain factor variables; see
[<strong>fvvarlist</strong>](http://www.stata.com/help.cgi?fvvarlist).

`depvar`, `indepvars`, `depvar_t`, and `indepvars_t` may contain
time-series operators; see
[<strong>tsvarlist</strong>](http://www.stata.com/help.cgi?tsvarlist).

`bootstrap`, `by`, `fp`, `jackknife`, `rolling`, `statsby`, and `svy`
are allowed; see
[<strong>prefix</strong>](http://www.stata.com/help.cgi?prefix).

Weights are not allowed with the
[<strong>bootstrap</strong>](http://www.stata.com/help.cgi?bootstrap)
prefix.

`aweight`s are not allowed with the
[<strong>jackknife</strong>](http://www.stata.com/help.cgi?jackknife)
prefix.

`twostep`, `cfunction`, `vce()`, `first`, `hazard()`, `lrmodel`, and
weights are not allowed with the
[<strong>svy</strong>](http://www.stata.com/help.cgi?svy)
prefix.

`pweight`s, `aweight`s, `fweight`s, and `iweight`s are allowed with both
maximum likelihood and control-function estimation; see
[<strong>weight</strong>](http://www.stata.com/help.cgi?weight).
No weights are allowed if `twostep` is specified.

`coeflegend` does not appear in the dialog box.

See
[<strong>[TE]</strong> etregress postestimation](http://www.stata.com/help.cgi?etregress_postestimation)
for features available after estimation.
