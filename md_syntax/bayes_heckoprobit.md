## Syntax

`bayes` \[`, bayesopts`\] `: heckoprobit`
[depvar](http://www.stata.com/help.cgi?depvar)
[indepvars](http://www.stata.com/help.cgi?indepvars)
_\[`if`\] \[`in`\]_ \[`weight`\]`,`
`select(`\[`depvar_s =`\] `varlist_s` \[`, noconstant`
`offset(varname_o)`\]`)` \[`options`\]

| Options                                                                                                                                                                                                                                                          |                   | Description                                                                                                        |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|--------------------------------------------------------------------------------------------------------------------|
| Model                                                                                                                                                                                                                                                            |                   |                                                                                                                    |
| \*                                                                                                                                                                                                                                                               | `select()`        | specify selection equation: dependent and independent variables; whether to have constant term and offset variable |
|                                                                                                                                                                                                                                                                  | `offset(varname)` | include `varname` in model with coefficient constrained to 1                                                       |
|                                                                                                                                                                                                                                                                  | `collinear`       | keep collinear variables                                                                                           |
| Reporting                                                                                                                                                                                                                                                        |                   |                                                                                                                    |
|                                                                                                                                                                                                                                                                  | `display_options` | control spacing, line width, and base and empty cells                                                              |
|                                                                                                                                                                                                                                                                  | `level(#)`        | set credible level; default is `level(95)`                                                                         |
| \* `select()` is required. The full specification is                                                                                                                                                                                                             |                   |                                                                                                                    |
| `select(`\[`depvar_s =`\] `varlist_s` \[`, noconstant offset(varname_o)`\]`)`                                                                                                                                                                            |                   |                                                                                                                    |
| `indepvars` and `varlist_s` may contain factor variables; see [<strong>fvvarlist</strong>](http://www.stata.com/help.cgi?fvvarlist).                                                                                                  |                   |                                                                                                                    |
| `depvar`, `indepvars`, `varlist_s`, and `depvar_s` may contain time-series operators; see [<strong>tsvarlist</strong>](http://www.stata.com/help.cgi?tsvarlist).                                                                      |                   |                                                                                                                    |
| `fweight`s are allowed; see [<strong>weight</strong>](http://www.stata.com/help.cgi?weight).                                                                                                                                          |                   |                                                                                                                    |
| `bayes: heckoprobit, level()` is equivalent to `bayes, clevel(): heckoprobit`.                                                                                                                                                                           |                   |                                                                                                                    |
| For a detailed description of `options`, see [<var class="command">Options</var><strong></strong>](heckoprobit##options) in [<strong>[R]</strong> heckoprobit](http://www.stata.com/help.cgi?heckoprobit). |                   |                                                                                                                    |

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

|                                                                                                                                                                                                                                                                                                                                                                                             |     |     |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|-----|
| \* Starred options are specific to the `bayes` prefix; other options are common between `bayes` and [<strong>bayesmh</strong>](http://www.stata.com/help.cgi?bayesmh).                                                                                                                                                                                           |     |     |
| Options `prior()` and `block()` can be repeated.                                                                                                                                                                                                                                                                                                                                            |     |     |
| [<var class="command">priorspec</var><strong></strong>](bayesmh##priorspec) and [<var class="command">paramref</var><strong></strong>](bayesmh##paramref) are defined in [<strong>[BAYES]</strong> bayesmh](http://www.stata.com/help.cgi?bayesmh).                                                        |     |     |
| `paramref` may contain factor variables; see [<strong>fvvarlist</strong>](http://www.stata.com/help.cgi?fvvarlist).                                                                                                                                                                                                                                              |     |     |
| See [<strong>[BAYES]</strong> bayesian postestimation](http://www.stata.com/help.cgi?bayesian_postestimation) for features available after estimation.                                                                                                                                                                                                           |     |     |
| Model parameters are regression coefficients `{c -(}depvar:indepvars{c )-}` for the main regression and `{c -(}select:varlist_s{c )-}` for the selection equation, atanh-transformed correlation `{c -(}athrho{c )-}`, and cutpoints `{c -(}cut1{c )-}`, `{c -(}cut2{c )-}`, and so on. Use the `dryrun` option to see the definitions of model parameters prior to estimation. |     |     |
| Flat priors, `flat`, are used by default for cutpoints.                                                                                                                                                                                                                                                                                                                                     |     |     |
| For a detailed description of `bayesopts`, see [<var class="command">Options</var><strong></strong>](bayes##options) in [<strong>[BAYES]</strong> bayes](http://www.stata.com/help.cgi?bayes).                                                                                                                                        |     |     |
