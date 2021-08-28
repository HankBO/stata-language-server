## Syntax

`mfp` \[`, options`\] `: regression_cmd` \[`yvar1` \[`yvar2`\]\]
`xvarlist` _\[`if`\] \[`in`\]_ \[`weight`\]
\[`, regression_cmd_options`\]

| Options    |                       | Description                                                                               |
|------------|-----------------------|-------------------------------------------------------------------------------------------|
| Model 2    |                       |                                                                                           |
|            | `sequential`          | use the Royston and Altman model-selection algorithm; default uses closed-test procedure  |
|            | `cycles(#)`           | maximum number of iteration cycles; default is `cycles(5)`                                |
|            | `dfdefault(#)`        | default maximum degrees of freedom; default is `dfdefault(4)`                             |
|            | `center(cent_list)`   | specification of centering for the independent variables                                  |
|            | `alpha(alpha_list)`   | p-values for testing between FP models; default is `alpha(0.05)`                          |
|            | `df(df_list)`         | degrees of freedom for each predictor                                                     |
|            | `powers(numlist)`     | list of FP powers to use; default is <span class="nowrap">`powers(-2 -1(.5)1 2 3)`_ |
| Adv. model |                       |                                                                                           |
|            | `xorder(+`\|`-`\|`n)` | order of entry into model-selection algorithm; default is `xorder(+)`                     |
|            | `select(select_list)` | nominal p-values for selection on each predictor                                          |
|            | `xpowers(xp_list)`    | FP powers for each predictor                                                              |
|            | `zero(varlist)`       | treat nonpositive values of specified predictors as zero when FP is transformed           |
|            | `catzero(varlist)`    | add indicator variable for specified predictors                                           |
|            | `all`                 | include out-of-sample observations in generated variables                                 |
| Reporting  |                       |                                                                                           |
|            | `level(#)`            | set confidence level; default is `level(95)`                                              |
|            | `display_options`     | control column formats and line width                                                     |

| regression\_cmd\_options |                          | Description                                          |
|--------------------------|--------------------------|------------------------------------------------------|
| Adv. model               |                          |                                                      |
|                          | `regression_cmd_options` | options appropriate to the regression command in use |

All weight types supported by `regression_cmd` are allowed; see
[<strong>weight</strong>](http://www.stata.com/help.cgi?weight).

See
[<strong>[R] mfp postestimation</strong>](http://www.stata.com/help.cgi?mfp%20postestimation)
for features available after estimation.

`fp generate` may be used to create new variables containing fractional
polynomial powers. See
[<strong>[R] fp</strong>](http://www.stata.com/help.cgi?fp).

<span options="reg_cmd">{marker reg\_cmd}_where

`regression_cmd` may be
[<strong>clogit</strong>](http://www.stata.com/help.cgi?clogit),
[<strong>glm</strong>](http://www.stata.com/help.cgi?glm),
[<strong>intreg</strong>](http://www.stata.com/help.cgi?intreg),
[<strong>logistic</strong>](http://www.stata.com/help.cgi?logistic),
[<strong>logit</strong>](http://www.stata.com/help.cgi?logit),
[<strong>mlogit</strong>](http://www.stata.com/help.cgi?mlogit),
[<strong>nbreg</strong>](http://www.stata.com/help.cgi?nbreg),
[<strong>ologit</strong>](http://www.stata.com/help.cgi?ologit),
[<strong>oprobit</strong>](http://www.stata.com/help.cgi?oprobit),
[<strong>poisson</strong>](http://www.stata.com/help.cgi?poisson),
[<strong>probit</strong>](http://www.stata.com/help.cgi?probit),
[<strong>qreg</strong>](http://www.stata.com/help.cgi?qreg),
[<strong>regress</strong>](http://www.stata.com/help.cgi?regress),
[<strong>rreg</strong>](http://www.stata.com/help.cgi?rreg),
[<strong>stcox</strong>](http://www.stata.com/help.cgi?stcox),
[<strong>stcrreg</strong>](http://www.stata.com/help.cgi?stcrreg),
[<strong>streg</strong>](http://www.stata.com/help.cgi?streg),
or
[<strong>xtgee</strong>](http://www.stata.com/help.cgi?xtgee).

`yvar1` is not allowed for `streg`, `stcrreg`, and `stcox`. For these
commands, you must first
[<strong>stset</strong>](http://www.stata.com/help.cgi?stset)
your data.

`yvar1` and `yvar2` must both be specified when `regression_cmd` is
`intreg`.

`xvarlist` has elements of type
[varlist](http://www.stata.com/help.cgi?varlist)
and/or `(varlist)`; for example,

`x1 x2 (x3 x4 x5)`

Elements enclosed in parentheses are tested jointly for inclusion in the
model and are not eligible for fractional polynomial transformation.
