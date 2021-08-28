## Syntax

`fmm` _\[`if`\] \[`in`\]_
\[[<var class="command">weight</var><strong></strong>](fmm%20pointmass##weight)\]
\[`, fmmopts`\]`: (pointmass`
[depvar](http://www.stata.com/help.cgi?depvar)
\[`, options`\]`) (component_1)` \[`(component_2)` ...\]

`component` is defined in
[<strong>[FMM]</strong> fmm](http://www.stata.com/help.cgi?fmm).

| Options                                                                                                                                           |                   | Description                                         |
|---------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|-----------------------------------------------------|
|                                                                                                                                                   | `lcprob(varlist)` | specify independent variables for class probability |
|                                                                                                                                                   | `value(#)`        | integer-valued location of the point mass           |
| `depvar` may contain time-series operators; see [<strong>tsvarlist</strong>](http://www.stata.com/help.cgi?tsvarlist). |                   |                                                     |

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

|                                                                                                                                                                                                                                            |     |     |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|-----|
| `varlist` may contain factor variables; see [<strong>fvvarlist</strong>](http://www.stata.com/help.cgi?fvvarlist).                                                                                              |     |     |
| `by`, `statsby`, and `svy` are allowed; see [<strong>prefix</strong>](http://www.stata.com/help.cgi?prefix).                                                                                                    |     |     |
| `vce()` and weights are not allowed with the [<strong>svy</strong>](http://www.stata.com/help.cgi?svy) prefix.                                                                                                  |     |     |
| `fweight`s, `iweight`s, and `pweight`s are allowed; see [<strong>weight</strong>](http://www.stata.com/help.cgi?weight).                                                                                        |     |     |
| `coeflegend` does not appear in the dialog box.                                                                                                                                                                                            |     |     |
| See [<strong>[FMM]</strong> fmm postestimation](http://www.stata.com/help.cgi?fmm_postestimation) for features available after estimation.                                                                      |     |     |
| For a detailed description of `fmmopts`, see [<var class="command">Options</var><strong></strong>](fmm##options) in [<strong>[FMM]</strong> fmm](http://www.stata.com/help.cgi?fmm). |     |     |

| pclassname |          | Description                    |
|------------|----------|--------------------------------|
|            | `cons`   | intercepts and cutpoints       |
|            | `coef`   | fixed coefficients             |
|            | `errvar` | covariances of errors          |
|            | `scale`  | scaling parameters             |
|            | `all`    | all the above                  |
|            | `none`   | none of the above; the default |
