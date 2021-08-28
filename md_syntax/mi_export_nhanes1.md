## Syntax

`mi export nhanes1 filenamestub` \[`, options odd_options`\]

| Options |             | Description                    |
|---------|-------------|--------------------------------|
|         | `replace`   | okay to replace existing files |
|         | `uppercase` | uppercase prefix and suffix    |
|         | `passiveok` | include passive variables      |

| odd\_options                                                                                                                 |                                        | Description                             |
|------------------------------------------------------------------------------------------------------------------------------|----------------------------------------|-----------------------------------------|
|                                                                                                                              | `nacode(#)`                        | not applicable code; default is `0`     |
|                                                                                                                              | `obscode(#)`                       | observed code; default is `1`           |
|                                                                                                                              | `impcode(#)`                       | imputed code; default is `2`            |
|                                                                                                                              | `impprefix("string" "string")` | variable prefix; default is `"" ""`     |
|                                                                                                                              | `impsuffix("string" "string")` | variable suffix; default is `"if" "mi"` |
| Note: `odd_options` are not specified unless you want to create results that are nhanes1-like but not really nhanes1 format. |                                        |                                         |
