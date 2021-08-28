## Syntax

**Univariate linear models**

`bayesmh depvar`
\[[indepvars](http://www.stata.com/help.cgi?indepvars)\]
_\[`if`\] \[`in`\]_ \[`weight`\]`,`
`likelihood(modelspec) prior(priorspec)`
\[`reffects(varname) options`\]

**Multivariate linear models**

Multivariate normal linear regression with common regressors

`bayesmh depvars =`
\[[indepvars](http://www.stata.com/help.cgi?indepvars)\]
_\[`if`\] \[`in`\]_ \[`weight`\]`,`
`likelihood(mvnormal(`...`)) prior(priorspec)` \[`options`\]

Multivariate normal regression with outcome-specific regressors

`bayesmh (`\[`eqname1:`\]`depvar1` \[`indepvars1`\]`)`

`(`\[`eqname2:`\]`depvar2` \[`indepvars2`\]`)` \[...\] <span
class="command">\[`if`\] \[`in`\]_ \[`weight`\]`,`

`likelihood(mvnormal(`...`)) prior(priorspec)` \[`options`\]

**Multiple-equation linear models**

`bayesmh (eqspec)` \[`(eqspec)`\] \[...\] <span
class="command">\[`if`\] \[`in`\]_ \[`weight`\]`,`

`prior(priorspec)` \[`options`\]

**Nonlinear models**

Univariate nonlinear regression

`bayesmh depvar = (subexpr)` _\[`if`\]
\[`in`\]_ \[`weight`\]`,`

`likelihood(modelspec) prior(priorspec)` \[`options`\]

Multivariate normal nonlinear regression

`bayesmh (depvar1 = (subexpr1))`

`(depvar2 = (subexpr2))` \[...\] <span
class="command">\[`if`\] \[`in`\]_ \[`weight`\]`,`

`likelihood(mvnormal(`...`)) prior(priorspec)` \[`options`\]

**Probability distributions**

Univariate distributions

`bayesmh depvar` _\[`if`\] \[`in`\]_
\[`weight`\]`, likelihood(distribution)`
`prior(priorspec)` \[`options`\]

Multiple-equation distribution specifications

`bayesmh (deqspec)` \[`(deqspec)`\] \[...\] <span
class="command">\[`if`\] \[`in`\]_ \[`weight`\]`,`

`prior(priorspec)` \[`options`\]

The syntax of `eqspec` is

`varspec` _\[`if`\] \[`in`\]_ \[`weight`\]`,`
`likelihood(modelspec)` \[`noconstant`\]

The syntax of `varspec` is one of the following:

\[`eqname:`\]`depvar`
\[[indepvars](http://www.stata.com/help.cgi?indepvars)\]

`depvars =`
\[[indepvars](http://www.stata.com/help.cgi?indepvars)\]

`(`\[`eqname1:`\]`depvar1` \[`indepvars1`\]`)`
`(`\[`eqname2:`\]`depvar2` \[`indepvars2`\]`)` \[...\]

The syntax of `deqspec` is

\[`eqname:`\] `depvar` _\[`if`\] \[`in`\]_
\[`weight`\]`, likelihood(distribution)`

`subexpr`, `subexpr1`, `subexpr2`, and so on are substitutable
expressions; see
[<var class="command">Substitutable expressions</var><strong></strong>](#subexp)
for details.

The syntax of `modelspec` is

`model` \[`, modelopts`\]

| model                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |                   | Description                                                            |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|------------------------------------------------------------------------|
| Model                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |                   |                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | `normal(var)`     | normal regression with variance `var`                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | `t(sigma2, df)`   | t regression with squared scale `sigma2` and degrees of freedom `df`   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | `lognormal(var)`  | lognormal regression with variance `var`                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | `lnormal(var)`    | synonym for `lognormal()`                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | `exponential`     | exponential regression                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | `mvnormal(Sigma)` | multivariate normal regression with covariance matrix `Sigma`          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | `probit`          | probit regression                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | `logit`           | logistic regression                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | `logistic`        | logistic regression; synonym for `logit`                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | `binomial(n)`     | binomial regression with logit link and number of trials `n`           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | `binlogit(n)`     | synonym for `binomial()`                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | `oprobit`         | ordered probit regression                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | `ologit`          | ordered logistic regression                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | `poisson`         | Poisson regression                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | `llf(subexpr)`    | substitutable expression for observation-level log-likelihood function |
| A distribution argument is a number for scalar arguments such as `var`; a variable name, [varname](http://www.stata.com/help.cgi?varname) (except for matrix arguments); a matrix for matrix arguments such as `Sigma`; a model parameter, `paramspec`; an expression, `expr`; or a substitutable expression, `subexpr`. See [BAYES bayesmhRemarksandexamplesSpecifyingargumentsoflikelihoodmodelsandpriordistributions`Specifying arguments of likelihood models and prior distributions`](http://www.stata.com/manuals14/bayesbayesmhremarksandexamplesspecifyingargumentsoflikelihoodmodelsandpriordistributions.pdf). |                   |                                                                        |

| modelopts |                       | Description                                                                                                  |
|-----------|-----------------------|--------------------------------------------------------------------------------------------------------------|
| Model     |                       |                                                                                                              |
|           | `offset(varname_o)`   | include `varname_o` in model with coefficient constrained to 1; not allowed with `normal()` and `mvnormal()` |
|           | `exposure(varname_e)` | include ln(`varname_e`) in model with coefficient constrained to 1; allowed only with `poisson`              |

| distribution                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |                      | Description                                                                 |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------|-----------------------------------------------------------------------------|
| Model                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |                      |                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | `dexponential(beta)` | exponential distribution with scale parameter `beta`                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | `dbernoulli(p)`      | Bernoulli distribution with success probability `p`                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | `dbinomial(p,n)`     | binomial distribution with success probability `p` and number of trials `n` |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | `dpoisson(mu)`       | Poisson distribution with mean `mu`                                         |
| A distribution argument is a model parameter, `paramspec`, or a substitutable expression, `subexpr`, containing model parameters. An `n` argument may be a number; an expression, `expr`; or a variable name, [varname](http://www.stata.com/help.cgi?varname). See [BAYES bayesmhRemarksandexamplesSpecifyingargumentsoflikelihoodmodelsandpriordistributions`Specifying arguments of likelihood models and prior distributions`](http://www.stata.com/manuals14/bayesbayesmhremarksandexamplesspecifyingargumentsoflikelihoodmodelsandpriordistributions.pdf). |                      |                                                                             |

The syntax of `priorspec` is

`paramref, priordist`

where the simplest specification of `paramref` is

`paramspec` \[`paramspec`\] \[...\]\]

Also see
[<var class="command">Referring to model parameters</var><strong></strong>](#refer)
for other specifications.

The syntax of `paramspec` is

`{c -(}`\[`eqname:`\]`param`\[, `matrix`\]`{c )-}`

where the parameter label `eqname` and parameter name `param` are valid
Stata names. Model parameters are either scalars such as
`{c -(}var{c )-}`, `{c -(}mean{c )-}`,
`{c -(}scale:beta{c )-}`, or matrices such as
`{c -(}Sigma, matrix{c )-}` and `{c -(}Scale:V, matrix{c )-}`.
For scalar parameters, you can use `{c -(}param=#{c )-}` to
specify an initial value. For example, you can specify,
`{c -(}var=1{c )-}`, `{c -(}mean=1.267{c )-}`, or
` {c -(}shape:alpha=3{c )-}`.

| priordist |                                                       | Description                                                                                                                                                                                                                             |
|-----------|-------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Model     |                                                       |                                                                                                                                                                                                                                         |
|           | `normal(mu,var)`                                      | normal with mean `mu` and variance `var`                                                                                                                                                                                                |
|           | `t(mu,sigma2,df)`                                     | location-scale `t` with mean `mu`, squared scale `sigma2`, and degrees of freedom `df`                                                                                                                                                  |
|           | `lognormal(mu,var)`                                   | lognormal with mean `mu` and variance `var`                                                                                                                                                                                             |
|           | `lnormal(mu,var)`                                     | synonym for `lognormal()`                                                                                                                                                                                                               |
|           | `uniform(a,b)`                                        | uniform on (a,b)                                                                                                                                                                                                                        |
|           | `gamma(alpha,beta)`                                   | gamma with shape `alpha` and scale `beta`                                                                                                                                                                                               |
|           | `igamma(alpha,beta)`                                  | inverse gamma with shape `alpha` and scale `beta`                                                                                                                                                                                       |
|           | `exponential(beta)`                                   | exponential with scale `beta`                                                                                                                                                                                                           |
|           | `laplace(mu,beta)`                                    | Laplace with mean `mu` and scale `beta`                                                                                                                                                                                                 |
|           | `cauchy(loc,beta)`                                    | Cauchy with location `loc` and scale `beta`                                                                                                                                                                                             |
|           | `beta(a,b)`                                           | beta with shape parameters `a` and `b`                                                                                                                                                                                                  |
|           | `chi2(df)`                                            | central chi-squared with degrees of freedom `df`                                                                                                                                                                                        |
|           | `jeffreys`                                            | Jeffreys prior for variance of a normal distribution                                                                                                                                                                                    |
|           | `mvnormal(d,mean,Sigma)`                              | multivariate normal of dimension `d` with mean vector `mean` and covariance matrix `Sigma`; `mean` can be a matrix name or a list of `d` means separated by comma: `mu1, mu2,` ...`, mud`                                       |
|           | `mvnormal0(d,Sigma)`                                  | multivariate normal of dimension `d` with zero mean vector and covariance matrix `Sigma`                                                                                                                                                |
|           | `mvn0(d,Sigma)`                                       | synonym for `mvnormal0()`                                                                                                                                                                                                               |
|           | `zellnersg(d,g,mean,{c -(}var{c )-})` | Zellner's g-prior of dimension `d` with `g` degrees of freedom, mean vector `mean`, and variance parameter `{c -(}var{c )-}`; `mean` can be a matrix name or a list of `d` means separated by comma: `mu1, mu2,` ...`, mud` |
|           | `zellnersg0(d,g,{c -(}var{c )-})`         | Zellner's g-prior of dimension `d` with `g` degrees of freedom, zero mean vector, and variance parameter `{c -(}var{c )-}`                                                                                                          |
|           | `wishart(d,df,V)`                                     | Wishart of dimension `d` with degrees of freedom `df` and scale matrix `V`                                                                                                                                                              |
|           | `iwishart(d,df,V)`                                    | inverse Wishart of dimension `d` with degrees of freedom `df` and scale matrix `V`                                                                                                                                                      |
|           | `jeffreys(d)`                                         | Jeffreys prior for covariance of a multivariate normal distribution of dimension `d`                                                                                                                                                    |
|           | `bernoulli(p)`                                        | Bernoulli with success probability `p`                                                                                                                                                                                                  |
|           | `index(p1,...,pk)`                                    | discrete indices 1, 2, ..., `k` with probabilities `p1`, `p2`, ..., `pk`                                                                                                                                                                |
|           | `poisson(mu)`                                         | Poisson with mean `mu`                                                                                                                                                                                                                  |

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |                          |                                                           |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------|-----------------------------------------------------------|
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | `flat`                   | flat prior; equivalent to `density(1)` or `logdensity(0)` |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | `density(f)`       | generic density `f`                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | `logdensity(logf)` | generic logdensity `logf`                                 |
| Dimension `d` is a positive `#`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |                          |                                                           |
| A distribution argument is a number for scalar arguments such as `var`, `alpha`, `beta`; a Stata matrix for matrix arguments such as `Sigma` and `V`; a model parameter, `paramspec`; an expression, `expr`; or a substitutable expression `subexpr`. See [BAYES bayesmhRemarksandexamplesSpecifyingargumentsoflikelihoodmodelsandpriordistributions`Specifying arguments of likelihood models and prior distributions`](http://www.stata.com/manuals14/bayesbayesmhremarksandexamplesspecifyingargumentsoflikelihoodmodelsandpriordistributions.pdf). |                          |                                                           |
| <span options="generic_f">{marker generic\_f}_ `f` is a nonnegative number, `#`; an expression `expr`; or a substitutable expression, `subexpr`.                                                                                                                                                                                                                                                                                                                                                                                                 |                          |                                                           |
| <span options="generic_logf">{marker generic\_logf}_ `logf` is a number, `#`; an expression, `expr`; or a substitutable expression, `subexpr`.                                                                                                                                                                                                                                                                                                                                                                                                   |                          |                                                           |
| When `mvnormal()` or `mvnormal0()` of dimension `d` is applied to `paramref` with `n` parameters (`n`!=`d`), `paramref` is reshaped into a matrix with `d` columns, and its rows are treated as independent samples from the specified `mvnormal()` distribution. If such reshaping is not possible, an error is issued. See [example 25](http://www.stata.com/manuals14/bayesbayesmhremarksandexamplesex25.pdf) for application of this feature.                                                                                                      |                          |                                                           |

| Options |                                       | Description                                                                                              |
|---------|---------------------------------------|----------------------------------------------------------------------------------------------------------|
| Model   |                                       |                                                                                                          |
|         | `noconstant`                          | suppress constant term; not allowed with ordered models, nonlinear models, and probability distributions |
| \*      | `likelihood(lspec)`             | distribution for the likelihood model                                                                    |
| \*      | `prior(priorspec)`              | prior for model parameters; this option may be repeated                                                  |
|         | `dryrun`                              | show model summary without estimation                                                                    |
| Model 2 |                                       |                                                                                                          |
|         | `redefine(label:i.varname)` | specify a random-effects linear form; this option may be repeated                                        |
|         | `xbdefine(label:varlist)`   | specify a linear form                                                                                    |

|            |                     |                                                                     |
|------------|---------------------|---------------------------------------------------------------------|
| Simulation |                     |                                                                     |
|            | `mcmcsize(#)`       | MCMC sample size; default is `mcmcsize(10000)`                      |
|            | `burnin(#)`         | burn-in period; default is `burnin(2500)`                           |
|            | `thinning(#)`       | thinning interval; default is `thinning(1)`                         |
|            | `rseed(#)`          | random-number seed                                                  |
|            | `exclude(paramref)` | specify model parameters to be excluded from the simulation results |

|          |                                                                                                                                                                                                               |                                                                  |
|----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------|
| Blocking |                                                                                                                                                                                                               |                                                                  |
|          | `block(`[<var class="command">paramref</var><strong></strong>](#paramref)\[`,` [<var class="command">blockopts</var><strong></strong>](#blockopts)\]`)` | specify a block of model parameters; this option may be repeated |
|          | `blocksummary`                                                                                                                                                                                                | display block summary                                            |

|                |                     |                                                                     |
|----------------|---------------------|---------------------------------------------------------------------|
| Initialization |                     |                                                                     |
|                | `initial(initspec)` | initial values for model parameters                                 |
|                | `nomleinitial`      | suppress the use of maximum likelihood estimates as starting values |
|                | `initrandom`        | specify random initial values                                       |
|                | `initsummary`       | display initial values used for simulation                          |

|            |                         |                                                               |
|------------|-------------------------|---------------------------------------------------------------|
| Adaptation |                         |                                                               |
|            | `adaptation(adaptopts)` | control the adaptive MCMC procedure                           |
|            | `scale(#)`              | initial multiplier for scale factor; default is `scale(2.38)` |
|            | `covariance(cov)`       | initial proposal covariance; default is the identity matrix   |

Reporting

`clevel(#)`

set credible interval level; default is `clevel(95)`

`hpd`

display HPD credible intervals instead of the default equal-tailed
credible intervals

`batch(#)`

specify length of block for batch-means calculations; default is
`batch(0)`

`saving(`[<var class="command">filename</var><strong></strong>](http://www.stata.com/help.cgi?filename)`, replace)`

save simulation results to `filename.dta`

`nomodelsummary`

suppress model summary

`noexpression`

suppress output of expressions from model summary

\[`no`\]`dots`

suppress dots or display dots every 100 iterations and iteration numbers
every 1,000 iterations; default is `nodots`

`dots(#`\[`, every(#)`\]`)`

display dots as simulation is performed

\[`no`\]`show(paramref)`

specify model parameters to be excluded from or included in the output

`showreffects`\[`(reref)`\]

specify that all or a subset of random-effects parameters be included in
the output

`notable`

suppress estimation table

`noheader`

suppress output header

`title(string)`

display `string` as title above the table of parameter estimates

[<var class="command">display_options</var><strong></strong>](#display_options)

control spacing, line width, and base and empty cells

INCLUDE help bayesmh\_eform

Advanced

`search(search_options)`

control the search for feasible initial values

INCLUDE help bayesmh\_corropts

|                                                                                                                                                                                   |     |     |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|-----|
| \* Options `likelihood()` and `prior()` are required. `prior()` must be specified for all model parameters.                                                                       |     |     |
| Options `prior()`, `redefine()`, and `block()` can be repeated.                                                                                                                   |     |     |
| `indepvars` and `paramref` may contain factor variables; see [<strong>fvvarlist</strong>](http://www.stata.com/help.cgi?fvvarlist).                    |     |     |
| With multiple-equations specifications, a local `if` specified within an equation is applied together with the global `if` specified with the command.                            |     |     |
| Only `fweight`s are allowed; see [<strong>weight</strong>](http://www.stata.com/help.cgi?weight).                                                      |     |     |
| With multiple-equations specifications, local weights or (weights specified within an equation) override global weights (weights specified with the command).                     |     |     |
| See [<strong>[BAYES]</strong> bayesian postestimation](http://www.stata.com/help.cgi?bayesian_postestimation) for features available after estimation. |     |     |

| blockopts                                                                        |                         | Description                                                                                                                   |
|----------------------------------------------------------------------------------|-------------------------|-------------------------------------------------------------------------------------------------------------------------------|
|                                                                                  | `gibbs`                 | requests Gibbs sampling; available for selected models only and not allowed with `scale()`, `covariance()`, or `adaptation()` |
|                                                                                  | `split`                 | requests that all parameters in a block be treated as separate blocks                                                         |
|                                                                                  | `reffects`              | requests that all parameters in a block be treated as random-effects parameters                                               |
|                                                                                  | `scale(#)`              | initial multiplier for scale factor for current block; default is `scale(2.38)`; not allowed with `gibbs`                     |
|                                                                                  | `covariance(cov)`       | initial proposal covariance for the current block; default is the identity matrix; not allowed with `gibbs`                   |
|                                                                                  | `adaptation(adaptopts)` | control the adaptive MCMC procedure of the current block; not allowed with `gibbs`                                            |
| Only `tarate()` and `tolerance()` may be specified in the `adaptation()` option. |                         |                                                                                                                               |

| adaptopts                                                                                         |                | Description                                                                                                                                                                                                           |
|---------------------------------------------------------------------------------------------------|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                                                   | `every(#)`     | adaptation interval; default is `every(100)`                                                                                                                                                                          |
|                                                                                                   | `maxiter(#)`   | maximum number of adaptation loops; default is `maxiter(25)` or max{25,`floor(burnin()/every())`} whenever default values of these options are modified |
|                                                                                                   | `miniter(#)`   | minimum number of adaptation loops; default is `miniter(5)`                                                                                                                                                           |
|                                                                                                   | `alpha(#)`     | parameter controlling acceptance rate (AR); default is `alpha(0.75)`                                                                                                                                                  |
|                                                                                                   | `beta(#)`      | parameter controlling proposal covariance; default is `beta(0.8)`                                                                                                                                                     |
|                                                                                                   | `gamma(#)`     | parameter controlling adaptation rate; default is `gamma(0)`                                                                                                                                                          |
| \*                                                                                                | `tarate(#)`    | target acceptance rate (TAR); default is parameter specific                                                                                                                                                           |
| \*                                                                                                | `tolerance(#)` | tolerance for AR; default is `tolerance(0.01)`                                                                                                                                                                        |
| \* Only starred options may be specified in the `adaptation()` option specified within `block()`. |                |                                                                                                                                                                                                                       |
