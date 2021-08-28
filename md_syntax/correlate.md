## Syntax

Display correlation matrix or covariance matrix

`correlate`
\[[varlist](http://www.stata.com/help.cgi?varlist)\]
_\[`if`\] \[`in`\]_ \[`weight`\] \[`,`
`correlate_options`\]

Display all pairwise correlation coefficients

`pwcorr`
\[[varlist](http://www.stata.com/help.cgi?varlist)\]
_\[`if`\] \[`in`\]_ \[`weight`\] \[`,`
`pwcorr_options`\]

| correlate\_options |              | Description                                                            |
|--------------------|--------------|------------------------------------------------------------------------|
| Options            |              |                                                                        |
|                    | `means`      | display means, standard deviations, minimums, and maximums with matrix |
|                    | `noformat`   | ignore display format associated with variables                        |
|                    | `covariance` | display covariances                                                    |
|                    | `wrap`       | allow wide matrices to wrap                                            |

| pwcorr\_options |              | Description                                    |
|-----------------|--------------|------------------------------------------------|
| Main            |              |                                                |
|                 | `obs`        | print number of observations for each entry    |
|                 | `sig`        | print significance level for each entry        |
|                 | `listwise`   | use listwise deletion to handle missing values |
|                 | `casewise`   | synonym for `listwise`                         |
|                 | `print(#)`   | significance level for displaying coefficients |
|                 | `star(#)`    | significance level for displaying with a star  |
|                 | `bonferroni` | use Bonferroni-adjusted significance level     |
|                 | `sidak`      | use Sidak-adjusted significance level          |

`varlist` may contain time-series operators; see
[<strong>tsvarlist</strong>](http://www.stata.com/help.cgi?tsvarlist).

`by` is allowed with `correlate` and `pwcorr`; see
[<strong>[D]</strong> by](http://www.stata.com/help.cgi?by).

`aweight`s and `fweight`s are allowed; see
[<strong>weight</strong>](http://www.stata.com/help.cgi?weight).
