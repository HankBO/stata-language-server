## Syntax

Dotplot of varname, with one column per value of groupvar

`dotplot`
[varname](http://www.stata.com/help.cgi?varname)
_\[`if`\] \[`in`\]_ \[`, options`\]

Dotplot for each variable in varlist, with one column per variable

`dotplot`
[varlist](http://www.stata.com/help.cgi?varlist)
_\[`if`\] \[`in`\]_ \[`, options`\]

Options

Description

Options

`"over(groupvar)`

display one columnar dotplot for each value of `groupvar`

`nx(#)`

horizontal dot density; default is `nx(0)`

`ny(#)`

vertical dot density; default is `ny(35)`

`incr(#)`

label every `#` group; default is `incr(1)`

`mean`\|`median`

plot a horizontal line of pluses at the mean or median

`bounded`

use minimum and maximum as boundaries

`bar`

plot horizontal dashed lines at shoulders of each group

`nogroup`

use the actual values of `yvar`

`center`

center the dot for each column

Plot

change look of markers (color, size, etc.) add marker labels; change
look or position

Y axis, X axis, Titles, Legend, Overall

`twoway_options`

any options other than `by()` documented in
[<strong>[G-3]</strong> <em>twoway_options</em>](http://www.stata.com/help.cgi?twoway_options)
