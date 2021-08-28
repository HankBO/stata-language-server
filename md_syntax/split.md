## Syntax

`split strvar` _\[`if`\] \[`in`\]_ \[`,`
`options`\]

| Options  |                        | Description                                                                                                        |
|----------|------------------------|--------------------------------------------------------------------------------------------------------------------|
| Main     |                        |                                                                                                                    |
|          | `generate(stub)`       | begin new variable names with `stub`; default is `strvar`                                                          |
|          | `parse(parse_strings)` | parse on specified strings; default is to parse on spaces                                                          |
|          | `limit(#)`             | create a maximum of `#` new variables                                                                              |
|          | `notrim`               | do not trim leading or trailing spaces of original variable                                                        |
| Destring |                        |                                                                                                                    |
|          | `destring`             | apply `destring` to new string variables, replacing initial string variables with numeric variables where possible |
|          | `ignore("chars")`  | remove specified nonnumeric characters                                                                             |
|          | `force`                | convert nonnumeric strings to missing values                                                                       |
|          | `float`                | generate numeric variables as type `float`                                                                         |
|          | `percent`              | convert percent variables to fractional form                                                                       |
