## Syntax

`_robust`
[varlist](http://www.stata.com/help.cgi?varlist)
_\[`if`\] \[`in`\]_ \[`weight`\] \[`,`
`variance:(matname) minus(#) strata(varname) psu(varname)`
`cluster(varname) fpc(varname) subpop(varname) vsrs(matname)`
`srssubpop zeroweight`\]

`_robust` works with models that have all types of varlists, including
those with factor variables and times-series operators; see
[<strong>fvvarlist</strong>](http://www.stata.com/help.cgi?fvvarlist)
and
[<strong>tsvarlist</strong>](http://www.stata.com/help.cgi?tsvarlist).

`pweight`s, `aweight`s, `fweight`s, and `iweight`s are allowed; see
[<strong>weight</strong>](http://www.stata.com/help.cgi?weight).
