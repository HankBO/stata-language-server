## Syntax

Summary statistics for all model parameters

`bayesstats summary` \[`, options showreffects`\[`(reref)`\]\]

`bayesstats summary _all` \[`, options`
`showreffects`\[`(reref)`\]\]

Summary statistics for selected model parameters

`bayesstats summary paramspec` \[`, options`\]

Summary statistics for functions of model parameters

`bayesstats summary exprspec` \[`, options`\]

Summary statistics of log-likelihood or log-posterior functions

`bayesstats summary _loglikelihood` \| `_logposterior` \[`,`
`options`\]

Full syntax

`bayesstats summary spec` \[`spec` ...\] \[`, options`\]

`paramspec` can be one of the following:

`{c -(}eqname:param{c )-}` refers to a parameter `param` with
equation name `eqname`;

`{c -(}eqname:{c )-}` refers to all model parameters with equation
name `eqname`;

`{c -(}eqname:paramlist{c )-}` refers to parameters with names
in `paramlist` and with equation name `eqname`; or

`{c -(}param{c )-}` refers to all parameters named `param` from all
equations.

In the above, `param` can refer to a matrix name, in which case it will
imply all elements of this matrix. See
`Different ways of specifying model parameters` in **\[BAYES\] bayesian
postestimation** for examples.

`exprspec` is an optionally labeled expression of model parameters
specified in parentheses:

`(`\[`exprlabel:`\]`expr)`

`exprlabel` is a valid Stata name, and `expr` is a scalar expression
that may not contain matrix model parameters. See
`Specifying functions of model parameters` in **\[BAYES\] bayesian
postestimation** for examples.

`_loglikelihood` and `_logposterior` also have respective synonyms `_ll`
and `_lp`.

`spec` is one of `paramspec`, `exprspec`, `_loglikelihood` (or `_ll`),
or `_logposterior` (or `_lp`).

| Options  |                   | Description                                                                         |
|----------|-------------------|-------------------------------------------------------------------------------------|
| Main     |                   |                                                                                     |
|          | `clevel(#)`       | set credible interval level; default is `clevel(95)`                                |
|          | `hpd`             | display HPD credible intervals instead of the default equal-tail credible intervals |
|          | `batch(#)`        | specify length of block for batch-mean calculations; default is `batch(0)`          |
|          | `skip(#)`         | skip every `#` observations from the MCMC sample; default is `skip(0)`              |
|          | `nolegend`        | suppress table legend                                                               |
|          | `display_options` | control spacing, line width, and base and empty cells                               |
| Advanced |                   |                                                                                     |
|          | `corrlag(#)`      | specify maximum autocorrelation lag; default varies                                 |
|          | `corrtol(#)`      | specify autocorrelation tolerance; default is `corrtol(0.01)`                       |
