## Syntax

`kdensity`
[varname](http://www.stata.com/help.cgi?varname)
_\[`if`\] \[`in`\]_ \[`weight`\] \[`,`
`options`\]

| Options                                 |                               | Description                                                                                                                                                           |
|-----------------------------------------|-------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Main                                    |                               |                                                                                                                                                                       |
|                                         | `kernel(kernel)`              | specify kernel function; default is `kernel(epanechnikov)`                                                                                                            |
|                                         | `bwidth(#)`                   | half-width of kernel                                                                                                                                                  |
|                                         | `generate(newvar_x newvar_d)` | store the estimation points in `newvar_x` and the density estimate in `newvar_d`                                                                                      |
|                                         | `n(#)`                        | estimate density using `#` points; default is min(N, 50)                                                                                                              |
|                                         | `at(var_x)`                   | estimate density using the values specified by `var_x`                                                                                                                |
|                                         | `nograph`                     | suppress graph                                                                                                                                                        |
| Kernel plot                             |                               |                                                                                                                                                                       |
|                                         | `cline_options`               | affect rendition of the plotted kernel density estimate                                                                                                               |
| Density plots                           |                               |                                                                                                                                                                       |
|                                         | `normal`                      | add normal density to the graph                                                                                                                                       |
|                                         | `normopts(cline_options)`     | affect rendition of normal density                                                                                                                                    |
|                                         | `student(#)`                  | add Student's t density with `#` degrees of freedom to the graph                                                                                                      |
|                                         | `stopts(cline_options)`       | affect rendition of the Student's t density                                                                                                                           |
| Add plots                               |                               |                                                                                                                                                                       |
|                                         | `"addplot(plot)`              | add other plots to the generated graph                                                                                                                                |
| Y axis, X axis, Titles, Legend, Overall |                               |                                                                                                                                                                       |
|                                         | `twoway_options`              | any options other than `by()` documented in [<strong>[G-3]</strong> <em>twoway_options</em>](http://www.stata.com/help.cgi?twoway_options) |

| kernel |                | Description                               |
|--------|----------------|-------------------------------------------|
|        | `epanechnikov` | Epanechnikov kernel function; the default |
|        | `epan2`        | alternative Epanechnikov kernel function  |
|        | `biweight`     | biweight kernel function                  |
|        | `cosine`       | cosine trace kernel function              |
|        | `gaussian`     | Gaussian kernel function                  |
|        | `parzen`       | Parzen kernel function                    |
|        | `rectangle`    | rectangle kernel function                 |
|        | `triangle`     | triangle kernel function                  |

`fweight`s, `aweight`s, and `iweight`s are allowed; see
[<strong>weight</strong>](http://www.stata.com/help.cgi?weight).
