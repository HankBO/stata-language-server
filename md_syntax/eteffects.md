## Syntax

`eteffects`
`(`[<var class="command">ovar</var><strong></strong>](http://www.stata.com/help.cgi?varlist)
[<var class="command">omvarlist</var><strong></strong>](http://www.stata.com/help.cgi?varlist)
\[`,`
[<var class="command">omodel</var><strong></strong>](#omodel)
`noconstant`\]`)`
`(`[<var class="command">tvar</var><strong></strong>](http://www.stata.com/help.cgi?varlist)
[<var class="command">tmvarlist</var><strong></strong>](http://www.stata.com/help.cgi?varlist)
\[`, noconstant`\]`)` _\[`if`\] \[`in`\]_
\[[<var class="command">weight</var><strong></strong>](#weight)\]
\[`,`
[<var class="command">stat</var><strong></strong>](#stat)
[<var class="command">options</var><strong></strong>](#opttable)\]

`ovar` is the
[depvar](http://www.stata.com/help.cgi?depvar)
of the outcome model.

`omvarlist` is the list of exogenous
[indepvars](http://www.stata.com/help.cgi?indepvars)
in the outcome model.

`tvar` is the binary treatment variable.

`tmvarlist` is the list of covariates that predict treatment assignment.

| omodel |               | Description                       |
|--------|---------------|-----------------------------------|
| Model  |               |                                   |
|        | `linear`      | linear outcome model; the default |
|        | `fractional`  | fractional probit outcome model   |
|        | `probit`      | probit outcome model              |
|        | `exponential` | exponential-mean outcome model    |

| stat  |           | Description                                                  |
|-------|-----------|--------------------------------------------------------------|
| Model |           |                                                              |
|       | `ate`     | estimate average treatment effect in population; the default |
|       | `atet`    | estimate average treatment effect on the treated             |
|       | `pomeans` | estimate potential-outcome means                             |

| Options                                                                                                                                                                          |                    | Description                                                                                                                                      |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| Model                                                                                                                                                                            |                    |                                                                                                                                                  |
|                                                                                                                                                                                  | `noconstant`       | suppress constant term                                                                                                                           |
| SE/Robust                                                                                                                                                                        |                    |                                                                                                                                                  |
|                                                                                                                                                                                  | `vce(vcetype)`     | `vcetype` may be `robust`, `cluster clustvar`, `bootstrap`, or `jackknife`                                                                     |
| Reporting                                                                                                                                                                        |                    |                                                                                                                                                  |
|                                                                                                                                                                                  | `level(#)`         | set confidence level; default is `level(95)`                                                                                                     |
|                                                                                                                                                                                  | `aequations`       | display auxiliary-equation results                                                                                                               |
|                                                                                                                                                                                  | `display_options`  | control columns and column formats, row spacing, line width, display of omitted variables and base and empty cells, and factor-variable labeling |
| Maximization                                                                                                                                                                     |                    |                                                                                                                                                  |
|                                                                                                                                                                                  | `maximize_options` | control the maximization process; seldom used                                                                                                    |
| Advanced                                                                                                                                                                         |                    |                                                                                                                                                  |
|                                                                                                                                                                                  | `pstolerance(#)`   | set tolerance for overlap assumption                                                                                                             |
|                                                                                                                                                                                  | `osample(newvar)`  | generate `newvar` to mark observations that violate the overlap assumption                                                                       |
|                                                                                                                                                                                  | `coeflegend`       | display legend instead of statistics                                                                                                             |
| `omvarlist` and `tmvarlist` may contain factor variables; see [<strong>fvvarlists</strong>](http://www.stata.com/help.cgi?fvvarlists).                |                    |                                                                                                                                                  |
| `bootstrap`, `by`, `jackknife`, and `statsby` are allowed; see [<strong>prefix</strong>](http://www.stata.com/help.cgi?prefix).                       |                    |                                                                                                                                                  |
| Weights are not allowed with the [<strong>bootstrap</strong>](http://www.stata.com/help.cgi?bootstrap) prefix.                                        |                    |                                                                                                                                                  |
| `fweight`s, `iweight`s, and `pweight`s are allowed; see [<strong>weight</strong>](http://www.stata.com/help.cgi?weight).                              |                    |                                                                                                                                                  |
| `coeflegend` does not appear in the dialog box.                                                                                                                                  |                    |                                                                                                                                                  |
| See [<strong>[TE]</strong> eteffects postestimation](http://www.stata.com/help.cgi?eteffects_postestimation) for features available after estimation. |                    |                                                                                                                                                  |
