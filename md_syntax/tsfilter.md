## Syntax

Filter one variable

`tsfilter filter` _\[`type`\] \[_
[newvar](http://www.stata.com/help.cgi?newvar)
`=`
[<var class="command">varname</var><strong></strong>](http://www.stata.com/help.cgi?varname)
_\[`if`\] \[`in`\]_ \[`, options`\]

Filter multiple variables, unique names

`tsfilter filter` _\[`type`\] \[_
[<var class="command">newvarlist</var><strong></strong>](http://www.stata.com/help.cgi?newvarlist)
`=`
[<var class="command">varlist</var><strong></strong>](http://www.stata.com/help.cgi?varlist)
_\[`if`\] \[`in`\]_ \[`, options`\]

Filter multiple variables, common name stub

`tsfilter filter` _\[`type`\] \[_ `stub*`
`=`
[<var class="command">varlist</var><strong></strong>](http://www.stata.com/help.cgi?varlist)
_\[`if`\] \[`in`\]_ \[`, options`\]

|                                                                                                                                                                                                                                                                     |          |                                                                                                                                                               |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                                                                                                                                                                                                                     | `filter` | Name<span options="20">{space 20}_See help for                                                                                                          |
|                                                                                                                                                                                                                                                                     | `bk`     | Baxter-King<span options="13">{space 13}_[<strong>tsfilter bk</strong>](http://www.stata.com/help.cgi?tsfilter%20bk)         |
|                                                                                                                                                                                                                                                                     | `bw`     | Butterworth<span options="13">{space 13}_[<strong>tsfilter bw</strong>](http://www.stata.com/help.cgi?tsfilter%20bw)         |
|                                                                                                                                                                                                                                                                     | `cf`     | Christiano-Fitzgerald<span options="3">{space 3}_[<strong>tsfilter cf</strong>](http://www.stata.com/help.cgi?tsfilter%20cf) |
|                                                                                                                                                                                                                                                                     | `hp`     | Hodrick-Prescott<span options="8">{space 8}_[<strong>tsfilter hp</strong>](http://www.stata.com/help.cgi?tsfilter%20hp)      |
| You must `tsset` or `xtset` your data before using `tsfilter`; see [<strong>[TS]</strong> tsset](http://www.stata.com/help.cgi?tsset) and [<strong>[XT]</strong> xtset](http://www.stata.com/help.cgi?xtset). |          |                                                                                                                                                               |
| `varname` and `varlist` may contain time-series operators; see [<strong>tsvarlist</strong>](http://www.stata.com/help.cgi?tsvarlist).                                                                                                    |          |                                                                                                                                                               |
| `options` differ across the filters and are documented in each `filter`'s manual entry.                                                                                                                                                                             |          |                                                                                                                                                               |
