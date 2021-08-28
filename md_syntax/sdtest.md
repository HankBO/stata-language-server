## Syntax

One-sample variance-comparison test

`sdtest`<span options="2">{space
2}_[varname](http://www.stata.com/help.cgi?varname)
`== #` _\[`if`\] \[`in`\]_ \[`,`
`level(#)`\]

Two-sample variance-comparison test using groups

`sdtest`<span options="2">{space
2}_[varname](http://www.stata.com/help.cgi?varname)
_\[`if`\] \[`in`\]_ `, by(groupvar)`
\[`level(#)`\]

Two-sample variance-comparison test using variables

`sdtest`<span options="2">{space
2}_[varname1](http://www.stata.com/help.cgi?varname)
`==`
[varname2](http://www.stata.com/help.cgi?varname)
_\[`if`\] \[`in`\]_ \[`, level(#)`\]

Immediate form of one-sample variance-comparison test

`sdtesti #obs` {`#mean` \| `.` <span
options=")-">{c )-}_ `#sd #val` \[`, level(#)`\]

Immediate form of two-sample variance-comparison test

`sdtesti #obs1` {`#mean1` \| `.` <span
options=")-">{c )-}_ `#sd1 #obs2` <span options="-(">{c
-(}_`#mean2` \| `.` } `#sd2` \[`,`
`level(#)`\]

Robust tests for equality of variances

`robvar`<span options="2">{space
2}_[varname](http://www.stata.com/help.cgi?varname)
_\[`if`\] \[`in`\]_ `, by(groupvar)`

`by` is allowed with `sdtest` and `robvar`; see
[<strong>[D]</strong> by](http://www.stata.com/help.cgi?by).
