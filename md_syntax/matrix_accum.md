## Syntax

`matrix accum A =`
[varlist](http://www.stata.com/help.cgi?varlist)
_\[`if`\] \[`in`\]_ \[`weight`\] \[`,`
`noconstant deviations means:(M) absorb(varname)`\]

`matrix glsaccum A =`
[varlist](http://www.stata.com/help.cgi?varlist)
_\[`if`\] \[`in`\]_ \[`weight`\]`,`
`group:(groupvar) glsmat:(W`\|`stringvar) row:(rowvar)`
\[`noconstant`\]

`matrix opaccum A =`
[varlist](http://www.stata.com/help.cgi?varlist)
_\[`if`\] \[`in`\]_ `,`
`group:(groupvar) opvar:(opvar)` \[`noconstant`\]

`matrix vecaccum a =`
[varlist](http://www.stata.com/help.cgi?varlist)
_\[`if`\] \[`in`\]_ \[`weight`\] \[`,`
`noconstant`\]

`varlist` in `matrix accum` and in `matrix vecaccum` may contain factor
variables (except for the first variable in `matrix vecaccum`
`varlist`); see
[<strong>fvvarlist</strong>](http://www.stata.com/help.cgi?fvvarlist).

`varlist` may contain time-series operators; see
[<strong>tsvarlist</strong>](http://www.stata.com/help.cgi?tsvarlist).

`aweight`s, `fweight`s, `iweight`s, and `pweight`s are allowed; see
[<strong>weight</strong>](http://www.stata.com/help.cgi?weight).
