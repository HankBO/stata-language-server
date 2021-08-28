## Syntax

`jackknife exp_list` \[`, options eform_option`\] `:`
[<var class="command">command</var><strong></strong>](#command)

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
<td><code class="command" data-options="e">eclass</code></td>
<td>number of observations used is stored in <code class="command">e(N)</code></td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="r">rclass</code></td>
<td>number of observations used is stored in <code class="command">r(N)</code></td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="n(exp)">n(exp)</code></td>
<td>specify <var class="command">exp</var> that evaluates to the number of observations used</td>
</tr>
</tbody>
<tbody>
<tr class="odd section">
<td colspan="3">Options</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="cl">cluster(varlist)</code></td>
<td>variables identifying sample clusters</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="id">idcluster(newvar)</code></td>
<td>create new cluster ID variable</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td>[<strong></strong>](http://www.stata.com/help.cgi?prefix_saving_option)
<ul>
</ul>
ving(<var class="command">filename</var><strong>, ...)</strong></td>
<td>save results to <var class="command">filename</var>; save statistics in double precision; save results to <var class="command">filename</var> every <var class="command">#</var> replications</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="keep">keep</code></td>
<td>keep pseudovalues</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="mse">mse</code></td>
<td>use MSE formula for variance estimation</td>
</tr>
</tbody>
<tbody>
<tr class="odd section">
<td colspan="3">Reporting</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="l">level(#)</code></td>
<td>set confidence level; default is <code class="command">level(95)</code></td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="notable">notable</code></td>
<td>suppress table of results</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="noh">noheader</code></td>
<td>suppress table header</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="nol">nolegend</code></td>
<td>suppress table legend</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="v">verbose</code></td>
<td>display the full table legend</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="nodots">nodots</code></td>
<td>suppress replication dots</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="dots(#)">dots(#)</code></td>
<td>display dots every <var class="command">#</var> replications</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="noi">noisily</code></td>
<td>display any output from <var class="command">command</var></td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="tr">trace</code></td>
<td>trace <var class="command">command</var></td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="ti">title(text)</code></td>
<td>use <var class="command">text</var> as title for jackknife results</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><var class="command">display_options</var></td>
<td>control columns and column formats, row spacing, line width, display of omitted variables and base and empty cells, and factor-variable labeling</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><var class="command">eform_option</var></td>
<td>display coefficient table in exponentiated form</td>
</tr>
</tbody>
<tbody>
<tr class="odd section">
<td colspan="3">Advanced</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="nodrop">nodrop</code></td>
<td>do not drop observations</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="reject(exp)">reject(exp)</code></td>
<td>identify invalid results</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="coefl">coeflegend</code></td>
<td>display legend instead of statistics</td>
</tr>
</tbody><tfoot>
<tr class="even footnote">
<td colspan="3"><code class="command" data-options="svy">svy</code> is allowed; see [<strong>[SVY]</strong> svy jackknife](http://www.stata.com/help.cgi?svy_jackknife).</td>
</tr>
<tr class="odd footnote">
<td colspan="3"><var class="command">command</var> is any command that follows standard Stata syntax. All weight types supported by <var class="command">command</var> are allowed except <code class="command">aweight</code>s; see [<strong>weight</strong>](http://www.stata.com/help.cgi?weight).</td>
</tr>
<tr class="even footnote">
<td colspan="3"><code class="command" data-options="coeflegend">coeflegend</code> does not appear in the dialog box.</td>
</tr>
<tr class="odd footnote">
<td colspan="3">See [<strong>[R]</strong> jackknife postestimation](http://www.stata.com/help.cgi?jackknife_postestimation) for features available after estimation.</td>
</tr>
</tfoot>

</table>
