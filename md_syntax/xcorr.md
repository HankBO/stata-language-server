## Syntax

`xcorr varname1 varname2` _\[`if`\]
\[`in`\]_ \[`, options`\]

Options

Description

Main

`generate(newvar)`

create `newvar` containing cross-correlation values

`table`

display a table instead of graphical output

`noplot`

do not include the character-based plot in tabular output

`lags(#)`

include `#` lags and leads in graph

Plot

value to drop to; default is 0 change look of markers (color, size,
etc.) add marker labels; change look or position change look of dropped
lines

Add plots

`"addplot(plot)`

add other plots to the generated graph

Y axis, X axis, Titles, Legend, Overall

`twoway_options`

any options other than `by()` documented in
[<strong>[G-3]</strong> <em>twoway_options</em>](http://www.stata.com/help.cgi?twoway_options)

You must `tsset` your data before using `xcorr`; see
[<strong>[TS] tsset</strong>](http://www.stata.com/help.cgi?tsset).

`varname1` and `varname2` may contain time-series operators; see
[<strong>tsvarlist</strong>](http://www.stata.com/help.cgi?tsvarlist).
