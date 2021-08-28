## Syntax

Sample-size determination

`stpower cox` \[`coef`\] \[`, options`\]

Power determination

`stpower cox ` \[`coef`\]`, n(numlist)` \[`options`\]

Effect-size determination

`stpower cox, n(numlist)` <span options="-(">{c
-(}_`power(numlist)` \| `beta(numlist)`<span options=")-">{c
)-}_ \[`options`\]

where `coef` is the regression coefficient (effect size) of a covariate
of interest, in a Cox proportional hazards model, desired to be detected
by a test with a prespecified power. `coef` may be specified either as
one number or as a list of values (see `numlist`) enclosed in
parentheses.

| Options                                                                                          |                                         | Description                                                                                                                                            |
|--------------------------------------------------------------------------------------------------|-----------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| Main                                                                                             |                                         |                                                                                                                                                        |
| \*                                                                                               | `alpha(numlist)`                        | significance level; default is `alpha(0.05)`                                                                                                           |
| \*                                                                                               | `power(numlist)`                        | power; default is `power(0.8)`                                                                                                                         |
| \*                                                                                               | `beta(numlist)`                         | probability of type II error; default is `beta(0.2)`                                                                                                   |
| \*                                                                                               | `n(numlist)`                            | sample size; required to compute power or effect size                                                                                                  |
| \*                                                                                               | `hratio(numlist)`                       | hazard ratio (effect size) associated with a one-unit increase in covariate of interest; default is `hratio(0.5)`                                      |
|                                                                                                  | `onesided`                              | one-sided test; default is two sided                                                                                                                   |
|                                                                                                  | `sd(#)`                                 | standard deviation of covariate of interest; default is `sd(0.5)`                                                                                      |
|                                                                                                  | `r2(#)`                                 | squared coefficient of multiple correlation with other covariates; default is `r2(0)`                                                                  |
|                                                                                                  | `failprob(#)`                           | overall probability of an event (failure) of interest; default is `failprob(1)`, meaning no censoring                                                  |
|                                                                                                  | `wdprob(#)`                             | the proportion of subjects anticipated to withdraw from the study; default is `wdprob(0)`                                                              |
|                                                                                                  | `parallel`                              | treat number lists in starred options as parallel (do not enumerate all possible combinations of values) when multiple values per option are specified |
| Reporting                                                                                        |                                         |                                                                                                                                                        |
|                                                                                                  | `hr`                                    | report hazard ratio, not coefficient                                                                                                                   |
|                                                                                                  | `table`                                 | display results in a table with default columns                                                                                                        |
|                                                                                                  | `columns(colnames)`                     | display results in a table with specified ` colnames` columns                                                                                          |
|                                                                                                  | `notitle`                               | suppress table title                                                                                                                                   |
|                                                                                                  | `nolegend`                              | suppress table legend                                                                                                                                  |
|                                                                                                  | `colwidth(# [# ...])`                   | column widths; default is `colwidth(9)`                                                                                                                |
|                                                                                                  | `separator(#)`                          | draw a horizontal separator line every `#` lines; default is `separator(0)` meaning no separator lines                                                 |
|                                                                                                  | `saving(filename`\[`, replace`\]`)` | save the table data to `filename`; use `replace` to overwrite existing `filename`                                                                      |
|                                                                                                  | `noheader`                              | suppress table header; seldom used                                                                                                                     |
|                                                                                                  | `continue`                              | draw a continuation border in the table output; seldom used                                                                                            |
| \* Starred options may be specified either as one number or as a list of values (see `numlist`). |                                         |                                                                                                                                                        |
| `noheader` and `continue` are not shown in the dialog box.                                       |                                         |                                                                                                                                                        |

| colnames                                                                                   |         | Description                               |
|--------------------------------------------------------------------------------------------|---------|-------------------------------------------|
|                                                                                            | `alpha` | significance level                        |
|                                                                                            | `power` | power                                     |
|                                                                                            | `beta`  | type II error probability                 |
|                                                                                            | `n`     | total number of subjects                  |
|                                                                                            | `e`     | total number of events (failures)         |
|                                                                                            | `hr`    | hazard ratio                              |
|                                                                                            | `coef`  | coefficient (log hazard-ratio)            |
|                                                                                            | `sd`    | standard deviation                        |
|                                                                                            | `r2`    | squared multiple-correlation coefficient  |
|                                                                                            | `pr`    | overall probability of an event (failure) |
|                                                                                            | `w`     | proportion of withdrawals                 |
| By default, the following `colnames` are displayed:                                        |         |                                           |
| `power`, `n`, `e`, `sd`, and `alpha` are always displayed;                                 |         |                                           |
| `coef` is displayed, unless the `hr` option is specified, in which case `hr` is displayed; |         |                                           |
| `pr` if overall probability of an event (`failprob()`) is specified;                       |         |                                           |
| `r2` if squared multiple-correlation coefficient (`r2()`) is specified; and                |         |                                           |
| `w` if withdrawal proportion (`wdprob()`) is specified.                                    |         |                                           |
