## Syntax

Standard syntax

`fmm #` _\[`if`\] \[`in`\]_ \[`weight`\]
\[`, fmmopts`\] `: component`

Hybrid syntax

`fmm` _\[`if`\] \[`in`\]_ \[`weight`\] \[`,`
`fmmopts`\] `: (component_1) (component_2)` ...

where the standard syntax for `component` is

`model`
[depvar](http://www.stata.com/help.cgi?depvar)
[indepvars](http://www.stata.com/help.cgi?indepvars)
\[`, options`\]

the hybrid syntax for `component` is

`model`
[depvar](http://www.stata.com/help.cgi?depvar)
[indepvars](http://www.stata.com/help.cgi?indepvars)
\[`, lcprob(varlist) options`\]

`model` is an estimation command, and `options` are `model`-specific
estimation options.

| fmmopts   |                                | Description                                                                                                                            |
|-----------|--------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| Model     |                                |                                                                                                                                        |
|           | `lcinvariant(pclassname)`      | specify parameters that are equal across classes; default is `lcinvariant(none)`                                                       |
|           | `lcprob(varlist)`              | specify independent variables for class probabilities                                                                                  |
|           | `lclabel(name)`                | name of the categorical latent variable; default is `lclabel(Class)`                                                                   |
|           | `lcbase(#)`                    | base latent class                                                                                                                      |
|           | `constraints(constraints)` | apply specified linear constraints                                                                                                     |
|           | `collinear`                    | keep collinear variables                                                                                                               |
| SE/Robust |                                |                                                                                                                                        |
|           | `vce(vcetype)`                 | `vcetype` may be `oim`, `robust`, or `cluster clustvar`                                                                              |
| Reporting |                                |                                                                                                                                        |
|           | `level(#)`                     | set confidence level; default is `level(95)`                                                                                           |
|           | `nocnsreport`                  | do not display constraints                                                                                                             |
|           | `noheader`                     | do not display header above parameter table                                                                                            |
|           | `nodvheader`                   | do not display dependent variables information in the header                                                                           |
|           | `notable`                      | do not display parameter table                                                                                                         |
|           | `display_options`              | control INCLUDE help shortdes-displayoptall {syntab None:Maximization} {synopt None}`maximize_options`control the maximization process |
|           | `startvalues(svmethod)`        | method for obtaining starting values; default is `startvalues(factor)`                                                                 |
|           | `emopts(maxopts)`              | control EM algorithm for improved starting values                                                                                      |
|           | `noestimate`                   | do not fit the model; show starting values instead                                                                                     |

|                                                                                                                                                                       |     |     |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|-----|
| `varlist` may contain factor variables; see [<strong>fvvarlist</strong>](http://www.stata.com/help.cgi?fvvarlist).                         |     |     |
| `by`, `statsby`, and `svy` are allowed; see [<strong>prefix</strong>](http://www.stata.com/help.cgi?prefix).                               |     |     |
| `vce()` and weights are not allowed with the [<strong>svy</strong>](http://www.stata.com/help.cgi?svy) prefix.                             |     |     |
| `fweight`s, `iweight`s, and `pweight`s are allowed; see [<strong>weight</strong>](http://www.stata.com/help.cgi?weight).                   |     |     |
| `coeflegend` does not appear in the dialog box.                                                                                                                       |     |     |
| See [<strong>[FMM]</strong> fmm postestimation](http://www.stata.com/help.cgi?fmm_postestimation) for features available after estimation. |     |     |

| pclassname |          | Description                    |
|------------|----------|--------------------------------|
|            | `cons`   | intercepts and cutpoints       |
|            | `coef`   | fixed coefficients             |
|            | `errvar` | covariances of errors          |
|            | `scale`  | scaling parameters             |
|            | `all`    | all the above                  |
|            | `none`   | none of the above; the default |
