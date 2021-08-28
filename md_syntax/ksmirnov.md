## Syntax

One-sample Kolmogorov-Smirnov test

`ksmirnov`
[varname](http://www.stata.com/help.cgi?varname)
`= exp` _\[`if`\] \[`in`\]_

Two-sample Kolmogorov-Smirnov test

`ksmirnov`
[varname](http://www.stata.com/help.cgi?varname)
_\[`if`\] \[`in`\]_ `, "by(groupvar)`
\[`exact`\]

In the first syntax,
[varname](http://www.stata.com/help.cgi?varname)
is the variable whose distribution is being tested, and `exp` must
evaluate to the corresponding (theoretical) cumulative. In the second
syntax, `groupvar` must take on two distinct values. The distribution of
`varname` for the first value of `groupvar` is compared with that of the
second value.
