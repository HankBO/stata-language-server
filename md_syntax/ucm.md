## Syntax

`ucm`
[depvar](http://www.stata.com/help.cgi?depvar)
\[[indepvars](http://www.stata.com/help.cgi?indepvars)\]
_\[`if`\] \[`in`\]_ \[`, options`\]

| Options      |                                        | Description                                                                                                                                                                        |
|--------------|----------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Model        |                                        |                                                                                                                                                                                    |
|              | `model(model)`                         | specify trend and idiosyncratic components                                                                                                                                         |
|              | `seasonal(#)`                      | include a seasonal component with a period of `#` time units                                                                                                                       |
|              | `cycle(#` \[`, frequency(#f)`\]`)` | include a cycle component of order `#` and optionally set initial frequency to `#f`, <span class="nowrap">0 &lt; `#f` &lt; pi_; `cycle()` may be specified up to three times |
|              | `constraints(constraints)`         | apply specified linear constraints                                                                                                                                                 |
|              | `collinear`                            | keep collinear variables {syntab None:SE/Robust} {synopt None}`vce(vcetype)vcetype` may be `oim` or `robust`                                                                     |
| Reporting    |                                        |                                                                                                                                                                                    |
|              | `level(#)`                             | set confidence level; default is `level(95)`                                                                                                                                       |
|              | `nocnsreport`                          | do not display constraints                                                                                                                                                         |
|              | `display_options`                      | control columns and column formats, row spacing, display of omitted variables and base and empty cells, and factor-variable labeling                                               |
| Maximization |                                        |                                                                                                                                                                                    |
|              | `maximize_options`                     | control the maximization process                                                                                                                                                   |
|              | `coeflegend`                           | display legend instead of statistics                                                                                                                                               |

| model |             | Description                                            |
|-------|-------------|--------------------------------------------------------|
|       | `rwalk`     | random-walk model; the default                         |
|       | `none`      | no trend or idiosyncratic component                    |
|       | `ntrend`    | no trend component but include idiosyncratic component |
|       | `dconstant` | deterministic constant with idiosyncratic component    |
|       | `llevel`    | local-level model                                      |
|       | `dtrend`    | deterministic-trend model with idiosyncratic component |
|       | `lldtrend`  | local-level model with deterministic trend             |
|       | `rwdrift`   | random-walk-with-drift model                           |
|       | `lltrend`   | local-linear-trend model                               |
|       | `strend`    | smooth-trend model                                     |
|       | `rtrend`    | random-trend model                                     |

You must `tsset` your data before using `ucm`; see
[<strong>[TS]</strong> tsset](http://www.stata.com/help.cgi?tsset).

`indepvars` may contain factor variables; see
[<strong>fvvarlist</strong>](http://www.stata.com/help.cgi?fvvarlist).

`indepvars` and `depvar` may contain time-series operators; see
[<strong>tsvarlist</strong>](http://www.stata.com/help.cgi?tsvarlist).

`by`, `fp`, `rolling`, and `statsby` are allowed; see
[<strong>prefix</strong>](http://www.stata.com/help.cgi?prefix).

`coeflegend` does not appear in the dialog box.

See
[<strong>[TS]</strong> ucm postestimation](http://www.stata.com/help.cgi?ucm_postestimation)
for features available after estimation.
