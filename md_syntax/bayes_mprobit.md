## Syntax

`bayes` \[`, bayesopts`\] `: mprobit`
[depvar](http://www.stata.com/help.cgi?depvar)
\[[indepvars](http://www.stata.com/help.cgi?indepvars)\]
_\[`if`\] \[`in`\]_ \[`weight`\] \[`,`
`options`\]

| Options                                                                                                                                                                                                                                              |                   | Description                                                                                                      |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|------------------------------------------------------------------------------------------------------------------|
| Model                                                                                                                                                                                                                                                |                   |                                                                                                                  |
|                                                                                                                                                                                                                                                      | `noconstant`      | suppress constant term                                                                                           |
|                                                                                                                                                                                                                                                      | `baseoutcome(#)`  | value of [depvar](http://www.stata.com/help.cgi?depvar) that will be the base outcome |
|                                                                                                                                                                                                                                                      | `probitparam`     | use the probit variance parameterization                                                                         |
|                                                                                                                                                                                                                                                      | `collinear`       | keep collinear variables                                                                                         |
| Reporting                                                                                                                                                                                                                                            |                   |                                                                                                                  |
|                                                                                                                                                                                                                                                      | `display_options` | control spacing, line width, and base and empty cells                                                            |
|                                                                                                                                                                                                                                                      | `level(#)`        | set credible level; default is `level(95)`                                                                       |
| `indepvars` may contain factor variables; see [<strong>fvvarlist</strong>](http://www.stata.com/help.cgi?fvvarlist).                                                                                                      |                   |                                                                                                                  |
| `fweight`s are allowed; see [<strong>weight</strong>](http://www.stata.com/help.cgi?weight).                                                                                                                              |                   |                                                                                                                  |
| `bayes: mprobit, level()` is equivalent to `bayes, clevel(): mprobit`.                                                                                                                                                                       |                   |                                                                                                                  |
| For a detailed description of `options`, see [<var class="command">Options</var><strong></strong>](mprobit##options) in [<strong>[R]</strong> mprobit](http://www.stata.com/help.cgi?mprobit). |                   |                                                                                                                  |

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

|                                                                                                                                                                                                                                                                                                                                                              |     |     |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|-----|
| \* Starred options are specific to the `bayes` prefix; other options are common between `bayes` and [<strong>bayesmh</strong>](http://www.stata.com/help.cgi?bayesmh).                                                                                                                                                            |     |     |
| Options `prior()` and `block()` can be repeated.                                                                                                                                                                                                                                                                                                             |     |     |
| [<var class="command">priorspec</var><strong></strong>](bayesmh##priorspec) and [<var class="command">paramref</var><strong></strong>](bayesmh##paramref) are defined in [<strong>[BAYES]</strong> bayesmh](http://www.stata.com/help.cgi?bayesmh).                         |     |     |
| `paramref` may contain factor variables; see [<strong>fvvarlist</strong>](http://www.stata.com/help.cgi?fvvarlist).                                                                                                                                                                                                               |     |     |
| See [<strong>[BAYES]</strong> bayesian postestimation](http://www.stata.com/help.cgi?bayesian_postestimation) for features available after estimation.                                                                                                                                                                            |     |     |
| Model parameters are regression coefficients `{c -(}outcome1:indepvars{c )-}`, `{c -(}outcome2:indepvars{c )-}`, and so on, where `outcome#`'s are the values of the dependent variable or the value labels of the dependent variable if they exist. Use the `dryrun` option to see the definitions of model parameters prior to estimation. |     |     |
| For a detailed description of `bayesopts`, see [<var class="command">Options</var><strong></strong>](bayes##options) in [<strong>[BAYES]</strong> bayes](http://www.stata.com/help.cgi?bayes).                                                                                                         |     |     |
