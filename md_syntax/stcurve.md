## Syntax

`stcurve` \[`, options`\]

Options

Description

Main

\*

`survival`

plot survivor function

\*

`hazard`

plot hazard function

\*

`cumhaz`

plot cumulative hazard function

\*

`cif`

plot cumulative incidence function

`at(`[varname](http://www.stata.com/help.cgi?varname)`=#`
\[[varname](http://www.stata.com/help.cgi?varname)`=# ...`\]`)`

value of the specified covariates and

\[`at2(`[varname](http://www.stata.com/help.cgi?varname)`=#`
\[[varname](http://www.stata.com/help.cgi?varname)`=# ...`\]`)`

\[...\]\]\]

{syntab None:Options} {synopt None}`alpha1`conditional frailty model

`fixedonly`

set all random effects to zero

`unconditional`

unconditional frailty model or random-effects model

`marginal`

synonym for `unconditional`

`range(# #)`

range of analysis time

`outfile:(filename` \[`, replace`\]`)`

save values used to plot the curves

`width(#)`

override "optimal" width; use with `hazard`

`kernel(kernel)`

kernel function; use with `hazard`

`noboundary`

no boundary correction; use with `hazard`

mean of unspecified covariates

Plot

`connect_options`

affect rendition of plotted survivor, hazard, or cumulative hazard
function

Add plots

`"addplot(plot)`

add other plots to the generated graph

Y axis, X axis, Titles, Legend, Overall

`twoway_options`

any options other than `by()` documented in
[<strong>[G-3]</strong> <em>twoway_options</em>](http://www.stata.com/help.cgi?twoway_options)

\* One of `survival`, `hazard`, `cumhaz`, or `cif` must be specified.

`survival` and `hazard` are not allowed after estimation with
[<strong>stcrreg</strong>](http://www.stata.com/help.cgi?stcrreg).

`cif` is allowed only after estimation with
[<strong>stcrreg</strong>](http://www.stata.com/help.cgi?stcrreg).
