## Syntax

Filter one variable

`tsfilter hp` _\[`type`\] \[_
[newvar](http://www.stata.com/help.cgi?newvar)
`=`
[<var class="command">varname</var><strong></strong>](http://www.stata.com/help.cgi?varname)
_\[`if`\] \[`in`\]_ \[`, options`\]

Filter multiple variables, unique names

`tsfilter hp` _\[`type`\] \[_
[<var class="command">newvarlist</var><strong></strong>](http://www.stata.com/help.cgi?newvarlist)
`=`
[<var class="command">varlist</var><strong></strong>](http://www.stata.com/help.cgi?varlist)
_\[`if`\] \[`in`\]_ \[`, options`\]

Filter multiple variables, common name stub

`tsfilter hp` _\[`type`\] \[_ `stub* =`
[<var class="command">varlist</var><strong></strong>](http://www.stata.com/help.cgi?varlist)
_\[`if`\] \[`in`\]_ \[`, options`\]

options

Description

Main

`smooth(#)`

smoothing parameter for the Hodrick-Prescott filter

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
