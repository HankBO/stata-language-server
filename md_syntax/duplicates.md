## Syntax

Report duplicates

`duplicates report`
\[[varlist](http://www.stata.com/help.cgi?varlist)\]
_\[`if`\] \[`in`\]_

List one example for each group of duplicates

`duplicates examples`
\[[varlist](http://www.stata.com/help.cgi?varlist)\]
_\[`if`\] \[`in`\]_ \[`, options`\]

List all duplicates

`duplicates list`
\[[varlist](http://www.stata.com/help.cgi?varlist)\]
_\[`if`\] \[`in`\]_ \[`, options`\]

Tag duplicates

`duplicates tag`
\[[varlist](http://www.stata.com/help.cgi?varlist)\]
_\[`if`\] \[`in`\]_ `, generate(newvar)`

Drop duplicates

`duplicates drop` _\[`if`\] \[`in`\]_

`duplicates drop`
[varlist](http://www.stata.com/help.cgi?varlist)
_\[`if`\] \[`in`\]_ `, force`

| Options  |                                                                                                 | Description                                                                                                                        |
|----------|-------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|
| Main     |                                                                                                 |                                                                                                                                    |
|          | `compress`                                                                                      | compress width of columns in both table and display formats                                                                        |
|          | `nocompress`                                                                                    | use display format of each variable                                                                                                |
|          | `fast`                                                                                          | synonym for `nocompress`; no delay in output of large datasets                                                                     |
|          | `abbreviate(#)`                                                                                 | abbreviate variable names to `#` characters; default is `ab(8)`                                                                    |
|          | `string(#)`                                                                                     | truncate string variables to `#` characters; default is `string(10)`                                                               |
| Options  |                                                                                                 |                                                                                                                                    |
|          | `table`                                                                                         | force table format                                                                                                                 |
|          | `display`                                                                                       | force display format                                                                                                               |
|          | `header`                                                                                        | display variable header once; default is table mode                                                                                |
|          | `noheader`                                                                                      | suppress variable header                                                                                                           |
|          | `header(#)`                                                                                     | display variable header every `#` lines                                                                                            |
|          | `clean`                                                                                         | force table format with no divider or separator lines                                                                              |
|          | `divider`                                                                                       | draw divider lines between columns                                                                                                 |
|          | `separator(#)`                                                                                  | draw a separator line every `#` lines; default is `separator(5)`                                                                   |
|          | `sepby(varlist)`                                                                                | draw a separator line whenever `varlist` values change                                                                             |
|          | `nolabel`                                                                                       | display numeric codes rather than label values                                                                                     |
| Summary  |                                                                                                 |                                                                                                                                    |
|          | `mean`\[`(`[varlist](http://www.stata.com/help.cgi?varlist)`)`\]     | add line reporting the mean for each of the (specified) variables                                                                  |
|          | `sum`\[`(`[varlist](http://www.stata.com/help.cgi?varlist)`)`\]      | add line reporting the sum for each of the (specified) variables                                                                   |
|          | `N`\[`(`[varlist](http://www.stata.com/help.cgi?varlist)`)`\]        | add line reporting the number of nonmissing values for each of the (specified) variables                                           |
|          | `labvar(varname)`                                                                               | substitute `Mean`, `Sum`, or `N` for value of `varname` in last row of table                                                       |
| Advanced |                                                                                                 |                                                                                                                                    |
|          | `constant`\[`(`[varlist](http://www.stata.com/help.cgi?varlist)`)`\] | separate and list variables that are constant only once                                                                            |
|          | `notrim`                                                                                        | suppress string trimming                                                                                                           |
|          | `absolute`                                                                                      | display overall observation numbers when using `by` [varlist](http://www.stata.com/help.cgi?varlist)`:` |
|          | `nodotz`                                                                                        | display numerical values equal to `.z` as field of blanks                                                                          |
|          | `subvarname`                                                                                    | substitute characteristic for variable name in header                                                                              |
|          | `linesize(#)`                                                                                   | columns per line; default is `linesize(79)`                                                                                        |
