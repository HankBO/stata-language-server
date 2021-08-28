## Syntax

`_ms_dydx_parse` \[`dydx_varlist`\] \[`, ey ex`\]

`dydx_varlistdydx_vardydx_varlistdydx_vardydx_varindepvar_continuous_factor_all*`

where `indepvar` is any valid single variable specification that
identifies an independent variable participating in the column stripe
for `e(b)`, for example, standard variables with or without time-series
operators, and factor-level variables (but not interactions of
variables).

`_continuous` is a shortcut notation that means all the continuous
`indepvar`s.

`_factor` is a shortcut notation that means all the factor-variable
`indepvar`s.

`_all` and `*` are synonyms for `_continuous _factor`.
