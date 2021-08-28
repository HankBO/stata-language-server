## Syntax

Spearman's rank correlation coefficients

`spearman`
\[[varlist](http://www.stata.com/help.cgi?varlist)\]
_\[`if`\] \[`in`\]_ \[`,`
`spearman_options`\]

Kendall's rank correlation coefficients

`ktau`
\[[varlist](http://www.stata.com/help.cgi?varlist)\]
_\[`if`\] \[`in`\]_ \[`, ktau_options`\]

| spearman\_options |                            | Description                                                                 |
|-------------------|----------------------------|-----------------------------------------------------------------------------|
| Main              |                            |                                                                             |
|                   | `stats(spearman_list)` | list of statistics; select up to three statistics; default is `stats(rho)`  |
|                   | `print(#)`                 | significance level for displaying coefficients                              |
|                   | `star(#)`                  | significance level for displaying with a star                               |
|                   | `bonferroni`               | use Bonferroni-adjusted significance level                                  |
|                   | `sidak`                    | use Sidak-adjusted significance level                                       |
|                   | `pw`                       | calculate all pairwise correlation coefficients by using all available data |
|                   | `matrix`                   | display output in matrix form                                               |

| ktau\_options                                                                                                                           |                        | Description                                                                 |
|-----------------------------------------------------------------------------------------------------------------------------------------|------------------------|-----------------------------------------------------------------------------|
| Main                                                                                                                                    |                        |                                                                             |
|                                                                                                                                         | `stats(ktau_list)` | list of statistics; select up to six statistics; default is `stats(taua)`   |
|                                                                                                                                         | `print(#)`             | significance level for displaying coefficients                              |
|                                                                                                                                         | `star(#)`              | significance level for displaying with a star                               |
|                                                                                                                                         | `bonferroni`           | use Bonferroni-adjusted significance level                                  |
|                                                                                                                                         | `sidak`                | use Sidak-adjusted significance level                                       |
|                                                                                                                                         | `pw`                   | calculate all pairwise correlation coefficients by using all available data |
|                                                                                                                                         | `matrix`               | display output in matrix form                                               |
| `by` is allowed with `spearman` and `ktau`; see [<strong>[D]</strong> by](http://www.stata.com/help.cgi?by). |                        |                                                                             |

<span options="spearman_list">{marker spearman\_list}_{nobreak
None} where the elements of `spearman_list` may be

`rho`<span options="5">{space 5}_ correlation coefficient

`obs`<span options="5">{space 5}_ number of observations

`p`<span options="7">{space 7}_ significance level

<span options="ktau_list">{marker ktau\_list}_{nobreak None} and
the elements of `ktau_list` may be

`taua`<span options="4">{space 4}_ correlation coefficient tau\_a

`taub`<span options="4">{space 4}_ correlation coefficient tau\_b

`score`<span options="3">{space 3}_ score

`se`<span options="6">{space 6}_ standard error of score

`obs`<span options="5">{space 5}_ number of observations

`p`<span options="7">{space 7}_ significance level
