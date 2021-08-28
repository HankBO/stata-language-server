## Syntax

`mata: _parse_colon("hascolon", "rhscmd")`

Inputs (from Stata):

 `0' <span style="padding-left: 12.5rem;">_string to be parsed

Outputs (to Stata):

  hascolon'`<span style="padding-left: 12.5rem;">_0 or 1,
whether  `0'  had colon

 `0' <span style="padding-left: 12.5rem;">_original  `0' 
prior to colon {nobreak None}

  rhscmd'`<span style="padding-left: 12.5rem;">_original
 `0'  to the right of the colon ("" if no colon)

(Syntax is shown in Stata format because `_parse_colon()` is intended
for use from Stata ado-files. Arguments are names of local macros to be
created. Mata function `_parse_colon()` is in fact `void`, and each
argument is `string scalar`.)
