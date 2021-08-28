## Syntax

Basic syntax

`irtgraph icc`
\[[varlist](http://www.stata.com/help.cgi?varlist)\]
\[`, options`\]

Full syntax

`irtgraph icc`
`(`[varlist](http://www.stata.com/help.cgi?varlist)
\[`,`
[<var class="command">plot_options</var><strong></strong>](#plot_options)\]`)`
`(`[varlist](http://www.stata.com/help.cgi?varlist)
\[`,`
[<var class="command">plot_options</var><strong></strong>](#plot_options)\]`)`
\[...\] \[`, options`\]

`varlist` is a list of items from the currently fitted IRT model.

| Options                                 |                                                                                                                                                        | Description                                                                                                                                                           |
|-----------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Plots                                   |                                                                                                                                                        |                                                                                                                                                                       |
|                                         | `blocation`\[`(`[<var class="command">line_options</var><strong></strong>](http://www.stata.com/help.cgi?line_options)`)`\] | add vertical lines for estimated item difficulties                                                                                                                    |
|                                         | `plocation`\[`(`[<var class="command">line_options</var><strong></strong>](http://www.stata.com/help.cgi?line_options)`)`\] | add horizontal lines for midpoint probabilities                                                                                                                       |
|                                         | `bcc`                                                                                                                                                  | plot boundary characteristic curves for categorical items                                                                                                             |
|                                         | `ccc`                                                                                                                                                  | plot category characteristic curves                                                                                                                                   |
|                                         | `range(# #)`                                                                                                                                           | plot over theta = `#` to `#`                                                                                                                                          |
| Line                                    |                                                                                                                                                        |                                                                                                                                                                       |
|                                         | `line_options`                                                                                                                                         | affect rendition of the plotted curves                                                                                                                                |
| Add plots                               |                                                                                                                                                        |                                                                                                                                                                       |
|                                         | `addplot(plot)`                                                                                                                                        | add other plots to the ICC plot                                                                                                                                       |
| Y axis, X axis, Titles, Legend, Overall |                                                                                                                                                        |                                                                                                                                                                       |
|                                         | `twoway_options`                                                                                                                                       | any options other than `by()` documented in [<strong>[G-3]</strong> <em>twoway_options</em>](http://www.stata.com/help.cgi?twoway_options) |
| Data                                    |                                                                                                                                                        |                                                                                                                                                                       |
|                                         | `n(#)`                                                                                                                                                 | evaluate curves at `#` points; default is `n(300)`                                                                                                                    |
|                                         | `data(filename`\[`, replace`\]`)`                                                                                                                    | save plot data to a file                                                                                                                                              |

| plot\_options |                                     | Description                                               |
|---------------|-------------------------------------|-----------------------------------------------------------|
|               | `blocation`\[`(line_options)`\] | add vertical lines for estimated item difficulties        |
|               | `plocation`\[`(line_options)`\] | add horizontal lines for midpoint probabilities           |
|               | `bcc`                               | plot boundary characteristic curves for categorical items |
|               | `ccc`                               | plot category characteristic curves                       |
|               | `line_options`                      | affect rendition of the plotted curves                    |

`varlist` may use factor-variable notation; see
[<strong>fvvarlist</strong>](http://www.stata.com/help.cgi?fvvarlist).

`line_options` in `plot_options` override the same options specified in
`options`.
