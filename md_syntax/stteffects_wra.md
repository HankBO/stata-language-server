## Syntax

`stteffects wra (omvarlist` \[`, omoptions`\]`) (tvar)`
`(cmvarlist` \[`, cmoptions`\]`)` _\[`if`\]
\[`in`\]_ \[`, stat options`\]

`omvarlist` specifies the variables that predict the survival-time
variable in the outcome model.

`tvar` must contain integer values representing the treatment levels.

`cmvarlist` specifies the variables that predict censoring in the
censoring model.

| omoptions |                                               | Description                                         |
|-----------|-----------------------------------------------|-----------------------------------------------------|
| Model     |                                               |                                                     |
|           | `weibull`                                     | Weibull; the default                                |
|           | `exponential`                                 | exponential                                         |
|           | `gamma`                                       | two-parameter gamma                                 |
|           | `lnormal`                                     | lognormal                                           |
|           | `ancillary(avarlist`\[`, noconstant`\]`)` | specify variables used to model ancillary parameter |
|           | `noconstant`                                  | suppress constant from outcome model                |

| cmoptions |                                               | Description                                         |
|-----------|-----------------------------------------------|-----------------------------------------------------|
| Model     |                                               |                                                     |
|           | `weibull`                                     | Weibull; the default                                |
|           | `exponential`                                 | exponential                                         |
|           | `gamma`                                       | two-parameter gamma                                 |
|           | `lnormal`                                     | lognormal                                           |
|           | `ancillary(avarlist`\[`, noconstant`\]`)` | specify variables used to model ancillary parameter |
|           | `noconstant`                                  | suppress constant from censoring model              |

| stat |           | Description                                                  |
|------|-----------|--------------------------------------------------------------|
| Stat |           |                                                              |
|      | `ate`     | estimate average treatment effect in population; the default |
|      | `atet`    | estimate average treatment effect on the treated             |
|      | `pomeans` | estimate potential-outcome means                             |

| Options      |                    | Description                                                                                                                                      |
|--------------|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| SE/Robust    |                    |                                                                                                                                                  |
|              | `vce(vcetype)`     | `vcetype` may be `robust`, `cluster clustvar`, `bootstrap`, or `jackknife`                                                                     |
| Reporting    |                    |                                                                                                                                                  |
|              | `level(#)`         | set confidence level; default is `level(95)`                                                                                                     |
|              | `aequations`       | display auxiliary-equation results                                                                                                               |
|              | `noshow`           | do not show st setting information                                                                                                               |
|              | `display_options`  | control columns and column formats, row spacing, line width, display of omitted variables and base and empty cells, and factor-variable labeling |
| Maximization |                    |                                                                                                                                                  |
|              | `maximize_options` | control the maximization process; seldom used                                                                                                    |
|              | `iterinit(#)`      | specify starting-value iterations; seldom used                                                                                                   |
| Advanced     |                    |                                                                                                                                                  |
|              | `pstolerance(#)`   | set tolerance for overlap assumption                                                                                                             |
|              | `osample(newvar)`  | identify observations that violate the overlap assumption                                                                                        |
|              | `control(#,label)` | specify the level of `tvar` that is the control                                                                                                  |
|              | `tlevel(#,label)`  | specify the level of `tvar` that is the treatment                                                                                                |
|              | `coeflegend`       | display legend instead of statistics                                                                                                             |

You must `stset` your data before using `stteffects`; see
[<strong>[ST]</strong> stset](http://www.stata.com/help.cgi?stset).

`omvarlist`, `cmvarlist`, and `avarlist` may contain factor variables;
see
[<strong>fvvarlists</strong>](http://www.stata.com/help.cgi?fvvarlists).

`bootstrap`, `by`, `jackknife`, and `statsby` are allowed; see
[<strong>prefix</strong>](http://www.stata.com/help.cgi?prefix).

Weights are not allowed with the
[<strong>bootstrap</strong>](http://www.stata.com/help.cgi?bootstrap)
prefix.

`fweight`s, `iweight`s, and `pweight`s may be specified using `stset`;
see `Weights` under `Remarks and examples` in **\[ST\] stset**. However,
weights may not be specified if you are using the `bootstrap` prefix.

`coeflegend` does not appear in the dialog box.

See
[<strong>[TE]</strong> stteffects postestimation](http://www.stata.com/help.cgi?stteffects_postestimation)
for features available after estimation.
