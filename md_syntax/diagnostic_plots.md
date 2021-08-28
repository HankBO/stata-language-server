## Syntax

Symmetry plot

`symplot`
[varname](http://www.stata.com/help.cgi?varname)
_\[`if`\] \[`in`\]_ \[`, options1`\]

Ordered values of varname against quantiles of uniform distribution

`quantile`
[varname](http://www.stata.com/help.cgi?varname)
_\[`if`\] \[`in`\]_ \[`, options1`\]

Quantiles of varname1 against quantiles of varname2

`qqplot varname1 varname2` _\[`if`\]
\[`in`\]_ \[`, options1`\]

Quantiles of varname against quantiles of normal distribution

`qnorm`
[varname](http://www.stata.com/help.cgi?varname)
_\[`if`\] \[`in`\]_ \[`, options2`\]

Standardized normal probability plot

`pnorm`
[varname](http://www.stata.com/help.cgi?varname)
_\[`if`\] \[`in`\]_ \[`, options2`\]

Quantiles of varname against quantiles of chi-squared distribution

`qchi`
[varname](http://www.stata.com/help.cgi?varname)
_\[`if`\] \[`in`\]_ \[`, options3`\]

Chi-squared probability plot

`pchi`
[varname](http://www.stata.com/help.cgi?varname)
_\[`if`\] \[`in`\]_ \[`, options3`\]

options1

Description

Plot

change look of markers (color, size, etc.) add marker labels; change
look or position

Reference line

`rlopts(cline_options)`

affect rendition of the reference line

Add plots

`"addplot(plot)`

add other plots to the generated graph

Y axis, X axis, Titles, Legend, Overall

`twoway_options`

any options other than `by()` documented in
[<strong>[G-3]</strong> <em>twoway_options</em>](http://www.stata.com/help.cgi?twoway_options)

options2

Description

Main

`grid`

add grid lines

Plot

change look of markers (color, size, etc.) add marker labels; change
look or position

Reference line

`rlopts(cline_options)`

affect rendition of the reference line

Add plots

`"addplot(plot)`

add other plots to the generated graph

Y axis, X axis, Titles, Legend, Overall

`twoway_options`

any options other than `by()` documented in
[<strong>[G-3]</strong> <em>twoway_options</em>](http://www.stata.com/help.cgi?twoway_options)

options3

Description

Main

`grid`

add grid lines

`df(#)`

degrees of freedom of chi-squared distribution; default is `df(1)`

Plot

change look of markers (color, size, etc.) add marker labels; change
look or position

Reference line

`rlopts(cline_options)`

affect rendition of the reference line

Add plots

`"addplot(plot)`

add other plots to the generated graph

Y axis, X axis, Titles, Legend, Overall

`twoway_options`

any options other than `by()` documented in
[<strong>[G-3]</strong> <em>twoway_options</em>](http://www.stata.com/help.cgi?twoway_options)
