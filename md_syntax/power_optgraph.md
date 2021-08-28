## Syntax

Produce default graph

`power` ... `, graph` ...

Graph power against sample size

`power` ... `, graph(y(power) x(N))` ...

Graph sample size against target parameter

`power` ... `, graph(y(N) x(target))` ...

Graph effect size against sample size

`power` ... `, graph(y(delta) x(N))` ...

Produce other custom graphs

\[`power`\] ... `, graph(graphopts)` ...

<table id="graphopts" class="syntab">
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">graphopts</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd section">
<td colspan="3">Main</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command">ydimension(</code>[<var class="command">dimlist</var><strong></strong>](#dimlist) [<code class="command">,</code> [<var class="command">dimopts</var><strong></strong>](#dimopts)]<code class="command">)</code></td>
<td>use <var class="command">dimlist</var> to define y axis</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command">xdimension(</code>[<var class="command">dimlist</var><strong></strong>](#dimlist) [<code class="command">,</code> [<var class="command">dimopts</var><strong></strong>](#dimopts)]<code class="command">)</code></td>
<td>use <var class="command">dimlist</var> to define x axis</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command">plotdimension(</code>[<var class="command">dimlist</var><strong></strong>](#dimlist) [<code class="command">,</code> [<var class="command">dimopts</var><strong></strong>](#dimopts)]<code class="command">)</code></td>
<td>create plots for groups in <var class="command">dimlist</var></td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command">bydimension(</code>[<var class="command">dimlist</var><strong></strong>](#dimlist) [<code class="command">,</code> [<var class="command">dimopts</var><strong></strong>](#dimopts)]<code class="command">)</code></td>
<td>create subgraphs for groups in <var class="command">dimlist</var></td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command">graphdimension(</code>[<var class="command">dimlist</var><strong></strong>](#dimlist) [<code class="command">,</code> [<var class="command">dimopts</var><strong></strong>](#dimopts)]<code class="command">)</code></td>
<td>create graphs for groups in <var class="command">dimlist</var></td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="horiz">horizontal</code></td>
<td>swap x and y axes</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="schemeg">schemegrid</code></td>
<td>do not apply default x and y grid lines</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command">name(</code><var class="command">name</var>|<var class="command">stub</var> [<code class="command">, replace</code>]<code class="command">)</code></td>
<td>name of graph, or stub if multiple graphs</td>
</tr>
</tbody>
<tbody>
<tr class="odd section">
<td colspan="3">Labels</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="yreg">yregular</code></td>
<td>place regularly spaced ticks and labels on the y axis</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="xreg">xregular</code></td>
<td>place regularly spaced ticks and labels on the x axis</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="yval">yvalues</code></td>
<td>place ticks and labels on the y axis for each distinct value</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="xval">xvalues</code></td>
<td>place ticks and labels on the x axis for each distinct value</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command"> collabels(</code>[<var class="command">colspec</var><strong></strong>](#colspec)<code class="command">)</code></td>
<td>change default labels for columns</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="nolab">nolabels</code></td>
<td>label groups with their values, not their labels</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="allsim">allsimplelabels</code></td>
<td>forgo column label and equal signs in all labels</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="nosim">nosimplelabels</code></td>
<td>include column label and equal signs in all labels</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="eqsep">eqseparator(string)</code></td>
<td>replace equal sign separator with <var class="command">string</var></td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="sep">separator(string)</code></td>
<td>separator for labels when multiple columns are specified in a dimension</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="nosep">noseparator</code></td>
<td>do not use a separator</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command">format(</code>[<strong>%</strong><var class="command">fmt</var><strong></strong>](http://www.stata.com/help.cgi?format)<code class="command">)</code></td>
<td>format for converting numeric values to labels</td>
</tr>
</tbody>
<tbody>
<tr class="odd section">
<td colspan="3">Plot</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command">plotopts(</code><var class="command">plot_options</var><code class="command">)</code></td>
<td>affect rendition of all plots</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command">plot</code>
<ul>
</ul>
<code class="command">opts(</code><var class="command">plot_options</var><code class="command">)</code></td>
<td>affect rendition of <var class="command">#</var>th plot</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="recast">recast(plottype)</code></td>
<td>plot all plots using <var class="command">plottype</var></td>
</tr>
</tbody>
<tbody>
<tr class="odd section">
<td colspan="3">Add plots</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="&quot;addplot(addplot_option:plot)&quot;">"addplot(plot)</code></td>
<td>add other plots to the generated graph</td>
</tr>
</tbody>
<tbody>
<tr class="odd section">
<td colspan="3">Y axis, X axis, Titles, Legend, Overall, By</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><var class="command">twoway_options</var></td>
<td>any options documented in [<strong>[G-3]</strong> <em>twoway_options</em>](http://www.stata.com/help.cgi?twoway_options)</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="byop">byopts(byopts)</code></td>
<td>how subgraphs are combined, labeled, etc.</td>
</tr>
</tbody>
</table>

`dimlist` may contain any of the following columns:

| column |                  | Description                                                                                                        |
|--------|------------------|--------------------------------------------------------------------------------------------------------------------|
|        | `alpha`          | significance level                                                                                                 |
|        | `power`          | power                                                                                                              |
|        | `beta`           | type II error probability                                                                                          |
|        | `N`              | total number of subjects                                                                                           |
|        | `N1`             | number of subjects in the control group                                                                            |
|        | `N2`             | number of subjects in the experimental group                                                                       |
|        | `nratio`         | ratio of sample sizes, experimental to control                                                                     |
|        | `K`              | number of clusters                                                                                                 |
|        | `K1`             | number of clusters in the control group                                                                            |
|        | `K2`             | number of clusters in the experimental group                                                                       |
|        | `kratio`         | ratio of numbers of clusters, experimental to control                                                              |
|        | `M`              | cluster size                                                                                                       |
|        | `M1`             | cluster size in the control group                                                                                  |
|        | `M2`             | cluster size in the experimental group                                                                             |
|        | `mratio`         | ratio of cluster sizes, experimental to control                                                                    |
|        | `delta`          | effect size                                                                                                        |
|        | `target`         | target parameter                                                                                                   |
|        | `method_columns` | columns specific to the [<strong>method</strong>](power##method) specified with `power` |

`colspec` is

`column "label"` \[`column "label"` \[...\]\]

| dimopts |                                                                                                                                                  | Description                                                               |
|---------|--------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------|
|         | `labels(lablist)`                                                                                                                                | list of quoted strings to label each level of the dimension               |
|         | `elabels(elablist)`                                                                                                                              | list of enumerated labels                                                 |
|         | `nolabels`                                                                                                                                       | label groups with their values, not their labels                          |
|         | `allsimplelabels`                                                                                                                                | forgo column name and equal signs in all labels                           |
|         | `nosimplelabels`                                                                                                                                 | include column name and equal signs in all labels                         |
|         | `eqseparator(string)`                                                                                                                            | replace equal sign separator with `string` in the dimension               |
|         | `separator(string)`                                                                                                                              | separator for labels when multiple columns are specified in the dimension |
|         | `noseparator`                                                                                                                                    | do not use a separator                                                    |
|         | `format(`[<strong>%</strong><var class="command">fmt</var><strong></strong>](http://www.stata.com/help.cgi?format)`)` | format for converting numeric values to labels                            |

where `lablist` is defined as

`"label"` \[`"label"` \[...\]\]

`elablist` is defined as

`# "label"` \[`# "label"` \[...\]\]

and the `#`s are the levels of the dimension.

plot\_options

Description

change look of markers (color, size, etc.) add marker labels; change
look or position change look of the line
