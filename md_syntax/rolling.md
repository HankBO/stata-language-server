## Syntax

`rolling` \[`exp_list`\] _\[`if`\] \[`in`\]_
`, window(#)` \[`options`\] `: command`

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
<tr class="even" style="has_footnote">
<td>*</td>
<td><code class="command" data-options="w">window(#)</code></td>
<td>number of consecutive data points in each sample</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="r">recursive</code></td>
<td>use recursive samples</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="rr">rrecursive</code></td>
<td>use reverse recursive samples</td>
</tr>
</tbody>
<tbody>
<tr class="odd section">
<td colspan="3">Options</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="clear">clear</code></td>
<td>replace data in memory with results</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td>[<strong></strong>](http://www.stata.com/help.cgi?prefix_saving_option)
<ul>
</ul>
ving(<var class="command">filename</var><strong>, ...)</strong></td>
<td>save results to <var class="command">filename</var>; save statistics in double precision; save results to <var class="command">filename</var> every <var class="command">#</var> replications</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="step">stepsize(#)</code></td>
<td>number of periods to advance window</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="st">start(time_constant)</code></td>
<td>period at which rolling is to start</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="e">end(time_constant)</code></td>
<td>period at which rolling is to end</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command">keep(</code>[varname](http://www.stata.com/help.cgi?varname)[<code class="command">,</code> <code class="command" data-options="start">start</code>]<code class="command">)</code></td>
<td>save <var class="command">varname</var> with results; optionally, use value at left edge of window</td>
</tr>
</tbody>
<tbody>
<tr class="odd section">
<td colspan="3">Reporting</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="nodots">nodots</code></td>
<td>suppress replication dots</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="dots(#)">dots(#)</code></td>
<td>display dots every <var class="command">#</var> replications</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="noi">noisily</code></td>
<td>display any output from <var class="command">command</var></td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="tr">trace</code></td>
<td>trace <var class="command">command</var>'s execution</td>
</tr>
</tbody>
<tbody>
<tr class="odd section">
<td colspan="3">Advanced</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="reject">reject(exp)</code></td>
<td>identify invalid results</td>
</tr>
</tbody><tfoot>
<tr class="odd footnote">
<td colspan="3">* <code class="command" data-options="window(#)">window(#)</code> is required.</td>
</tr>
<tr class="even footnote">
<td colspan="3">You must <code class="command">tsset</code> your data before using <code class="command" data-options="rolling">rolling</code>; see [<strong>[TS] tsset</strong>](http://www.stata.com/help.cgi?tsset).</td>
</tr>
<tr class="odd footnote">
<td colspan="3"><var class="command">command</var> is any command that follows standard Stata syntax and allows the <code class="command">if</code> qualifier. The <code class="command">by</code> prefix cannot be part of <var class="command">command</var>.</td>
</tr>
<tr class="even footnote">
<td colspan="3"><code class="command" data-options="aweight">aweight</code>s are allowed in <var class="command">command</var> if <var class="command">command</var> accepts <code class="command">aweight</code>s; see [<strong>weight</strong>](http://www.stata.com/help.cgi?weight).</td>
</tr>
</tfoot>

</table>
