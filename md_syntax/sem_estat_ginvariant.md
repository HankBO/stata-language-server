## Syntax

`estat ginvariant` \[`, options`\]

| Options |                          | Description                                                    |
|---------|--------------------------|----------------------------------------------------------------|
|         | `showpclass(pclassname)` | restrict output to parameters in the specified parameter class |
|         | `class`                  | include joint tests for parameter classes                      |
|         | `legend`                 | include legend describing parameter classes                    |

|              |                                                       |
|--------------|-------------------------------------------------------|
| `pclassname` | Description {p2line None}                             |
| `scoef`      | structural coefficients                               |
| `scons`      | structural intercepts                                 |
| `mcoef`      | measurement coefficients                              |
| `mcons`      | measurement intercepts                                |
| `serrvar`    | covariances of structural errors                      |
| `merrvar`    | covariances of measurement errors                     |
| `smerrcov`   | covariances between structural and measurement errors |
| `meanex`     | means of exogenous variables                          |
| `covex`      | covariances of exogenous variables {p2line None}      |
| `all`        | all the above                                         |
| `none`       | none of the above {p2line None}                       |
