## Syntax

Statistics for all model parameters

`bayesstats ess` \[`, options showreffects`\[`(reref)`\]\]

`bayesstats ess _all` \[`, options`
`showreffects`\[`(reref)`\]\]

Statistics for selected model parameters

`bayesstats ess paramspec` \[`, options`\]

Statistics for functions of model parameters

`bayesstats ess exprspec` \[`, options`\]

Full syntax

`bayesstats ess spec` \[`spec` ...\] \[`, options`\]

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

`spec` is one of `paramspec` or `exprspec`.

| Options  |                   | Description                                                            |
|----------|-------------------|------------------------------------------------------------------------|
| Main     |                   |                                                                        |
|          | `skip(#)`         | skip every `#` observations from the MCMC sample; default is `skip(0)` |
|          | `nolegend`        | suppress table legend                                                  |
|          | `display_options` | control spacing, line width, and base and empty cells                  |
| Advanced |                   |                                                                        |
|          | `corrlag(#)`      | specify maximum autocorrelation lag; default varies                    |
|          | `corrtol(#)`      | specify autocorrelation tolerance; default is `corrtol(0.01)`          |
