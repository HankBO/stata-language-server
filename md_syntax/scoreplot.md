## Syntax

Plot score variables

`scoreplot` _\[`if`\] \[`in`\]_ \[`,`
`scoreplot_options`\]

Plot the loadings (factors, components, or discriminant functions)

`loadingplot` \[`, loadingplot_options`\]

| scoreplot\_options              |                          | Description                                                                                                                                                           |
|---------------------------------|--------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Main                            |                          |                                                                                                                                                                       |
|                                 | `factors(#)`             | number of factors/scores to be plotted; default is `factors(2)`                                                                                                       |
|                                 | `components(#)`          | synonym for `factors()`                                                                                                                                               |
|                                 | `norotated`              | use unrotated factors or scores, even if rotated results exist                                                                                                        |
|                                 | `matrix`                 | graph as a matrix plot, available only when `factors(2)` is specified; default is a scatterplot                                                                       |
|                                 | `combined`               | graph as a combined plot, available when <span class="nowrap">`factors(#` &gt; 2`)`_; default is a matrix plot                                                |
|                                 | `half`                   | graph lower half only; allowed only with `matrix`                                                                                                                     |
|                                 | `graph_matrix_options`   | affect the rendition of the matrix graph                                                                                                                              |
|                                 | `combine_options`        | affect the rendition of the combined graph                                                                                                                            |
|                                 | `scoreopt(predict_opts)` | options for `predict` generating score variables                                                                                                                      |
|                                 | `marker_options`         | change look of markers (color, size, etc.)                                                                                                                            |
|                                 | `marker_label_options`   | change look or position of marker labels                                                                                                                              |
| Y axis, X axis, Titles, Overall |                          |                                                                                                                                                                       |
|                                 | `twoway_options`         | any options other than `by()` documented in [<strong>[G-3]</strong> <em>twoway_options</em>](http://www.stata.com/help.cgi?twoway_options) |

| loadingplot\_options            |                        | Description                                                                                                                                                           |
|---------------------------------|------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Main                            |                        |                                                                                                                                                                       |
|                                 | `factors(#)`           | number of factors/scores to be plotted; default is `factors(2)`                                                                                                       |
|                                 | `components(#)`        | synonym for `factors()`                                                                                                                                               |
|                                 | `norotated`            | use unrotated factors or scores, even if rotated results exist                                                                                                        |
|                                 | `matrix`               | graph as a matrix plot, available only when `factors(2)` is specified; default is a scatterplot                                                                       |
|                                 | `combined`             | graph as a combined plot, available when <span class="nowrap">`factors(#` &gt; 2`)`_; default is a matrix plot                                                |
|                                 | `half`                 | graph lower half only; allowed only with `matrix`                                                                                                                     |
|                                 | `graph_matrix_options` | affect the rendition of the matrix graph                                                                                                                              |
|                                 | `combine_options`      | affect the rendition of the combined graph                                                                                                                            |
|                                 | `maxlength(#)`         | abbreviate variable names to `#` characters; default is `maxlength(12)`                                                                                               |
|                                 | `marker_options`       | change look of markers (color, size, etc.)                                                                                                                            |
|                                 | `marker_label_options` | change look or position of marker labels                                                                                                                              |
| Y axis, X axis, Titles, Overall |                        |                                                                                                                                                                       |
|                                 | `twoway_options`       | any options other than `by()` documented in [<strong>[G-3]</strong> <em>twoway_options</em>](http://www.stata.com/help.cgi?twoway_options) |
