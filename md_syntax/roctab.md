## Syntax

`roctab`<span options="1">{space 1}_ `refvar classvar` <span
class="command">\[`if`\] \[`in`\]_ \[`weight`\] \[`, options`\]

options

Description

Main

`lorenz`

report Gini and Pietra indices

`binomial`

calculate exact binomial confidence intervals

`nolabel`

display numeric codes rather than value labels

`detail`

show details on sensitivity/specificity for each cutpoint

`table`

display the raw data in a 2 x k contingency table

`bamber`

calculate standard errors by using the Bamber method

`hanley`

calculate standard errors by using the Hanley method

`graph`

graph the ROC curve

`norefline`

suppress plotting the 45-degree reference line

`summary`

report the area under the ROC curve

`specificity`

graph sensitivity versus specificity

`level(#)`

set confidence level; default is `level(95)`

Plot

`plotopts(plot_options)`

affect rendition of the ROC curve

Reference line

`rlopts(cline_options)`

affect rendition of the reference line

Add plots

`"addplot(plot)`

add other plots to generated graph

Y axis, X axis, Titles, Legend, Overall

`twoway_options`

any options other than `by()` documented in
[<strong>[G-3]</strong> <em>twoway_options</em>](http://www.stata.com/help.cgi?twoway_options)

add marker labels; change look or position change look of the line

`fweight`s are allowed; see
[<strong>weight</strong>](http://www.stata.com/help.cgi?weight).
<span options="plot_options">{marker plot\_options}_{nobreak None}
<span options="25">{synoptset 25}_{nobreak None} {synopthdr
None:plot\_options} {synoptline None} {p2col None}`marker_options`change
look of markers (color, size, etc.)
