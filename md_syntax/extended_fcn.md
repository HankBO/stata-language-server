## Syntax

{`local` \| `global`<span options=")-">{c
)-}_ `mname : extended_function`

where `extended_function` is any of the following:

Macro extended function for extracting program properties

`properties command`

Macro extended functions for extracting data attributes

`type`
[varname](http://www.stata.com/help.cgi?varname)

`format`
[varname](http://www.stata.com/help.cgi?varname)

`value label`
[varname](http://www.stata.com/help.cgi?varname)

`variable label`
[varname](http://www.stata.com/help.cgi?varname)

`data label`

`sortedby`

`label` { `valuelabelname` \|
`(`[varname](http://www.stata.com/help.cgi?varname)`)`
} {
`maxlength` \| `#` \[`#_2`\] } \[`,`
`strict` \]

`constraint` { `dir` \| `#` <span
options=")-">{c )-}_

`char` {
[varname](http://www.stata.com/help.cgi?varname)`[]`
\|
[varname](http://www.stata.com/help.cgi?varname)`[charname]`
}

`char` { `_dta[]` \| `_dta[charname]`
}

Macro extended function for naming variables

`permname suggestedname` \[`, length:(#)` \]

Macro extended functions for filenames and file paths

`adosubdir` \[`"`\]`filename`\[`"`\]

`dir` \[`"`\]`dirname`\[`"`\] <span options="-(">{c
-(}_`files`\|`dirs`\|`other`}
\[`"`\]`pattern`\[`"`\] \[`, nofail respectcase`\]

`sysdir` \[ `STATA` \| `BASE` \| `SITE` \| `PLUS` \| `PERSONAL` \|
`dirname` \]

Macro extended function for accessing operating-system parameters

`environment name`

Macro extended functions for names of stored results

`e(scalars` \| `macros` \| `matrices` \| `functions)`

`r(scalars` \| `macros` \| `matrices` \| `functions)`

`s(macros)`

`all` <span options="-(">{c
-(}_`globals`\|`scalars`\|`matrices`<span options=")-">{c
)-}_ \[`"pattern"`\]

`all` {`numeric`\|`string`<span
options=")-">{c )-}_ `scalars` \[`"pattern"`\]

Macro extended function for formatting results

`display display_directive`

Macro extended functions for manipulating lists

`list macrolist_directive`

Macro extended functions related to matrices

`rownames` <span options="3">{space 3}_ `matrixname`

`colnames` <span options="3">{space 3}_ `matrixname`

`rowfullnames matrixname`

`colfullnames matrixname`

`roweq` <span options="6">{space 6}_ `matrixname` \[`, quoted`
\]

`coleq` <span options="6">{space 6}_ `matrixname` \[`, quoted`
\]

`rownumb` <span options="4">{space 4}_ `matrixname string`

`colnumb` <span options="4">{space 4}_ `matrixname string`

`roweqnumb` <span options="2">{space 2}_ `matrixname string`

`coleqnumb` <span options="2">{space 2}_ `matrixname string`

`rownfreeparms` <span options="2">{space 2}_ `matrixname`

`colnfreeparms` <span options="2">{space 2}_ `matrixname`

`rownlfs` <span options="2">{space 2}_ `matrixname`

`colnlfs` <span options="2">{space 2}_ `matrixname`

`rowsof` <span options="2">{space 2}_ `matrixname`

`colsof` <span options="2">{space 2}_ `matrixname`

`rowvarlist` <span options="2">{space 2}_ `matrixname`

`colvarlist` <span options="2">{space 2}_ `matrixname`

`rowlfnames` <span options="2">{space 2}_ `matrixname` \[`,`
`quoted` \]

`collfnames` <span options="2">{space 2}_ `matrixname` \[`,`
`quoted` \]

Macro extended function related to time-series operators

`tsnorm string` \[`, varname` \]

Macro extended function for copying a macro

`copy` { `local` \| `global` <span
options=")-">{c )-}_ `mname`

Macro extended functions for parsing

`word count string`

`word # of string`

`piece #_1 #_2 of` \[ ` \]`"string"`\[`'`\] \[`,`
`nobreak` \]

`strlen` { `local` \| `global` <span
options=")-">{c )-}_ `mname`

`ustrlen` { `local` \| `global` <span
options=")-">{c )-}_ `mname`

`udstrlen` { `local` \| `global` <span
options=")-">{c )-}_ `mname`

`subinstr` { `local` \| `global` <span
options=")-">{c )-}_ `mname` \[ ` \]`"from"`\[`'`\]
\[ ` \]`"to"`\[`'`\] \[`, all word count:(`<span
options="-(">{c -(}_ `local` \| `global` <span options=")-">{c
)-}_ `mname)` \]
