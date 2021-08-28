## Syntax

Orthogonalize variables

`orthog`
\[[varlist](http://www.stata.com/help.cgi?varlist)\]
_\[`if`\] \[`in`\]_ \[`weight`\] `,`
`generate(newvarlist)` \[`matrix(matname)`\]

Compute orthogonal polynomial

`orthpoly`
[varname](http://www.stata.com/help.cgi?varname)
_\[`if`\] \[`in`\]_ \[`weight`\] `,`  
{`generate(newvarlist)`<span
options="|">{c \|}_`poly(matname)`}
\[`degree(#)`\]

`orthpoly` requires that `generate(newvarlist)` or `poly(matname)`, or
both, be specified.

`varlist` may contain time-series operators; see
[<strong>tsvarlist</strong>](http://www.stata.com/help.cgi?tsvarlist).

`iweight`s, `aweight`s, `fweight`s, and `pweight`s are allowed; see
[<strong>weight</strong>](http://www.stata.com/help.cgi?weight).
