## Syntax

`storedresults save` <span options="3">{space 3}_ `name`
{`r()`\|`e()`}

`storedresults compare name` {`r()`\|`e()`} \[`,`
`tolerance:(#) reverse verbose exclude:(list)`
`include:(list)` \]

`storedresults drop` <span options="3">{space 3}_ `name`

where list is

`class: name` \[`name` \[`...`\]\] \[`list`\]

and `class` is `macro`, `macros`, `matrix`, `matrices`, `scalar`, or
`scalars`.

This command is intended for authors of certification scripts --
do-files used to test that commands work properly; see
[<strong>[P]</strong> cscript](http://www.stata.com/help.cgi?cscript).
