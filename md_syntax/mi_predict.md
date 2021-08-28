## Syntax

Obtain multiple-imputation linear predictions

`mi predict` _\[`type`\] \[_
[newvar](http://www.stata.com/help.cgi?newvar)
\[`if`\] `using miestfile` \[`, predict_options options`\]

Obtain multiple-imputation nonlinear predictions

`mi predictnl` _\[`type`\] \[_
[newvar](http://www.stata.com/help.cgi?newvar)
= `pnl_exp` \[`if`\] `using miestfile` \[`, pnl_options options`\]

`miestfile.ster` contains estimation results previously saved by `mi`
`estimate, saving(miestfile)`; see
[<strong>[MI]</strong> mi estimate](http://www.stata.com/help.cgi?mi_estimate).

`pnl_exp` is any valid Stata expression and may also contain calls to
two special functions unique to `predictnl`: `predict()` and `xb()`; see
[<strong>[R]</strong> predictnl](http://www.stata.com/help.cgi?predictnl)
for details.

| predict\_options |                        | Description                                        |
|------------------|------------------------|----------------------------------------------------|
| Predict options  |                        |                                                    |
|                  | `xb`                   | calculate linear prediction; the default           |
|                  | `stdp`                 | calculate standard error of the prediction         |
|                  | `nooffset`             | ignore any `offset()` or `exposure()` variable     |
|                  | `equation(eqno)` | specify equations after multiple-equation commands |

| pnl\_options    |                     | Description                                                                                                                   |
|-----------------|---------------------|-------------------------------------------------------------------------------------------------------------------------------|
| Predict options |                     |                                                                                                                               |
|                 | `se(newvar)`        | create `newvar` containing standard errors                                                                                    |
|                 | `variance(newvar)`  | create `newvar` containing variances                                                                                          |
|                 | `wald(newvar)`      | create `newvar` containing the Wald test statistic                                                                            |
|                 | `p(newvar)`         | create `newvar` containing the significance level (p-value) of the Wald test                                                  |
|                 | `ci(newvars)`       | create `newvars` containing lower and upper confidence intervals                                                              |
|                 | `level(#)`          | set confidence level; default is `level(95)`                                                                                  |
|                 | `bvariance(newvar)` | create `newvar` containing between-imputation variances                                                                       |
|                 | `wvariance(newvar)` | create `newvar` containing within-imputation variances                                                                        |
|                 | `df(newvar)`        | create `newvar` containing MI degrees of freedom                                                                              |
|                 | `nosmall`           | do not apply small-sample correction to degrees of freedom                                                                    |
|                 | `rvi(newvar)`       | create `newvar` containing relative variance increases                                                                        |
|                 | `fmi(newvar)`       | create `newvar` containing fractions of missing information                                                                   |
|                 | `re(newvar)`        | create `newvar` containing relative efficiencies                                                                              |
| Advanced        |                     |                                                                                                                               |
|                 | `iterate(#)`        | maximum iterations for finding optimal step size to compute completed-data numerical derivatives of `pnl_exp`; default is 100 |
|                 | `force`             | calculate completed-data standard errors, etc., even when possibly inappropriate                                              |

| Options                                                                          |                        | Description                                                                                                                                          |
|----------------------------------------------------------------------------------|------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| MI options                                                                       |                        |                                                                                                                                                      |
|                                                                                  | `nimputations(#)`      | specify number of imputations to use in computation; default is to use all existing imputations                                                      |
|                                                                                  | `imputations(numlist)` | specify which imputations to use in computation                                                                                                      |
|                                                                                  | `estimations(numlist)` | specify which estimation results to use in computation                                                                                               |
|                                                                                  | `esample(varname)`     | restrict the prediction to the estimation subsample identified by a binary variable `varname`                                                        |
|                                                                                  | `storecompleted`       | store completed-data predictions in the imputed data; available only in the flong and flongsep styles                                                |
| Reporting                                                                        |                        |                                                                                                                                                      |
|                                                                                  | `replay`               | replay command-specific results from each individual estimation in `miestfile.ster`                                                                |
|                                                                                  | `cmdlegend`            | display the command legend                                                                                                                           |
|                                                                                  | `noupdate`             | do not perform `mi update`; see [<strong>[MI]</strong> noupdate option](http://www.stata.com/help.cgi?mi_noupdate_option) |
|                                                                                  | `noerrnotes`           | suppress error notes associated with failed estimation results in `miestfile.ster`                                                                 |
|                                                                                  | `showimputations`      | show imputations saved in `miestfile.ster`                                                                                                         |
| `noupdate`, `noerrnotes`, and `showimputations` do not appear in the dialog box. |                        |                                                                                                                                                      |
