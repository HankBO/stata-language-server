## Syntax

Filter one variable

`tsfilter bw` _\[`type`\] \[_
[newvar](http://www.stata.com/help.cgi?newvar)
`=`
[<var class="command">varname</var><strong></strong>](http://www.stata.com/help.cgi?varname)
_\[`if`\] \[`in`\]_ \[`, options`\]

Filter multiple variables, unique names

`tsfilter bw` _\[`type`\] \[_
[<var class="command">newvarlist</var><strong></strong>](http://www.stata.com/help.cgi?newvarlist)
`=`
[<var class="command">varlist</var><strong></strong>](http://www.stata.com/help.cgi?varlist)
_\[`if`\] \[`in`\]_ \[`, options`\]

Filter multiple variables, common name stub

`tsfilter bw` _\[`type`\] \[_ `stub* =`
[<var class="command">varlist</var><strong></strong>](http://www.stata.com/help.cgi?varlist)
_\[`if`\] \[`in`\]_ \[`, options`\]

options

Description

Main

`maxperiod(#)`

filter out stochastic cycles at periods larger than `#`

`order(#)`

set the order of the filter; default is `order(2)`

Trend

save the trend component(s) in new variable(s)

Gain

`gain(gainvar anglevar)`

save the gain and angular frequency

You must `tsset` or `xtset` your data before using `tsfilter`; see
[<strong>[TS]</strong> tsset](http://www.stata.com/help.cgi?tsset)
and
[<strong>[XT]</strong> xtset](http://www.stata.com/help.cgi?xtset).

`varname` and `varlist` may contain time-series operators; see
[<strong>tsvarlist</strong>](http://www.stata.com/help.cgi?tsvarlist).
