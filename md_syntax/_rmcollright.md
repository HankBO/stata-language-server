## Syntax

`_rmcollright varblocklist` _\[`if`\]
\[`in`\]_ _\[`weight`\]_ \[`,`
`noconstant collinear`\]

where `varblocklist` is a list of one or more `varblock`s, and a
`varblock` is either
[varname](http://www.stata.com/help.cgi?varname)
or
`(`[varlist](http://www.stata.com/help.cgi?varlist)`)`
(a `varlist` in parentheses indicates that this list of variables is to
be considered as a group).

`fweight`s, `aweight`s, `iweight`s, and `pweight`s are allowed; see
[<strong>weight</strong>](http://www.stata.com/help.cgi?weight).
