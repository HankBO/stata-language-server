## Syntax

After `var`

`irf create irfname` \[`, var_options`\]

After `svar`

`irf create irfname` \[`, svar_options`\]

After `vec`

`irf create irfname` \[`, vec_options`\]

After `arima`

`irf create irfname` \[`, arima_options`\]

After `arfima`

`irf create irfname` \[`, arfima_options`\]

`irfname` is any valid name that does not exceed 15 characters.

| var\_options |                                        | Description                                                               |
|--------------|----------------------------------------|---------------------------------------------------------------------------|
| Main         |                                        |                                                                           |
|              | `set(filename`\[`, replace`\]`)`     | make `filename` active                                                    |
|              | `replace`                              | replace `irfname` if it already exists                                    |
|              | `step(#)`                              | set forecast horizon to `#`; default is `step(8)`                         |
|              | `order(varlist)`                       | specify Cholesky ordering of endogenous variables                         |
|              | `estimates(estname)`                   | use previously stored results `estname`; default is to use active results |
| Std. errors  |                                        |                                                                           |
|              | `nose`                                 | do not calculate standard errors                                          |
|              | `bs`                                   | obtain standard errors from bootstrapped residuals                        |
|              | `bsp`                                  | obtain standard errors from parametric bootstrap                          |
|              | `nodots`                               | do not display "`.`" for each bootstrap replication                       |
|              | `reps(#)`                              | use `#` bootstrap replications; default is `reps(200)`                    |
|              | `bsaving(filename`\[`, replace`\]`)` | save bootstrap results in `filename`                                      |

| svar\_options |                                        | Description                                                               |
|---------------|----------------------------------------|---------------------------------------------------------------------------|
| Main          |                                        |                                                                           |
|               | `set(filename`\[`, replace`\]`)`     | make `filename` active                                                    |
|               | `replace`                              | replace `irfname` if it already exists                                    |
|               | `step(#)`                              | set forecast horizon to `#`; default is `step(8)`                         |
|               | `estimates(estname)`                   | use previously stored results `estname`; default is to use active results |
| Std. errors   |                                        |                                                                           |
|               | `nose`                                 | do not calculate standard errors                                          |
|               | `bs`                                   | obtain standard errors from bootstrapped residuals                        |
|               | `bsp`                                  | obtain standard errors from parametric bootstrap                          |
|               | `nodots`                               | do not display "`.`" for each bootstrap replication                       |
|               | `reps(#)`                              | use `#` bootstrap replications; default is `reps(200)`                    |
|               | `bsaving(filename`\[`, replace`\]`)` | save bootstrap results in `filename`                                      |

| vec\_options |                                    | Description                                                               |
|--------------|------------------------------------|---------------------------------------------------------------------------|
| Main         |                                    |                                                                           |
|              | `set(filename`\[`, replace`\]`)` | make `filename` active                                                    |
|              | `replace`                          | replace `irfname` if it already exists                                    |
|              | `step(#)`                          | set forecast horizon to `#`; default is `step(8)`                         |
|              | `estimates(estname)`               | use previously stored results `estname`; default is to use active results |

| arima\_options |                                    | Description                                                               |
|----------------|------------------------------------|---------------------------------------------------------------------------|
| Main           |                                    |                                                                           |
|                | `set(filename`\[`, replace`\]`)` | make `filename` active                                                    |
|                | `replace`                          | replace `irfname` if it already exists                                    |
|                | `step(#)`                          | set forecast horizon to `#`; default is `step(8)`                         |
|                | `estimates(estname)`               | use previously stored results `estname`; default is to use active results |
| Std. errors    |                                    |                                                                           |
|                | `nose`                             | do not calculate standard errors                                          |

| arfima\_options |                                    | Description                                                               |
|-----------------|------------------------------------|---------------------------------------------------------------------------|
| Main            |                                    |                                                                           |
|                 | `set(filename`\[`, replace`\]`)` | make `filename` active                                                    |
|                 | `replace`                          | replace `irfname` if it already exists                                    |
|                 | `step(#)`                          | set forecast horizon to `#`; default is `step(8)`                         |
|                 | `smemory`                          | calculate short-memory IRFs                                               |
|                 | `estimates(estname)`               | use previously stored results `estname`; default is to use active results |
| Std. errors     |                                    |                                                                           |
|                 | `nose`                             | do not calculate standard errors                                          |

The default is to use asymptotic standard errors if no options are
specified.

`irf create` is for use after fitting a model with the `var`, `svar`,
`vec`, `arima`, or `arfima` command; see
[<strong>[TS] var</strong>](http://www.stata.com/help.cgi?var),
[<strong>[TS] var svar</strong>](http://www.stata.com/help.cgi?svar),
[<strong>[TS] vec</strong>](http://www.stata.com/help.cgi?vec),
[<strong>[TS] arima</strong>](http://www.stata.com/help.cgi?arima),
and
[<strong>[TS] arfima</strong>](http://www.stata.com/help.cgi?arfima).

You must `tsset` your data before using `var`, `svar`, `vec`, `arima`,
or `arfima` and, hence, before using `irf create`; see
[<strong>[TS] tsset</strong>](http://www.stata.com/help.cgi?tsset).
