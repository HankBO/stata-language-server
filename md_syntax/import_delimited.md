## Syntax

Load a delimited text file

`import delimited` \[`using`\] `filename` \[`,`
`import_delimited_options`\]

Rename specified variables from a delimited text file

`import delimited extvarlist using filename` \[`,`
`import_delimited_options`\]

Save data in memory to a delimited text file

`export delimited` \[`using`\] `filename` <span
class="command">\[`if`\] \[`in`\]_ \[`,`
`export_delimited_options`\]

Save subset of variables in memory to a delimited text file

`export delimited`
\[[varlist](http://www.stata.com/help.cgi?varlist)\]
`using filename` _\[`if`\] \[`in`\]_ \[`,`
`export_delimited_options`\]

If `filename` is specified without an extension, `.csv` is assumed for
both `import delimited` and `export delimited`. If `filename` contains
embedded spaces, enclose it in double quotes.

`extvarlist` specifies variable names of imported columns.

| import\_delimited\_options |                                                                                                                                 | Description                                                                      |
|----------------------------|---------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
|                            | `delimiters("chars"`\[`, collapse`\|`asstring`\]`)`                                                                       | use `chars` as delimiters                                                        |
|                            | `rowrange([start][:end])`                                                                                                       | row range of data to load                                                        |
|                            | `colrange([start][:end])`                                                                                                       | column range of data to load                                                     |
|                            | `varnames(#`\|`nonames)`                                                                                                      | treat row `#` of data as variable names or the data do not have variable names   |
|                            | `case(preserve`\|`lower`\|`upper)`                                                                                              | preserve the case or read variable names as lowercase (the default) or uppercase |
|                            | `asdouble`                                                                                                                      | import all floating-point data as `double`s                                      |
|                            | `asfloat`                                                                                                                       | import all floating-point data as `float`s                                       |
|                            | `clear`                                                                                                                         | replace data in memory                                                           |
|                            | `bindquotes(loose`\|`strict`\|`nobind)`                                                                                         | specify how to handle double quotes in data                                      |
|                            | `stripquotes(yes`\|`no`\|`default)`                                                                                             | remove or keep double quotes in data                                             |
|                            | `numericcols(numlist`\|`_all)`                                                                                                | force specified columns to be numeric                                            |
|                            | `stringcols(numlist`\|`_all)`                                                                                                 | force specified columns to be string                                             |
|                            | `encoding("`[<var class="command">encoding</var><strong></strong>](import%20delimited##encoding)`")` | specify the encoding of the text file being imported                             |

| export\_delimited\_options |                                | Description                                             |
|----------------------------|--------------------------------|---------------------------------------------------------|
| Main                       |                                |                                                         |
|                            | `delimiter("char"`\|`tab`) | use `char` as delimiter                                 |
|                            | `novarnames`                   | do not write variable names on the first line           |
|                            | `nolabel`                      | output numeric values (not labels) of labeled variables |
|                            | `datafmt`                      | use the variables' display format upon export           |
|                            | `quote`                        | always enclose strings in double quotes                 |
|                            | `replace`                      | overwrite existing `filename`                           |
