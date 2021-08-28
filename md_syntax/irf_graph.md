## Syntax

`irf graph stat` \[`, options`\]

<table id="stat" class="standard">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><var class="command">stat</var></td>
<td>Description <span>{p2line None}_ <span>{syntab None:Main}_</td>
</tr>
<tr class="even">
<td><code class="command">irf</code></td>
<td>impulse-response function</td>
</tr>
<tr class="odd">
<td><code class="command">oirf</code></td>
<td>orthogonalized impulse-response function</td>
</tr>
<tr class="even">
<td><code class="command">dm</code></td>
<td>dynamic-multiplier function</td>
</tr>
<tr class="odd">
<td><code class="command">cirf</code></td>
<td>cumulative impulse-response function</td>
</tr>
<tr class="even">
<td><code class="command">coirf</code></td>
<td>cumulative orthogonalized impulse-response function</td>
</tr>
<tr class="odd">
<td><code class="command">cdm</code></td>
<td>cumulative dynamic-multiplier function</td>
</tr>
<tr class="even">
<td><code class="command">fevd</code></td>
<td>Cholesky forecast-error variance decomposition</td>
</tr>
<tr class="odd">
<td><code class="command">sirf</code></td>
<td>structural impulse-response function</td>
</tr>
<tr class="even">
<td><code class="command">sfevd</code></td>
<td>structural forecast-error variance decomposition <span>{p2line None}_
Notes: (1) No statistic may appear more than once.
(2) If confidence intervals are included (the default), only two statistics may be included.
(3) If confidence intervals are suppressed (option <code class="command">noci</code>), up to four statistics may be included.</td>
</tr>
</tbody>
</table>

<table id="options_table" class="syntab">
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
<td><code class="command" data-options="set(filename)">set(filename)</code></td>
<td>make <var class="command">filename</var> active</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command">irf(</code><var class="command">irfnames</var><code class="command">)</code></td>
<td>use <var class="command">irfnames</var> IRF result sets</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="i">impulse(impulsevar)</code></td>
<td>use <var class="command">impulsevar</var> as impulse variables</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command">response:(</code><var class="command">endogvars</var><code class="command">)</code></td>
<td>use endogenous variables as response variables</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="noci">noci</code></td>
<td>suppress confidence bands</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="l">level(#)</code></td>
<td>set confidence level; default is <code class="command">level(95)</code></td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="lst">lstep(#)</code></td>
<td>use <var class="command">#</var> for first step</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="ust">ustep(#)</code></td>
<td>use <var class="command">#</var> for maximum step</td>
</tr>
</tbody>
<tbody>
<tr class="odd section">
<td colspan="3">Advanced</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="in">individual</code></td>
<td>graph each combination individually</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command">iname(</code><var class="command">namestub</var> [<code class="command">,</code> <code class="command" data-options="replace">replace</code>]<code class="command">)</code></td>
<td>stub for naming the individual graphs</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command">isaving(</code><var class="command">filenamestub</var> [<code class="command">,</code> <code class="command" data-options="replace">replace</code>]<code class="command">)</code></td>
<td>stub for saving the individual graphs to files</td>
</tr>
</tbody>
<tbody>
<tr class="odd section">
<td colspan="3">Plots</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command">plot</code>
<ul>
</ul>
<code class="command">opts(</code><var class="command">cline_options</var><code class="command">)</code></td>
<td>affect rendition of the line plotting the <var class="command">#</var> <var class="command">stat</var></td>
</tr>
</tbody>
<tbody>
<tr class="odd section">
<td colspan="3">CI plots</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command">ci</code>
<ul>
</ul>
<code class="command">opts(</code><var class="command">area_options</var><code class="command">)</code></td>
<td>affect rendition of the confidence interval for the <var class="command">#</var> <var class="command">stat</var></td>
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
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="byop">byopts(by_option)</code></td>
<td>how subgraphs are combined, labeled, etc.</td>
</tr>
</tbody>
</table>
