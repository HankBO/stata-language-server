## Syntax

`hausman name-consistent` \[`name-efficient`\] \[`, options`\]

| Options  |                        | Description                                                                                |
|----------|------------------------|--------------------------------------------------------------------------------------------|
| Main     |                        |                                                                                            |
|          | `constant`             | include estimated intercepts in comparison; default is to exclude                          |
|          | `alleqs`               | use all equations to perform test; default is first equation only                          |
|          | `skipeqs(eqlist)`      | skip specified equations when performing test                                              |
|          | `equations(matchlist)` | associate/compare the specified (by number) pairs of equations                             |
|          | `force`                | force performance of test, even though assumptions are not met                             |
|          | `df(#)`                | use `#` degrees of freedom                                                                 |
|          | `sigmamore`            | base both (co)variance matrices on disturbance variance estimate from efficient estimator  |
|          | `sigmaless`            | base both (co)variance matrices on disturbance variance estimate from consistent estimator |
| Advanced |                        |                                                                                            |
|          | `tconsistent(string)`  | consistent estimator column header                                                         |
|          | `tefficient(string)`   | efficient estimator column header                                                          |

where `name-consistent` and `name-efficient` are names under which
estimation results were stored via
[<strong>estimates store</strong>](http://www.stata.com/help.cgi?estimates%20store).

A period (`.`) may be used to refer to the last estimation results, even
if these were not already stored.

Not specifying `name-efficient` is equivalent to specifying the last
estimation results as "`.`".
