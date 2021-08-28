## Syntax

`outsheet`
\[[varlist](http://www.stata.com/help.cgi?varlist)\]
`using filename` _\[`if`\] \[`in`\]_ \[`,`
`options`\]

| Options                                                                               |                         | Description                                                 |
|---------------------------------------------------------------------------------------|-------------------------|-------------------------------------------------------------|
| Main                                                                                  |                         |                                                             |
|                                                                                       | `comma`                 | output in comma-separated (instead of tab-separated) format |
|                                                                                       | `delimiter("char")` | use `char` as delimiter                                     |
|                                                                                       | `nonames`               | do not write variable names on the first line               |
|                                                                                       | `nolabel`               | output numeric values (not labels) of labeled variables     |
|                                                                                       | `noquote`               | do not enclose strings in double quotes                     |
|                                                                                       | `replace`               | overwrite existing `filename`                               |
| If `filename` is specified without a suffix, `.out` is assumed.                       |                         |                                                             |
| If your `filename` contains embedded spaces, remember to enclose it in double quotes. |                         |                                                             |
| `replace` does not appear in the dialog box.                                          |                         |                                                             |
