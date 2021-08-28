## Syntax

`dprobit`
\[[depvar](http://www.stata.com/help.cgi?depvar)
[indepvars](http://www.stata.com/help.cgi?indepvars)
_\[`if`\] \[`in`\]_ <span
class="command">\[`weight`\]_\] \[`, options`\]

| Options      |                    | Description                                                            |
|--------------|--------------------|------------------------------------------------------------------------|
| Model        |                    |                                                                        |
|              | `offset(varname)`  | include `varname` in model with coefficient constrained to 1           |
|              | `at(matname)`      | point at which marginal effects are evaluated                          |
|              | `asis`             | retain perfect predictor variables                                     |
|              | `classic`          | calculate mean effects for dummies like those for continuous variables |
| SE/Robust    |                    |                                                                        |
|              | `vce(vcetype)`     | `vcetype` may be `oim`, `robust`, or `cluster clustvar`              |
| Reporting    |                    |                                                                        |
|              | `level(#)`         | set confidence level; default is `level(95)`                           |
| Maximization |                    |                                                                        |
|              | `maximize_options` | control the maximization process; seldom used                          |

|                                                                                                                                                                         |          |                                                   |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|---------------------------------------------------|
| \+                                                                                                                                                                      | `nocoef` | do not display the coefficient table; seldom used |
| \+ `nocoef` does not appear in the dialog box.                                                                                                                          |          |                                                   |
| `indepvars` may contain factor variables; see [<strong>fvvarlist</strong>](http://www.stata.com/help.cgi?fvvarlist).                         |          |                                                   |
| `by`, `rolling`, and `statsby` are allowed; see [<strong>prefix</strong>](http://www.stata.com/help.cgi?prefix).                             |          |                                                   |
| `fweight`s and `pweight`s are allowed; see [<strong>weight</strong>](http://www.stata.com/help.cgi?weight).                                  |          |                                                   |
| See [<strong>dprobit postestimation</strong>](http://www.stata.com/help.cgi?dprobit_postestimation) for features available after estimation. |          |                                                   |
