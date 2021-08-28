## Syntax

Return results for general commands, stored in r()

`return list` \[`, all`\]

`return clear`

`return scalar name = exp`

`return local name = exp`

`return local name` \[`"`\]`string`\[`"`\]

`return matrix name` \[`=`\] `matname` \[`, copy`\]

`return add`

`ereturn list` \[`, all`\]

`ereturn clear`

`ereturn post` \[`b` \[`V` \[`Cns`\]\]\] \[`weight`\] \[`,`
`depname:(string) obs:(#) dof:(#)`
`esample:(`[varname](http://www.stata.com/help.cgi?varname)`)`
`properties(string)`\]

`ereturn scalar name = exp`

`ereturn local name = exp`

`ereturn local name` \[`"`\]`string`\[`"`\]

`ereturn matrix name` \[`=`\] `matname` \[`, copy`\]

`ereturn repost` \[`b = b`\] \[`V = V`\] \[`Cns = Cns`\]
\[`weight`\] \[`,`
`esample:(`[varname](http://www.stata.com/help.cgi?varname)`)`
`properties(string) rename`\]

Return results for parsing commands, stored in s()

`sreturn list`

`sreturn clear`

`sreturn local name = exp`

`sreturn local name` \[`"`\]`string`\[`"`\]

where `b`, `V`, and `Cns` are `matname`s, which is the name of an
existing matrix.

`fweight`s, `aweight`s, `iweight`s, and `pweight`s are allowed; see
[<strong>weight</strong>](http://www.stata.com/help.cgi?weight).
