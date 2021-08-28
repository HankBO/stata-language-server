## Syntax

` twoway lpolyci yvar xvar` _\[`if`\]
\[`in`\]_ \[`weight`\] \[`, options`\]

|     |                     |                                                                                    |
|-----|---------------------|------------------------------------------------------------------------------------|
|     | `options`           | Description                                                                        |
|     | `kernel(kernel)`    | kernel function; default is `kernel(epanechnikov)`                                 |
|     | `bwidth(#)`         | kernel bandwidth                                                                   |
|     | `degree(#)`         | degree of the polynomial smooth; default is `degree(0)`                            |
|     | `n(#)`              | obtain the smooth at `#` points; default is <span class="nowrap">min(N, 50)_ |
|     | `level(#)`          | set confidence level; default is `level(95)`                                       |
|     | `pwidth(#)`         | pilot bandwidth for standard error calculation                                     |
|     | `var(#)`            | estimate of the constant conditional variance                                      |
|     | `nofit`             | do not plot the smooth                                                             |
|     | `fitplot(plottype)` | how to plot the smooth; default is `fitplot(line)`                                 |
|     | `ciplot(plottype)`  | how to plot CIs; default is `ciplot(rarea)`                                        |
|     | `fcline_options`    | change look of the smoothed line                                                   |
|     | `fitarea_options`   | change look of CI                                                                  |

|                       |                                                                                                  |
|-----------------------|--------------------------------------------------------------------------------------------------|
| `axis_choice_options` | associate plot with alternative axis                                                             |
| `twoway_options`      | titles, legends, axes, added lines and text, by, regions, name, aspect ratio, etc. {p2line None} |

|     |                |                                           |
|-----|----------------|-------------------------------------------|
|     | `kernel`       | Description                               |
|     | `epanechnikov` | Epanechnikov kernel function; the default |
|     | `epan2`        | alternative Epanechnikov kernel function  |
|     | `biweight`     | biweight kernel function                  |
|     | `cosine`       | cosine trace kernel function              |
|     | `gaussian`     | Gaussian kernel function                  |
|     | `parzen`       | Parzen kernel function                    |
|     | `rectangle`    | rectangle kernel function                 |
|     | `triangle`     | triangle kernel function                  |

`fweight`s and `aweight`s are allowed; see
[<strong>weight</strong>](http://www.stata.com/help.cgi?weight).
