## Syntax

`cluster dendrogram` \[`clname`\] _\[`if`\]
\[`in`\]_ \[`, options` \]

| Options                                 |                       | Description                                                                                                                                                          |
|-----------------------------------------|-----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Main                                    |                       |                                                                                                                                                                      |
|                                         | `quick`               | do not center parent branches                                                                                                                                        |
|                                         | `labels(varname)`     | name of variable containing leaf labels                                                                                                                              |
|                                         | `cutnumber(#)`        | display top \# branches only                                                                                                                                         |
|                                         | `cutvalue(#)`         | display branches above \# (dis)similarity measure only                                                                                                               |
|                                         | `showcount`           | display number of observations for each branch                                                                                                                       |
|                                         | `countprefix(string)` | prefix the branch count with `string`; default is \`\`n=''                                                                                                           |
|                                         | `countsuffix(string)` | suffix the branch count with `string`; default is empty string                                                                                                       |
|                                         | `countinline`         | put branch count in line with branch label                                                                                                                           |
|                                         | `vertical`            | orient dendrogram vertically (default)                                                                                                                               |
|                                         | `horizontal`          | orient dendrogram horizontally                                                                                                                                       |
| Plot                                    |                       |                                                                                                                                                                      |
|                                         | `line_options`        | affect rendition of the plotted lines                                                                                                                                |
| Add plots                               |                       |                                                                                                                                                                      |
|                                         | `"addplot(plot)`      | add other plots to the dendrogram                                                                                                                                    |
| Y axis, X axis, Titles, Legend, Overall |                       |                                                                                                                                                                      |
|                                         | `twoway_options`      | any option other than `by()` documented in [<strong>[G-3]</strong> <em>twoway_options</em>](http://www.stata.com/help.cgi?twoway_options) |

Note: `cluster tree` is a synonym for `cluster dendrogram`.

In addition to the restrictions imposed by `if` and `in`, the
observations are automatically restricted to those that were used in the
cluster analysis.
