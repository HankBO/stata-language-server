## Syntax

Test equality of ROC areas

`roccomp refvar classvar` \[`classvars`\] <span
class="command">\[`if`\] \[`in`\]_ \[`weight`\] \[`,`
`roccomp_options`\]

Test equality of ROC area against a standard ROC curve

`rocgold refvar goldvar classvar` \[`classvars`\] <span
class="command">\[`if`\] \[`in`\]_ \[`weight`\] \[`,`
`rocgold_options`\]

<table id="roccomp_options" class="syntab">
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">roccomp_options</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd section">
<td colspan="3">Main</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="by(varname)">by(varname)</code></td>
<td>split into groups by variable</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="test(matname)">test(matname)</code></td>
<td>use contrast matrix for comparing ROC areas</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="g">graph</code></td>
<td>graph the ROC curve</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="noref">norefline</code></td>
<td>suppress plotting the 45-degree reference line</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="sep">separate</code></td>
<td>place each ROC curve on its own graph</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="sum">summary</code></td>
<td>report the area under the ROC curve</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="bin">binormal</code></td>
<td>estimate areas by using binormal distribution assumption</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command">line</code>
<ul>
</ul>
<code class="command">opts(</code><var class="command">cline_options</var><code class="command">)</code></td>
<td>affect rendition of the <var class="command">#</var>th binormal fit line</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="l">level(#)</code></td>
<td>set confidence level; default is <code class="command">level(95)</code></td>
</tr>
</tbody>
<tbody>
<tr class="odd section">
<td colspan="3">Plot</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command">plot</code>
<ul>
</ul>
<code class="command">opts(</code><var class="command">plot_options</var><code class="command">)</code></td>
<td>affect rendition of the <var class="command">#</var>th ROC curve</td>
</tr>
</tbody>
<tbody>
<tr class="odd section">
<td colspan="3">Reference line</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="rlop">rlopts(cline_options)</code></td>
<td>affect rendition of the reference line</td>
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

<table id="rocgold_options" class="syntab">
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">rocgold_options</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd section">
<td colspan="3">Main</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="sid">sidak</code></td>
<td>adjust the p-value by using Sidak's method</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="test(matname)">test(matname)</code></td>
<td>use contrast matrix for comparing ROC areas</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="g">graph</code></td>
<td>graph the ROC curve</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="noref">norefline</code></td>
<td>suppress plotting the 45-degree reference line</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="sep">separate</code></td>
<td>place each ROC curve on its own graph</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="sum">summary</code></td>
<td>report the area under the ROC curve</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="bin">binormal</code></td>
<td>estimate areas by using binormal distribution assumption</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command">line</code>
<ul>
</ul>
<code class="command">opts(</code><var class="command">cline_options</var><code class="command">)</code></td>
<td>affect rendition of the <var class="command">#</var>th binormal fit line</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="l">level(#)</code></td>
<td>set confidence level; default is <code class="command">level(95)</code></td>
</tr>
</tbody>
<tbody>
<tr class="odd section">
<td colspan="3">Plot</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command">plot</code>
<ul>
</ul>
<code class="command">opts(</code><var class="command">plot_options</var><code class="command">)</code></td>
<td>affect rendition of the <var class="command">#</var>th ROC curve; plot 1 is the "gold standard"</td>
</tr>
</tbody>
<tbody>
<tr class="odd section">
<td colspan="3">Reference line</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="rlop">rlopts(cline_options)</code></td>
<td>affect rendition of the reference line</td>
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

plot\_options

Description

change look of markers (color, size, etc.) add marker labels; change
look or position change look of the line

`fweight`s are allowed; see
[<strong>weight</strong>](http://www.stata.com/help.cgi?weight).
