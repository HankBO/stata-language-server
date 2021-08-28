## Syntax

`outfile`
\[[varlist](http://www.stata.com/help.cgi?varlist)\]
`using filename` _\[`if`\] \[`in`\]_ \[`,`
`options`\]

| Options                                      |               | Description                                                                                              |
|----------------------------------------------|---------------|----------------------------------------------------------------------------------------------------------|
| Main                                         |               |                                                                                                          |
|                                              | `dictionary`  | write the file in Stata's dictionary format                                                              |
|                                              | `nolabel`     | output numeric values (not labels) of labeled variables; the default is to write labels in double quotes |
|                                              | `noquote`     | do not enclose strings in double quotes                                                                  |
|                                              | `comma`       | write file in comma-separated (instead of space-separated) format                                        |
|                                              | `wide`        | force one observation per line (no matter how wide)                                                      |
| Advanced                                     |               |                                                                                                          |
|                                              | `rjs`         | right-justify string variables; the default is to left-justify                                           |
|                                              | `fjs`         | left-justify if format width &lt; 0; right-justify if format width &gt; 0                                |
|                                              | `runtogether` | all on one line, no quotes, no space between, and ignore formats                                         |
|                                              | `missing`     | retain missing values; use only with `comma`                                                             |
|                                              | `replace`     | overwrite the existing file                                                                              |
| `replace` does not appear in the dialog box. |               |                                                                                                          |
