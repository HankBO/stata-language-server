## Syntax

`anova`
[varname](http://www.stata.com/help.cgi?varname)
\[`termlist`\] _\[`if`\] \[`in`\]_
\[`weight`\] \[`, options`\]

where `termlist` is a
[<strong>factor-variable list</strong>](http://www.stata.com/help.cgi?fvvarlist)
with the following additional features:

o Variables are assumed to be categorical; use the `c.` factor-variable
operator to override this.

o The `|` symbol (indicating nesting) may be used in place of the `#`
symbol (indicating interaction).

o The `/` symbol is allowed after a term and indicates that the
following term is the error term for the preceding terms.

| Options                                                                                                                                                                 |                     | Description                                                          |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------|----------------------------------------------------------------------|
| Model                                                                                                                                                                   |                     |                                                                      |
|                                                                                                                                                                         | `repeated(varlist)` | variables in `term`s that are repeated-measures variables            |
|                                                                                                                                                                         | `partial`           | use partial (or marginal) sums of squares                            |
|                                                                                                                                                                         | `sequential`        | use sequential sums of squares                                       |
|                                                                                                                                                                         | `noconstant`        | suppress constant term                                               |
|                                                                                                                                                                         | `dropemptycells`    | drop empty cells from the design matrix                              |
| Adv. model                                                                                                                                                              |                     |                                                                      |
|                                                                                                                                                                         | `bse(term)`         | between-subjects error term in repeated-measures ANOVA               |
|                                                                                                                                                                         | `bseunit(varname)`  | variable representing lowest unit in the between-subjects error term |
|                                                                                                                                                                         | `grouping(varname)` | grouping variable for computing pooled covariance matrix             |
| `bootstrap`, `by`, `fp`, `jackknife`, and `statsby` are allowed; see [<strong>prefix</strong>](http://www.stata.com/help.cgi?prefix).        |                     |                                                                      |
| Weights are not allowed with the [<strong>bootstrap</strong>](http://www.stata.com/help.cgi?bootstrap) prefix.                               |                     |                                                                      |
| `aweight`s are not allowed with the [<strong>jackknife</strong>](http://www.stata.com/help.cgi?jackknife) prefix.                            |                     |                                                                      |
| `aweight`s and `fweight`s are allowed; see [<strong>weight</strong>](http://www.stata.com/help.cgi?weight).                                  |                     |                                                                      |
| See [<strong>[R]</strong> anova postestimation](http://www.stata.com/help.cgi?anova_postestimation) for features available after estimation. |                     |                                                                      |
