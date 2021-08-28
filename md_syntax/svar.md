## Syntax

Short-run constraints

`svar`
[depvarlist](http://www.stata.com/help.cgi?depvarlist)
_\[`if`\] \[`in`\]_ `,` <span options="-(">{c
-(}_ `aconstraints(constraints_a) aeq(matrix_aeq)`
`acns(matrix_acns) bconstraints(constraints_b) beq(matrix_beq)`
`bcns(matrix_bcns)` }
\[`short_run_options`\]

Long-run constraints

`svar`
[depvarlist](http://www.stata.com/help.cgi?depvarlist)
_\[`if`\] \[`in`\]_ `,` <span options="-(">{c
-(}_ `lrconstraints(constraints_lr) lreq(matrix_lreq)`
`lrcns(matrix_lrcns)` }
\[`long_run_options`\]

| short\_run\_options                                                                                                                                                                               |                                 | Description                                                                  |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------|------------------------------------------------------------------------------|
| Model                                                                                                                                                                                             |                                 |                                                                              |
|                                                                                                                                                                                                   | `noconstant`                    | suppress constant term                                                       |
| \*                                                                                                                                                                                                | `aconstraints(constraints_a)`   | apply previously defined `constraints_a` to **A**                            |
| \*                                                                                                                                                                                                | `aeq(matrix_aeq)`               | define and apply to **A** equality constraint matrix `matrix_aeq`            |
| \*                                                                                                                                                                                                | `acns(matrix_acns)`             | define and apply to **A** cross-parameter constraint matrix `matrix_acns`    |
| \*                                                                                                                                                                                                | `bconstraints(constraints_b)`   | apply previously defined `constraints_b` to **B**                            |
| \*                                                                                                                                                                                                | `beq(matrix_beq)`               | define and apply to **B** equality constraint matrix `matrix_beq`            |
| \*                                                                                                                                                                                                | `bcns(matrix_bcns)`             | define and apply to **B** cross-parameter constraint `matrix_bcns`           |
|                                                                                                                                                                                                   | `lags(numlist)`                 | use lags `numlist` in the underlying VAR                                     |
| Model 2                                                                                                                                                                                           |                                 |                                                                              |
|                                                                                                                                                                                                   | `exog(varlist_exog)`            | use exogenous variables `varlist`                                            |
|                                                                                                                                                                                                   | `varconstraints(constraints_v)` | apply `constraints_v` to underlying VAR                                      |
|                                                                                                                                                                                                   | `noislog`                       | suppress SURE iteration log                                                  |
|                                                                                                                                                                                                   | `isiterate(#)`                  | set maximum number of iterations for SURE; default is `isiterate(1600)`      |
|                                                                                                                                                                                                   | `istolerance(#)`                | set convergence tolerance of SURE                                            |
|                                                                                                                                                                                                   | `noisure`                       | use one-step SURE                                                            |
|                                                                                                                                                                                                   | `dfk`                           | make small-sample degrees-of-freedom adjustment                              |
|                                                                                                                                                                                                   | `small`                         | report small-sample t and F statistics                                       |
|                                                                                                                                                                                                   | `noidencheck`                   | do not check for local identification                                        |
|                                                                                                                                                                                                   | `nobigf`                        | do not compute parameter vector for coefficients implicitly set to zero      |
| Reporting                                                                                                                                                                                         |                                 |                                                                              |
|                                                                                                                                                                                                   | `level(#)`                      | set confidence level; default is `level(95)`                                 |
|                                                                                                                                                                                                   | `full`                          | show constrained parameters in table                                         |
|                                                                                                                                                                                                   | `var`                           | display underlying `var` output                                              |
|                                                                                                                                                                                                   | `lutstats`                      | report L<span options="u">{c u}_tkepohl lag-order selection statistics |
|                                                                                                                                                                                                   | `nocnsreport`                   | do not display constraints                                                   |
|                                                                                                                                                                                                   | `display_options`               | control columns and column formats                                           |
| Maximization                                                                                                                                                                                      |                                 |                                                                              |
|                                                                                                                                                                                                   | `maximize_options`              | control the maximization process; seldom used                                |
|                                                                                                                                                                                                   | `coeflegend`                    | display legend instead of statistics                                         |
| \* `aconstraints(constraints_a)`, `aeq(matrix_aeq)`, `acns(matrix_acns)`, `bconstraints(constraints_b)`, `beq(matrix_beq)`, `bcns(matrix_bcns)`: at least one of these options must be specified. |                                 |                                                                              |
| `coeflegend` does not appear in the dialog box.                                                                                                                                                   |                                 |                                                                              |

| long\_run\_options                                                                                                               |                                 | Description                                                                  |
|----------------------------------------------------------------------------------------------------------------------------------|---------------------------------|------------------------------------------------------------------------------|
| Model                                                                                                                            |                                 |                                                                              |
|                                                                                                                                  | `noconstant`                    | suppress constant term                                                       |
| \*                                                                                                                               | `lrconstraints(constraints_lr)` | apply previously defined `constraints_lr` to **C**                           |
| \*                                                                                                                               | `lreq(matrix_lreq)`             | define and apply to **C** equality constraint matrix `matrix_lreq`           |
| \*                                                                                                                               | `lrcns(matrix_lrcns)`           | define and apply to **C** cross-parameter constraint matrix `matrix_lrcns`   |
|                                                                                                                                  | `lags(numlist)`                 | use lags `numlist` in the underlying VAR                                     |
| Model 2                                                                                                                          |                                 |                                                                              |
|                                                                                                                                  | `exog(varlist_exog)`            | use exogenous variables `varlist`                                            |
|                                                                                                                                  | `varconstraints(constraints_v)` | apply `constraints_v` to underlying VAR                                      |
|                                                                                                                                  | `noislog`                       | suppress SURE iteration log                                                  |
|                                                                                                                                  | `isiterate(#)`                  | set maximum number of iterations for SURE; default is `isiterate(1600)`      |
|                                                                                                                                  | `istolerance(#)`                | set convergence tolerance of SURE                                            |
|                                                                                                                                  | `noisure`                       | use one-step SURE                                                            |
|                                                                                                                                  | `dfk`                           | make small-sample degrees-of-freedom adjustment                              |
|                                                                                                                                  | `small`                         | report small-sample t and F statistics                                       |
|                                                                                                                                  | `noidencheck`                   | do not check for local identification                                        |
|                                                                                                                                  | `nobigf`                        | do not compute parameter vector for coefficients implicitly set to zero      |
| Reporting                                                                                                                        |                                 |                                                                              |
|                                                                                                                                  | `level(#)`                      | set confidence level; default is `level(95)`                                 |
|                                                                                                                                  | `full`                          | show constrained parameters in table                                         |
|                                                                                                                                  | `var`                           | display underlying `var` output                                              |
|                                                                                                                                  | `lutstats`                      | report L<span options="u">{c u}_tkepohl lag-order selection statistics |
|                                                                                                                                  | `nocnsreport`                   | do not display constraints                                                   |
|                                                                                                                                  | `display_options`               | control columns and column formats                                           |
| Maximization                                                                                                                     |                                 |                                                                              |
|                                                                                                                                  | `maximize_options`              | control the maximization process; seldom used                                |
|                                                                                                                                  | `coeflegend`                    | display legend instead of statistics                                         |
| \* `lrconstraints(constraints_lr)`, `lreq(matrix_lreq)`, `lrcns(matrix_lrcns)`: at least one of these options must be specified. |                                 |                                                                              |
| `coeflegend` does not appear in the dialog box.                                                                                  |                                 |                                                                              |

You must `tsset` your data before using `svar`; see
[<strong>[TS] tsset</strong>](http://www.stata.com/help.cgi?tsset).

The `depvarlist` and `varlist_exog` may contain time-series operators;
see
[<strong>tsvarlist</strong>](http://www.stata.com/help.cgi?tsvarlist).

`by`, `fp`, `rolling`, `statsby`, and `xi` are allowed; see
[<strong>prefix</strong>](http://www.stata.com/help.cgi?prefix).

See
[<strong>[TS]</strong> var svar postestimation](http://www.stata.com/help.cgi?svar_postestimation)
for features available after estimation.
