## Syntax

`etpoisson`
[depvar](http://www.stata.com/help.cgi?depvar)
\[[indepvars](http://www.stata.com/help.cgi?indepvars)\]
_\[`if`\] \[`in`\]_ \[`weight`\]`,`
`treat(depvar_t = indepvars_t` \[`, noconstant`
`offset(varname_o)`\]`)` \[`options`\]

| Options                                                                           |                                | Description                                                                                                                                      |
|-----------------------------------------------------------------------------------|--------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| Model                                                                             |                                |                                                                                                                                                  |
| \*                                                                                | `treat()`                      | equation for treatment effects                                                                                                                   |
|                                                                                   | `noconstant`                   | suppress constant term                                                                                                                           |
|                                                                                   | `exposure(varname_e)`          | include ln(`varname_e`) in model with coefficient constrained to 1                                                                               |
|                                                                                   | `offset(varname_o)`            | include `varname_o` in model with coefficient constrained to 1                                                                                   |
|                                                                                   | `constraints(constraints)` | apply specified linear constraints                                                                                                               |
|                                                                                   | `collinear`                    | keep collinear variables                                                                                                                         |
| SE/Robust                                                                         |                                |                                                                                                                                                  |
|                                                                                   | `vce(vcetype)`                 | `vcetype` may be `oim`, `robust`, `cluster clustvar`, `opg`, `bootstrap`, or `jackknife`                                                       |
| Reporting                                                                         |                                |                                                                                                                                                  |
|                                                                                   | `level(#)`                     | set confidence level; default is `level(95)`                                                                                                     |
|                                                                                   | `irr`                          | report incidence-rate ratios                                                                                                                     |
|                                                                                   | `nocnsreport`                  | do not display constraints                                                                                                                       |
|                                                                                   | `display_options`              | control columns and column formats, row spacing, line width, display of omitted variables and base and empty cells, and factor-variable labeling |
| Integration                                                                       |                                |                                                                                                                                                  |
|                                                                                   | `intpoints(#)`                 | use `#` Gauss-Hermite quadrature points; default is `intpoints(24)`                                                                              |
| Maximization                                                                      |                                |                                                                                                                                                  |
|                                                                                   | `maximize_options`             | control the maximization process; seldom used                                                                                                    |
|                                                                                   | `coeflegend`                   | display legend instead of statistics                                                                                                             |
| \* `treat()` is required. The full specification is                               |                                |                                                                                                                                                  |
| `treat(depvar_t = indepvars_t` \[`, noconstant offset(varname_o)`\]`)`. |                                |                                                                                                                                                  |

`indepvars` and `indepvars_t` may contain factor variables; see
[<strong>fvvarlist</strong>](http://www.stata.com/help.cgi?fvvarlist).

`depvar`, `depvar_t`, `indepvars`, and `indepvars_t` may contain
time-series operators; see
[<strong>tsvarlist</strong>](http://www.stata.com/help.cgi?tsvarlist).

`bootstrap`, `by`, `jackknife`, `rolling`, `statsby`, and `svy` are
allowed; see
[<strong>prefix</strong>](http://www.stata.com/help.cgi?prefix).

Weights are not allowed with the
[<strong>bootstrap</strong>](http://www.stata.com/help.cgi?bootstrap)
prefix.

`aweight`s are not allowed with the
[<strong>jackknife</strong>](http://www.stata.com/help.cgi?jackknife)
prefix.

`vce()` and weights are not allowed with the
[<strong>svy</strong>](http://www.stata.com/help.cgi?svy)
prefix.

`fweight`s, `aweight`s, `iweight`s, and `pweight`s are allowed; see
[<strong>weight</strong>](http://www.stata.com/help.cgi?weight).

`coeflegend` does not appear in the dialog box.

See
[<strong>[TE]</strong> etpoisson postestimation](http://www.stata.com/help.cgi?etpoisson_postestimation)
for features available after estimation.
