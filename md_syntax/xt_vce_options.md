## Syntax

`estimation_cmd` ... \[`, vce_options` ...\]

|     |                                                  |                                                                                      |
|-----|--------------------------------------------------|--------------------------------------------------------------------------------------|
|     | `vce_options`                                    | Description                                                                          |
|     | `vce(oim)`                                       | observed information matrix (OIM)                                                    |
|     | `vce(opg)`                                       | outer product of the gradient (OPG) vectors                                          |
|     | `vce(robust)`                                | Huber/White/sandwich estimator                                                       |
|     | `vce(cluster clustvar)`                    | clustered sandwich estimator                                                         |
|     | `vce(bootstrap` \[`, bootstrap_options`\]`)` | bootstrap estimation                                                                 |
|     | `vce(jackknife` \[`, jackknife_options`\]`)` | jackknife estimation                                                                 |
|     | `nmp`                                            | use divisor N - P instead of the default N                                           |
|     | `scale(x2`\|`dev`\|`phi`\|`#)`                 | override the default scale parameter; available only with population-averaged models |
