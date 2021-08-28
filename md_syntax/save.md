## Syntax

Save data in memory to file

`save` \[`filename`\] \[`, save_options`\]

Save data in memory to file in Stata 13, 12, or 11 format

`saveold filename` \[`, saveold_options`\]

| save\_options |           | Description                                               |
|---------------|-----------|-----------------------------------------------------------|
|               | `nolabel` | omit value labels from the saved dataset                  |
|               | `replace` | overwrite existing dataset                                |
|               | `all`     | save `e(sample)` with the dataset; programmer's option    |
|               | `orphans` | save all value labels                                     |
|               | `emptyok` | save dataset even if zero observations and zero variables |

| saveold\_options |              | Description                                                                          |
|------------------|--------------|--------------------------------------------------------------------------------------|
|                  | `version(#)` | specify version 11&lt;=`#`&lt;=14; default is `version(13)`, meaning Stata 13 format |
|                  | `nolabel`    | omit value labels from the saved dataset                                             |
|                  | `replace`    | overwrite existing dataset                                                           |
|                  | `all`        | save `e(sample)` with the dataset; programmer's option                               |
