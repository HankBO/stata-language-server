## Syntax

`testnl exp = exp` \[`= exp` ...\] \[`, options`\]

`testnl (exp = exp` \[`= exp`...\]`)` \[`(exp = exp`
\[`= exp` ...\]`) ...`\] \[`, options`\]

| Options                                                    |                    | Description                                                                                                               |
|------------------------------------------------------------|--------------------|---------------------------------------------------------------------------------------------------------------------------|
|                                                            | `mtest`\[`(opt)`\] | test each condition separately                                                                                            |
|                                                            | `iterate(#)`       | use maximum `#` of iterations to find the optimal step size                                                               |
|                                                            | `df(#)`            | use F distribution with `#` denominator degrees of freedom for the reference distribution of the test statistic           |
|                                                            | `nosvyadjust`      | carry out the Wald test as W/k \~ F(k,d); for use with `svy` estimation commands when the `df()` option is also specified |
| `df(#)` and `nosvyadjust` do not appear in the dialog box. |                    |                                                                                                                           |

The second syntax means that if more than one expression is specified,
each must be surrounded by parentheses.

`exp` is a possibly nonlinear expression containing

`_b[coef]_b[eqno:coef][eqno]coef[eqno]_b[coef]`

`eqno` is

`##name`

`coef` identifies a coefficient in the model. `coef` is typically a
variable name, a level indicator, an interaction indicator, or an
interaction involving continuous variables. Level indicators identify
one level of a factor variable and interaction indicators identify one
combination of levels of an interaction; see
[<strong>fvvarlist</strong>](http://www.stata.com/help.cgi?fvvarlist).
`coef` may contain time-series operators; see
[<strong>tsvarlist</strong>](http://www.stata.com/help.cgi?tsvarlist).

Distinguish between `[]`, which are to be typed, and \[\], which
indicate optional arguments.
