## Syntax

`binreg`
[depvar](http://www.stata.com/help.cgi?depvar)
\[[indepvars](http://www.stata.com/help.cgi?indepvars)\]
_\[`if`\] \[`in`\]_ \[`weight`\] \[`,`
`options`\]

Options

Description

Model

`noconstant`

suppress constant term

`or`

use logit link and report odds ratios

`rr`

use log link and report risk ratios

`hr`

use log-complement link and report health ratios

`rd`

use identity link and report risk differences

`n(#`\|`varname)`

use `#` or `varname` for number of trials

`exposure(varname)`

include ln(`varname`) in model with coefficient constrained to 1

`offset(varname)`

include `varname` in model with coefficient constrained to 1

`constraints(constraints)`

apply specified linear constraints

`collinear`

keep collinear variables

`mu(varname)`

use `varname` as the initial estimate for the mean of
[depvar](http://www.stata.com/help.cgi?depvar)

`init(varname)`

synonym for `mu(varname)`

SE/Robust

`vce(vcetype)`

`vcetype` may be `eim`, `robust`, `cluster clustvar`, `oim`, `opg`,
`bootstrap`, `jackknife`, `hac`
[<var class="command">kernel</var><strong></strong>](#kernel),
`jackknife1`, or `unbiased`

`t(varname)`

variable name corresponding to time

`vfactor(#)`

multiply variance matrix by scalar `#`

`disp(#)`

quasilikelihood multiplier

set the scale parameter; default is

Reporting

`level(#)`

set confidence level; default is `level(95)`

`coefficients`

report nonexponentiated coefficients

`nocnsreport`

do not display constraints

`display_options`

control columns and column formats, row spacing, line width, display of
omitted variables and base and empty cells, and factor-variable labeling

Maximization

`irls`

use iterated, reweighted least-squares optimization; the default

`ml`

use maximum likelihood optimization

`maximize_options`

control the maximization process; seldom used

`fisher(#)`

Fisher scoring steps

`search`

search for good starting values

`coeflegend`

display legend instead of statistics

`indepvars` may contain factor variables; see
[<strong>fvvarlist</strong>](http://www.stata.com/help.cgi?fvvarlist).

`depvar` and `indepvars` may contain time-series operators; see
[<strong>tsvarlist</strong>](http://www.stata.com/help.cgi?tsvarlist).

`bayes`, `bootstrap`, `by`, `fp`, `jackknife`, `mi estimate`, `rolling`,
and `statsby` are allowed; see
[<strong>prefix</strong>](http://www.stata.com/help.cgi?prefix).
For more details, see
[<strong>[BAYES]</strong> bayes: binreg](http://www.stata.com/help.cgi?bayes_binreg).

`vce(bootstrap)`, `vce(jackknife)`, and `vce(jackknife1)` are not
allowed with the
[<strong>mi estimate</strong>](http://www.stata.com/help.cgi?mi%20estimate)
prefix.

Weights are not allowed with the
[<strong>bootstrap</strong>](http://www.stata.com/help.cgi?bootstrap)
prefix.

`aweight`s are not allowed with the
[<strong>jackknife</strong>](http://www.stata.com/help.cgi?jackknife)
prefix.

`fweight`s, `aweight`s, `iweight`s, and `pweight`s are allowed; see
[<strong>weight</strong>](http://www.stata.com/help.cgi?weight).

`coeflegend` does not appear in the dialog box.

See
[<strong>[R]</strong> binreg postestimation](http://www.stata.com/help.cgi?binreg_postestimation)
for features available after estimation.
