## Syntax

Basic syntax

`test coeflist` <span options="31">{space
31}_([<strong>Syntax 1</strong>](#Syntax1))

`test exp = exp` \[`=` ...\] <span options="22">{space
22}_([<strong>Syntax 2</strong>](#Syntax2))

`test [eqno]` \[`: coeflist`\] <span options="20">{space
20}_([<strong>Syntax 3</strong>](#Syntax3))

`test [eqno = eqno` \[`=` ...\]`]` \[`: coeflist`\] <span
options="5">{space
5}_([<strong>Syntax 4</strong>](#Syntax4))

`testparm`
[varlist](http://www.stata.com/help.cgi?varlist)
\[`,`
[<var class="command">testparm_options</var><strong></strong>](#testparm_options)\]

Full syntax

`test (spec)` \[`(spec)` ...\] \[`,`
[<var class="command">test_options</var><strong></strong>](#test_options)\]

| testparm\_options                          |                  | Description                                                                                                                                                                                                     |
|--------------------------------------------|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                            | `equal`          | hypothesize that the coefficients are equal to each other                                                                                                                                                       |
|                                            | `equation(eqno)` | specify equation name or number for which the hypothesis is tested                                                                                                                                              |
|                                            | `nosvyadjust`    | compute unadjusted Wald tests for survey results                                                                                                                                                                |
|                                            | `df(#)`          | use F distribution with `#` denominator degrees of freedom for the reference distribution of the test statistic; for survey data, `#` specifies the design degrees of freedom unless `nosvyadjust` is specified |
| `df(#)` does not appear in the dialog box. |                  |                                                                                                                                                                                                                 |

| test\_options                                                                                                                                                                                                                                                                               |                        | Description                                                                                                                                                                                                     |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Options                                                                                                                                                                                                                                                                                     |                        |                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                             | `mtest`\[`(opt)`\] | test each condition separately                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                             | `coef`                 | report estimated constrained coefficients                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                             | `accumulate`           | test hypothesis jointly with previously tested hypotheses                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                             | `notest`               | suppress the output                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                             | `common`               | test only variables common to all the equations                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                             | `constant`             | include the constant in coefficients to be tested                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                             | `nosvyadjust`          | compute unadjusted Wald tests for survey results                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                             | `minimum`              | perform test with the constant, drop terms until the test becomes nonsingular, and test without the constant on the remaining terms; highly technical                                                           |
|                                                                                                                                                                                                                                                                                             | `matvlc(matname)`      | save the variance-covariance matrix; programmer's option                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                             | `df(#)`                | use F distribution with `#` denominator degrees of freedom for the reference distribution of the test statistic; for survey data, `#` specifies the design degrees of freedom unless `nosvyadjust` is specified |
| `coeflist` and `varlist` may contain factor variables and time-series operators; see [<strong>fvvarlist</strong>](http://www.stata.com/help.cgi?fvvarlist) and [<strong>tsvarlist</strong>](http://www.stata.com/help.cgi?tsvarlist). |                        |                                                                                                                                                                                                                 |
| `matvlc(matname)` and `df(#)` do not appear in the dialog box.                                                                                                                                                                                                                              |                        |                                                                                                                                                                                                                 |

<span options="Syntax1">{marker Syntax1}_
[<strong>Syntax 1</strong>](#syntax1) tests
that coefficients are 0.

<span options="Syntax2">{marker Syntax2}_
[<strong>Syntax 2</strong>](#syntax2) tests
that linear expressions are equal.

<span options="Syntax3">{marker Syntax3}_
[<strong>Syntax 3</strong>](#syntax3) tests
that coefficients in `eqno` are 0.

<span options="Syntax4">{marker Syntax4}_
[<strong>Syntax 4</strong>](#syntax4) tests
equality of coefficients between equations.

`spec` is one of

`coeflist`

`exp=exp`\[=`exp`\]

`[eqno]`\[`: coeflist`\]

`[eqno1=eqno2`\[`=`...\]`]`\[`:  coeflist`\]

`coeflistcoefcoef[eqno]coef[eqno]coef[eqno]_b[coef][eqno]_b[coef]expcoef_b[coef]_b[eqno:coef][eqno]coef[eqno]_b[coef]eqno##name`

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

Although not shown in the syntax diagram, parentheses around `spec` are
required only with multiple specifications. Also, the diagram does not
show that `test` may be called without arguments to redisplay the
results from the last `test`.

[<strong>anova</strong>](http://www.stata.com/help.cgi?anova)
and
[<strong>manova</strong>](http://www.stata.com/help.cgi?manova)
allow the `test` syntax above plus more (see
[<strong>[R] anova postestimation</strong>](anova_postestimation##test)
for `test` after `anova`; see
[<strong>[MV] manova postestimation</strong>](manova_postestimation##test)
for `test` after `manova`).
