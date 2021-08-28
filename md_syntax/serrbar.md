## Syntax

`serrbar mvar svar xvar` _\[`if`\]
\[`in`\]_ \[`, options`\]

| Options                                 |                           | Description                                                                                                                                                           |
|-----------------------------------------|---------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Main                                    |                           |                                                                                                                                                                       |
|                                         | `scale(#)`                | scale length of graph bars; default is `scale(1)`                                                                                                                     |
| Error bars                              |                           |                                                                                                                                                                       |
|                                         | `rcap_options`            | affect rendition of capped spikes                                                                                                                                     |
| Plotted points                          |                           |                                                                                                                                                                       |
|                                         | `mvopts(scatter_options)` | affect rendition of plotted points                                                                                                                                    |
| Add plots                               |                           |                                                                                                                                                                       |
|                                         | `"addplot(plot)`          | add other plots to generated graph                                                                                                                                    |
| Y axis, X axis, Titles, Legend, Overall |                           |                                                                                                                                                                       |
|                                         | `twoway_options`          | any options other than `by()` documented in [<strong>[G-3]</strong> <em>twoway_options</em>](http://www.stata.com/help.cgi?twoway_options) |
