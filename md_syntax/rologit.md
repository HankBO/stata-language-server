## Syntax

`rologit`
[depvar](http://www.stata.com/help.cgi?depvar)
[indepvars](http://www.stata.com/help.cgi?indepvars)
_\[`if`\] \[`in`\]_ \[`weight`\]`,`
`group(varname)` \[`options`\]

options

Description

Model

\*

`group(varname)`

identifier variable that links the alternatives

`offset(varname)`

include `varname` in model with coefficient constrained to 1

`incomplete(#)`

use `#` to code unranked alternatives; default is `incomplete(0)`

`reverse`

reverse the preference order

`notestrhs`

keep right-hand-side variables that do not vary within group

`ties(spec)`

method to handle ties: `exactm`, `breslow`, `efron`, or `none`

SE/Robust

`"vce(vcetype)`

`vcetype` may be `oim`, `robust`, `cluster clustvar`, `bootstrap`, or
`jackknife`

Reporting

`level(#)`

set confidence level; default is `level(95)`

`display_options`

control columns and column formats, row spacing, line width, display of
omitted variables and base and empty cells, and factor-variable labeling

Maximization

`maximize_options`

control the maximization process; seldom used

`coeflegend`

display legend instead of statistics

Breslow's method (default if s specified) Efron's method (default if
robust VCE) no ties allowed

\*`group(varname)` is required.

`indepvars` may contain factor variables; see
[<strong>fvvarlist</strong>](http://www.stata.com/help.cgi?fvvarlist).

`bootstrap`, `by`, `fp`, `jackknife`, `rolling`, and `statsby` are
allowed; see
[<strong>prefix</strong>](http://www.stata.com/help.cgi?prefix).

Weights are not allowed with the
[<strong>bootstrap</strong>](http://www.stata.com/help.cgi?bootstrap)
prefix.

`fweight`s, `iweight`s, and `pweight`s are allowed, except with
`ties(efron)`; see
[<strong>weight</strong>](http://www.stata.com/help.cgi?weight).

`coeflegend` does not appear in the dialog box.

See
[<strong>[R]</strong> rologit postestimation](http://www.stata.com/help.cgi?rologit_postestimation)
for features available after estimation. <span options="menu">{marker
menu}_{nobreak None} {title None:Menu} {phang None} **Statistics
&gt; Ordinal outcomes &gt; Rank-ordered logistic regression** <span
options="description">{marker description}_{nobreak None} {title
None:Description} {pstd None} `rologit` fits the rank-ordered logistic
regression model by maximum likelihood
([<strong>Beggs, Cardell, and Hausman 1981</strong>](#BCH1981)).
This model is also known as the Plackett-Luce model
([<strong>Marden 1995</strong>](#M1995)), as
the exploded logit model
([<strong>Punj and Staelin 1978</strong>](#PS1978)),
and as the choice-based method of conjoint analysis
([<strong>Hair et al. 2010</strong>](#HBBA2010)).
{pstd None} `rologit` expects the data to be in long form, similar to
`clogit`, in which each of the ranked alternatives forms an observation;
all observations related to an individual are linked together by the
variable that you specify in the `group()` option. The distinction from
`clogit` is that
[depvar](http://www.stata.com/help.cgi?depvar)
in `rologit` records the rankings of the alternatives, whereas for
`clogit`, `depvar` marks only the best alternative by a value not equal
to zero. `rologit` interprets equal scores of `depvar` as ties. The
ranking information may be incomplete "at the bottom" (least preferred
alternatives). That is, unranked alternatives may be coded as 0 or as a
common value that may be specified with the `incomplete()` option. {pstd
None} If your data record only the unique alternative, `rologit` fits
the same model as `clogit`. <span options="linkspdf">{marker
linkspdf}_{nobreak None} {title None:Links to PDF documentation}
[Quick start](http://www.stata.com/manuals14/rrologitquickstart.pdf)
[Remarks and
examples](http://www.stata.com/manuals14/rrologitremarksandexamples.pdf)
[Methods and
formulas](http://www.stata.com/manuals14/rrologitmethodsandformulas.pdf)
{pstd None} The above sections are not included in this help file. <span
options="options">{marker options}_{nobreak None} {title
None:Options} {dlgtab None:Model} {phang None} `group(varname)` is
required, and it specifies the identifier variable (numeric or string)
that links the alternatives for an individual, which have been compared
and rank ordered with respect to one another. {phang None}
`offset(varname)`; see
[<strong>[R] estimation options</strong>](estimation%20options##offset()).
{phang None} `incomplete(#)` specifies the numeric value used to code
alternatives that are not ranked. It is assumed that unranked
alternatives are less preferred than the ranked alternatives (that is,
the data record the ranking of the most preferred alternatives). It is
not assumed that subjects are indifferent between the unranked
alternatives. `#` defaults to 0. {phang None} `reverse` specifies that
in the preference order, a higher number means a less attractive
alternative. The default is that higher values indicate more attractive
alternatives. The rank-ordered logit model is not symmetric in the sense
that reversing the ordering simply leads to a change in the signs of the
coefficients. {phang None} `notestrhs` suppresses the test that the
independent variables vary within (at least some of) the groups. Effects
of variables that are always constant are not identified. For instance,
a rater's gender cannot directly affect his or her rankings; it could
affect the rankings only via an interaction with a variable that does
vary over alternatives. {phang None} `ties(spec)` specifies the method
for handling ties (indifference between alternatives) (see
[<strong>[ST]</strong> stcox](http://www.stata.com/help.cgi?stcox)
for details): <span options="9 19 21 2">{p2colset 9 19 21
2}_{nobreak None} {p2col None}`exactm`exact marginal likelihood
(default)

### SE/Robust

`vce(vcetype)` specifies the type of standard error reported, which
includes types that are derived from asymptotic theory (`oim`), that are
robust to some kinds of misspecification (`robust`), that allow for
intragroup correlation (`cluster clustvar`), and that use bootstrap or
jackknife methods (`bootstrap`, `jackknife`); see
[<var class="command">vce_option</var><strong>[R]</strong>](http://www.stata.com/help.cgi?vce_option)
.

If `ties(exactm)` is specified, `vcetype` may be only `oim`,
`bootstrap`, or `jackknife`.

### Reporting

`level(#)`; see
[<strong>[R] estimation options</strong>](estimation%20options##level()).

`display_options`: `noci`, `nopvalues`, `noomitted`, `vsquish`,
`noemptycells`, `baselevels`, `allbaselevels`, `nofvlabel`, `fvwrap(#)`,
`fvwrapon(style)`, `cformat(%fmt)`, `pformat(%fmt)`, `sformat(%fmt)`,
and `nolstretch`; see
[<strong>[R] estimation options</strong>](estimation%20options##display_options).

### Maximization

`maximize_options`: `iterate(#)`, `trace`, \[

\]

`g`, `tolerance(#)`, `ltolerance(#)`, `nrtolerance(#)`, and
`nonrtolerance`; see
[<strong>[R]</strong> maximize](http://www.stata.com/help.cgi?maximize).
These options are seldom used.

The following option is available with `rologit` but is not shown in the
dialog box:

`coeflegend`; see
[<strong>[R] estimation options</strong>](estimation%20options##coeflegend).
