## Syntax

`_qreg`
\[[depvar](http://www.stata.com/help.cgi?depvar)
\[[indepvars](http://www.stata.com/help.cgi?indepvars)\]
_\[`if`\] \[`in`\]_ <span
class="command">\[`weight`\]_\] \[`, options`\]

| options                                                                                                                                                |                        | Description                                                                          |
|--------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------|--------------------------------------------------------------------------------------|
|                                                                                                                                                        | `quantile(#)`          | estimate `#` quantile; default is `quantile(.5)`                                     |
|                                                                                                                                                        | `level(#)`             | set confidence level; default is `level(95)`                                         |
|                                                                                                                                                        | `accuracy(#)`          | relative accuracy required for linear programming algorithm; should not be specified |
|                                                                                                                                                        | `optimization_options` | control the optimization process; seldom used                                        |
| `_qreg` allows `fweight`s, `aweight`s, and `iweight`s; see [<strong>weight</strong>](http://www.stata.com/help.cgi?weight). |                        |                                                                                      |
