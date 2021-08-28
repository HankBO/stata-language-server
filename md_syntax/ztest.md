## Syntax

One-sample z test

`ztest`
[varname](http://www.stata.com/help.cgi?varname)
`== #` _\[`if`\] \[`in`\]_ \[`,`
`onesampleopts`\]

Two-sample z test using groups

`ztest`
[varname](http://www.stata.com/help.cgi?varname)
_\[`if`\] \[`in`\]_ `, by(groupvar)`
\[`twosamplegropts`\]

Two-sample z test using variables

`ztest`
[varname1](http://www.stata.com/help.cgi?varname)
`==`
[varname2](http://www.stata.com/help.cgi?varname)
_\[`if`\] \[`in`\]_`, unpaired`
\[`twosamplevaropts`\]

Paired z test

`ztest`
[varname1](http://www.stata.com/help.cgi?varname)
`==`
[varname2](http://www.stata.com/help.cgi?varname)
_\[`if`\] \[`in`\]_ `, sddiff(#)`
\[`level(#)`\]

`ztest`
[varname1](http://www.stata.com/help.cgi?varname)
`==`
[varname2](http://www.stata.com/help.cgi?varname)
_\[`if`\] \[`in`\]_ `, corr(#)`
\[`pairedopts`\]

Immediate form of one-sample z test

`ztesti #obs #mean #sd #val` \[`, level(#)`\]

Immediate form of two-sample unpaired z test

`ztesti #obs1 #mean1 #sd1 #obs2 #mean2 #sd2` \[`,`
`level(#)`\]

| onesampleopts |                    | Description                                           |
|---------------|--------------------|-------------------------------------------------------|
| Main          |                    |                                                       |
|               | `sd(#)`            | one-population standard deviation; default is `sd(1)` |
|               | `level(#)`         | confidence level; default is `level(95)`              |
|               | `cluster(varname)` | variable defining the clusters                        |
|               | `rho(#)`           | intraclass correlation                                |

| twosamplegropts                |                    | Description                                                                                       |
|--------------------------------|--------------------|---------------------------------------------------------------------------------------------------|
| Main                           |                    |                                                                                                   |
| \*                             | `by(groupvar)`     | variable defining the groups                                                                      |
|                                | `unpaired`         | unpaired test; implied when `by()` is specified                                                   |
|                                | `sd(#)`            | two-population common standard deviation; default is `sd(1)`                                      |
|                                | `sd1(#)`           | standard deviation of the first population; requires `sd2()` and may not be combined with `sd()`  |
|                                | `sd2(#)`           | standard deviation of the second population; requires `sd1()` and may not be combined with `sd()` |
|                                | `level(#)`         | confidence level; default is `level(95)`                                                          |
|                                | `cluster(varname)` | variable defining the clusters                                                                    |
|                                | `rho(#)`           | common intraclass correlation                                                                     |
|                                | `rho1(#)`          | intraclass correlation for group 1                                                                |
|                                | `rho2(#)`          | intraclass correlation for group 2                                                                |
| \* `by(groupvar)` is required. |                    |                                                                                                   |

| twosamplevaropts           |            | Description                                                                                       |
|----------------------------|------------|---------------------------------------------------------------------------------------------------|
| Main                       |            |                                                                                                   |
| \*                         | `unpaired` | unpaired test                                                                                     |
|                            | `sd(#)`    | two-population common standard deviation; default is `sd(1)`                                      |
|                            | `sd1(#)`   | standard deviation of the first population; requires `sd2()` and may not be combined with `sd()`  |
|                            | `sd2(#)`   | standard deviation of the second population; requires `sd1()` and may not be combined with `sd()` |
|                            | `level(#)` | confidence level; default is `level(95)`                                                          |
| \* `unpaired` is required. |            |                                                                                                   |

| pairedopts                |            | Description                                                                                                                  |
|---------------------------|------------|------------------------------------------------------------------------------------------------------------------------------|
| Main                      |            |                                                                                                                              |
| \*                        | `corr(#)`  | correlation between paired observations                                                                                      |
|                           | `sd(#)`    | two-population common standard deviation; default is `sd(1)`; may not be combined with `sd1()`, `sd2()`, or `sddiff()`       |
|                           | `sd1(#)`   | standard deviation of the first population; requires `corr()` and `sd2()` and may not be combined with `sd()` or `sddiff()`  |
|                           | `sd2(#)`   | standard deviation of the second population; requires `corr()` and `sd1()` and may not be combined with `sd()` or `sddiff()` |
|                           | `level(#)` | confidence level; default is `level(95)`                                                                                     |
| \* `corr(#)` is required. |            |                                                                                                                              |

`by` is allowed with `ztest`; see
[<strong>[D]</strong> by](http://www.stata.com/help.cgi?by).
