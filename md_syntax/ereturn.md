## Syntax

`ereturnlocalname ...`{right None:(see
}[<strong>[P]</strong> macro](http://www.stata.com/help.cgi?macro))

`ereturn scalar name = exp`

`ereturn matrix name` \[`=`\] `matname` \[`, copy`\]

`ereturn clear`

`ereturn list` \[`, all`\]

`ereturn post` \[`b` \[`V` \[`Cns`\]\]\] \[`weight`\] \[`,`
`depname:(string) obs:(#) dof:(#)`
`esample:(`[varname](http://www.stata.com/help.cgi?varname)`)`
`properties:(string) buildfvinfo findomitted`\]

`ereturn repost` \[`b = b`\] \[`V = V`\] \[`Cns = Cns`\]
\[`weight`\] \[`,`
`esample:(`[varname](http://www.stata.com/help.cgi?varname)`)`
`properties:(string) buildfvinfo findomitted rename`
`resize`\]

`ereturn display` \[`, eform:(string) first neq(#)`
`plus level:(#) display_options`\]

where `name` is the name of the macro, scalar, or matrix that will be
returned in **e(**`name`**)** by the estimation program; `matname` is
the name of an existing matrix; `b` is a 1 x p coefficient vector
(matrix); `V` is a p x p covariance matrix; and `Cns` is a c x (p+1)
constraint matrix.

`fweight`s, `aweight`s, `iweight`s, and `pweight`s are allowed; see
[<strong>weight</strong>](http://www.stata.com/help.cgi?weight).
