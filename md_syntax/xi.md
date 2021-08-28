## Syntax

`xi` \[`, prefix(string) noomit`\] `term(s)`

`xi` \[`, prefix(string) noomit`\] `: any_stata_command`
`varlist_with_terms ...`

where a `term` has the form

`i.varname`<span style="padding-left: 19.5rem;">_or<span
style="padding-left: 24.0rem;">_`I.varname`

`i.varname1*i.varname2`<span
style="padding-left: 24.0rem;">_`I.varname1*I.varname2`

`i.varname1*varname3`<span
style="padding-left: 24.0rem;">_`I.varname1*varname3`

`i.varname1|varname3`<span
style="padding-left: 24.0rem;">_`I.varname1|varname3`

`varname`, `varname1`, and `varname2` denote numeric or string
categorical variables. `varname3` denotes a continuous, numeric
variable.
