## Syntax

`global`<span options="3">{space 3}_`mname` <span
options="1">{space 1}_ \[`=exp` \| `:extended_fcn` \|
`"`\[`string`\]`"` \|   "`\[`string`\]`"'`\]

`local`<span options="4">{space 4}_`lclname` \[`=exp` \|
`:extended_fcn` \| `"`\[`string`\]`"` \|
  "`\[`string`\]`"'`\]

`tempvar`<span options="2">{space 2}_`lclname` \[`lclname`
\[`...`\]\]

`tempname lclname` \[`lclname` \[`...`\]\]

`tempfile lclname` \[`lclname` \[`...`\]\]

`local` { `++lclname` \| `--lclname`
}

`macro dir`

`macro drop` { `mname` \[`mname`
\[`...`\]\] \| `mname*` \| `_all` }

`macro list` \[ `mname` \[`mname` \[`...`\]\] \| `_all` \]

`macro shift` \[`#`\]

\[`...`\]   expansion_optr'` \[`...`\]

where `expansion_optr` is

`lclname`  
`++lclname`  
`lclname++`  
`--lclname`  
`lclname--`  
`=exp`  
`:extended_fcn`  
`.class_directive`  
`macval(lclname)`
