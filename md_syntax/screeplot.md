## Syntax

`screeplot` \[`eigvals`\] \[`, options`\]

`scree` is a synonym for `screeplot`.

| Options                                 |                            | Description                                                                                                                                                           |
|-----------------------------------------|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Main                                    |                            |                                                                                                                                                                       |
|                                         | `neigen(#)`                | graph only largest `#` eigenvalues; default is to plot all eigenvalues                                                                                                |
| Mean                                    |                            |                                                                                                                                                                       |
|                                         | `mean`                     | graph horizontal line at the mean of the eigenvalues                                                                                                                  |
|                                         | `meanlopts(cline_options)` | affect rendition of the mean line                                                                                                                                     |
| CI                                      |                            |                                                                                                                                                                       |
|                                         | `ci`\[`(ci_options)`\] | graph confidence intervals (after [<strong>pca</strong>](http://www.stata.com/help.cgi?pca) only); `ci` is a synonym for `ci(asymptotic)`  |
| Plot                                    |                            |                                                                                                                                                                       |
|                                         | `cline_options`            | affect rendition of the lines connecting points                                                                                                                       |
|                                         | `marker_options`           | change look of markers (color, size, etc.)                                                                                                                            |
| Add plots                               |                            |                                                                                                                                                                       |
|                                         | `"addplot(plot)`           | add other plots to the generated graph                                                                                                                                |
| Y axis, X axis, Titles, Legend, Overall |                            |                                                                                                                                                                       |
|                                         | `twoway_options`           | any options other than `by()` documented in [<strong>[G-3]</strong> <em>twoway_options</em>](http://www.stata.com/help.cgi?twoway_options) |

| ci\_options |                   | Description                                                                                                                             |
|-------------|-------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
|             | `asymptotic`      | compute asymptotic confidence intervals; the default                                                                                    |
|             | `heteroskedastic` | compute heteroskedastic bootstrap confidence intervals                                                                                  |
|             | `homoskedastic`   | compute homoskedastic bootstrap confidence intervals                                                                                    |
|             | `area_options`    | affect the rendition of the confidence bands                                                                                            |
|             | `table`           | produce a table of confidence intervals                                                                                                 |
|             | `level(#)`        | set confidence level; default is `level(95)`                                                                                            |
|             | `reps(#)`         | number of bootstrap simulations; default is `reps(200)`                                                                                 |
|             | `seed(str)`       | random-number [<strong>seed</strong>](http://www.stata.com/help.cgi?seed) used for the bootstrap simulations |
