## Syntax

`serset create`
[varlist](http://www.stata.com/help.cgi?varlist)
_\[`if`\] \[`in`\]_ \[`, omitanymiss`
`omitallmiss omitdupmiss omitnothing sort(varlist)`\]

`serset create_xmedians svn_y svn_x` \[`svn_w`\] \[`,`
`bands(#) xmin(#) xmax(#) logx logy`\]

`serset create_cspline svn_y svn_x` \[`, n(#)`\]

`serset` \[`set`\] `#_s`

`serset sort` \[`svn` \[`svn` \[...\]\]\]

`serset summarize svn` \[`, detail` \]

`serset`

`serset use` \[`, clear` \]

`serset reset_id #_s`

`serset drop` \[`numlist` \| `_all`\]

`serset clear`

`serset dir`

The
[<strong>file</strong>](http://www.stata.com/help.cgi?file)
command is also extended to allow

`file sersetwrite handle`

`file sersetread handle`

The following
[<strong>extended macro functions</strong>](http://www.stata.com/help.cgi?macro)
are also available:

------------------------------------------------------------------------

`: serset id: serset k: serset N: serset varnumsvnsvnumsvn: serset typesvnsvn: serset formatsvnsvn: serset varnamessvns: serset minsvnsvn: serset maxsvnsvn`

------------------------------------------------------------------------

`localmacname:serset set`

In the above syntax diagrams,

`#_s` refers to a serset number, 0

`#_s`

1,999.

[varlist](http://www.stata.com/help.cgi?varlist)
refers to the usual Stata varlist, that is, a list of variables that
appear in the current dataset, not the current serset.

`svn` refers to a variable in a serset. The variable may be referred to
by either its name (for example, `mpg` or `l.gnp`) or its number (for
example, 1 or 5); which is used makes no difference.

`svnum` refers to a variable number in a serset.
