## Syntax

`mi impute logit ivar` \[`indepvars`\] \[`if`\] \[`weight`\] \[`,`
`impute_options options`\]

| options                                                                                                                                                                           |                    | Description                                                        |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------|--------------------------------------------------------------------|
| Main                                                                                                                                                                              |                    |                                                                    |
|                                                                                                                                                                                   | `noconstant`       | suppress constant term                                             |
|                                                                                                                                                                                   | `offset(varname)`  | include `varname` in model with coefficient constrained to 1       |
|                                                                                                                                                                                   | `augment`          | perform augmented regression in the presence of perfect prediction |
|                                                                                                                                                                                   | `conditional(if)`  | perform conditional imputation                                     |
|                                                                                                                                                                                   | `bootstrap`        | estimate model parameters using sampling with replacement          |
| Maximization                                                                                                                                                                      |                    |                                                                    |
|                                                                                                                                                                                   | `maximize_options` | control the maximization process; seldom used                      |
| You must `mi set` your data before using `mi impute logit`; see [<strong>[MI]</strong> mi set](http://www.stata.com/help.cgi?mi_set).              |                    |                                                                    |
| You must `mi register ivar` as imputed before using `mi impute logit`; see [<strong>[MI]</strong> mi set](http://www.stata.com/help.cgi?mi_set). |                    |                                                                    |
| `indepvars` may contain factor variables; see [<strong>fvvarlist</strong>](http://www.stata.com/help.cgi?fvvarlist).                                   |                    |                                                                    |
| `fweight`s, `iweight`s, and `pweight`s are allowed; see [<strong>weight</strong>](http://www.stata.com/help.cgi?weight).                               |                    |                                                                    |
