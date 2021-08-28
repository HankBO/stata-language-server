## Syntax

`dsge`
[<var class="command">eqlist</var><strong></strong>](#eqlist)
_\[`if`\] \[`in`\]_ \[`, options`\]

| Options                                                                                                                                                                                                                                                                                                                                                                                                                                                    |                                | Description                                                                                              |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------|----------------------------------------------------------------------------------------------------------|
| Main                                                                                                                                                                                                                                                                                                                                                                                                                                                       |                                |                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                            | `constraints(constraints)` | apply specified linear constraints                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                            | `noidencheck`                  | do not check for parameter identification                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                            | `solve`                        | return model solution at initial values                                                                  |
| SE/Robust                                                                                                                                                                                                                                                                                                                                                                                                                                                  |                                |                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                            | `vce(vcetype)`                 | `vcetype` may be `oim` or `robust`                                                                       |
| Reporting                                                                                                                                                                                                                                                                                                                                                                                                                                                  |                                |                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                            | `level(#)`                     | set confidence level; default is `level(95)`                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                            | `nocnsreport`                  | do not display constraints                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                            | `display_options`              | control columns and column formats and line width                                                        |
| Maximization                                                                                                                                                                                                                                                                                                                                                                                                                                               |                                |                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                            | `maximize_options`             | control the maximization process                                                                         |
| Advanced                                                                                                                                                                                                                                                                                                                                                                                                                                                   |                                |                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                            | `nodemean`                     | do not demean data prior to estimation                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                            | `post`                         | force posting of estimation results in the event of errors caused by lack of identification or stability |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                            | `idtolerance(#)`               | set tolerance used for identification check; seldom used                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                            | `lintolerance(#)`              | set tolerance used for linearity check; seldom used                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                            | `coeflegend`                   | display legend instead of statistics                                                                     |
| You must `tsset` your data before using `dsge`; see [<strong>[TS]</strong> tsset](http://www.stata.com/help.cgi?tsset).                                                                                                                                                                                                                                                                                                         |                                |                                                                                                          |
| `coeflegend` does not appear in the dialog box.                                                                                                                                                                                                                                                                                                                                                                                                            |                                |                                                                                                          |
| See [<strong>[DSGE]</strong> dsge postestimation](http://www.stata.com/help.cgi?dsge_postestimation) for features available after estimation. {pstd None} Below we present the full specification of `eqlist`. You may prefer to start with the syntax discussion in [**\[DSGE\] intro 2**](http://www.stata.com/manuals14/dsgeintro2.pdf). <span options="eqlist">{marker eqlist}_{nobreak None} {pstd None} `eqlist` is |                                |                                                                                                          |
| `eq`                                                                                                                                                                                                                                                                                                                                                                                                                                                       |                                |                                                                                                          |
| `eq eqlist`                                                                                                                                                                                                                                                                                                                                                                                                                                                |                                |                                                                                                          |

`eq` is

`cntrl_eq`

`state_eq`

`cntrl_eq` contains

`(ocntrl_var = termlist)`

`(ucntrl_var = termlist, unobserved)`

`(parm_exp * ocntrl_var = termlist)`

`(parm_exp * ucntrl_var = termlist, unobserved)`

`state_eq` contains

`(F.state_var = , state)`

`(F.state_var = termlist, state` \[`noshock`\]`)`

`(parm_exp * F.state_var = termlist, state`
\[`noshock`\]`)`

`ocntrl_var` is

Stata variable to be treated as an observed control in the system

`ucntrl_var` is

name to be treated as an unobserved control in the system

`state_var` is

name to be treated as an unobserved state in the system

If there happens to be a Stata variable with the same name as
`ucntrl_var` or `state_var`, the variable is ignored and plays no role
in the estimation.

`termlist` is

`term`

`term + termlist`

`term - termlist`

`term` is

`rhs_var`

`parm_exp * rhs_var`

`parm_exp * (termlist)`

`rhs_var` is

`ocntrl_var`

`ucntrl_var`

`state_var`

`E(F.ocntrl_var)`

`E(F.ucntrl_var)`

`parm_exp` is

scalar substitutable expression;

`parm_spec` elements are allowed and expected

`rhs_var` are not allowed

`parm_spec` is

`{c -(}parm_name{c )-}`

`{c -(}parm_name=initial_val{c )-}`

`parm_name` is

name used to identify model parameter

`initial_val` is

numeric literal; specifies an initial value
