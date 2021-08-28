## Syntax

Test that coefficients are zero

`mi test coeflist`

Test that coefficients within a single equation are zero

`mi test` \[`eqno`\] \[`: coeflist`\]

Test that subsets of coefficients are zero (full syntax)

`mi test (spec)` \[`(spec)` ...\] \[`, test_options`\]

Test that subsets of transformed coefficients are zero

`mi testtransform name` \[`(name)` ...\] \[`,`
`transform_options`\]

| test\_options |            | Description                                                |
|---------------|------------|------------------------------------------------------------|
| Test          |            |                                                            |
|               | `ufmitest` | perform unrestricted FMI model test                        |
|               | `nosmall`  | do not apply small-sample correction to degrees of freedom |
|               | `constant` | include the constant in coefficients to be tested          |

| transform\_options |            | Description                                                |
|--------------------|------------|------------------------------------------------------------|
| Test               |            |                                                            |
|                    | `ufmitest` | perform unrestricted FMI model test                        |
|                    | `nosmall`  | do not apply small-sample correction to degrees of freedom |
|                    | `nolegend` | suppress transformation legend                             |

`coeflist` may contain factor variables and time-series operators; see
[<strong>fvvarlist</strong>](http://www.stata.com/help.cgi?fvvarlist)
and
[<strong>tsvarlist</strong>](http://www.stata.com/help.cgi?tsvarlist).

`coeflistcoefcoef[eqno]coef[eqno]coef[eqno]_b[coef][eqno][coef]eqno##eqnamespeccoeflist[eqno]:coeflist`

`coef` identifies a coefficient in the model; see the
[<strong>description</strong>](test##coef) in
[<strong>[R]</strong> test](http://www.stata.com/help.cgi?test)
for details. `eqname` is an equation name.

`name` is an expression name as specified with `mi estimate` or
`mi estimate using` (see
[<strong>[MI]</strong> mi estimate](http://www.stata.com/help.cgi?mi_estimate)
or
[<strong>[MI]</strong> mi estimate using](http://www.stata.com/help.cgi?mi_estimate_using)).
