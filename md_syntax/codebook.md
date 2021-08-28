## Syntax

`codebook`
\[[varlist](http://www.stata.com/help.cgi?varlist)\]
_\[`if`\] \[`in`\]_ \[`, options`\]

| Options   |                                 | Description                                                                                                                                                    |
|-----------|---------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Options   |                                 |                                                                                                                                                                |
|           | `all`                           | print complete report without missing values                                                                                                                   |
|           | `header`                        | print dataset name and last saved date                                                                                                                         |
|           | `notes`                         | print any notes attached to variables                                                                                                                          |
|           | `mv`                            | report pattern of missing values                                                                                                                               |
|           | `tabulate(#)`                   | set tables/summary statistics threshold; default is `tabulate(9)`                                                                                              |
|           | `problems`                      | report potential problems in dataset                                                                                                                           |
|           | `detail`                        | display detailed report on the variables; only with `problems`                                                                                                 |
|           | `compact`                       | display compact report on the variables                                                                                                                        |
|           | `dots`                          | display a dot for each variable processed; only with `compact`                                                                                                 |
| Languages |                                 |                                                                                                                                                                |
|           | `languages`\[`(namelist)`\] | use with multilingual datasets; see [<strong>[D]</strong> label language](http://www.stata.com/help.cgi?label_language) for details |
