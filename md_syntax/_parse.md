## Syntax

`_parse expand lcstub lgstub :`<span options="1">{space
1}_`lin` \[`, common:(opnamelist) gweight` \]

`_parse canonicalize lres :`<span options="1">{space
1}_`lcstub lgstub` \[`, drop gweight` \]

`_parse factor lnew :`<span options="1">{space 1}_`lold,`
`option:(OPname)` \[ `to(strXing) n(#) rmquotes` \]

`_parse factordot lnew :`<span options="1">{space
1}_`lold, n(#)`

`_parse combine lnew :`<span options="1">{space 1}_`lold`

`_parse combop lnew :`<span options="1">{space 1}_`lold,`
`option:(OPname)` \[ `opsin rightmost` \]

`_parse expandarg lnew :`<span options="1">{space
1}_`lold, n(#) option:(string)`

`_parse comma lhs rhs : lin`

where `lcstub` and `lgstub` are the stub of local macronames and `lin`,
`lres`, `lhs`, `rhs`, `lnew`, and `lold` are macronames,

and where

`opnamelist` := `op` \[`op` \[...\]\]

`op` := `OPname`  
`OPname(`\[`string`\]`)`
