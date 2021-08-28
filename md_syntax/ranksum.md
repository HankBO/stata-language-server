## Syntax

Wilcoxon rank-sum test

`ranksum`
[varname](http://www.stata.com/help.cgi?varname)
_\[`if`\] \[`in`\]_`, by(groupvar)`
\[`porder`\]

Nonparametric equality-of-medians test

`median`
[varname](http://www.stata.com/help.cgi?varname)
_\[`if`\] \[`in`\]_ \[`weight`\] `,`
`by(groupvar)` \[`median_options`\]

| ranksum\_options |                | Description                                                                        |
|------------------|----------------|------------------------------------------------------------------------------------|
| Main             |                |                                                                                    |
| \*               | `by(groupvar)` | grouping variable                                                                  |
|                  | `porder`       | probability that variable for first group is larger than variable for second group |

| median\_options                                                                                                                          |                     | Description                                                     |
|------------------------------------------------------------------------------------------------------------------------------------------|---------------------|-----------------------------------------------------------------|
| Main                                                                                                                                     |                     |                                                                 |
| \*                                                                                                                                       | `by(groupvar)`      | grouping variable                                               |
|                                                                                                                                          | `exact`             | performs Fisher's exact test                                    |
|                                                                                                                                          | `medianties(below)` | assign values equal to the median to below group                |
|                                                                                                                                          | `medianties(above)` | assign values equal to the median to above group                |
|                                                                                                                                          | `medianties(drop)`  | drop values equal to the median from the analysis               |
|                                                                                                                                          | `medianties(split)` | split values equal to the median equally between the two groups |
| \* `by(groupvar)` is required.                                                                                                           |                     |                                                                 |
| `by` is allowed with `ranksum` and `median`; see [<strong>[D]</strong> by](http://www.stata.com/help.cgi?by). |                     |                                                                 |
| `fweight`s are allowed with `median`; see [<strong>weight</strong>](http://www.stata.com/help.cgi?weight).    |                     |                                                                 |
