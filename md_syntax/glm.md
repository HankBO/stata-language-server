## Syntax

`glm`
[depvar](http://www.stata.com/help.cgi?depvar)
\[[indepvars](http://www.stata.com/help.cgi?indepvars)\]
_\[`if`\] \[`in`\]_ \[`weight`\] \[`,`
`options`\]

| Options      |                                | Description                                                                                                                                                                                                                 |
|--------------|--------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Model        |                                |                                                                                                                                                                                                                             |
|              | `family(familyname)`           | distribution of [depvar](http://www.stata.com/help.cgi?depvar); default is `family(gaussian)`                                                                                                    |
|              | `link(linkname)`               | link function; default is canonical link for `family()` specified                                                                                                                                                           |
| Model 2      |                                |                                                                                                                                                                                                                             |
|              | `noconstant`                   | suppress constant term                                                                                                                                                                                                      |
|              | `exposure(varname)`            | include ln(`varname`) in model with coefficient constrained to 1                                                                                                                                                            |
|              | `offset(varname)`              | include `varname` in model with coefficient constrained to 1                                                                                                                                                                |
|              | `constraints(constraints)` | apply specified linear constraints                                                                                                                                                                                          |
|              | `collinear`                    | keep collinear variables                                                                                                                                                                                                    |
|              | `asis`                         | retain perfect predictor variables                                                                                                                                                                                          |
|              | `mu(varname)`                  | use `varname` as the initial estimate for the mean of [depvar](http://www.stata.com/help.cgi?depvar)                                                                                             |
|              | `init(varname)`                | synonym for `mu(varname)`                                                                                                                                                                                                   |
| SE/Robust    |                                |                                                                                                                                                                                                                             |
|              | `vce(vcetype)`             | `vcetype` may be `oim`, `robust`, `cluster clustvar`, `eim`, `opg`, `bootstrap`, `jackknife`, `hac` [<var class="command">kernel</var><strong></strong>](#kernel), `jackknife1`, or `unbiased` |
|              | `vfactor(#)`                   | multiply variance matrix by scalar `#`                                                                                                                                                                                      |
|              | `disp(#)`                      | quasilikelihood multiplier                                                                                                                                                                                                  |
|              | `scale(x2`\|`dev`\|`#)`      | set the scale parameter                                                                                                                                                                                                     |
| Reporting    |                                |                                                                                                                                                                                                                             |
|              | `level(#)`                     | set confidence level; default is `level(95)`                                                                                                                                                                                |
|              | `eform`                        | report exponentiated coefficients                                                                                                                                                                                           |
|              | `nocnsreport`                  | do not display constraints                                                                                                                                                                                                  |
|              | `display_options`              | control columns and column formats, row spacing, line width, display of omitted variables and base and empty cells, and factor-variable labeling                                                                            |
| Maximization |                                |                                                                                                                                                                                                                             |
|              | `ml`                           | use maximum likelihood optimization; the default                                                                                                                                                                            |
|              | `irls`                         | use iterated, reweighted least-squares optimization of the deviance                                                                                                                                                         |
|              | `maximize_options`             | control the maximization process; seldom used                                                                                                                                                                               |
|              | `fisher(#)`                    | use the Fisher scoring Hessian or expected information matrix (EIM)                                                                                                                                                         |
|              | `search`                       | search for good starting values                                                                                                                                                                                             |
|              | `noheader`                     | suppress header table from above coefficient table                                                                                                                                                                          |
|              | `notable`                      | suppress coefficient table                                                                                                                                                                                                  |
|              | `nodisplay`                    | suppress the output; iteration log is still displayed                                                                                                                                                                       |
|              | `coeflegend`                   | display legend instead of statistics                                                                                                                                                                                        |

| familyname |                                | Description        |
|------------|--------------------------------|--------------------|
|            | `gaussian`                     | Gaussian (normal)  |
|            | `igaussian`                    | inverse Gaussian   |
|            | `binomial`\[`varnameN`\|`#N`\] | Bernoulli/binomial |
|            | `poisson`                      | Poisson            |
|            | `nbinomial`\[`#k`\|`ml`\]      | negative binomial  |
|            | `gamma`                        | gamma              |

| linkname |              | Description       |
|----------|--------------|-------------------|
|          | `identity`   | identity          |
|          | `log`        | log               |
|          | `logit`      | logit             |
|          | `probit`     | probit            |
|          | `cloglog`    | clog-log          |
|          | `power #`  | power             |
|          | `opower #` | odds power        |
|          | `nbinomial`  | negative binomial |
|          | `loglog`     | log-log           |
|          | `logc`       | log-complement    |

`indepvars` may contain factor variables; see
[<strong>fvvarlist</strong>](http://www.stata.com/help.cgi?fvvarlist).

`depvar` and `indepvars` may contain time-series operators; see
[<strong>tsvarlist</strong>](http://www.stata.com/help.cgi?tsvarlist).

`bayes`, `bootstrap`, `by`, `fmm`, `fp`, `jackknife`, `mfp`,
`mi estimate`, `nestreg`, `rolling`, `statsby`, `stepwise`, and `svy`
are allowed; see
[<strong>prefix</strong>](http://www.stata.com/help.cgi?prefix).
For more details, see
[<strong>[BAYES]</strong> bayes: glm](http://www.stata.com/help.cgi?bayes_glm)
and
[<strong>[FMM]</strong> fmm: glm](http://www.stata.com/help.cgi?fmm_glm).

`vce(bootstrap)`, `vce(jackknife)`, and `vce(jackknife1)` are not
allowed with the
[<strong>mi estimate</strong>](http://www.stata.com/help.cgi?mi%20estimate)
prefix.

Weights are not allowed with the
[<strong>bootstrap</strong>](http://www.stata.com/help.cgi?bootstrap)
prefix.

`aweight`s are not allowed with the
[<strong>jackknife</strong>](http://www.stata.com/help.cgi?jackknife)
prefix.

`vce()`, `vfactor()`, `disp()`, `scale()`, `irls`, `fisher()`,
`noheader`, `notable`, `nodisplay`, and weights are not allowed with the
[<strong>svy</strong>](http://www.stata.com/help.cgi?svy)
prefix.

`fweight`s, `aweight`s, `iweight`s, and `pweight`s are allowed; see
[<strong>weight</strong>](http://www.stata.com/help.cgi?weight).

`noheader`, `notable`, `nodisplay`, and `coeflegend` do not appear in
the dialog box.

See
[<strong>[R]</strong> glm postestimation](http://www.stata.com/help.cgi?glm_postestimation)
for features available after estimation.
