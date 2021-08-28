## Syntax

`pkexamine time concentration` _\[`if`\]
\[`in`\]_ \[`, options`\]

Options

Description

Main

`fit(#)`

use `#` points to estimate AUC\_0,inf; default is `fit(3)`

`trapezoid`

use trapezoidal rule; default is cubic splines

`graph`

graph the AUC

`line`

graph the linear extension

`log`

graph the log extension

`exp(#)`

plot the exponential fit for the AUC\_0,inf

AUC plot

`cline_options`

affect rendition of plotted points connected by lines

change look of markers (color, size, etc.) add marker labels; change
look or position

Add plots

`"addplot(plot)`

add other plots to the generated graph

Y axis, X axis, Titles, Legend, Overall

`twoway_options`

any options other than `by()` documented in
[<strong>[G-3]</strong> <em>twoway_options</em>](http://www.stata.com/help.cgi?twoway_options)

`r(auc)`

AUC

`r(half)`

half-life of the drug

`r(ke)`

elimination rate

`r(tmax)`

time at last concentration measurement

`r(cmax)`

maximum concentration

`r(tomc)`

time of maximum concentration

`r(auc_line)`

AUC\_0,inf estimated with a linear fit

`r(auc_exp)`

AUC\_0,inf estimated with an exponential fit

`r(auc_ln)`

AUC\_0,inf estimated with a linear fit of the natural log

`by` is allowed; see
[<strong>[D]</strong> by](http://www.stata.com/help.cgi?by).
<span options="menu">{marker menu}_{nobreak None} {title
None:Menu} {phang None} **Statistics &gt; Epidemiology and related &gt;
Other &gt; Pharmacokinetic measures** <span
options="description">{marker description}_{nobreak None} {title
None:Description} {pstd None} `pkexamine` calculates pharmacokinetic
measures from concentration-and-time subject-level data. `pkexamine`
computes and displays the maximum measured concentration, the time at
the maximum measured concentration, the time of the last measurement,
the elimination time, the half-life, and the area under the
concentration-time curve (AUC\_0,tmax). Three estimates of the AUC from
0 to infinity (AUC\_0,inf) are also calculated. {pstd None} `pkexamine`
is one of the pk commands. Please read
[<strong>pk</strong>](http://www.stata.com/help.cgi?pk)
before reading this entry. <span options="linkspdf">{marker
linkspdf}_{nobreak None} {title None:Links to PDF documentation}
[Quick start](http://www.stata.com/manuals14/rpkexaminequickstart.pdf)
[Remarks and
examples](http://www.stata.com/manuals14/rpkexamineremarksandexamples.pdf)
[Methods and
formulas](http://www.stata.com/manuals14/rpkexaminemethodsandformulas.pdf)
{pstd None} The above sections are not included in this help file. <span
options="options">{marker options}_{nobreak None} {title
None:Options} {dlgtab None:Main} {phang None} `fit(#)` specifies the
number of points, counting back from the last measurement, to use in
fitting the extension to estimate the AUC\_0,inf. The default is
`fit(3)`, or the last three points. This should be viewed as a minimum;
the appropriate number of points will depend on your data. {phang None}
`trapezoid` specifies that the trapezoidal rule be used to calculate the
AUC\_0,tmax. The default is cubic splines, which give better results for
most functions. When the curve is irregular, `trapezoid` may give better
results. {phang None} `graph` tells `pkexamine` to graph the
concentration-time curve. {phang None} `line` and `log` specify the
estimates of the AUC\_0,inf to display when graphing the AUC\_0,inf. If
the `graph` option is not also specified, then these options are
ignored. {phang None} `exp(#)` specifies that the exponential fit for
the AUC\_0,inf be plotted. You must specify the maximum time value to
which you want to plot the curve, and this time value must be greater
than the maximum time measurement in the data. If you specify 0, the
curve will be plotted to the point at which the linear extension would
cross the `x` axis. If the `graph` option is not also specified, then
this option is ignored. This option is not valid with the `line` or
`log` option. {dlgtab None:AUC plot} {phang None} `cline_options` affect
the rendition of the plotted points connected by lines; see
[<strong>[G-3]</strong> <em>cline_options</em>](http://www.stata.com/help.cgi?cline_options).
{phang None} `marker_options` specify the look of markers. This look
includes the marker symbol, size, color, and outline; see
[<strong>[G-3]</strong> <em>marker_options</em>](http://www.stata.com/help.cgi?marker_options).
{phang None} `marker_label_options` specify if and how the markers are
to be labeled; see
[<strong>[G-3]</strong> <em>marker_label_options</em>](http://www.stata.com/help.cgi?marker_label_options).
{dlgtab None:Add plots} {phang None} `addplot(plot)` provides a way to
add other plots to the generated graph; see
[<strong>[G-3]</strong> <em>addplot_option</em>](http://www.stata.com/help.cgi?addplot_option).
{dlgtab None:Y axis, X axis, Titles, Legend, Overall} {phang None}
`twoway_options` are any of the options documented in
[<strong>[G-3]</strong> <em>twoway_options</em>](http://www.stata.com/help.cgi?twoway_options),
excluding `by()`. These include options for titling the graph (see
[<strong>[G-3]</strong> <em>title_options</em>](http://www.stata.com/help.cgi?title_options))
and for saving the graph to disk (see
[<strong>[G-3]</strong> <em>saving_option</em>](http://www.stata.com/help.cgi?saving_option)).
<span options="examples">{marker examples}_{nobreak None} {title
None:Examples} {phang None}`. webuse auc`<span options="32">{space
32}_(setup)

`. pkexamine time concentration` <span options="12">{space 12}_
(show measures)

`. pkexamine time concentration, fit(7)` <span options="4">{space
4}_ (use last 7 points to fit model)

`. pkexamine time concentration, trapezoid` <span options="1">{space
1}_ (use trapezoidal rule in calculating AUC)

`. pkexamine time concentration, graph` <span options="5">{space
5}_ (graph the AUC) <span options="results">{marker
results}_{nobreak None} {title None:Stored results} {pstd None}
`pkexamine` stores the following in `r()`: <span
options="15 tabbed">{synoptset 15 tabbed}_{nobreak None} <span
options="5 15 19 2">{p2col 5 15 19 2: Scalars}_
