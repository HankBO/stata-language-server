## Syntax

`bayes` \[`, bayesopts`\] `: glm`
[depvar](http://www.stata.com/help.cgi?depvar)
\[[indepvars](http://www.stata.com/help.cgi?indepvars)\]
_\[`if`\] \[`in`\]_ \[`weight`\] \[`,`
`options`\]

| Options                                                                                                                                                                                                                                  |                      | Description                                                                                                                     |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------|---------------------------------------------------------------------------------------------------------------------------------|
| Model                                                                                                                                                                                                                                    |                      |                                                                                                                                 |
|                                                                                                                                                                                                                                          | `family(familyname)` | distribution of [depvar](http://www.stata.com/help.cgi?depvar); default is `family(gaussian)`        |
|                                                                                                                                                                                                                                          | `link(linkname)`     | link function; default is canonical link for `family()` specified                                                               |
| Model 2                                                                                                                                                                                                                                  |                      |                                                                                                                                 |
|                                                                                                                                                                                                                                          | `noconstant`         | suppress constant term                                                                                                          |
|                                                                                                                                                                                                                                          | `exposure(varname)`  | include ln(`varname`) in model with coefficient constrained to 1                                                                |
|                                                                                                                                                                                                                                          | `offset(varname)`    | include `varname` in model with coefficient constrained to 1                                                                    |
|                                                                                                                                                                                                                                          | `collinear`          | keep collinear variables                                                                                                        |
|                                                                                                                                                                                                                                          | `asis`               | retain perfect predictor variables                                                                                              |
|                                                                                                                                                                                                                                          | `mu(varname)`        | use `varname` as the initial estimate for the mean of [depvar](http://www.stata.com/help.cgi?depvar) |
|                                                                                                                                                                                                                                          | `init(varname)`      | synonym for `mu(varname)`                                                                                                       |
| Reporting                                                                                                                                                                                                                                |                      |                                                                                                                                 |
|                                                                                                                                                                                                                                          | `eform`              | report exponentiated coefficients                                                                                               |
|                                                                                                                                                                                                                                          | `display_options`    | control spacing, line width, and base and empty cells                                                                           |
|                                                                                                                                                                                                                                          | `level(#)`           | set credible level; default is `level(95)`                                                                                      |
| `indepvars` may contain factor variables; see [<strong>fvvarlist</strong>](http://www.stata.com/help.cgi?fvvarlist).                                                                                          |                      |                                                                                                                                 |
| `depvar` and `indepvars` may contain time-series operators; see [<strong>tsvarlist</strong>](http://www.stata.com/help.cgi?tsvarlist).                                                                        |                      |                                                                                                                                 |
| `fweight`s are allowed; see [<strong>weight</strong>](http://www.stata.com/help.cgi?weight).                                                                                                                  |                      |                                                                                                                                 |
| `bayes: glm, level()` is equivalent to `bayes, clevel(): glm`.                                                                                                                                                                   |                      |                                                                                                                                 |
| For a detailed description of `options`, see [<var class="command">Options</var><strong></strong>](glm##options) in [<strong>[R]</strong> glm](http://www.stata.com/help.cgi?glm). |                      |                                                                                                                                 |

bayesopts

Description

[<strong>Priors</strong>](bayes##priors_options)

\*

`normalprior(#)`

specify standard deviation of default normal priors for regression
coefficients; default is `normalprior(100)`

INCLUDE help bayesmh\_prioropts

[<strong>Simulation</strong>](bayes##simulation_options)

INCLUDE help bayesmh\_simopts

[<strong>Blocking</strong>](bayes##blocking_options)

\*

`blocksize(#)`

maximum block size; default is `blocksize(50)`

INCLUDE help bayesmh\_blockopts

|     |              |                                    |
|-----|--------------|------------------------------------|
| \*  | `noblocking` | do not block parameters by default |

[<strong>Initialization</strong>](bayes##initialization_options)

INCLUDE help bayesmh\_initopts

|     |           |                                                                  |
|-----|-----------|------------------------------------------------------------------|
| \*  | `noisily` | display output from the estimation command during initialization |

[<strong>Adaptation</strong>](bayes##adaptation_options)

INCLUDE help bayesmh\_adaptopts

[<strong>Reporting</strong>](bayes##reporting_options)

INCLUDE help bayesecmd\_reportopts

[<strong>Advanced</strong>](bayes##advanced_options)

INCLUDE help bayesmh\_advancedopts

|                                                                                                                                                                                                                                                                                                                                      |     |     |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|-----|
| \* Starred options are specific to the `bayes` prefix; other options are common between `bayes` and [<strong>bayesmh</strong>](http://www.stata.com/help.cgi?bayesmh).                                                                                                                                    |     |     |
| Options `prior()` and `block()` can be repeated.                                                                                                                                                                                                                                                                                     |     |     |
| [<var class="command">priorspec</var><strong></strong>](bayesmh##priorspec) and [<var class="command">paramref</var><strong></strong>](bayesmh##paramref) are defined in [<strong>[BAYES]</strong> bayesmh](http://www.stata.com/help.cgi?bayesmh). |     |     |
| `paramref` may contain factor variables; see [<strong>fvvarlist</strong>](http://www.stata.com/help.cgi?fvvarlist).                                                                                                                                                                                       |     |     |
| See [<strong>[BAYES]</strong> bayesian postestimation](http://www.stata.com/help.cgi?bayesian_postestimation) for features available after estimation.                                                                                                                                                    |     |     |
| Model parameters are regression coefficients `{c -(}depvar:indepvars{c )-}`. Use the `dryrun` option to see the definitions of model parameters prior to estimation.                                                                                                                                                         |     |     |
| For a detailed description of `bayesopts`, see [<var class="command">Options</var><strong></strong>](bayes##options) in [<strong>[BAYES]</strong> bayes](http://www.stata.com/help.cgi?bayes).                                                                                 |     |     |
