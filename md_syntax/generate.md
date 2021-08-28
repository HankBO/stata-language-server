## Syntax

Create new variable

`generate` _\[`type`\] \[_
[newvar](http://www.stata.com/help.cgi?newvar)\[`:lblname`\]
`=exp` _\[`if`\] \[`in`\]_ \[`,`
`before(varname)` \| `after(varname)`\]

Replace contents of existing variable

`replace oldvar =exp` _\[`if`\]
\[`in`\]_ \[`, nopromote`\]

Specify default storage type assigned to new variables

`set type` {`float`|`double`} \[`, permanently`\]

where `type` is one of  
`byte`|`int`|`long`|`float`<span
options="|">{c \|}_`double`|`str`|`str1`|`str2`|...|`str{ccl maxstrvarlen}`

See
[<var class="command">Description</var><strong></strong>](#description)
below for an explanation of `str`. For the other types, see
[<strong>[D]</strong> data types](http://www.stata.com/help.cgi?data_types).

`by` is allowed with `generate` and `replace`; see
[<strong>[D]</strong> by](http://www.stata.com/help.cgi?by).
