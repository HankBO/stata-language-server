## Syntax

`grmeanby`
[varlist](http://www.stata.com/help.cgi?varlist)
_\[`if`\] \[`in`\]_ \[`weight`\] `,`
`summarize(varname)` \[`options`\]

Options

Description

Main

\*

`summarize(varname)`

graph mean (or median) of `varname`

`median`

graph medians; default is to graph means

Plot

change look of the lines change look of markers (color, size, etc.) add
marker labels; change look or position

Y axis, X axis, Titles, Legend, Overall

`twoway_options`

any options other than `by()` documented in
[<strong>[G-3]</strong> <em>twoway_options</em>](http://www.stata.com/help.cgi?twoway_options)

\*`summarize(varname)` is required.

`aweight`s and `fweight`s are allowed; see
[<strong>weight</strong>](http://www.stata.com/help.cgi?weight).
