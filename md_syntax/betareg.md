## Syntax

`betareg`
[depvar](http://www.stata.com/help.cgi?depvar)
[indepvars](http://www.stata.com/help.cgi?indepvars)
_\[`if`\] \[`in`\]_ \[`weight`\] \[`,`
`options`\]

| Options      |                                                                                                           | Description                                                                                                                                      |
|--------------|-----------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| Model        |                                                                                                           |                                                                                                                                                  |
|              | `noconstant`                                                                                              | suppress constant term                                                                                                                           |
|              | `scale(`[varlist](http://www.stata.com/help.cgi?varlist) \[`, noconstant)` | specify independent variables for scale                                                                                                          |
|              | `link(linkname)`                                                                                          | specify link function for the conditional mean; default is `link(logit)`                                                                         |
|              | `slink(slinkname)`                                                                                        | specify link function for the conditional scale; default is `slink(log)`                                                                         |
|              | `constraints(constraints)`                                                                            | apply specified linear constraints                                                                                                               |
| SE/Robust    |                                                                                                           |                                                                                                                                                  |
|              | `vce(vcetype)`                                                                                            | `vcetype` may be `oim`, `robust`, `cluster clustvar`, `bootstrap`, or `jackknife`                                                              |
| Reporting    |                                                                                                           |                                                                                                                                                  |
|              | `level(#)`                                                                                                | set confidence level; default is `level(95)`                                                                                                     |
|              | `nocnsreport`                                                                                             | do not display constraints                                                                                                                       |
|              | `display_options`                                                                                         | control columns and column formats, row spacing, line width, display of omitted variables and base and empty cells, and factor-variable labeling |
| Maximization |                                                                                                           |                                                                                                                                                  |
|              | `maximize_options`                                                                                        | control the maximization process; seldom used                                                                                                    |
|              | `coeflegend`                                                                                              | display legend instead of statistics                                                                                                             |

| linkname |           | Description           |
|----------|-----------|-----------------------|
|          | `logit`   | logit                 |
|          | `probit`  | probit                |
|          | `cloglog` | complementary log-log |
|          | `loglog`  | log-log               |

| slinkname |            | Description |
|-----------|------------|-------------|
|           | `log`      | log         |
|           | `root`     | square root |
|           | `identity` | identity    |

`indepvars` and `varlist` specified in `scale()` may contain factor
variables; see
[<strong>fvvarlist</strong>](http://www.stata.com/help.cgi?fvvarlist).

`bayes`, `bootstrap`, `by`, `fmm`, `fp`, `jackknife`, `nestreg`,
`rolling`, `statsby`, `stepwise`, and `svy` are allowed; see
[<strong>prefix</strong>](http://www.stata.com/help.cgi?prefix).
For more details, see
[<strong>[BAYES]</strong> bayes: betareg](http://www.stata.com/help.cgi?bayes_betareg)
and
[<strong>[FMM]</strong> fmm: betareg](http://www.stata.com/help.cgi?fmm_betareg).

Weights are not allowed with the
[<strong>bootstrap</strong>](http://www.stata.com/help.cgi?bootstrap)
prefix.

`vce()` and weights are not allowed with the
[<strong>svy</strong>](http://www.stata.com/help.cgi?svy)
prefix.

`fweight`s, `iweight`s, and `pweight`s are allowed; see
[<strong>weight</strong>](http://www.stata.com/help.cgi?weight).

`coeflegend` does not appear in the dialog box.

See
[<strong>[R]</strong> betareg postestimation](http://www.stata.com/help.cgi?betareg_postestimation)
for features available after estimation.
