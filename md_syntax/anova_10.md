## Syntax

`anova`
[varname](http://www.stata.com/help.cgi?varname)
\[`term` \[`/`\] \[`term` \[`/`\] `...`\]\] <span
class="command">\[`if`\] \[`in`\]_ <span
class="command">\[`weight`\]_ \[`, options`\]

where `term` is of the form <span options="2">{space
2}_`varname`\[{`*`\|`|`<span
options=")-">{c )-}_`varname`\[`...`\]\]

| Options                                                                                                                                                                   |                       | Description                                                          |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------|----------------------------------------------------------------------|
| Model                                                                                                                                                                     |                       |                                                                      |
|                                                                                                                                                                           | `category(varlist)`   | variables in `terms` that are categorical or class                   |
|                                                                                                                                                                           | `class(varlist)`      | synonym for `category(varlist)`                                  |
|                                                                                                                                                                           | `continuous(varlist)` | variables in `terms` that are continuous                             |
|                                                                                                                                                                           | `repeated(varlist)`   | variables in `terms` that are repeated-measures variables            |
|                                                                                                                                                                           | `partial`             | use partial (or marginal) sums of squares                            |
|                                                                                                                                                                           | `sequential`          | use sequential sums of squares                                       |
|                                                                                                                                                                           | `noconstant`          | suppress constant term                                               |
| Adv. model                                                                                                                                                                |                       |                                                                      |
|                                                                                                                                                                           | `bse(term)`           | between-subjects error term in repeated-measures ANOVA               |
|                                                                                                                                                                           | `bseunit(varname)`    | variable representing lowest unit in the between-subjects error term |
|                                                                                                                                                                           | `grouping(varname)`   | grouping variable for computing pooled covariance matrix             |
| Reporting                                                                                                                                                                 |                       |                                                                      |
|                                                                                                                                                                           | `regress`             | display the regression table                                         |
|                                                                                                                                                                           | \[`no`\]`anova`       | display or suppress the ANOVA table                                  |
|                                                                                                                                                                           | `detail`              | show mapping from values to level numbers for categorical variables  |
| `by` is allowed; see [<strong>prefix</strong>](http://www.stata.com/help.cgi?prefix).                                                          |                       |                                                                      |
| `aweight`s and `fweight`s are allowed; see [<strong>weight</strong>](http://www.stata.com/help.cgi?weight).                                    |                       |                                                                      |
| See [<strong>anova_postestimation_10</strong>](http://www.stata.com/help.cgi?anova_postestimation_10) for features available after estimation. |                       |                                                                      |
