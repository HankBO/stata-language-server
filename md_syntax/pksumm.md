## Syntax

`pksumm id time concentration` _\[`if`\]
\[`in`\]_ \[`, options`\]

| Options                                                           |                     | Description                                                                                                                                     |
|-------------------------------------------------------------------|---------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| Main                                                              |                     |                                                                                                                                                 |
|                                                                   | `trapezoid`         | use trapezoidal rule to calculate AUC\_0,tmax; default is cubic splines                                                                         |
|                                                                   | `fit(#)`            | use `#` points to estimate AUC\_0,inf; default is `fit(3)`                                                                                      |
|                                                                   | `notimechk`         | do not check whether follow-up time for all subjects is the same                                                                                |
|                                                                   | `nodots`            | suppress the dots during calculation                                                                                                            |
|                                                                   | `graph`             | graph the distribution of `statistic`                                                                                                           |
|                                                                   | `stat(statistic)`   | graph the specified statistic; default is `stat(auc)`                                                                                           |
| Histogram, Density plots, Y axis, X axis, Titles, Legend, Overall |                     |                                                                                                                                                 |
|                                                                   | `histogram_options` | any option other than `by()` documented in [<strong>[R]</strong> histogram](http://www.stata.com/help.cgi?histogram) |

| statistic |           | Description                                                                                                |
|-----------|-----------|------------------------------------------------------------------------------------------------------------|
|           | `auc`     | area under the concentration-time curve (AUC\_0,tmax); the default                                         |
|           | `aucline` | AUC\_0,inf using a linear extension                                                                        |
|           | `aucexp`  | AUC\_0,inf using an exponential extension                                                                  |
|           | `auclog`  | area under the concentration-time curve from 0 to infinity extended with a linear fit to log concentration |
|           | `half`    | half-life of the drug                                                                                      |
|           | `ke`      | elimination rate                                                                                           |
|           | `cmax`    | maximum concentration                                                                                      |
|           | `tmax`    | time at last concentration                                                                                 |
|           | `tomc`    | time of maximum concentration                                                                              |
