## Syntax

After `var` and `svar`

`fcast compute prefix` \[`, options1`\]

After `vec`

`fcast compute prefix` \[`, options2`\]

`prefix` is the prefix appended to the names of the dependent variables
to create the names of the variables holding the dynamic forecasts.

| options1    |                                       | Description                                                                          |
|-------------|---------------------------------------|--------------------------------------------------------------------------------------|
| Main        |                                       |                                                                                      |
|             | `step(#)`                             | set `#` periods to forecast; default is `step(1)`                                    |
|             | `dynamic(time_constant)`              | begin dynamic forecasts at `time_constant`                                           |
|             | `estimate(estname)`                   | use previously stored results `estname`; default is to use active results            |
|             | `replace`                             | replace existing forecast variables that have the same prefix                        |
| Std. Errors |                                       |                                                                                      |
|             | `nose`                                | suppress asymptotic standard errors                                                  |
|             | `bs`                                  | obtain standard errors from bootstrapped residuals                                   |
|             | `bsp`                                 | obtain standard errors from parametric bootstrap                                     |
|             | `bscentile`                           | estimate bounds by using centiles of bootstrapped dataset                            |
|             | `reps(#)`                             | perform `#` bootstrap replications; default is `reps(200)`                           |
|             | `nodots`                              | suppress the usual dot after each bootstrap replication                              |
|             | `saving(filename`\[`, replace`\]`)` | save bootstrap results as `filename`; use `replace` to overwrite existing `filename` |
| Reporting   |                                       |                                                                                      |
|             | `level(#)`                            | set confidence level; default is `level(95)`                                         |

| options2    |                          | Description                                                               |
|-------------|--------------------------|---------------------------------------------------------------------------|
| Main        |                          |                                                                           |
|             | `step(#)`                | set `#` periods to forecast; default is `step(1)`                         |
|             | `dynamic(time_constant)` | begin dynamic forecasts at `time_constant`                                |
|             | `estimate(estname)`      | use previously stored results `estname`; default is to use active results |
|             | `replace`                | replace existing forecast variables that have the same prefix             |
|             | `differences`            | save dynamic predictions of the first-differenced variables               |
| Std. errors |                          |                                                                           |
|             | `nose`                   | suppress asymptotic standard errors                                       |
| Reporting   |                          |                                                                           |
|             | `level(#)`               | set confidence level; default is `level(95)`                              |

Default is to use asymptotic standard errors if no options are
specified.

`fcast compute` can be used only after `var`, `svar`, and `vec`; see
[<strong>[TS] var</strong>](http://www.stata.com/help.cgi?var),
[<strong>[TS] var svar</strong>](http://www.stata.com/help.cgi?svar),
and
[<strong>[TS] vec</strong>](http://www.stata.com/help.cgi?vec).

You must `tsset` your data before using `fcast compute`; see
[<strong>[TS]</strong> tsset](http://www.stata.com/help.cgi?tsset).
