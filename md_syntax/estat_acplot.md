## Syntax

`estat acplot` \[`, options`\]

<table class="syntab">
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">options</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td class="normal"></td>
<td>[<strong></strong>](#saving())
<ul>
</ul>
ving(<var class="command">filename</var><strong>[, ...])</strong></td>
<td>save results to <var class="command">filename</var>; save variables in double precision; save variables with prefix <var class="command">stubname</var></td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="l">level(#)</code></td>
<td>set confidence level; default is <code class="command">level(95)</code></td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="lag">lags(#)</code></td>
<td>use <var class="command">#</var> autocorrelations</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="cov">covariance</code></td>
<td>calculate autocovariances; the default is to calculate autocorrelations</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="smem">smemory</code></td>
<td>report short-memory ACF; only allowed after <code class="command">arfima</code></td>
</tr>
</tbody>
<tbody>
<tr class="odd section">
<td colspan="3">CI plot</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="ciop">ciopts(rcap_options)</code></td>
<td>affect rendition of the confidence bands</td>
</tr>
</tbody>
<tbody>
<tr class="odd section">
<td colspan="3">Plot</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><var class="command">marker_options</var></td>
<td>change look of markers (color, size, etc.)</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><var class="command">marker_label_options</var></td>
<td>add marker labels; change look or position</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><var class="command">cline_options</var></td>
<td>affect rendition of the plotted points</td>
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
