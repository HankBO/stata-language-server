## Syntax

`bayes` \[`,`
[<var class="command">bayesopts</var><strong></strong>](#bayesopts)\]
`: estimation_command` \[`, estopts`\]

<span options="estimation_command">{marker
estimation\_command}_{nobreak None} `estimation_command` is a
likelihood-based estimation command, and `estopts` are command-specific
estimation options; see
[<strong>[BAYES]</strong> bayesian estimation](http://www.stata.com/help.cgi?bayesian_estimation)
for a list of supported commands, and see the command-specific entries
for the supported estimation options, `estopts`.

| bayesopts                                                             |                                                                                                                         | Description                                                                                                                                     |
|-----------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| [<strong>Priors</strong>](#priors_options) |                                                                                                                         |                                                                                                                                                 |
| \*                                                                    | `gibbs`                                                                                                                 | specify Gibbs sampling; available only with the `regress` or `mvreg` for certain prior combinations                                             |
| \*                                                                    | `normalprior(#)`                                                                                                        | specify standard deviation of default normal priors for regression coefficients and other real scalar parameters; default is `normalprior(100)` |
| \*                                                                    | `igammaprior(# #)`                                                                                                      | specify shape and scale of default inverse-gamma prior for variances; default is `igammaprior(0.01 0.01)`                                       |
| \*                                                                    | `iwishartprior(`[<var class="command">#</var> [...]<strong></strong>](#iwishartpriorspec)`)` | specify degrees of freedom and, optionally, scale matrix of default inverse-Wishart prior for unstructured random-effects covariance            |
|                                                                       | `prior(priorspec)`                                                                                                      | prior for model parameters; this option may be repeated                                                                                         |
|                                                                       | `dryrun`                                                                                                                | show model summary without estimation                                                                                                           |

|                                                                               |                                |                                                                                                 |
|-------------------------------------------------------------------------------|--------------------------------|-------------------------------------------------------------------------------------------------|
| [<strong>Simulation</strong>](#simulation_options) |                                |                                                                                                 |
|                                                                               | `mcmcsize(#)`                  | MCMC sample size; default is `mcmcsize(10000)`                                                  |
|                                                                               | `burnin(#)`                    | burn-in period; default is `burnin(2500)`                                                       |
|                                                                               | `thinning(#)`                  | thinning interval; default is `thinning(1)`                                                     |
|                                                                               | `rseed(#)`                     | random-number seed                                                                              |
|                                                                               | `exclude(paramref)`            | specify model parameters to be excluded from the simulation results                             |
|                                                                               | `restubs(restub1 restub2 ...)` | specify stubs for random-effects parameters for all levels; allowed only with multilevel models |

|                                                                           |                                                                                                                                                                                                                       |                                                                  |
|---------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------|
| [<strong>Blocking</strong>](#blocking_options) |                                                                                                                                                                                                                       |                                                                  |
| \*                                                                        | `blocksize(#)`                                                                                                                                                                                                        | maximum block size; default is `blocksize(50)`                   |
|                                                                           | `block(`[<var class="command">paramref</var><strong></strong>](bayesmh##paramref)\[`,` [<var class="command">blockopts</var><strong></strong>](#blockopts)\]`)` | specify a block of model parameters; this option may be repeated |
|                                                                           | `blocksummary`                                                                                                                                                                                                        | display block summary                                            |
| \*                                                                        | `noblocking`                                                                                                                                                                                                          | do not block parameters by default                               |

|                                                                                       |                     |                                                                     |
|---------------------------------------------------------------------------------------|---------------------|---------------------------------------------------------------------|
| [<strong>Initialization</strong>](#initialization_options) |                     |                                                                     |
|                                                                                       | `initial(initspec)` | initial values for model parameters                                 |
|                                                                                       | `nomleinitial`      | suppress the use of maximum likelihood estimates as starting values |
|                                                                                       | `initrandom`        | specify random initial values                                       |
|                                                                                       | `initsummary`       | display initial values used for simulation                          |
| \*                                                                                    | `noisily`           | display output from the estimation command during initialization    |

|                                                                               |                         |                                                               |
|-------------------------------------------------------------------------------|-------------------------|---------------------------------------------------------------|
| [<strong>Adaptation</strong>](#adaptation_options) |                         |                                                               |
|                                                                               | `adaptation(adaptopts)` | control the adaptive MCMC procedure                           |
|                                                                               | `scale(#)`              | initial multiplier for scale factor; default is `scale(2.38)` |
|                                                                               | `covariance(cov)`       | initial proposal covariance; default is the identity matrix   |

|                                                                             |                                                                                                                                                      |                                                                                                                              |
|-----------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|
| [<strong>Reporting</strong>](#reporting_options) |                                                                                                                                                      |                                                                                                                              |
|                                                                             | `clevel(#)`                                                                                                                                          | set credible interval level; default is `clevel(95)`                                                                         |
|                                                                             | `hpd`                                                                                                                                                | display HPD credible intervals instead of the default equal-tailed credible intervals                                        |
|                                                                             | [<var class="command">eform_option</var><strong></strong>](http://www.stata.com/help.cgi?eform_option)                    | display coefficient table in exponentiated form                                                                              |
|                                                                             | `remargl`                                                                                                                                            | compute log marginal likelihood                                                                                              |
|                                                                             | `batch(#)`                                                                                                                                           | specify length of block for batch-means calculations; default is `batch(0)`                                                  |
|                                                                             | `saving(`[<var class="command">filename</var><strong></strong>](http://www.stata.com/help.cgi?filename)\[`, replace`\]`)` | save simulation results to `filename.dta`                                                                                  |
|                                                                             | `nomodelsummary`                                                                                                                                     | suppress model summary                                                                                                       |
|                                                                             | `nomesummary`                                                                                                                                        | suppress multilevel-structure summary; allowed only with multilevel models                                                   |
|                                                                             | \[`no`\]`dots`                                                                                                                                       | suppress dots or display dots every 100 iterations and iteration numbers every 1,000 iterations; default is command-specific |
|                                                                             | `dots(#`\[`, every(#)`\]`)`                                                                                                                      | display dots as simulation is performed                                                                                      |
|                                                                             | \[`no`\]`show(paramref)`                                                                                                                             | specify model parameters to be excluded from or included in the output                                                       |
|                                                                             | `showreffects`\[`(reref)`\]                                                                                                                      | specify that all or a subset of random-effects parameters be included in the output; allowed only with multilevel commands   |
|                                                                             | `melabel`                                                                                                                                            | display estimation table using the same row labels as `estimation_command`; allowed only with multilevel commands            |
|                                                                             | `nogroup`                                                                                                                                            | suppress table summarizing groups; allowed only with multilevel models                                                       |
|                                                                             | `notable`                                                                                                                                            | suppress estimation table                                                                                                    |
|                                                                             | `noheader`                                                                                                                                           | suppress output header                                                                                                       |
|                                                                             | `title(string)`                                                                                                                                      | display `string` as title above the table of parameter estimates                                                             |
|                                                                             | [<var class="command">display_options</var><strong></strong>](bayesmh##display_options)                                   | control spacing, line width, and base and empty cells                                                                        |

[<strong>Advanced</strong>](#advanced_options)

`search(search_options)`

control the search for feasible initial values

INCLUDE help bayesmh\_corropts

<table class="syntab">
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<tfoot>
<tr class="even footnote">
<td colspan="3">* Starred options are specific to the <code class="command">bayes</code> prefix; other options are common between <code class="command">bayes</code> and [<strong>bayesmh</strong>](http://www.stata.com/help.cgi?bayesmh).</td>
</tr>
<tr class="odd footnote">
<td colspan="3">The full specification of <code class="command" data-options="iwishartprior()">iwishartprior()</code> is<br />
<code class="command">iwishartprior(</code>[<var class="command">#</var> [<var class="command">matname</var>] [<strong>,</strong> <strong></strong>](#iwishartpriorspec)
<ul>
</ul>
el(<var class="command">levelvar</var><strong>)</strong>]<strong></strong><code class="command">)</code>.</td>
</tr>
<tr class="even footnote">
<td colspan="3">Options <code class="command">prior()</code> and <code class="command">block()</code> can be repeated.</td>
</tr>
<tr class="odd footnote">
<td colspan="3">[<var class="command">priorspec</var><strong></strong>](bayesmh##priorspec) and [<var class="command">paramref</var><strong></strong>](bayesmh##paramref) are defined in [<strong>[BAYES]</strong> bayesmh](http://www.stata.com/help.cgi?bayesmh).</td>
</tr>
<tr class="even footnote">
<td colspan="3"><var class="command">paramref</var> may contain factor variables; see [<strong>fvvarlist</strong>](http://www.stata.com/help.cgi?fvvarlist).</td>
</tr>
<tr class="odd footnote">
<td colspan="3">See [<strong>[BAYES]</strong> bayesian postestimation](http://www.stata.com/help.cgi?bayesian_postestimation) for features available after estimation.</td>
</tr>
</tfoot>

</table>
