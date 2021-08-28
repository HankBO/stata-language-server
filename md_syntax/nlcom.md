## Syntax

Nonlinear combination of estimators -- one expression

`nlcom` \[`name:`\]`exp` \[`, options`\]

Nonlinear combinations of estimators -- more than one expression

`nlcom (`\[`name:`\]`exp)` \[`(`\[`name:`\]`exp)` ...\] \[`,`
`options`\]

| Options                                                 |                   | Description                                                                                    |
|---------------------------------------------------------|-------------------|------------------------------------------------------------------------------------------------|
|                                                         | `level(#)`        | set confidence level; default is `level(95)`                                                   |
|                                                         | `iterate(#)`      | maximum number of iterations                                                                   |
|                                                         | `post`            | post estimation results                                                                        |
|                                                         | `display_options` | control column formats and line width                                                          |
|                                                         | `noheader`        | suppress output header                                                                         |
|                                                         | `df(#)`           | use t distribution with `#` degrees of freedom for computing p-values and confidence intervals |
| `noheader` and `df(#)` do not appear in the dialog box. |                   |                                                                                                |

The second syntax means that if more than one expression is specified,
each must be surrounded by parentheses. The optional `name` is any valid
Stata name and labels the transformations.

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
