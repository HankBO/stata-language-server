## Syntax

Preestimation syntax

`varsoc`
[depvarlist](http://www.stata.com/help.cgi?depvarlist)
_\[`if`\] \[`in`\]_ \[`,`
`preestimation_options`\]

Postestimation syntax

`varsoc` \[`, estimates(estname)`\]

| preestimation\_options                                                                                                                                      |                            | Description                                                                  |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------|------------------------------------------------------------------------------|
| Main                                                                                                                                                        |                            |                                                                              |
|                                                                                                                                                             | `maxlag(#)`                | set maximum lag order to `#`; default is `maxlag(4)`                         |
|                                                                                                                                                             | `exog(varlist)`            | use `varlist` as exogenous variables                                         |
|                                                                                                                                                             | `constraints(constraints)` | apply constraints to exogenous variables                                     |
|                                                                                                                                                             | `noconstant`               | suppress constant term                                                       |
|                                                                                                                                                             | `lutstats`                 | use L<span options="u">{c u}_tkepohl's version of information criteria |
|                                                                                                                                                             | `level(#)`                 | set confidence level; default is `level(95)`                                 |
|                                                                                                                                                             | `separator(#)`             | draw separator line after every `#` rows                                     |
| You must `tsset` your data before using `varsoc`; see [<strong>[TS] tsset</strong>](http://www.stata.com/help.cgi?tsset).        |                            |                                                                              |
| `by` is allowed with the preestimation version of `varsoc`; see [<strong>prefix</strong>](http://www.stata.com/help.cgi?prefix). |                            |                                                                              |
