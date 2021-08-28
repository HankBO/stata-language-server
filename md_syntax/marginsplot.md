## Syntax

`marginsplot` \[`, options`\]

<table class="syntab">
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">Options</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd section">
<td colspan="3">Main</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command">xdimension(</code>[<var class="command">dimlist</var><strong></strong>](#dimlist) [<code class="command">,</code> [<var class="command">dimopts</var><strong></strong>](#dimopts)]<code class="command">)</code></td>
<td>use <var class="command">dimlist</var> to define x axis</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command">plotdimension(</code>[<var class="command">dimlist</var><strong></strong>](#dimlist) [<code class="command">,</code> [<var class="command">dimopts</var><strong></strong>](#dimopts)]<code class="command">)</code></td>
<td>create plots for groups in <var class="command">dimlist</var></td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command">bydimension(</code>[<var class="command">dimlist</var><strong></strong>](#dimlist) [<code class="command">,</code> [<var class="command">dimopts</var><strong></strong>](#dimopts)]<code class="command">)</code></td>
<td>create subgraphs for groups in <var class="command">dimlist</var></td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command">graphdimension(</code>[<var class="command">dimlist</var><strong></strong>](#dimlist) [<code class="command">,</code> [<var class="command">dimopts</var><strong></strong>](#dimopts)]<code class="command">)</code></td>
<td>create graphs for groups in <var class="command">dimlist</var></td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="horiz">horizontal</code></td>
<td>swap x and y axes</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="noci">noci</code></td>
<td>do not plot confidence intervals</td>
</tr>
<tr class="even">
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
<td><code class="command" data-options="allx">allxlabels</code></td>
<td>place ticks and labels on the x axis for each value</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="nolab">nolabels</code></td>
<td>label groups with their values, not their labels</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="allsim">allsimplelabels</code></td>
<td>forgo variable name and equal signs in all labels</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="nosim">nosimplelabels</code></td>
<td>include variable name and equal signs in all labels</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="sep">separator(string)</code></td>
<td>separator for labels when multiple variables are specified in a dimension</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="nosep">noseparator</code></td>
<td>do not use a separator</td>
</tr>
</tbody>
<tbody>
<tr class="odd section">
<td colspan="3">Plot</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command">plotopts(</code><var class="command">plot_options</var><code class="command">)</code></td>
<td>affect rendition of all margin plots</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command">plot</code>
<ul>
</ul>
<code class="command">opts(</code><var class="command">plot_options</var><code class="command">)</code></td>
<td>affect rendition of <var class="command">#</var>th margin plot</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="recast">recast(plottype)</code></td>
<td>plot margins using <var class="command">plottype</var></td>
</tr>
</tbody>
<tbody>
<tr class="odd section">
<td colspan="3">CI plot</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="ciop">ciopts(rcap_options)</code></td>
<td>affect rendition of all confidence interval plots</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command">ci</code>
<ul>
</ul>
<code class="command">opts(</code><var class="command">rcap_options</var><code class="command">)</code></td>
<td>affect rendition of <var class="command">#</var>th confidence interval plot</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="recastci">recastci(plottype)</code></td>
<td>plot confidence intervals using <var class="command">plottype</var></td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="mcomp">mcompare(method)</code></td>
<td>adjust for multiple comparisons</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="l">level(#)</code></td>
<td>set confidence level</td>
</tr>
</tbody>
<tbody>
<tr class="odd section">
<td colspan="3">Pairwise</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="uniq">unique</code></td>
<td>plot only unique pairwise comparisons</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="csort">csort</code></td>
<td>sort comparison categories first</td>
</tr>
</tbody>
<tbody>
<tr class="odd section">
<td colspan="3">Add plots</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="&quot;addplot(addplot_option:plot)&quot;">"addplot(plot)</code></td>
<td>add other plots to the graph</td>
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
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="elab">elabels(elablist)</code></td>
<td>list of enumerated labels</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="nolab">nolabels</code></td>
<td>label groups with their values, not their labels</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="allsim">allsimplelabels</code></td>
<td>forgo variable name and equal signs in all labels</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="nosim">nosimplelabels</code></td>
<td>include variable name and equal signs in all labels</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="sep">separator(string)</code></td>
<td>separator for labels when multiple variables are specified in the dimension</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="nosep">noseparator</code></td>
<td>do not use a separator</td>
</tr>
</tbody><tfoot>
<tr class="even footnote">
<td colspan="3">where <var class="command">dimlist</var> may be any of the dimensions across which margins were computed in the immediately preceding [<strong>margins</strong>](http://www.stata.com/help.cgi?margins) command. That is to say, <var class="command">dimlist</var> may be any variable used in the <code class="command">margins</code> command, including variables specified in the <code class="command">at()</code>, <code class="command">over()</code>, and <code class="command">within()</code> options. More advanced specifications of <var class="command">dimlist</var> are covered in <var class="command">Addendum: Advanced uses of dimlist</var> below. <span data-options="dimopts">{marker dimopts}_<span>{nobreak None}_ <span data-options="26">{synoptset 26}_<span>{nobreak None}_ <span>{synopthdr None:dimopts}_ <span>{synoptline None}_ <span>{synopt None}<code class="command" data-options="lab">labels(lablist)</code>_list of quoted strings to label each level of the dimension</td>
</tr>
</tfoot>

</table>

where `lablist` is defined as

`"label"` \[`"label"` \[...\]\]

`elablist` is defined as

`# "label"` \[`# "label"` \[...\]\]

and the `#`s are the indices of the levels of the dimension -- 1 is the
first level, 2 is the second level, and so on.

plot\_options

Description

change look of markers (color, size, etc.) add marker labels; change
look or position change look of the line

| method |                              | Description                                  |
|--------|------------------------------|----------------------------------------------|
|        | `noadjust`                   | do not adjust for multiple comparisons       |
|        | `bonferroni` \[`adjustall`\] | Bonferroni's method; adjust across all terms |
|        | `sidak` \[`adjustall`\]      | Sidak's method; adjust across all terms      |
|        | `scheffe`                    | Scheffe's method                             |
