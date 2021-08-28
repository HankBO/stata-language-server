## Syntax

Linear-regression-adjusted sampling weights

`svycal regress`
[varlist](http://www.stata.com/help.cgi?varlist)
_\[`weight`\]_ _\[`if`\]
\[`in`\]_ `, generate(newvar) totals(spec)` \[`noconstant`
`ll(#) ul(#) iterate(#) tolerance(#) force`\]

Raking-ratio-adjusted sampling weights

`svycal rake`
[varlist](http://www.stata.com/help.cgi?varlist)
_\[`weight`\]_ _\[`if`\]
\[`in`\]_ `, generate(newvar) totals(spec)` \[`noconstant`\]

[varlist](http://www.stata.com/help.cgi?varlist)
may contain factor variables; see
[<strong>fvvarlist</strong>](http://www.stata.com/help.cgi?fvvarlist).

`pweight`s and `iweight`s are allowed; see
[<strong>weights</strong>](http://www.stata.com/help.cgi?weights).
