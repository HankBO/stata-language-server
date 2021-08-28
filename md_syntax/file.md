## Syntax

`file open` <span options="1">{space 1}_`handle using`
`filename,` {`read`\|`write`\|`read`
`write`} \[ \[`text`\|`binary`\]
\[`replace`\|`append`\] `all` \]

`file read` <span options="1">{space 1}_`handle` \[`specs`\]

`file write handle` \[`specs`\]

`file seek` <span options="1">{space 1}_`handle` <span
options="-(">{c -(}_`query`\|`tof`\|`eof`\|`#`<span
options=")-">{c )-}_

`file set` <span options="2">{space 2}_`handle byteorder`
{`hilo`\|`lohi`\|`1`\|`2`<span
options=")-">{c )-}_

`file close` {`handle`\|`_all`<span
options=")-">{c )-}_

`file query`

where `specs` for `text` output is

`"string" " `string"'(exp)`

(parentheses are required)

[<strong>%</strong><var class="command">fmt</var><strong></strong>](http://www.stata.com/help.cgi?format)`(exp)`

(see
[<strong>[D]</strong> format](http://www.stata.com/help.cgi?format)
about `%fmt`)

`_skip(#)_column(#)_newline(#)_char(#)`

(`0`

`#`

`255`)

`_tab(#)_page(#)_dup(#)`

`specs` for `text` input is `localmacroname`,

`specs` for `binary` output is

`%`{`84`<span options=")-">{c
)-}_`z(exp)%`<span options="-(">{c
-(}_`421`<span options=")-">{c
)-}_`bsu(exp)%#s"text"`

(`1`

`#`

`max_macrolen`)

`%#s " `text"'%#s(exp)`

and `specs` for `binary` input is

`%`{`84`<span options=")-">{c
)-}_`zscalarname%`<span options="-(">{c
-(}_`421`<span options=")-">{c
)-}_`bsuscalarname%#slocalmacroname`

(`1`

`#`

`max_macrolen`)
