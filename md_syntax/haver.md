## Syntax

Describe contents of a Haver dataset

`haver describe filename` \[`, detail`\]

Describe specified variables in a Haver dataset

`haver describe`
[varlist](http://www.stata.com/help.cgi?varlist)
`using filename` \[`, detail`\]

Load Haver dataset

`haver use filename` \[`, use_options`\]

Load specified variables from a Haver dataset

`haver use`
[varlist](http://www.stata.com/help.cgi?varlist)
`using filename` \[`, use_options`\]

| use\_options |                                                | Description                                                                                    |
|--------------|------------------------------------------------|------------------------------------------------------------------------------------------------|
|              | `tin:(`\[`constant`\]`,` \[`constant`\]`)`     | load data within specified date range                                                          |
|              | `twithin:(`\[`constant`\]`,` \[`constant`\]`)` | same as `tin()`, except exclude the end points of range                                        |
|              | `tvar(varname)`                                | create time variable `varname`                                                                 |
|              | `hmissing(misval)`                             | record missing values as `misval`                                                              |
|              | `fill`                                         | include observations with missing data in resulting dataset and record missing values for them |
|              | `clear`                                        | clear data in memory before loading the Haver dataset                                          |
