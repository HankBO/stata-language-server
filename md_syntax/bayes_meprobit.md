## Syntax

`bayes` \[`, bayesopts`\] `: meprobit`
[depvar](http://www.stata.com/help.cgi?depvar)
`fe_equation` \[`|| re_equation`\] \[`|| re_equation` ...\] \[`,`
`options`\]

where the syntax of `fe_equation` is

\[[indepvars](http://www.stata.com/help.cgi?indepvars)\]
_\[`if`\] \[`in`\]_ \[`weight`\] \[`,`
`fe_options`\]

and the syntax of `re_equation` is one of the following:

for random coefficients and intercepts

`levelvar:`
\[[varlist](http://www.stata.com/help.cgi?varlist)\]
\[`, re_options`\]

for a random effect among the values of a factor variable

`levelvar:`
`R.`[varname](http://www.stata.com/help.cgi?varname)

`levelvar` either is a variable identifying the group structure for the
random effects at that level or is `_all`, representing one group
comprising all observations.

| fe\_options |                   | Description                                                                                                                                    |
|-------------|-------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| Model       |                   |                                                                                                                                                |
|             | `noconstant`      | suppress constant term from the [<strong>fixed-effects</strong>](bayes_glossary##fixed_effects_parameters) equation |
|             | `offset(varname)` | include `varname` in model with coefficient constrained to 1                                                                                   |
|             | `asis`            | retain perfect predictor variables                                                                                                             |

| re\_options |                       | Description                                                                                                                                                                                                           |
|-------------|-----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Model       |                       |                                                                                                                                                                                                                       |
|             | `covariance(vartype)` | variance-covariance structure of the [<strong>random effects</strong>](bayes_glossary##random_effects_parameters); only structures `independent`, `identity`, and `unstructured` supported |
|             | `noconstant`          | suppress constant term from the random-effects equation                                                                                                                                                               |

| options                                                                                                                                                                                                                                                  |                                | Description                                           |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------|-------------------------------------------------------|
| Model                                                                                                                                                                                                                                                    |                                |                                                       |
|                                                                                                                                                                                                                                                          | `binomial(varname`\|`#)` | set binomial trials if data are in binomial form      |
|                                                                                                                                                                                                                                                          | `collinear`                    | keep collinear variables                              |
| Reporting                                                                                                                                                                                                                                                |                                |                                                       |
|                                                                                                                                                                                                                                                          | `notable`                      | suppress coefficient table                            |
|                                                                                                                                                                                                                                                          | `noheader`                     | suppress output header                                |
|                                                                                                                                                                                                                                                          | `nogroup`                      | suppress table summarizing groups                     |
|                                                                                                                                                                                                                                                          | ` display_options`             | control spacing, line width, and base and empty cells |
|                                                                                                                                                                                                                                                          | `level(#)`                     | set credible level; default is `level(95)`            |
| `indepvars` may contain factor variables; see [<strong>fvvarlist</strong>](http://www.stata.com/help.cgi?fvvarlist).                                                                                                          |                                |                                                       |
| `depvar`, `indepvars`, and `varlist` may contain time-series operators; see [<strong>tsvarlist</strong>](http://www.stata.com/help.cgi?tsvarlist).                                                                            |                                |                                                       |
| `fweight`s are allowed; see [<strong>weight</strong>](http://www.stata.com/help.cgi?weight).                                                                                                                                  |                                |                                                       |
| `bayes: meprobit, level()` is equivalent to `bayes, clevel(): meprobit`.                                                                                                                                                                         |                                |                                                       |
| For a detailed description of `options`, see [<var class="command">Options</var><strong></strong>](meprobit##options) in [<strong>[ME]</strong> meprobit](http://www.stata.com/help.cgi?meprobit). |                                |                                                       |

| bayesopts                                                                   |                                                                                                                               | Description                                                                                                                          |
|-----------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| [<strong>Priors</strong>](bayes##priors_options) |                                                                                                                               |                                                                                                                                      |
| \*                                                                          | `normalprior(#)`                                                                                                              | specify standard deviation of default normal priors for regression coefficients; default is `normalprior(100)`                       |
| \*                                                                          | `igammaprior(# #)`                                                                                                            | specify shape and scale of default inverse-gamma prior for variance components; default is `igammaprior(0.01 0.01)`                  |
| \*                                                                          | `iwishartprior(`[<var class="command">#</var> [...]<strong></strong>](bayes##iwishartpriorspec)`)` | specify degrees of freedom and, optionally, scale matrix of default inverse-Wishart prior for unstructured random-effects covariance |
|                                                                             | `prior(priorspec)`                                                                                                            | prior for model parameters; this option may be repeated                                                                              |
|                                                                             | `dryrun`                                                                                                                      | show model summary without estimation                                                                                                |

|                                                                                     |                                |                                                                     |
|-------------------------------------------------------------------------------------|--------------------------------|---------------------------------------------------------------------|
| [<strong>Simulation</strong>](bayes##simulation_options) |                                |                                                                     |
|                                                                                     | `mcmcsize(#)`                  | MCMC sample size; default is `mcmcsize(10000)`                      |
|                                                                                     | `burnin(#)`                    | burn-in period; default is `burnin(2500)`                           |
|                                                                                     | `thinning(#)`                  | thinning interval; default is `thinning(1)`                         |
|                                                                                     | `rseed(#)`                     | random-number seed                                                  |
|                                                                                     | `exclude(paramref)`            | specify model parameters to be excluded from the simulation results |
|                                                                                     | `restubs(restub1 restub2 ...)` | specify stubs for random-effects parameters for all levels          |

|                                                                                 |                                                                                                                                                                                                                               |                                                                  |
|---------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------|
| [<strong>Blocking</strong>](bayes##blocking_options) |                                                                                                                                                                                                                               |                                                                  |
| \*                                                                              | `blocksize(#)`                                                                                                                                                                                                                | maximum block size; default is `blocksize(50)`                   |
|                                                                                 | `block(`[<var class="command">paramref</var><strong></strong>](bayesmh##paramref)\[`,` [<var class="command">blockopts</var><strong></strong>](bayesmh##blockopts)\]`)` | specify a block of model parameters; this option may be repeated |
|                                                                                 | `blocksummary`                                                                                                                                                                                                                | display block summary                                            |
| \*                                                                              | `noblocking`                                                                                                                                                                                                                  | do not block parameters by default                               |

|                                                                                             |                     |                                                                     |
|---------------------------------------------------------------------------------------------|---------------------|---------------------------------------------------------------------|
| [<strong>Initialization</strong>](bayes##initialization_options) |                     |                                                                     |
|                                                                                             | `initial(initspec)` | initial values for model parameters                                 |
|                                                                                             | `nomleinitial`      | suppress the use of maximum likelihood estimates as starting values |
|                                                                                             | `initrandom`        | specify random initial values                                       |
|                                                                                             | `initsummary`       | display initial values used for simulation                          |
| \*                                                                                          | `noisily`           | display output from the estimation command during initialization    |

|                                                                                     |                         |                                                               |
|-------------------------------------------------------------------------------------|-------------------------|---------------------------------------------------------------|
| [<strong>Adaptation</strong>](bayes##adaptation_options) |                         |                                                               |
|                                                                                     | `adaptation(adaptopts)` | control the adaptive MCMC procedure                           |
|                                                                                     | `scale(#)`              | initial multiplier for scale factor; default is `scale(2.38)` |
|                                                                                     | `covariance(cov)`       | initial proposal covariance; default is the identity matrix   |

[<strong>Reporting</strong>](bayes##reporting_options)

INCLUDE help bayes\_clevel\_hpd\_short

|     |                                                                                                                                                      |                                                                                                                    |
|-----|------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|
|     | `remargl`                                                                                                                                            | compute log marginal likelihood                                                                                    |
|     | `batch(#)`                                                                                                                                           | specify length of block for batch-means calculations; default is `batch(0)`                                        |
|     | `saving(`[<var class="command">filename</var><strong></strong>](http://www.stata.com/help.cgi?filename)\[`, replace`\]`)` | save simulation results to `filename.dta`                                                                        |
|     | `nomodelsummary`                                                                                                                                     | suppress model summary                                                                                             |
|     | `nomesummary`                                                                                                                                        | suppress multilevel-structure summary                                                                              |
|     | \[`no`\]`dots`                                                                                                                                       | suppress dots or display dots every 100 iterations and iteration numbers every 1,000 iterations; default is `dots` |
|     | `dots(#`\[`, every(#)`\]`)`                                                                                                                      | display dots as simulation is performed                                                                            |
|     | \[`no`\]`show(paramref)`                                                                                                                             | specify model parameters to be excluded from or included in the output                                             |
|     | `showreffects`\[`(reref)`\]                                                                                                                      | specify that all or a subset of random-effects parameters be included in the output                                |
|     | `melabel`                                                                                                                                            | display estimation table using the same row labels as `meprobit`                                                   |
|     | `nogroup`                                                                                                                                            | suppress table summarizing groups                                                                                  |
|     | `notable`                                                                                                                                            | suppress estimation table                                                                                          |
|     | `noheader`                                                                                                                                           | suppress output header                                                                                             |
|     | `title(string)`                                                                                                                                      | display `string` as title above the table of parameter estimates                                                   |
|     | [<var class="command">display_options</var><strong></strong>](bayesmh##display_options)                                   | control spacing, line width, and base and empty cells                                                              |

[<strong>Advanced</strong>](bayes##advanced_options)

`search(search_options)`

control the search for feasible initial values

INCLUDE help bayesmh\_corropts

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |     |     |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|-----|
| \* Starred options are specific to the `bayes` prefix; other options are common between `bayes` and [<strong>bayesmh</strong>](http://www.stata.com/help.cgi?bayesmh).                                                                                                                                                                                                                                                                                                                                                                                                                           |     |     |
| Options `prior()` and `block()` can be repeated.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |     |     |
| [<var class="command">priorspec</var><strong></strong>](bayesmh##priorspec) and [<var class="command">paramref</var><strong></strong>](bayesmh##paramref) are defined in [<strong>[BAYES]</strong> bayesmh](http://www.stata.com/help.cgi?bayesmh).                                                                                                                                                                                                                                                                                        |     |     |
| `paramref` may contain factor variables; see [<strong>fvvarlist</strong>](http://www.stata.com/help.cgi?fvvarlist).                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |     |     |
| See [<strong>[BAYES]</strong> bayesian postestimation](http://www.stata.com/help.cgi?bayesian_postestimation) for features available after estimation.                                                                                                                                                                                                                                                                                                                                                                                                                                           |     |     |
| Model parameters are regression coefficients `{c -(}depvar:indepvars{c )-}`, random effects `{c -(}rename{c )-}`, and either variance components `{c -(}rename:sigma2{c )-}` or, if option `covariance(unstructured)` is specified, matrix parameter `{c -(}restub:Sigma,matrix{c )-}`; see [BAYES bayesRemarksandexamplesLikelihoodmodel`Likelihood model`](http://www.stata.com/manuals14/bayesbayesremarksandexampleslikelihoodmodel.pdf) in **\[BAYES\] bayes** for how `rename`s and `restub` are defined. Use the `dryrun` option to see the definitions of model parameters prior to estimation. |     |     |
| For a detailed description of `bayesopts`, see [<var class="command">Options</var><strong></strong>](bayes##options) in [<strong>[BAYES]</strong> bayes](http://www.stata.com/help.cgi?bayes).                                                                                                                                                                                                                                                                                                                                                                        |     |     |
