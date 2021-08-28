## Syntax

`estimation_cmd` ... \[`, options`\]

| Options     |                                | Description                                                                    |
|-------------|--------------------------------|--------------------------------------------------------------------------------|
| Model       |                                |                                                                                |
|             | `noconstant`                   | suppress constant term                                                         |
|             | `offset(varname_o)`            | include `varname_o` in model with coefficient constrained to 1                 |
|             | `exposure(varname_o)`          | include ln(`varname_e`) in model with coefficient constrained to 1             |
|             | `constraints(constraints)` | apply specified linear constraints                                             |
|             | `collinear`                    | keep collinear variables                                                       |
| Reporting   |                                |                                                                                |
|             | `level(#)`                     | set confidence level; default is `level(95)`                                   |
|             | `lrmodel`                      | perform likelihood-ratio model test instead of the default Wald test           |
|             | `nocnsreport`                  | do not display constraints                                                     |
|             | `noci`                         | suppress confidence intervals                                                  |
|             | `nopvalues`                    | suppress p-values and their test statistics                                    |
|             | `noomitted`                    | do not display omitted collinear variables                                     |
|             | `vsquish`                      | suppress blank space separating factor variables or time-series variables      |
|             | `noemptycells`                 | do not display empty interaction cells of factor variables                     |
|             | `baselevels`                   | report base levels for factor variables and interactions                       |
|             | `allbaselevels`                | display all base levels for factor variables and interactions                  |
|             | `nofvlabel`                    | display factor-variable level values rather than value labels                  |
|             | `fvwrap(#)`                    | allow `#` lines when wrapping long value labels                                |
|             | `fvwrapon(style)`              | apply `style` for wrapping long value labels; `style` may be `word` or `width` |
|             | `cformat(%fmt)`                | format for coefficients, standard errors, and confidence limits                |
|             | `pformat(%fmt)`                | format for p-values                                                            |
|             | `sformat(%fmt)`                | format for test statistics                                                     |
|             | `nolstretch`                   | do not automatically widen coefficient table for long variable names           |
| Integration |                                |                                                                                |
|             | `intmethod(intmethod)`         | integration method for random-effects models                                   |
|             | `intpoints(#)`                 | use `#` integration (quadrature) points                                        |
|             | `coeflegend`                   | display legend instead of statistics                                           |
