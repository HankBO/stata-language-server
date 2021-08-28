## Syntax

`estat gof` _\[`if`\] \[`in`\]_ \[`weight`\]
\[`, options`\]

| gof\_options                                                                                                                                                                                              |             | Description                                                      |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|------------------------------------------------------------------|
| Main                                                                                                                                                                                                      |             |                                                                  |
|                                                                                                                                                                                                           | `group(#)`  | perform Hosmer-Lemeshow goodness-of-fit test using `#` quantiles |
|                                                                                                                                                                                                           | `all`       | execute test for all observations in the data                    |
|                                                                                                                                                                                                           | `outsample` | adjust degrees of freedom for samples outside estimation sample  |
|                                                                                                                                                                                                           | `table`     | display table of groups used for test                            |
| `fweight`s are allowed; see [<strong>weight</strong>](http://www.stata.com/help.cgi?weight).                                                                                   |             |                                                                  |
| `estat gof` is not appropriate after the `svy` prefix. <span options="menu_estat">{marker menu\_estat}_{nobreak None} {title None:Menu for estat} {phang None} **Statistics &gt; Postestimation** |             |                                                                  |
