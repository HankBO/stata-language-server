## Syntax

`irt rsm`
[varlist](http://www.stata.com/help.cgi?varlist)
_\[`if`\] \[`in`\]_
\[[<var class="command">weight</var><strong></strong>](irt%20rsm##weight)\]
\[`, options`\]

Options

Description

Model

`listwise`

drop observations with any missing items

SE/Robust

`vce(vcetype)`

`vcetype` may be `oim`, `robust`, `cluster clustvar`, `bootstrap`, or
`jackknife`

Reporting

`level(#)`

set confidence level; default is `level(95)`

`notable`

suppress coefficient table

`noheader`

suppress output header

[<var class="command">display_options</var><strong></strong>](#display_options)

control columns and column formats

Integration

`intmethod(`[<var class="command">intmethod</var><strong></strong>](#intmethod)`)`

integration method

`intpoints(#)`

set the number of integration points; default is `intpoints(7)`

Maximization

`maximize_options`

control the maximization process; seldom used

`startvalues(svmethod)`

method for obtaining starting values

`noestimate`

do not fit the model; show starting values instead

`dnumerical`

use numerical derivative techniques

INCLUDE help shortdes-coeflegend

| intmethod |               | Description                                                  |
|-----------|---------------|--------------------------------------------------------------|
|           | `mvaghermite` | mean-variance adaptive Gauss-Hermite quadrature; the default |
|           | `mcaghermite` | mode-curvature adaptive Gauss-Hermite quadrature             |
|           | `ghermite`    | nonadaptive Gauss-Hermite quadrature                         |

`bootstrap`, `by`, `jackknife`, `statsby`, and `svy` are allowed; see
[<strong>prefix</strong>](http://www.stata.com/help.cgi?prefix).

Weights are not allowed with the
[<strong>bootstrap</strong>](http://www.stata.com/help.cgi?bootstrap)
prefix.

`vce()` and weights are not allowed with the
[<strong>svy</strong>](http://www.stata.com/help.cgi?svy)
prefix.

`fweight`s, `iweight`s, and `pweight`s are allowed; see
[<strong>weight</strong>](http://www.stata.com/help.cgi?weight).

`startvalues()`, `noestimate`, `dnumerical`, and `coeflegend` do not
appear in the dialog box.

See
[<strong>[IRT]</strong> irt rsm postestimation](http://www.stata.com/help.cgi?irt_rsm_postestimation)
for features available after estimation.
