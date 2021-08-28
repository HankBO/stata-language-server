## Syntax

`mi impute regress ivar` \[`indepvars`\] \[`if`\] \[`weight`\]
\[`, impute_options options`\]

| options                                                                                                                                                                             |                   | Description                                               |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|-----------------------------------------------------------|
| Main                                                                                                                                                                                |                   |                                                           |
|                                                                                                                                                                                     | `noconstant`      | suppress constant term                                    |
|                                                                                                                                                                                     | `conditional(if)` | perform conditional imputation                            |
|                                                                                                                                                                                     | `bootstrap`       | estimate model parameters using sampling with replacement |
| You must `mi set` your data before using `mi impute regress`; see [<strong>[MI]</strong> mi set](http://www.stata.com/help.cgi?mi_set).              |                   |                                                           |
| You must `mi register ivar` as imputed before using `mi impute regress`; see [<strong>[MI]</strong> mi set](http://www.stata.com/help.cgi?mi_set). |                   |                                                           |
| `indepvars` may contain factor variables; see [<strong>fvvarlist</strong>](http://www.stata.com/help.cgi?fvvarlist).                                     |                   |                                                           |
| `aweight`s, `fweight`s, `iweight`s, and `pweight`s are allowed; see [<strong>weight</strong>](http://www.stata.com/help.cgi?weight).                     |                   |                                                           |
