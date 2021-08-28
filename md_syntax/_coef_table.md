## Syntax

`_coef_table` \[`, options display_options eform_option`
`diparm_options` \]

| Options |                      | Description                                                   |
|---------|----------------------|---------------------------------------------------------------|
|         | `level(#)`           | set confidence level; default is `level(95)`                  |
|         | `first`              | show only the first equation                                  |
|         | `neq(#)`             | show only the first `#` equations                             |
|         | `plus`               | finish table with a continuation line                         |
|         | `separator(#)`       | add a separator line for every `#` ancillary parameters       |
|         | `notest`             | suppress tests for ancillary parameters                       |
|         | `coeftitle(title)`   | use `title` for coefficients column                           |
|         | `ptitle(title)`      | super title for p-value column                                |
|         | `cititle(title)`     | super title for confidence interval columns                   |
|         | `offsetonly1`        | report offset only for the first equation                     |
|         | `nocnsreport`        | do not display constraints                                    |
|         | `fullcnsreport`      | display all constraints                                       |
|         | `bmatrix(matname)`   | row vector of coefficient estimates                           |
|         | `vmatrix(matname)`   | matrix of variance estimates                                  |
|         | `cnsmatrix(matname)` | constraints matrix                                            |
|         | `dfmatrix(matname)`  | row vector of degrees of freedom                              |
|         | `eqmatrix(matname)`  | row vector identifying equation groups                        |
|         | `sort`               | sort rows by coefficient values within equation               |
|         | `dfci`               | report parameter degrees of freedom with confidence intervals |
|         | `dfpvalues`          | report parameter degrees of freedom with a test against zero  |
|         | `coeflegend`         | display legend instead of statistics                          |
