## Syntax

`sem`\|`gsem` ... \[`,` ...
`reliability(`[varname](http://www.stata.com/help.cgi?varname)
`#`
\[[varname](http://www.stata.com/help.cgi?varname)
`#` \[...\]\]`)`\]

where `varname` is the name of an observed variable and `#` is the
fraction or percentage of variance not due to measurement error:

{cmd:. {sem\|gsem} ..., ... reliability(x1 .8 x2 .9)}{p\_end}

{cmd:. {sem\|gsem} ..., ... reliability(x1 80% x2 90%)}{p\_end}
