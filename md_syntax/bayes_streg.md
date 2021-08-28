## Syntax

`bayes` \[`, bayesopts`\] `: streg`
\[[varlist](http://www.stata.com/help.cgi?varlist)\]
_\[`if`\] \[`in`\]_ \[`, options`\]

| Options                                                                                                                                                                                                                                         |                               | Description                                                  |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------|--------------------------------------------------------------|
| Model                                                                                                                                                                                                                                           |                               |                                                              |
|                                                                                                                                                                                                                                                 | `noconstant`                  | suppress constant term                                       |
|                                                                                                                                                                                                                                                 | `distribution(exponential)` | exponential survival distribution                            |
|                                                                                                                                                                                                                                                 | `distribution(gompertz)`    | Gompertz survival distribution                               |
|                                                                                                                                                                                                                                                 | `distribution(loglogistic)` | loglogistic survival distribution                            |
|                                                                                                                                                                                                                                                 | `distribution(llogistic)`   | synonym for `distribution(loglogistic)`                      |
|                                                                                                                                                                                                                                                 | `distribution(weibull)`     | Weibull survival distribution                                |
|                                                                                                                                                                                                                                                 | `distribution(lognormal)`   | lognormal survival distribution                              |
|                                                                                                                                                                                                                                                 | `distribution(lnormal)`     | synonym for `distribution(lognormal)`                        |
|                                                                                                                                                                                                                                                 | `distribution(ggamma)`      | generalized gamma survival distribution                      |
|                                                                                                                                                                                                                                                 | `frailty(gamma)`            | gamma frailty distribution                                   |
|                                                                                                                                                                                                                                                 | `frailty(invgaussian)`      | inverse-Gaussian distribution                                |
|                                                                                                                                                                                                                                                 | `time`                        | use accelerated failure-time metric                          |
| Model 2                                                                                                                                                                                                                                         |                               |                                                              |
|                                                                                                                                                                                                                                                 | `strata(varname)`             | strata ID variable                                           |
|                                                                                                                                                                                                                                                 | `offset(varname)`             | include `varname` in model with coefficient constrained to 1 |
|                                                                                                                                                                                                                                                 | `shared(varname)`             | shared frailty ID variable                                   |
|                                                                                                                                                                                                                                                 | `ancillary(varlist)`          | use `varlist` to model the first ancillary parameter         |
|                                                                                                                                                                                                                                                 | `anc2(varlist)`               | use `varlist` to model the second ancillary parameter        |
|                                                                                                                                                                                                                                                 | `collinear`                   | keep collinear variables                                     |
| Reporting                                                                                                                                                                                                                                       |                               |                                                              |
|                                                                                                                                                                                                                                                 | `nohr`                        | do not report hazard ratios                                  |
|                                                                                                                                                                                                                                                 | `tratio`                      | report time ratios                                           |
|                                                                                                                                                                                                                                                 | `noshow`                      | do not show st setting information                           |
|                                                                                                                                                                                                                                                 | `display_options`             | control spacing, line width, and base and empty cells        |
|                                                                                                                                                                                                                                                 | `level(#)`                    | set credible level; default is `level(95)`                   |
| You must `stset` your data before using `bayes: streg`; see [<strong>[ST]</strong> stset](http://www.stata.com/help.cgi?stset).                                                                                      |                               |                                                              |
| `varlist` may contain factor variables; see [<strong>fvvarlist</strong>](http://www.stata.com/help.cgi?fvvarlist).                                                                                                   |                               |                                                              |
| `bayes: streg, level()` is equivalent to `bayes, clevel(): streg`.                                                                                                                                                                      |                               |                                                              |
| For a detailed description of `options`, see [<var class="command">Options</var><strong></strong>](streg##options) in [<strong>[ST]</strong> streg](http://www.stata.com/help.cgi?streg). |                               |                                                              |

| bayesopts                                                                   |                    | Description                                                                                                                                 |
|-----------------------------------------------------------------------------|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| [<strong>Priors</strong>](bayes##priors_options) |                    |                                                                                                                                             |
| \*                                                                          | `normalprior(#)`   | specify standard deviation of default normal priors for regression coefficients and log-ancillary parameters; default is `normalprior(100)` |
|                                                                             | `prior(priorspec)` | prior for model parameters; this option may be repeated                                                                                     |
|                                                                             | `dryrun`           | show model summary without estimation                                                                                                       |

|                                                                                     |                     |                                                                     |
|-------------------------------------------------------------------------------------|---------------------|---------------------------------------------------------------------|
| [<strong>Simulation</strong>](bayes##simulation_options) |                     |                                                                     |
|                                                                                     | `mcmcsize(#)`       | MCMC sample size; default is `mcmcsize(10000)`                      |
|                                                                                     | `burnin(#)`         | burn-in period; default is `burnin(2500)`                           |
|                                                                                     | `thinning(#)`       | thinning interval; default is `thinning(1)`                         |
|                                                                                     | `rseed(#)`          | random-number seed                                                  |
|                                                                                     | `exclude(paramref)` | specify model parameters to be excluded from the simulation results |

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

`clevel(#)`

set credible interval level; default is `clevel(95)`

`hpd`

display HPD credible intervals instead of the default equal-tailed
credible intervals

\*

`nohr`

do not report hazard ratios

\*

`tratio`

report time ratios; requires option `time` with `streg`

`batch(#)`

specify length of block for batch-means calculations; default is
`batch(0)`

`saving(`[<var class="command">filename</var><strong></strong>](http://www.stata.com/help.cgi?filename)\[`, replace`\]`)`

save simulation results to `filename.dta`

`nomodelsummary`

suppress model summary

`dots`

display dots every 100 iterations and iteration numbers every 1,000
iterations

`dots(#`\[`, every(#)`\]`)`

display dots as simulation is performed

\[`no`\]`show(paramref)`

specify model parameters to be excluded from or included in the output

`notable`

suppress estimation table

`noheader`

suppress output header

`title(string)`

display `string` as title above the table of parameter estimates

[<var class="command">display_options</var><strong></strong>](bayesmh##display_options)

control spacing, line width, and base and empty cells

INCLUDE help bayesmh\_eform

[<strong>Advanced</strong>](bayes##advanced_options)

`search(search_options)`

control the search for feasible initial values

INCLUDE help bayesmh\_corropts

|                                                                                                                                                                                                                                                                                                                                                                                                                                            |     |     |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|-----|
| \* Starred options are specific to the `bayes` prefix; other options are common between `bayes` and [<strong>bayesmh</strong>](http://www.stata.com/help.cgi?bayesmh).                                                                                                                                                                                                                                          |     |     |
| Options `prior()` and `block()` can be repeated.                                                                                                                                                                                                                                                                                                                                                                                           |     |     |
| [<var class="command">priorspec</var><strong></strong>](bayesmh##priorspec) and [<var class="command">paramref</var><strong></strong>](bayesmh##paramref) are defined in [<strong>[BAYES]</strong> bayesmh](http://www.stata.com/help.cgi?bayesmh).                                                                                                       |     |     |
| `paramref` may contain factor variables; see [<strong>fvvarlist</strong>](http://www.stata.com/help.cgi?fvvarlist).                                                                                                                                                                                                                                                                                             |     |     |
| See [<strong>[BAYES]</strong> bayesian postestimation](http://www.stata.com/help.cgi?bayesian_postestimation) for features available after estimation.                                                                                                                                                                                                                                                          |     |     |
| Model parameters are regression coefficients `{c -(}depvar:indepvars{c )-}` and ancillary parameters as described in [BAYES bayesstregRemarksandexamplesAncillarymodelparameters`Ancillary model parameters`](http://www.stata.com/manuals14/bayesbayesstregremarksandexamplesancillarymodelparameters.pdf) in **\[BAYES\] bayes: streg**. Use the `dryrun` option to see the definitions of model parameters prior to estimation. |     |     |
| For a detailed description of `bayesopts`, see [<var class="command">Options</var><strong></strong>](bayes##options) in [<strong>[BAYES]</strong> bayes](http://www.stata.com/help.cgi?bayes).                                                                                                                                                                                       |     |     |
