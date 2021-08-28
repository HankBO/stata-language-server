## Syntax

`pwmean`
[varname](http://www.stata.com/help.cgi?varname)`,`
`over(varlist)` \[`options`\]

| Options                                                                                                                                                                   |                          | Description                                                                                               |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------|-----------------------------------------------------------------------------------------------------------|
| Main                                                                                                                                                                      |                          |                                                                                                           |
| \*                                                                                                                                                                        | `over(varlist)`      | compare means across each combination of the levels in `varlist`                                          |
|                                                                                                                                                                           | `mcompare(method)` | adjust for multiple comparisons; default is `mcompare(noadjust)`                                          |
| Reporting                                                                                                                                                                 |                          |                                                                                                           |
|                                                                                                                                                                           | `level(#)`               | confidence level; default is `level(95)`                                                                  |
|                                                                                                                                                                           | `cieffects`              | display a table of mean differences and confidence intervals; the default                                 |
|                                                                                                                                                                           | `pveffects`              | display a table of mean differences and p-values                                                          |
|                                                                                                                                                                           | `effects`                | display a table of mean differences with p-values and confidence intervals                                |
|                                                                                                                                                                           | `cimeans`                | display a table of means and confidence intervals                                                         |
|                                                                                                                                                                           | `groups`                 | display a table of means with codes that group them with other means that are not significantly different |
|                                                                                                                                                                           | `sort`                   | sort results tables by displayed mean or difference                                                       |
|                                                                                                                                                                           | `display_options`        | control column formats, line width, and factor-variable labeling                                          |
| \*`over(varlist)` is required.                                                                                                                                            |                          |                                                                                                           |
| See [<strong>[R]</strong> pwmean postestimation](http://www.stata.com/help.cgi?pwmean_postestimation) for features available after estimation. |                          |                                                                                                           |

| method |              | Description                                         |
|--------|--------------|-----------------------------------------------------|
|        | `noadjust`   | do not adjust for multiple comparisons; the default |
|        | `bonferroni` | Bonferroni's method                                 |
|        | `sidak`      | Sidak's method                                      |
|        | `scheffe`    | Scheffe's method                                    |
|        | `tukey`      | Tukey's method                                      |
|        | `snk`        | Student-Newman-Keuls's method                       |
|        | `duncan`     | Duncan's method                                     |
|        | `dunnett`    | Dunnett's method                                    |
