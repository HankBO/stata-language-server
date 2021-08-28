## Syntax

`asroprobit`
[depvar](http://www.stata.com/help.cgi?depvar)
\[[indepvars](http://www.stata.com/help.cgi?indepvars)\]
_\[`if`\] \[`in`\]_ \[`weight`\] `,`
`case(varname) alternatives(varname)` \[`options`\]

| Options      |                                                       | Description                                                                                                                                                     |
|--------------|-------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Model        |                                                       |                                                                                                                                                                 |
| \*           | `case(varname)`                                       | use `varname` to identify cases                                                                                                                                 |
| \*           | `alternatives(varname)`                               | use `varname` to identify the alternatives available for each case                                                                                              |
|              | `casevars(varlist)`                                   | case-specific variables                                                                                                                                         |
|              | `constraints(constraints)`                        | apply specified linear constraints                                                                                                                              |
|              | `collinear`                                           | keep collinear variables                                                                                                                                        |
| Model 2      |                                                       |                                                                                                                                                                 |
|              | `correlation(correlation)`                            | correlation structure of the latent-variable errors                                                                                                             |
|              | `stddev(stddev)`                                      | variance structure of the latent-variable errors                                                                                                                |
|              | `structural`                                          | use the structural covariance parameterization; default is the differenced covariance parameterization                                                          |
|              | `factor(#)`                                           | use the factor covariance structure with dimension `#`                                                                                                          |
|              | `noconstant`                                          | suppress the alternative-specific constant terms                                                                                                                |
|              | `basealternative(#,lbl,str)`                          | alternative used for normalizing location                                                                                                                       |
|              | `scalealternative(#,lbl,str)`                         | alternative used for normalizing scale                                                                                                                          |
|              | `altwise`                                             | use alternativewise deletion instead of casewise deletion                                                                                                       |
|              | `reverse`                                             | interpret the lowest rank in [depvar](http://www.stata.com/help.cgi?depvar) as the best; the default is the highest rank is the best |
| SE/Robust    |                                                       |                                                                                                                                                                 |
|              | `vce(vcetype)`                                        | `vcetype` may be `oim`, `robust`, `cluster clustvar`, `opg`, `bootstrap`, or `jackknife`                                                                      |
| Reporting    |                                                       |                                                                                                                                                                 |
|              | `level(#)`                                            | set confidence level; default is `level(95)`                                                                                                                    |
|              | `notransform`                                         | do not transform variance-covariance estimates to the standard deviation and correlation metric                                                                 |
|              | `nocnsreport`                                         | do not display constraints                                                                                                                                      |
|              | `display_options`                                     | control columns and column formats, row spacing, line width, display of omitted variables and base and empty cells, and factor-variable labeling                |
| Integration  |                                                       |                                                                                                                                                                 |
|              | `intmethod(seqtype)`                                  | type of quasi- or pseudouniform sequence                                                                                                                        |
|              | `intpoints(#)`                                        | number of points in each sequence                                                                                                                               |
|              | `intburn(#)`                                          | starting index in the Hammersley or Halton sequence                                                                                                             |
|              | `intseed(code`|`#)` | pseudouniform random-number seed                                                                                                                                |
|              | `antithetics`                                         | use antithetic draws                                                                                                                                            |
|              | `nopivot`                                             | do not use integration interval pivoting                                                                                                                        |
|              | `initbhhh(#)`                                         | use the BHHH optimization algorithm for the first `#` iterations                                                                                                |
|              | `favor(speed`\|`space)`                           | favor speed or space when generating integration points                                                                                                         |
| Maximization |                                                       |                                                                                                                                                                 |
|              | `maximize_options`                                    | control the maximization process                                                                                                                                |
|              | `coeflegend`                                          | display legend instead of statistics                                                                                                                            |

| correlation |                     | Description                                                                                                              |
|-------------|---------------------|--------------------------------------------------------------------------------------------------------------------------|
|             | `unstructured`      | one correlation parameter for each pair of alternatives; correlations with the `basealternative()` are zero; the default |
|             | `exchangeable`      | one correlation parameter common to all pairs of alternatives; correlations with the `basealternative()` are zero        |
|             | `independent`       | constrain all correlation parameters to zero                                                                             |
|             | `pattern matname` | user-specified matrix identifying the correlation pattern                                                                |
|             | `fixed matname`   | user-specified matrix identifying the fixed and free correlation parameters                                              |

| stddev |                     | Description                                                                                                                       |
|--------|---------------------|-----------------------------------------------------------------------------------------------------------------------------------|
|        | `heteroskedastic`   | estimate standard deviation for each alternative; standard deviations for `basealternative()` and `scalealternative()` set to one |
|        | `homoskedastic`     | all standard deviations are one                                                                                                   |
|        | `pattern matname` | user-specified matrix identifying the standard deviation pattern                                                                  |
|        | `fixed matname`   | user-specified matrix identifying the fixed and free standard deviations                                                          |

| seqtype |              | Description                    |
|---------|--------------|--------------------------------|
|         | `hammersley` | Hammersley point set           |
|         | `halton`     | Halton point set               |
|         | `random`     | uniform pseudorandom point set |

\* `case(varname)` and `alternatives(varname)` are required.

`indepvars` and `varlist` may contain factor variables; see
[<strong>fvvarlist</strong>](http://www.stata.com/help.cgi?fvvarlist).

`bootstrap`, `by`, `jackknife`, and `statsby` are allowed; see
[<strong>prefix</strong>](http://www.stata.com/help.cgi?prefix).

Weights are not allowed with the
[<strong>bootstrap</strong>](http://www.stata.com/help.cgi?bootstrap)
prefix.

`fweight`s, `iweight`s, and `pweight`s are allowed; see
[<strong>weight</strong>](http://www.stata.com/help.cgi?weight).

`coeflegend` does not appear in the dialog box.

See
[<strong>[R]</strong> asroprobit postestimation](http://www.stata.com/help.cgi?asroprobit_postestimation)
for features available after estimation.
