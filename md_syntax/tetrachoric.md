## Syntax

`tetrachoric`
[varlist](http://www.stata.com/help.cgi?varlist)
_\[`if`\] \[`in`\]_ \[`weight`\] \[`,`
`options`\]

| Options |                       | Description                                                                                         |
|---------|-----------------------|-----------------------------------------------------------------------------------------------------|
| Main    |                       |                                                                                                     |
|         | `stats(statlist)` | list of statistics; select up to 4 statistics; default is `stats(rho)`                              |
|         | `edwards`             | use the noniterative Edwards and Edwards estimator; default is the maximum likelihood estimator     |
|         | `print(#)`            | significance level for displaying coefficients                                                      |
|         | `star(#)`             | significance level for displaying with a star                                                       |
|         | `bonferroni`          | use Bonferroni-adjusted significance level                                                          |
|         | `sidak`               | use Sidak-adjusted significance level                                                               |
|         | `pw`                  | calculate all the pairwise correlation coefficients by using all available data (pairwise deletion) |
|         | `zeroadjust`          | adjust frequencies when one cell has a zero count                                                   |
|         | `matrix`              | display output in matrix form                                                                       |
|         | `notable`             | suppress display of correlations                                                                    |
|         | `posdef`              | modify correlation matrix to be positive semidefinite                                               |

| statlist |       | Description                         |
|----------|-------|-------------------------------------|
|          | `rho` | tetrachoric correlation coefficient |
|          | `se`  | standard error of rho               |
|          | `obs` | number of observations              |
|          | `p`   | exact two-sided significance level  |

`by` is allowed; see
[<strong>[D]</strong> by](http://www.stata.com/help.cgi?by).

`fweight`s are allowed; see
[<strong>weight</strong>](http://www.stata.com/help.cgi?weight).
