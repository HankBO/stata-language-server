## Syntax

Syntax for one ancillary parameter:

`_diparm eqname` \[`,` \[ `exp` \| `tanh` \| `invlogit` \|
`function:(expr(@)) derivative:(expr(@))` \]
`label:(string) prob dof(#) level:(#) notab` \]

where `expr(@)` is an expression with `@` substituted for the parameter
`[eqname]_cons`.

Syntax for a parameter that is a function of 2-9 ancillary parameters:

`_diparm eqname1 eqname2` \[`eqname3` ...\] `,`
`function:(expr(@1,@2,...)) derivative:(expr1(@1,@2,...)`
`expr2(@1,@2,...)` ...`)` \[ `ci(logit` \| `probit` \| `atanh` \| `log)`
`label:(string) prob dof(#) level:(#) notab` \]

where `expr(@1,@2,...)` is an expression with `@1,@2,...` substituted
for the parameters `[eqname1]_cons`, `[eqname2]_cons`,....

Syntax for drawing a separator line:

`_diparm __sep__`

Syntax for drawing the bottom line:

`_diparm __bot__`

Syntax for adding a labeled row:

`_diparm __lab__, label(string)` \[ `eqlabel value(#)`
`comment(string)` \]
