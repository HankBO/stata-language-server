## Syntax

Graphical summaries and convergence diagnostics for single parameter

`bayesgraph graph scalar_param` \[`, singleopts`\]

Graphical summaries and convergence diagnostics for multiple parameters

`bayesgraph graph spec` \[`spec` ...\] \[`, multiopts`\]

`bayesgraph matrix spec spec` \[`spec` ...\] \[`, singleopts`\]

Graphical summaries and convergence diagnostics for all parameters

`bayesgraph graph _all` \[`, multiopts`
`showreffects`\[`(reref)`\]\]

| graph                                                 |               | Description                          |
|-------------------------------------------------------|---------------|--------------------------------------|
|                                                       | `diagnostics` | multiple diagnostics in compact form |
|                                                       | `trace`       | trace plots                          |
|                                                       | `ac`          | autocorrelation plots                |
|                                                       | `histogram`   | histograms                           |
|                                                       | `kdensity`    | density plots                        |
|                                                       | `cusum`       | cumulative sum plots                 |
|                                                       | `matrix`      | scatterplot matrix                   |
| `bayesgraph matrix` requires at least two parameters. |               |                                      |

`scalar_param` is a
[<strong>scalar model parameter</strong>](bayes_glossary##scalar_model_parameter)
specified as `{c -(}param{c )-}` or `{c -(}eqname:param{c )-}`
or an expression `exprspec` of scalar model parameters. Matrix model
parameters are not allowed, but you may refer to their individual
elements.

`exprspec` is an optionally labeled expression of model parameters
specified in parentheses:

`(`\[`exprlabel:`\]`expr)`

`exprlabel` is a valid Stata name, and `expr` is a scalar expression
which may not contain matrix model parameters. See
`Specifying functions of model parameters` in **\[BAYES\] bayesian
postestimation** for examples.

`spec` is either `scalar_param` or `exprspec`.

| singleopts |                               | Description                                                            |
|------------|-------------------------------|------------------------------------------------------------------------|
| Options    |                               |                                                                        |
|            | `skip(#)`                     | skip every `#` observations from the MCMC sample; default is `skip(0)` |
|            | `name(name,` ...`)`       | specify name of graph                                                  |
|            | `saving(filename,` ...`)` | save graph in file                                                     |
|            | `graphopts`                   | graph-specific options                                                 |

| multiopts |                                     | Description                                                                                                                                                                |
|-----------|-------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Options   |                                     |                                                                                                                                                                            |
|           | `byparm`\[`(grbyparmopts)`\]    | specify the display of plots on one graph; default is a separate graph for each plot; not allowed with graphs `diagnostics` or `matrix` or with option `combine()`         |
|           | `combine`\[`(grcombineopts)`\]  | specify the display of plots on one graph; recommended when the number of parameters is large; not allowed with graphs `diagnostics` or `matrix` or with option `byparm()` |
|           | `sleep(#)`                          | pause for `#` seconds between multiple graphs; default is `sleep(0)`                                                                                                       |
|           | `wait`                              | pause until the —`more`— condition is cleared                                                                                                                              |
|           | \[`no`\]`close`                     | (do not) close Graph windows when the next graph is displayed with multiple graphs; default is `noclose`                                                                   |
|           | `skip(#)`                           | skip every `#` observations from the MCMC sample; default is `skip(0)`                                                                                                     |
|           | `name(namespec,` ...`)`       | specify names of graphs                                                                                                                                                    |
|           | `saving(filespec,` ...`)`     | save graphs in file                                                                                                                                                        |
|           | `graphopts(graphopts)`          | control the look of all graphs; not allowed with `byparm()`                                                                                                                |
|           | `graph`\[`#`\]`opts(graphopts)` | control the look of `#`th graph; not allowed with `byparm()`                                                                                                               |
|           | `graphopts`                         | equivalent to `graphopts(graphopts)`; only one may be specified                                                                                                            |

| graphopts |                   | Description                                           |
|-----------|-------------------|-------------------------------------------------------|
|           | `diagnosticsopts` | options for `bayesgraph diagnostics`                  |
|           | `tslineopts`      | options for `bayesgraph trace` and `bayesgraph cusum` |
|           | `acopts`          | options for `bayesgraph ac`                           |
|           | `histopts`        | options for `bayesgraph histogram`                    |
|           | `kdensityopts`    | options for `bayesgraph kdensity`                     |
|           | `grmatrixopts`    | options for `bayesgraph matrix`                       |

| diagnosticsopts |                                        | Description                                                                                                                             |
|-----------------|----------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
|                 | `traceopts(tslineopts)`            | affect rendition of all trace plots                                                                                                     |
|                 | `trace`\[`#`\]`opts(tslineopts)`   | affect rendition of `#`th trace plot                                                                                                    |
|                 | `acopts(acopts)`                   | affect rendition of all autocorrelation plots                                                                                           |
|                 | `ac`\[`#`\]`opts(acopts)`          | affect rendition of `#`th autocorrelation plot                                                                                          |
|                 | `histopts(histopts)`               | affect rendition of all histogram plots                                                                                                 |
|                 | `hist`\[`#`\]`opts(histopts)`      | affect rendition of `#`th histogram plot                                                                                                |
|                 | `kdensopts(kdensityopts)`          | affect rendition of all density plots                                                                                                   |
|                 | `kdens`\[`#`\]`opts(kdensityopts)` | affect rendition of `#`th density plot                                                                                                  |
|                 | `grcombineopts`                        | any option documented in [<strong>[G-2]</strong> graph combine](http://www.stata.com/help.cgi?graph_combine) |

| acopts |          | Description                                                                                                                                                                |
|--------|----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|        | `ci`     | plot autocorrelations with confidence intervals; not allowed with `byparm()`                                                                                               |
|        | `acopts` | any options other than `generate()` documented for the `ac` command in [<strong>[TS]</strong> corrgram](http://www.stata.com/help.cgi?corrgram) |

| kdensityopts |                                 | Description                                                              |
|--------------|---------------------------------|--------------------------------------------------------------------------|
|              | `kdensopts`                     | options for the overall kernel density plot                              |
|              | `show(showspec)`            | show first-half density, second-half density, or both; default is `both` |
|              | `kdensfirst(kdens1opts)`  | affect rendition of the first-half density plot                          |
|              | `kdenssecond(kdens2opts)` | affect rendition of the second-half density plot                         |
