## Syntax

Identify variables to be omitted because of collinearity

`_rmcoll`
[varlist](http://www.stata.com/help.cgi?varlist)
_\[`if`\] \[`in`\]_ \[`weight`\] \[`,`
`noconstant collinear expand forcedrop`\]

Identify independent variables to be omitted because of collinearity

`_rmdcoll`
[depvar](http://www.stata.com/help.cgi?depvar)
[indepvars](http://www.stata.com/help.cgi?indepvars)
_\[`if`\] \[`in`\]_ \[`weight`\] \[`,`
`noconstant collinear expand normcoll`\]

`varlist` and `indepvars` may contain factor variables; see
[<strong>fvvarlist</strong>](http://www.stata.com/help.cgi?fvvarlist).

`varlist`, `depvar`, and `indepvars` may contain time-series operators;
see
[<strong>tsvarlist</strong>](http://www.stata.com/help.cgi?tsvarlist).

`fweight`s, `aweight`s, `iweight`s, and `pweight`s are allowed; see
[<strong>weight</strong>](http://www.stata.com/help.cgi?weight).
