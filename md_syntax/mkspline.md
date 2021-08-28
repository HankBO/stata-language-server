## Syntax

Linear spline with knots at specified points

`mkspline newvar_1 #1` \[`newvar_2 #2` \[`...`\]\] `newvar_k =`
`oldvar` _\[`if`\] \[`in`\]_ \[`, marginal`
`displayknots`\]

Linear spline with knots equally spaced or at percentiles of data

`mkspline stubname # = oldvar` _\[`if`\]
\[`in`\]_ \[`weight`\] \[`, marginal pctile displayknots`\]

Restricted cubic spline

`mkspline stubname = oldvar` _\[`if`\]
\[`in`\]_ \[`weight`\] `, cubic` \[`nknots(#) knots(numlist)`
`displayknots`\]

`fweight`s are allowed with the second and third syntax; see
[<strong>weight</strong>](http://www.stata.com/help.cgi?weight).
