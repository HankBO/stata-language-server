## Syntax

`stack`
[varlist](http://www.stata.com/help.cgi?varlist)
_\[`if`\] \[`in`\]_ `,` <span options="-(">{c
-(}_`into(newvars)`\|`group(#)`<span options=")-">{c
)-}_ \[`options`\]

| Options                                              |                 | Description                                                                                                                       |
|------------------------------------------------------|-----------------|-----------------------------------------------------------------------------------------------------------------------------------|
| Main                                                 |                 |                                                                                                                                   |
| \*                                                   | `into(newvars)` | identify names of new variables to be created                                                                                     |
| \*                                                   | `group(#)`      | stack `#` groups of variables in [varlist](http://www.stata.com/help.cgi?varlist)                      |
|                                                      | `clear`         | clear dataset from memory                                                                                                         |
|                                                      | `wide`          | keep variables in [varlist](http://www.stata.com/help.cgi?varlist) that are not specified in `newvars` |
| \* Either `into(newvars)` or `group(#)` is required. |                 |                                                                                                                                   |
