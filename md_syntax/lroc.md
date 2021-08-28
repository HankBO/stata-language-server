## Syntax

`lroc`
\[[depvar](http://www.stata.com/help.cgi?depvar)\]
_\[`if`\] \[`in`\]_ \[`weight`\] \[`,`
`options`\]

Options

Description

Main

`all`

compute area under ROC curve and graph curve for all observations

`nograph`

suppress graph

Advanced

`beta(matname)`

row vector containing model coefficients

Plot

change look of the line change look of markers (color, size, etc.) add
marker labels; change look or position

Reference line

`rlopts(cline_options)`

affect rendition of the reference line

Add plots

`"addplot(plot)`

add other plots to the generated graph

Y axis, X axis, Titles, Legend, Overall

`twoway_options`

any options other than `by()` documented in
[<strong>[G-3]</strong> <em>twoway_options</em>](http://www.stata.com/help.cgi?twoway_options)

`r(N)`

number of observations

`r(area)`

area under the ROC curve

`fweight`s are allowed; see
[<strong>weight</strong>](http://www.stata.com/help.cgi?weight).

`lroc` is not appropriate after the `svy` prefix. <span
options="menu">{marker menu}_{nobreak None} {title None:Menu}
{phang None} **Statistics &gt; Binary outcomes &gt; Postestimation
&gt;** **ROC curve after logistic/logit/probit/ivprobit** <span
options="description">{marker description}_{nobreak None} {title
None:Description} {pstd None} `lroc` graphs the ROC curve and calculates
the area under the curve. {pstd None} `lroc` requires that the current
estimation results be from
[<strong>logistic</strong>](http://www.stata.com/help.cgi?logistic),
[<strong>logit</strong>](http://www.stata.com/help.cgi?logit),
[<strong>probit</strong>](http://www.stata.com/help.cgi?probit),
or
[<strong>ivprobit</strong>](http://www.stata.com/help.cgi?ivprobit).
<span options="linkspdf">{marker linkspdf}_{nobreak None} {title
None:Links to PDF documentation} [Quick
start](http://www.stata.com/manuals14/rlrocquickstart.pdf) [Remarks and
examples](http://www.stata.com/manuals14/rlrocremarksandexamples.pdf)
[Methods and
formulas](http://www.stata.com/manuals14/rlrocmethodsandformulas.pdf)
{pstd None} The above sections are not included in this help file. <span
options="options">{marker options}_{nobreak None} {title
None:Options} {dlgtab None:Main} {phang None} `all` requests that the
statistic be computed for all observations in the data, ignoring any
`if` or `in` restrictions specified by the estimation command. {phang
None} `nograph` suppresses graphical output. {dlgtab None:Advanced}
{phang None} `beta(matname)` specifies a row vector containing model
coefficients. The columns of the row vector must be labeled with the
corresponding names of the independent variables in the data. The
dependent variable
[depvar](http://www.stata.com/help.cgi?depvar)
must be specified immediately after the command name. See [R
lrocRemarksandexamplesModelsotherthanthelastfittedmodel`Models other than the last fitted model`](http://www.stata.com/manuals14/rlrocremarksandexamplesmodelsotherthanthelastfittedmodel.pdf)
in **\[R\] lroc**. {dlgtab None:Plot} {phang None} `cline_options`,
`marker_options`, and `marker_label_options` affect the rendition of the
ROC curve -- the plotted points connected by lines. These options affect
the size and color of markers, whether and how the markers are labeled,
and whether and how the points are connected; see
[<strong>[G-3]</strong> <em>cline_options</em>](http://www.stata.com/help.cgi?cline_options),
[<strong>[G-3]</strong> <em>marker_options</em>](http://www.stata.com/help.cgi?marker_options),
and
[<strong>[G-3]</strong> <em>marker_label_options</em>](http://www.stata.com/help.cgi?marker_label_options).
{dlgtab None:Reference line} {phang None} `rlopts(cline_options)`
affects the rendition of the reference line; see
[<strong>[G-3]</strong> <em>cline_options</em>](http://www.stata.com/help.cgi?cline_options).
<span options="addplot()">{marker addplot()}_{nobreak None}
{dlgtab None:Add plots} {phang None} `addplot(plot)` provides a way to
add other plots to the generated graph; see
[<strong>[G-3]</strong> <em>addplot_option</em>](http://www.stata.com/help.cgi?addplot_option).
<span options="twoway_options">{marker twoway\_options}_{nobreak
None} {dlgtab None:Y axis, X axis, Titles, Legend, Overall} {phang None}
`twoway_options` are any of the options documented in
[<strong>[G-3]</strong> <em>twoway_options</em>](http://www.stata.com/help.cgi?twoway_options),
excluding `by()`. These include options for titling the graph (see
[<strong>[G-3]</strong> <em>title_options</em>](http://www.stata.com/help.cgi?title_options))
and for saving the graph to disk (see
[<strong>[G-3]</strong> <em>saving_option</em>](http://www.stata.com/help.cgi?saving_option)).
<span options="example">{marker example}_{nobreak None} {title
None:Example} {pstd None}Setup

`. webuse lbw` {pstd None}Fit logistic regression to predict low birth
weight

`. logistic low age lwt i.race smoke ptl ht ui` {pstd None}Graph ROC
curve and calculate area under the curve

`. lroc` <span options="results">{marker results}_{nobreak None}
{title None:Stored results} {pstd None} `lroc` stores the following in
`r()`: <span options="20 tabbed">{synoptset 20 tabbed}_{nobreak
None} <span options="5 15 19 2">{p2col 5 15 19 2: Scalars}_
