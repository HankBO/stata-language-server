## Syntax

: `mata query`

: `mata set matacache`<span class="nowrap"> _ `#` \[`,`
`permanently` \]

: `mata set matalnum`<span class="nowrap"> _ <span
options="-(">{c -(}_`off` \| `on`}

: `mata set mataoptimize` {`on` \|
`off`}

: `mata set matafavor`<span class="nowrap"> _ <span
options="-(">{c -(}_`space` \| `speed`<span options=")-">{c
)-}_ \[`, permanently` \]

: `mata set matastrict`<span class="nowrap"> _ <span
options="-(">{c -(}_`off` \| `on`}
\[`, permanently` \]

: `mata set matalibs`<span class="nowrap"> _
`"libname;libname;`...`"`

: `mata set matamofirst`<span class="nowrap"> _ <span
options="-(">{c -(}_`off` \| `on`}
\[`, permanently` \]

These commands are for use in Mata mode following Mata's colon prompt.
To use these commands from Stata's dot prompt, type

`mata: mata querymata: mata set`
