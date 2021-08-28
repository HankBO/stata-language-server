## Syntax

`forecast identity varname = exp` \[`, options`\]

| Options                                                                            |            | Description                                              |
|------------------------------------------------------------------------------------|------------|----------------------------------------------------------|
|                                                                                    | `generate` | create new variable `varname`                            |
| \*                                                                                 | `double`   | store new variable as a `double` instead of as a `float` |
| `varname` is the name of an endogenous variable to be added to the forecast model. |            |                                                          |
| \* You can only specify `double` if you also specify `generate`.                   |            |                                                          |
