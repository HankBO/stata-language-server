## Syntax

`biplot`
[varlist](http://www.stata.com/help.cgi?varlist)
_\[`if`\] \[`in`\]_ \[`, options`\]

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
<td><code class="command" data-options="rowover(varlist)">rowover(varlist)</code></td>
<td>identify observations from different groups of <var class="command">varlist</var>; may not be combined with <code class="command">separate</code> or <code class="command">norow</code></td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="dim(# #)">dim(# #)</code></td>
<td>two dimensions to be displayed; default is <code class="command">dim(2 1)</code></td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="std">std</code></td>
<td>use standardized instead of centered variables</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="alp">alpha(#)</code></td>
<td>row weight=<var class="command">#</var>; column weight=1-<var class="command">#</var>; default is 0.5</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="st">stretch(#)</code></td>
<td>stretch the column (variable) arrows</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="mah">mahalanobis</code></td>
<td>approximate Mahalanobis distance; implies <code class="command">alpha(0)</code></td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="xneg">xnegate</code></td>
<td>negate the data relative to the <var class="command">x</var> axis</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="yneg">ynegate</code></td>
<td>negate the data relative to the <var class="command">y</var> axis</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="auto">autoaspect</code></td>
<td>adjust aspect ratio on the basis of the data; default aspect ratio is 1</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="sep">separate</code></td>
<td>produce separate plots for rows and columns; may not be combined with <code class="command" data-options="rowover()">rowover()</code></td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="nog">nograph</code></td>
<td>suppress graph</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="tab">table</code></td>
<td>display table showing biplot coordinates</td>
</tr>
</tbody>
<tbody>
<tr class="odd section">
<td colspan="3">Rows</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="row">rowopts(row_options)</code></td>
<td>affect rendition of rows (observations)</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command">row</code>
<ul>
</ul>
<code class="command" data-options="opts">opts(row_options)</code></td>
<td>affect rendition of rows (observations) in the <var class="command">#</var>th group of [varlist](http://www.stata.com/help.cgi?varlist) defined in <code class="command">rowover()</code>; available only with <code class="command">rowover()</code></td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="rowlabel(varname)">rowlabel(varname)</code></td>
<td>specify label variable for rows (observations)</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="norow">norow</code></td>
<td>suppress row points; may not be combined with <code class="command">rowover()</code></td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command">generate(</code><var class="command">newvar_x</var> <var class="command">newvar_y</var><code class="command">)</code></td>
<td>store biplot coordinates for observations in variables <var class="command">newvar_x</var> and <var class="command">newvar_y</var></td>
</tr>
</tbody>
<tbody>
<tr class="odd section">
<td colspan="3">Columns</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="col">colopts(col_options)</code></td>
<td>affect rendition of columns (variables)</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="negc">negcol</code></td>
<td>include negative column (variable) arrows</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="negcol">negcolopts(col_options)</code></td>
<td>affect rendition of negative columns (variables)</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="nocol">nocolumn</code></td>
<td>suppress column arrows</td>
</tr>
</tbody>
<tbody>
<tr class="odd section">
<td colspan="3">Y axis, X axis, Titles, Legend, Overall</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><var class="command">twoway_options</var></td>
<td>any options other than <code class="command" data-options="by()">by()</code> documented in [<strong>[G-3]</strong> <em>twoway_options</em>](http://www.stata.com/help.cgi?twoway_options)</td>
</tr>
</tbody>
</table>

| row\_options |                        | Description                                            |
|--------------|------------------------|--------------------------------------------------------|
|              | `marker_options`       | change look of markers (color, size, etc.)             |
|              | `marker_label_options` | change look or position of marker labels               |
|              | `nolabel`              | remove the default row (variable) label from the graph |
|              | `name(name)`           | override the default name given to rows (observations) |

| col\_options |                   | Description                                               |
|--------------|-------------------|-----------------------------------------------------------|
|              | `pcarrow_options` | affect the rendition of paired-coordinate arrows          |
|              | `nolabel`         | remove the default column (variable) label from the graph |
|              | `name(name)`      | override the default name given to columns (variables)    |
