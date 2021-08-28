## Syntax

`estat classification` _\[`if`\] \[`in`\]_
\[`weight`\] \[`, options`\]

| options                                                                                                                                                                                                              |             | Description                                                 |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|-------------------------------------------------------------|
| Main                                                                                                                                                                                                                 |             |                                                             |
|                                                                                                                                                                                                                      | `all`       | display summary statistics for all observations in the data |
|                                                                                                                                                                                                                      | `cutoff(#)` | positive outcome threshold; default is `cutoff(0.5)`        |
| `fweight`s are allowed; see [<strong>weight</strong>](http://www.stata.com/help.cgi?weight).                                                                                              |             |                                                             |
| `estat classification` is not appropriate after the `svy` prefix. <span options="menu_estat">{marker menu\_estat}_{nobreak None} {title None:Menu for estat} {phang None} **Statistics &gt; Postestimation** |             |                                                             |
