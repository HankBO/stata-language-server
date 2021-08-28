## Syntax

`irtgraph tif` \[`, options`\]

| Options                                 |                                     | Description                                                                                                                                                           |
|-----------------------------------------|-------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Plots                                   |                                     |                                                                                                                                                                       |
|                                         | `se`\[`(line_options)`\]        | plot the standard error of the TIF                                                                                                                                    |
|                                         | `range(# #)`                        | plot over theta = `#` to `#`                                                                                                                                          |
| Line                                    |                                     |                                                                                                                                                                       |
|                                         | `line_options`                      | affect rendition of the plotted TIF                                                                                                                                   |
| Add plots                               |                                     |                                                                                                                                                                       |
|                                         | `addplot(plot)`                     | add other plots to the TIF plot                                                                                                                                       |
| Y axis, X axis, Titles, Legend, Overall |                                     |                                                                                                                                                                       |
|                                         | `twoway_options`                    | any options other than `by()` documented in [<strong>[G-3]</strong> <em>twoway_options</em>](http://www.stata.com/help.cgi?twoway_options) |
| Data                                    |                                     |                                                                                                                                                                       |
|                                         | `n(#)`                              | evaluate TIF at `#` points; default is `n(300)`                                                                                                                       |
|                                         | `data(filename`\[`, replace`\]`)` | save plot data to a file                                                                                                                                              |
