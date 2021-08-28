## Syntax

`teffects overlap` \[`, treat_options kden_options`\]

| treat\_options |                        | Description                                                                                                                           |
|----------------|------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Main           |                        |                                                                                                                                       |
|                | `ptlevel(treat_level)` | calculate predicted probabilities for treatment level `treat_level`; by default, `ptlevel()` corresponds to the first treatment level |
|                | `tlevels(treatments)`  | specify conditioning treatment levels; default is all treatment levels                                                                |
|                | `nolabel`              | use treatment level values and not value labels in legend and axis titles                                                             |

| kden\_options                           |                                    | Description                                                                                                                                                           |
|-----------------------------------------|------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Main                                    |                                    |                                                                                                                                                                       |
|                                         | `kernel(kernel)`                   | specify kernel function; default is `kernel(triangle)`                                                                                                                |
|                                         | `n(#)`                             | estimate densities using `#` points; default is `e(N)`, the number of observations in the estimation sample                                                           |
|                                         | `bwidth(#)`                        | half-width of kernel                                                                                                                                                  |
|                                         | `at(var_x)`                        | estimate densities using the values specified by `var_x`                                                                                                              |
| Kernel plots                            |                                    |                                                                                                                                                                       |
|                                         | `line#opts(cline_options)` | affect rendition of density for conditioning treatment `#`                                                                                                            |
| Add plots                               |                                    |                                                                                                                                                                       |
|                                         | `"addplot(plot)`                   | add other plots to the generated graph                                                                                                                                |
| Y axis, X axis, Titles, Legend, Overall |                                    |                                                                                                                                                                       |
|                                         | `twoway_options`                   | any options other than `by()` documented in [<strong>[G-3]</strong> <em>twoway_options</em>](http://www.stata.com/help.cgi?twoway_options) |

| kernel |                | Description                              |
|--------|----------------|------------------------------------------|
|        | `triangle`     | triangle kernel function; the default    |
|        | `epanechnikov` | Epanechnikov kernel function             |
|        | `epan2`        | alternative Epanechnikov kernel function |
|        | `biweight`     | biweight kernel function                 |
|        | `cosine`       | cosine trace kernel function             |
|        | `gaussian`     | Gaussian kernel function                 |
|        | `parzen`       | Parzen kernel function                   |
|        | `rectangle`    | rectangle kernel function                |
