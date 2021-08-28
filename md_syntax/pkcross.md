## Syntax

`pkcross outcome` _\[`if`\] \[`in`\]_ \[`,`
`options`\]

| Options          |                      | Description                                                                                                                       |
|------------------|----------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| Model            |                      |                                                                                                                                   |
|                  | `sequence(varname)`  | sequence variable; default is `sequence(sequence)`                                                                                |
|                  | `treatment(varname)` | treatment variable; default is `treatment(treat)`                                                                                 |
|                  | `period(varname)`    | period variable; default is `period(period)`                                                                                      |
|                  | `id(varname)`        | ID variable; default is `id(id)`                                                                                                  |
|                  | `carryover(varname)` | carryover variable; default is `carryover(carry)`                                                                                 |
|                  | `carryover(none)`  | omit carryover effects from model; default is `carryover(carry)`                                                                  |
|                  | `model(string)`      | specify the model to fit                                                                                                          |
|                  | `sequential`         | estimate sequential instead of partial sums of squares                                                                            |
| Parameterization |                      |                                                                                                                                   |
|                  | `param(3)`         | estimate mean and the period, treatment, and sequence effects; assume no carryover effects exist; the default                     |
|                  | `param(1)`         | estimate mean and the period, treatment, and carryover effects; assume no sequence effects exist                                  |
|                  | `param(2)`         | estimate mean, period and treatment effects, and period-by-treatment interaction; assume no sequence or carryover effects exist   |
|                  | `param(4)`         | estimate mean, sequence and treatment effects, and sequence-by-treatment interaction; assume no period or carryover effects exist |
