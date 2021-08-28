## Syntax

Draw a c chart

`cchart defect_var unit_var` \[`, cchart_options`\]

Draw a p (fraction-defective) chart

`pchart reject_var unit_var ssize_var` \[`, pchart_options`\]

Draw an R (range or dispersion) chart

`rchart`
[varlist](http://www.stata.com/help.cgi?varlist)
_\[`if`\] \[`in`\]_ \[`, rchart_options`\]

Draw an X-bar (control line) chart

`xchart`
[varlist](http://www.stata.com/help.cgi?varlist)
_\[`if`\] \[`in`\]_ \[`, xchart_options`\]

Draw vertically aligned X-bar and R charts

`shewhart`
[varlist](http://www.stata.com/help.cgi?varlist)
_\[`if`\] \[`in`\]_ \[`,`
`shewhart_options`\]

cchart\_options

Description

Main

`nograph`

suppress graph

Plot

`connect_options`

affect rendition of the plotted points

change look of markers (color, size, etc.) add marker labels; change
look or position

Control limits

`clopts(cline_options)`

affect rendition of the control limits

Add plots

`"addplot(plot)`

add other plots to the generated graph

Y axis, X axis, Titles, Legend, Overall

`twoway_options`

any options other than `by()` documented in
[<strong>[G-3]</strong> <em>twoway_options</em>](http://www.stata.com/help.cgi?twoway_options)

pchart\_options

Description

Main

`stabilized`

stabilize the p chart when sample sizes are unequal

`nograph`

suppress graph

`generate(newvar_f newvar_lcl newvar_ucl)`

store the fractions of defective elements and the lower and upper
control limits

Plot

`connect_options`

affect rendition of the plotted points

change look of markers (color, size, etc.) add marker labels; change
look or position

Control limits

`clopts(cline_options)`

affect rendition of the control limits

Add plots

`"addplot(plot)`

add other plots to the generated graph

Y axis, X axis, Titles, Legend, Overall

`twoway_options`

any options other than `by()` documented in
[<strong>[G-3]</strong> <em>twoway_options</em>](http://www.stata.com/help.cgi?twoway_options)

rchart\_options

Description

Main

`std(#)`

user-specified standard deviation

`nograph`

suppress graph

Plot

`connect_options`

affect rendition of the plotted points

change look of markers (color, size, etc.) add marker labels; change
look or position

Control limits

`clopts(cline_options)`

affect rendition of the control limits

Add plots

`"addplot(plot)`

add other plots to the generated graph

Y axis, X axis, Titles, Legend, Overall

`twoway_options`

any options other than `by()` documented in
[<strong>[G-3]</strong> <em>twoway_options</em>](http://www.stata.com/help.cgi?twoway_options)

xchart\_options

Description

Main

`std(#)`

user-specified standard deviation

`mean(#)`

user-specified mean

`lower(#) upper(#)`

lower and upper limits of the X-bar limits

`nograph`

suppress graph

Plot

`connect_options`

affect rendition of the plotted points

change look of markers (color, size, etc.) add marker labels; change
look or position

Control limits

`clopts(cline_options)`

affect rendition of the control limits

Add plots

`"addplot(plot)`

add other plots to the generated graph

Y axis, X axis, Titles, Legend, Overall

`twoway_options`

any options other than `by()` documented in
[<strong>[G-3]</strong> <em>twoway_options</em>](http://www.stata.com/help.cgi?twoway_options)

shewhart\_options

Description

Main

`std(#)`

user-specified standard deviation

`mean(#)`

user-specified mean

`nograph`

suppress graph

Plot

`connect_options`

affect rendition of the plotted points

change look of markers (color, size, etc.) add marker labels; change
look or position

Control limits

`clopts(cline_options)`

affect rendition of the control limits

Y axis, X axis, Titles, Legend, Overall

`combine_options`

any options documented in
[<strong>[G-2]</strong> graph combine](http://www.stata.com/help.cgi?graph_combine)
