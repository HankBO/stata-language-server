## Syntax

`infix using dfilename` _\[`if`\]
\[`in`\]_ \[`, using(filename2) clear`\]

`infix specifications using filename` <span
class="command">\[`if`\] \[`in`\]_ \[`, clear`\]

If `dfilename` is specified without an extension, `.dct` is assumed. If
`dfilename` contains embedded spaces, remember to enclose it in double
quotes. `dfilename`, if it exists, contains

------------------------------------------------------------------------

------------------------------------------------------------------------

`infix dictionaryusingfilename{c -(}* comments preceded by* asterisk may appear freelyspecifications{c )-}(your data might appear here)`

------------------------------------------------------------------------

------------------------------------------------------------------------

If `filename` is specified without an extension, `.raw` is assumed. If
`filename` contains embedded spaces, remember to enclose it in double
quotes.

`specifications` is

`# firstlineoffile`

`# lines`

`#:`

`/`

\[`byte`\|`int`\|`float`\|`long`\|`double`\|`str`\] `varlist`
\[`#:`\]`#`\[`-#`\]
