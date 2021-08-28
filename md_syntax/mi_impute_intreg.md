## Syntax

`mi impute intreg newivar` \[`indepvars`\] \[`if`\] \[`weight`\]
\[`, impute_options options`\]

| options                                                                                                                                                               |                    | Description                                                  |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------|--------------------------------------------------------------|
| Main                                                                                                                                                                  |                    |                                                              |
|                                                                                                                                                                       | `noconstant`       | suppress constant term                                       |
| \*                                                                                                                                                                    | `ll(varname)`      | lower limit for interval censoring                           |
| \*                                                                                                                                                                    | `ul(varname)`      | upper limit for interval censoring                           |
|                                                                                                                                                                       | `offset(varname)`  | include `varname` in model with coefficient constrained to 1 |
|                                                                                                                                                                       | `conditional(if)`  | perform conditional imputation                               |
|                                                                                                                                                                       | `bootstrap`        | estimate model parameters using sampling with replacement    |
| Maximization                                                                                                                                                          |                    |                                                              |
|                                                                                                                                                                       | `maximize_options` | control the maximization process; seldom used                |
| \* `ll()` and `ul()` are required.                                                                                                                                    |                    |                                                              |
| You must `mi set` your data before using `mi impute intreg`; see [<strong>[MI]</strong> mi set](http://www.stata.com/help.cgi?mi_set). |                    |                                                              |
| `indepvars` may contain factor variables; see [<strong>fvvarlist</strong>](http://www.stata.com/help.cgi?fvvarlist).                       |                    |                                                              |
| `aweight`s, `fweight`s, `iweight`s, and `pweight`s are allowed; see [<strong>weight</strong>](http://www.stata.com/help.cgi?weight).       |                    |                                                              |
