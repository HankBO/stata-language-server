## Syntax

One-sample t test

`ttest`
[varname](http://www.stata.com/help.cgi?varname)
`== #` _\[`if`\] \[`in`\]_ \[`,`
`level(#)`\]

Two-sample t test using groups

`ttest`
[varname](http://www.stata.com/help.cgi?varname)
_\[`if`\] \[`in`\]_ `, by(groupvar)`
\[`options1`\]

Two-sample t test using variables

`ttest`
[varname1](http://www.stata.com/help.cgi?varname)
`==`
[varname2](http://www.stata.com/help.cgi?varname)
_\[`if`\] \[`in`\]_`, unpaired` \[`unequal`
`welch level(#)`\]

Paired t test

`ttest`
[varname1](http://www.stata.com/help.cgi?varname)
`==`
[varname2](http://www.stata.com/help.cgi?varname)
_\[`if`\] \[`in`\]_ \[`, level(#)`\]

Immediate form of one-sample t test

`ttesti #obs #mean #sd #val` \[`, level(#)`\]

Immediate form of two-sample t test

`ttesti #obs1 #mean1 #sd1 #obs2 #mean2 #sd2` \[`,`
`options2`\]

| options1                       |                | Description                                  |
|--------------------------------|----------------|----------------------------------------------|
| Main                           |                |                                              |
| \*                             | `by(groupvar)` | variable defining the groups                 |
|                                | `unequal`      | unpaired data have unequal variances         |
|                                | `welch`        | use Welch's approximation                    |
|                                | `level(#)`     | set confidence level; default is `level(95)` |
| \* `by(groupvar)` is required. |                |                                              |

| options2 |            | Description                                  |
|----------|------------|----------------------------------------------|
| Main     |            |                                              |
|          | `unequal`  | unpaired data have unequal variances         |
|          | `welch`    | use Welch's approximation                    |
|          | `level(#)` | set confidence level; default is `level(95)` |

`by` is allowed with `ttest`; see
[<strong>[D]</strong> by](http://www.stata.com/help.cgi?by).
