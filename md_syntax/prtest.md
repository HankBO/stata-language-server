## Syntax

One-sample test of proportion

`prtest`
[varname](http://www.stata.com/help.cgi?varname)
`== #p` _\[`if`\] \[`in`\]_ \[`,`
`onesampleopts`\]

Two-sample test of proportions using groups

`prtest`
[varname](http://www.stata.com/help.cgi?varname)
_\[`if`\] \[`in`\]_ `, "by(groupvar)`
\[`twosamplegropts`\]

Two-sample test of proportions using variables

`prtest varname1 == varname2` _\[`if`\]
\[`in`\]_ \[`, level(#)`\]

Immediate form of one-sample test of proportion

`prtesti #obs1 #p1 #p2` \[`, level(#) count`\]

Immediate form of two-sample test of proportions

`prtesti #obs1 #p1 #obs2 #p2` \[`, level(#) count`\]

| onesampleopts |                    | Description                              |
|---------------|--------------------|------------------------------------------|
| Main          |                    |                                          |
|               | `level(#)`         | confidence level; default is `level(95)` |
|               | `cluster(varname)` | variable defining the clusters           |
|               | `rho(#)`           | intraclass correlation                   |

| twosamplegropts                |                    | Description                              |
|--------------------------------|--------------------|------------------------------------------|
| Main                           |                    |                                          |
| \*                             | `by(groupvar)`     | variable defining the groups             |
|                                | `level(#)`         | confidence level; default is `level(95)` |
|                                | `cluster(varname)` | variable defining the clusters           |
|                                | `rho(#)`           | common intraclass correlation            |
|                                | `rho1(#)`          | intraclass correlation for group 1       |
|                                | `rho2(#)`          | intraclass correlation for group 2       |
| \* `by(groupvar)` is required. |                    |                                          |

`by` is allowed with `prtest`; see
[<strong>[D]</strong> by](http://www.stata.com/help.cgi?by).
