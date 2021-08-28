## Syntax

`lowess yvar xvar` _\[`if`\] \[`in`\]_
\[`, options`\]

Options

Description

Main

`mean`

running-mean smooth; default is running-line least squares

`noweight`

suppress weighted regressions; default is tricube weighting function

`bwidth(#)`

use `#` for the bandwidth; default is `bwidth(0.8)`

`logit`

transform dependent variable to logits

`adjust`

adjust smoothed mean to equal mean of dependent variable

`nograph`

suppress graph

`generate(newvar)`

create `newvar` containing smoothed values of `yvar`

Plot

change look of markers (color, size, etc.) add marker labels; change
look or position

Smoothed line

`lineopts(cline_options)`

affect rendition of the smoothed line

Add plots

`"addplot(plot)`

add other plots to generated graph

Y axis, X axis, Titles, Legend, Overall, By

`twoway_options`

any of the options documented in
[<strong>[G-3]</strong> <em>twoway_options</em>](http://www.stata.com/help.cgi?twoway_options)

`yvar` and `xvar` may contain time-series operators; see
[<strong>tsvarlist</strong>](http://www.stata.com/help.cgi?tsvarlist).
<span options="menu">{marker menu}_{nobreak None} {title
None:Menu} {phang None} **Statistics &gt; Nonparametric analysis &gt;
Lowess smoothing** <span options="description">{marker
description}_{nobreak None} {title None:Description} {pstd None}
`lowess` carries out a locally weighted regression of `yvar` on `xvar`,
displays the graph, and optionally saves the smoothed variable. {pstd
None} Warning: `lowess` is computationally intensive and may therefore
take a long time to run on a slow computer. Lowess calculations on 1,000
observations, for instance, require performing 1,000 regressions. <span
options="linkspdf">{marker linkspdf}_{nobreak None} {title
None:Links to PDF documentation} [Quick
start](http://www.stata.com/manuals14/rlowessquickstart.pdf) [Remarks
and
examples](http://www.stata.com/manuals14/rlowessremarksandexamples.pdf)
[Methods and
formulas](http://www.stata.com/manuals14/rlowessmethodsandformulas.pdf)
{pstd None} The above sections are not included in this help file. <span
options="options">{marker options}_{nobreak None} {title
None:Options} {dlgtab None:Main} {phang None} `mean` specifies
running-mean smoothing; the default is running-line least-squares
smoothing. {phang None} `noweight` prevents the use of Cleveland's
([<strong>1979</strong>](#C1979)) tricube
weighting function; the default is to use the weighting function. {phang
None} `bwidth(#)` specifies the bandwidth. Centered subsets of
`bwidth()`\*N observations are used for calculating smoothed values for
each point in the data except for end points, where smaller, uncentered
subsets are used. The greater the `bwidth()`, the greater the smoothing.
The default is 0.8. {phang None} `logit` transforms the smoothed `yvar`
into logits. Predicted values less than 0.0001 or greater than 0.9999
are set to 1/N and 1-1/N, respectively, before taking logits. {phang
None} `adjust` adjusts the mean of the smoothed `yvar` to equal the mean
of `yvar` by multiplying by an appropriate factor. This option is useful
when smoothing binary (0/1) data. {phang None} `nograph` suppresses
displaying the graph. {phang None} `generate(newvar)` creates `newvar`
containing the smoothed values of `yvar`. {dlgtab None:Plot} {phang
None} `marker_options` affect the rendition of markers drawn at the
plotted points, including their shape, size, color, and outline; see
[<strong>[G-3]</strong> <em>marker_options</em>](http://www.stata.com/help.cgi?marker_options).
{phang None} `marker_label_options` specify if and how the markers are
to be labeled; see
[<strong>[G-3]</strong> <em>marker_label_options</em>](http://www.stata.com/help.cgi?marker_label_options).

### Smoothed line

`lineopts(cline_options)` affects the rendition of the lowess-smoothed
line; see
[<strong>[G-3]</strong> <em>cline_options</em>](http://www.stata.com/help.cgi?cline_options).

### Add plots

`addplot(plot)` provides a way to add other plots to the generated
graph; see
[<strong>[G-3]</strong> <em>addplot_option</em>](http://www.stata.com/help.cgi?addplot_option).

### Y axis, X axis, Titles, Legend, Overall, By

`twoway_options` are any of the options documented in
[<strong>[G-3]</strong> <em>twoway_options</em>](http://www.stata.com/help.cgi?twoway_options).
These include options for titling the graph (see
[<strong>[G-3]</strong> <em>title_options</em>](http://www.stata.com/help.cgi?title_options)),
options for saving the graph to disk (see
[<strong>[G-3]</strong> <em>saving_option</em>](http://www.stata.com/help.cgi?saving_option)),
and the `by()` option (see
[<strong>[G-3]</strong> <em>by_option</em>](http://www.stata.com/help.cgi?by_option)).
