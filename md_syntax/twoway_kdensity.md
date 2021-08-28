## Syntax

`twoway kdensity`
[varname](http://www.stata.com/help.cgi?varname)
_\[`if`\] \[`in`\]_ \[`weight`\] \[`,`
`options`\]

|                       |                                                                                                               |
|-----------------------|---------------------------------------------------------------------------------------------------------------|
| `options`             | Description {p2line None}                                                                                     |
| `bwidth:(#)`      | smoothing parameter {synopt None: }`kernel(kernel)`specify kernel function; default is `kernel(epanechnikov)` |
| `range:(# #)`   | range for plot, minimum and maximum                                                                           |
| `range(varname)`      | range for plot obtained from `varname`                                                                        |
| `n(#)`            | number of points to evaluate                                                                                  |
| `area(#)`         | rescaling parameter                                                                                           |
| `horizontal`          | graph horizontally                                                                                            |
| `boundary`            | estimate density one `bwidth()` beyond maximum and minimum; not allowed with `range()`                        |
| `cline_options`       | change look of the line                                                                                       |
| `axis_choice_options` | associate plot with alternative axis                                                                          |
| `twoway_options`      | titles, legends, axes, added lines and text, by, regions, name, aspect ratio, etc. {p2line None}              |

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
