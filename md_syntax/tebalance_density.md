## Syntax

Density plots for the propensity score

`tebalance density` \[`, options`\]

Density plots for a covariate

`tebalance density varname` \[`, options`\]

| Options |                                     | Description                                                                                                                                                           |
|---------|-------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Main    |                                     |                                                                                                                                                                       |
|         | `kernel(kernel)`                | specify the kernel function; default is `kernel(epanechnikov)`                                                                                                        |
|         | `bwidth(*#)`                    | rescale default bandwidth                                                                                                                                             |
|         | `line#opts(line_options)` | `twoway line` options for density line number `#`                                                                                                                     |
|         | `twoway_options`                    | any options other than `by()` documented in [<strong>[G-3]</strong> <em>twoway_options</em>](http://www.stata.com/help.cgi?twoway_options) |
|         | `byopts(byopts)`                | how subgraphs are combined, labeled, etc.                                                                                                                             |

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
