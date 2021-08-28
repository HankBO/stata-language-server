## Syntax

Interactive version

`gmm (`\[`reqname1:`\]`rexp_1) (`\[`reqname2:`\]`rexp_2)`
... _\[`if`\] \[`in`\]_ \[`weight`\] \[`,`
`options`\]

Moment-evaluator program version

`gmm moment_prog` _\[`if`\] \[`in`\]_
\[`weight`\]`,` <span options="-(">{c
-(}_`equations(namelist)`|`nequations(#)`} <span
options="-(">{c -(}_`parameters(namelist)`|`nparameters(#)`} \[`options`\]
\[`program_options`\]

`reqname_j` is the `j`th residual equation name,

`rexp_j` is the substitutable expression for the `j`th residual
equation, and

`moment_prog` is a moment-evaluator program.

| Options                                                          |                                                                                                                                         | Description                                                                                                                                                                                           |
|------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Model                                                            |                                                                                                                                         |                                                                                                                                                                                                       |
|                                                                  | `derivative(`\[`reqname`|`#`\]`/name = dexp_jk)`                                                |                                                                                                                                                                                                       |
|                                                                  |                                                                                                                                         | specify derivative of `reqname` (or `#`) with respect to parameter `name`; can be specified more than once (interactive version only)                                                                 |
| \*                                                               | `twostep`                                                                                                                               | use two-step GMM estimator; the default                                                                                                                                                               |
| \*                                                               | `onestep`                                                                                                                               | use one-step GMM estimator                                                                                                                                                                            |
| \*                                                               | `igmm`                                                                                                                                  | use iterative GMM estimator                                                                                                                                                                           |
|                                                                  | `variables(varlist)`                                                                                                                    | specify variables in model                                                                                                                                                                            |
|                                                                  | `nocommonesample`                                                                                                                       | do not restrict estimation sample to be the same for all equations                                                                                                                                    |
| Instruments                                                      |                                                                                                                                         |                                                                                                                                                                                                       |
|                                                                  | `instruments(`\[`reqlist:`\][varlist](http://www.stata.com/help.cgi?varlist)\[`, noconstant`\]`)`      |                                                                                                                                                                                                       |
|                                                                  |                                                                                                                                         | specify instruments; can be specified more than once                                                                                                                                                  |
|                                                                  | `xtinstruments(`\[`reqlist:`\][varlist](http://www.stata.com/help.cgi?varlist)`, lags(#_1/#_2))` |                                                                                                                                                                                                       |
|                                                                  |                                                                                                                                         | specify panel-style instruments; can be specified more than once                                                                                                                                      |
| Weight matrix                                                    |                                                                                                                                         |                                                                                                                                                                                                       |
|                                                                  | `wmatrix(wmtype`\[`, independent`\]`)`                                                                                            |                                                                                                                                                                                                       |
|                                                                  |                                                                                                                                         | specify weight matrix; `wmtype` may be `robust`, `cluster clustvar`, `hac` [<var class="command">kernel</var><strong></strong>](#kernel) \[`lags`\], or `unadjusted`     |
|                                                                  | `center`                                                                                                                                | center moments in weight-matrix computation                                                                                                                                                           |
|                                                                  | `winitial(iwtype`\[`, independent`\]`)`                                                                                           |                                                                                                                                                                                                       |
|                                                                  |                                                                                                                                         | specify initial weight matrix; `iwtype` may be `unadjusted`, `identity`, `xt` [<var class="command">xtspec</var><strong></strong>](#xtspec), or the name of a Stata matrix |
| SE/Robust                                                        |                                                                                                                                         |                                                                                                                                                                                                       |
|                                                                  | `vce(vcetype`\[`, independent`\]`)`                                                                                                 | `vcetype` may be `robust`, `cluster clustvar`, `bootstrap`, `jackknife`, `hac kernel lags`, or `unadjusted`                                                                                     |
|                                                                  | `quickderivatives`                                                                                                                      | use alternative method of computing numerical derivatives for VCE                                                                                                                                     |
| Reporting                                                        |                                                                                                                                         |                                                                                                                                                                                                       |
|                                                                  | `level(#)`                                                                                                                              | set confidence level; default is `level(95)`                                                                                                                                                          |
|                                                                  | `title(string)`                                                                                                                         | display `string` as title above the table of parameter estimates                                                                                                                                      |
|                                                                  | `title2(string)`                                                                                                                        | display `string` as subtitle                                                                                                                                                                          |
|                                                                  | `display_options`                                                                                                                       | control columns and column formats, row spacing, line width, display of omitted variables and base and empty cells, and factor-variable labeling                                                      |
| Optimization                                                     |                                                                                                                                         |                                                                                                                                                                                                       |
|                                                                  | `from(initial_values)`                                                                                                                  | specify initial values for parameters                                                                                                                                                                 |
| \#                                                               | `igmmiterate(#)`                                                                                                                        | specify maximum number of iterations for iterated GMM estimator                                                                                                                                       |
| \#                                                               | `igmmeps(#)`                                                                                                                            | specify \# for iterated GMM parameter convergence criterion; default is `igmmeps(1e-6)`                                                                                                               |
| \#                                                               | `igmmweps(#)`                                                                                                                           | specify \# for iterated GMM weight-matrix convergence criterion; default is `igmmweps(1e-6)`                                                                                                          |
|                                                                  | `optimization_options`                                                                                                                  | control the optimization process; seldom used                                                                                                                                                         |
|                                                                  | `coeflegend`                                                                                                                            | display legend instead of statistics                                                                                                                                                                  |
| \* You can specify at most one of these options.                 |                                                                                                                                         |                                                                                                                                                                                                       |
| \# These options may be specified only when `igmm` is specified. |                                                                                                                                         |                                                                                                                                                                                                       |

| program\_options                                                                      |                        | Description                                                        |
|---------------------------------------------------------------------------------------|------------------------|--------------------------------------------------------------------|
| Model                                                                                 |                        |                                                                    |
|                                                                                       | `evaluator_options`    | additional options to be passed to the moment-evaluator program    |
| \+                                                                                    | `hasderivatives`       | moment-evaluator program can calculate parameter-level derivatives |
| \+                                                                                    | `haslfderivatives`     | moment-evaluator program can calculate linear-form derivatives     |
| \*                                                                                    | `equations(namelist)`  | specify residual equation names                                    |
| \*                                                                                    | `nequations(#)`        | specify number of residual equations                               |
| \#                                                                                    | `parameters(namelist)` | specify parameter names                                            |
| \#                                                                                    | `nparameters(#)`       | specify number of parameters                                       |
| \+ You may not specify both `hasderivatives` and `haslfderivatives`.                  |                        |                                                                    |
| \* You must specify `equations(namelist)` or `nequations(#)`; you may specify both.   |                        |                                                                    |
| \# You must specify `parameters(namelist)` or `nparameters(#)`; you may specify both. |                        |                                                                    |

`rexp_j` and `dexp_jk` may contain factor variables and time-series
operators; see
[<strong>fvvarlist</strong>](http://www.stata.com/help.cgi?fvvarlist)
and
[<strong>tsvarlist</strong>](http://www.stata.com/help.cgi?tsvarlist).

`bootstrap`, `by`, `jackknife`, `rolling`, and `statsby` are allowed;
see
[<strong>prefix</strong>](http://www.stata.com/help.cgi?prefix).

Weights are not allowed with the
[<strong>bootstrap</strong>](http://www.stata.com/help.cgi?bootstrap)
prefix.

`aweight`s are not allowed with the
[<strong>jackknife</strong>](http://www.stata.com/help.cgi?jackknife)
prefix.

`aweight`s, `fweight`s, `iweight`s, and `pweight`s are allowed; see
[<strong>weight</strong>](http://www.stata.com/help.cgi?weight).

`coeflegend` does not appear in the dialog box.

See
[<strong>[R]</strong> gmm postestimation](http://www.stata.com/help.cgi?gmm_postestimation)
for features available after estimation.

`rexp_j` and `dexp_jk` are substitutable expressions, that is, Stata
expressions that also contain parameters to be estimated. The parameters
are enclosed in curly braces and must satisfy the naming requirements
for variables; `{c -(}beta{c )-}` is an example of a parameter. The
notation `{c -(}lcname`:`varlist{c )-}` is allowed for linear
combinations of multiple covariates and their parameters. For example,
`{c -(}xb: mpg price turn _cons{c )-}` defines a linear
combination of the variables `mpg`, `price`, `turn`, and `_cons` (the
constant term). See [R
gmmRemarksandexamplesSubstitutableexpressions`Substitutable expressions`](http://www.stata.com/manuals14/rgmmremarksandexamplessubstitutableexpressions.pdf)
under `Remarks and examples` of **\[R\] gmm**.
