## Syntax

`_ms_at_parse` \[`at_list`\] \[`, asobserved`\]

`at_listat_specat_listat_specat_spec(at_stat)at_varat_statmeanomeanmedianomedianminominmaxomaxp1op1p99op99zeroasbalancedasobservedbaseat_varindepvarindepvar=valueindepvar=(numlist)indepvar=generate(exp)_continuous_factor_all*`

where `value` is a numeric (nonmissing) value, `exp` is a numeric
expression allowed by the
[<strong>generate</strong>](http://www.stata.com/help.cgi?generate)
command, and `indepvar` is any valid single variable specification that
identifies an independent variable participating in the column stripe
for `e(b)`, for example, standard variables with or without time-series
operators, and factor-level variables (but not interactions of
variables).

`_continuous` is a shortcut notation that means all the continuous
`indepvar`s.

`_factor` is a shortcut notation that means all the factor-variable
`indepvar`s.

`_all` and `*` are synonyms for `_continuous _factor`.

Although an `indepvar` can be specified multiple times, only the
rightmost `at_stat` has any affect, and only if the `indepvar` is not
associated with `value` or `numlist`.
