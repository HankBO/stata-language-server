## Syntax

`sem`
[<var class="command">paths</var><strong></strong>](http://www.stata.com/help.cgi?sem%20and%20gsem%20path%20notation)
... `,` ... `estimation_options`

| estimation\_options |                                  | Description                                                                                                   |
|---------------------|----------------------------------|---------------------------------------------------------------------------------------------------------------|
|                     | `method(method)`             | `method` may be `ml`, `mlmv`, or `adf`                                                                        |
|                     | `vce(vcetype)`               | `vcetype` may be `oim`, `eim`, `opg`, `sbentler`, `robust`, `cluster clustvar`, `bootstrap`, or `jackknife` |
|                     | `nm1`                            | compute sample variance rather than ML variance                                                               |
|                     | `noxconditional`                 | compute covariances, etc., of observed exogenous variables                                                    |
|                     | `allmissing`                     | for use with `method(mlmv)`                                                                                   |
|                     | `noivstart`                      | skip calculation of starting values                                                                           |
|                     | `noestimate`                     | do not fit the model; instead show starting values                                                            |
|                     | `maximize_options`               | control the maximization process for specified model; seldom used                                             |
|                     | `satopts(maximize_options)`  | control the maximization process for saturated model; seldom used                                             |
|                     | `baseopts(maximize_options)` | control the maximization process for baseline model; seldom used                                              |
