## Syntax

Fractional polynomial regression

`fracpoly` \[`, fracpoly_options`\] `: regression_cmd` \[`yvar1`
\[`yvar2`\]\] `xvar1` \[`#` \[`#...`\]\] \[`xvar2` \[`#`
\[`#...`\]\]\] \[`...`\] \[`xvarlist`\] _\[`if`\]
\[`in`\]_ _\[`weight`\]_ \[`,`
`regression_cmd_options`\]

Display table showing the best fractional polynomial model for each
degree

`fracpoly , compare`

Create variables containing fractional polynomial powers

`fracgen`
[varname](http://www.stata.com/help.cgi?varname)
`#` \[`# ...`\] _\[`if`\] \[`in`\]_ \[`,`
`fracgen_options`\]

| fracpoly\_options |                     | Description                                                       |
|-------------------|---------------------|-------------------------------------------------------------------|
| Model             |                     |                                                                   |
|                   | `degree(#)`         | degree of fractional polynomial to fit; default is `degree(2)`    |
| Model 2           |                     |                                                                   |
|                   | `noscaling`         | suppress scaling of first independent variable                    |
|                   | `noconstant`        | suppress constant term                                            |
|                   | `powers(numlist)`   | list of fractional polynomial powers from which models are chosen |
|                   | `center(cent_list)` | specification of centering for the independent variables          |
|                   | `all`               | include out-of-sample observations in generated variables         |
| Reporting         |                     |                                                                   |
|                   | `log`               | display iteration log                                             |
|                   | `compare`           | compare models by degree                                          |
|                   | `display_options`   | control column formats and line width                             |

| regression\_cmd\_options |                          | Description                                          |
|--------------------------|--------------------------|------------------------------------------------------|
| Model 2                  |                          |                                                      |
|                          | `regression_cmd_options` | options appropriate to the regression command in use |

All weight types supported by `regression_cmd` are allowed; see
[<strong>weight</strong>](http://www.stata.com/help.cgi?weight).

See
[<strong>[R]</strong> fracpoly postestimation](http://www.stata.com/help.cgi?fracpoly_postestimation)
for features available after estimation.

where

`cent_list` is a comma-separated list with elements
[varlist](http://www.stata.com/help.cgi?varlist)`:`<span
options="-(">{c -(}_`mean`\|`#`\|`no`}, except that the first
element may optionally be of the form <span options="-(">{c
-(}_`mean`\|`#`\|`no`} to specify the default for all variables.

<span options="regression_cmd">{marker regression\_cmd}_
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

| fracgen\_options |                                                                                                        | Description                                                                                                              |
|------------------|--------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| Main             |                                                                                                        |                                                                                                                          |
|                  | `center(no`\|`mean`\|`#)`                                                                            | center [varname](http://www.stata.com/help.cgi?varname) as specified; default is `center(no)` |
|                  | `noscaling`                                                                                            | suppress scaling of [varname](http://www.stata.com/help.cgi?varname)                          |
|                  | `restrict(`\[[varname](http://www.stata.com/help.cgi?varname)\] \[`if`\]`)` | compute centering and scaling using specified subsample                                                                  |
|                  | `replace`                                                                                              | replace variables if they exist                                                                                          |
