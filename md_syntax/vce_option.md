## Syntax

`estimation_cmd` ... \[`, vce(vcetype)` ...\]

|     |                                         |                                             |
|-----|-----------------------------------------|---------------------------------------------|
|     | `vcetype`                               | Description                                 |
|     | Likelihood based                        |                                             |
|     | `oim`                                   | observed information matrix (OIM)           |
|     | `opg`                                   | outer product of the gradient (OPG) vectors |
|     | Sandwich estimators                     |                                             |
|     | `robust`                                | Huber/White/sandwich estimator              |
|     | `cluster clustvar`                    | clustered sandwich estimator                |
|     | Replication based                       |                                             |
|     | `bootstrap` \[`, bootstrap_options`\] | bootstrap estimation                        |
|     | `jackknife` \[`, jackknife_options`\] | jackknife estimation                        |
