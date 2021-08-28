## Syntax

Moving average with uniform weights

`tssmooth ma` _\[`type`\] \[_
[newvar](http://www.stata.com/help.cgi?newvar)
`= exp` _\[`if`\] \[`in`\]_`,`
`window(#l`\[`#c`\[`#f`\]\]`)` \[`replace`\]

Moving average with specified weights

`tssmooth ma` _\[`type`\] \[_
[newvar](http://www.stata.com/help.cgi?newvar)
`= exp` _\[`if`\] \[`in`\]_`,`
`weights(`\[`numlist_l`\] `<#c>` \[`numlist_f`\]`)` \[`replace`\]

You must `tsset` your data before using `tssmooth ma`;
[<strong>[TS] tsset</strong>](http://www.stata.com/help.cgi?tsset).

`exp` may contain time-series operators; see
[<strong>tsvarlist</strong>](http://www.stata.com/help.cgi?tsvarlist).
