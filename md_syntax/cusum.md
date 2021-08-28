## Syntax

`cusum yvar xvar` _\[`if`\] \[`in`\]_
\[`, options`\]

| Options                                 |                    | Description                                                                                                                                                           |
|-----------------------------------------|--------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Main                                    |                    |                                                                                                                                                                       |
|                                         | `generate(newvar)` | save cumulative sum in `newvar`                                                                                                                                       |
|                                         | `yfit(fitvar)`     | calculate cumulative sum against `fitvar`                                                                                                                             |
|                                         | `nograph`          | suppress the plot                                                                                                                                                     |
|                                         | `nocalc`           | suppress cusum test statistics                                                                                                                                        |
| Cusum plot                              |                    |                                                                                                                                                                       |
|                                         | `connect_options`  | affect the rendition of the plotted line                                                                                                                              |
| Add plots                               |                    |                                                                                                                                                                       |
|                                         | `"addplot(plot)`   | add plots to the generated graph                                                                                                                                      |
| Y axis, X axis, Titles, Legend, Overall |                    |                                                                                                                                                                       |
|                                         | `twoway_options`   | any options other than `by()` documented in [<strong>[G-3]</strong> <em>twoway_options</em>](http://www.stata.com/help.cgi?twoway_options) |
