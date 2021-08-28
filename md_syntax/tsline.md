## Syntax

Time-series line plot

\[`twoway`\] `tsline`
[varlist](http://www.stata.com/help.cgi?varlist)
_\[`if`\] \[`in`\]_ \[`,`
[<var class="command">tsline_options</var><strong></strong>](#tsline_options)\]

Time-series range plot with lines

\[`twoway`\] `tsrline y_1 y_2` _\[`if`\]
\[`in`\]_ \[`,`
[<var class="command">tsrline_options</var><strong></strong>](#tsrline_options)\]

where the time variable is assumed set by
[<strong>tsset</strong>](http://www.stata.com/help.cgi?tsset),
`varlist` has the interpretation

`y_1y_2y_k`

| tsline\_options                                |                   | Description                                                                                                                                                                                                                                                                  |
|------------------------------------------------|-------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Plots                                          |                   |                                                                                                                                                                                                                                                                              |
|                                                | `scatter_options` | any options documented in [<strong>[G-2]</strong> graph twoway scatter](http://www.stata.com/help.cgi?scatter) with the exception of `marker_options`, `marker_placement_options`, and `marker_label_options`, which will be ignored if specified |
| Y axis, Time axis, Titles, Legend, Overall, By |                   |                                                                                                                                                                                                                                                                              |
|                                                | `twoway_options`  | any options documented in [<strong>[G-3]</strong> <em>twoway_options</em>](http://www.stata.com/help.cgi?twoway_options)                                                                                                                          |

| tsrline\_options                               |                  | Description                                                                                                                                         |
|------------------------------------------------|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| Plots                                          |                  |                                                                                                                                                     |
|                                                | `rline_options`  | any options documented in [<strong>[G-2]</strong> graph twoway rline](http://www.stata.com/help.cgi?twoway_rline)        |
| Y axis, Time axis, Titles, Legend, Overall, By |                  |                                                                                                                                                     |
|                                                | `twoway_options` | any options documented in [<strong>[G-3]</strong> <em>twoway_options</em>](http://www.stata.com/help.cgi?twoway_options) |
