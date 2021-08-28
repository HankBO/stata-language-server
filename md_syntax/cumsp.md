## Syntax

`cumsp`
[varname](http://www.stata.com/help.cgi?varname)
_\[`if`\] \[`in`\]_ \[`, options`\]

Options

Description

Main

`generate(newvar)`

create `newvar` holding distribution values

Plot

`cline_options`

affect rendition of the plotted points connected by lines

change look of markers (color, size, etc.) add marker labels; change
look or position

Add plots

`"addplot(plot)`

add other plots to the generated graph

Y axis, X axis, Titles, Legend, Overall

`twoway_options`

any options other than `by()` documented in
[<strong>[G-3]</strong> <em>twoway_options</em>](http://www.stata.com/help.cgi?twoway_options)

You must `tsset` your data before using `cumsp`; see
[<strong>[TS]</strong> tsset](http://www.stata.com/help.cgi?tsset).
Also, the time series must be dense (nonmissing and no gaps in the time
variable) in the sample specified.

`varname` may contain time-series operators; see
[<strong>tsvarlist</strong>](http://www.stata.com/help.cgi?tsvarlist).
