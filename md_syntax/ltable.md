## Syntax

`ltable timevar` \[`deadvar`\] _\[`if`\]
\[`in`\]_ \[`weight`\] \[`, options`\]

`timevar` specifies the time of failure or censoring. If `deadvar` is
not specified, all values of `timevar` are interpreted as failure times.
Observations with `timevar` equal to missing are ignored.

`deadvar` specifies how the time recorded in `timevar` is to be
interpreted. Observations with `deadvar` equal to 0 are treated as
censored and all other nonmissing values indicate that `timevar` should
be interpreted as a failure time. Observations with `deadvar` equal to
missing are ignored.

`deadvar` does not specify the number of failures. Specify frequency
weights for aggregated data recording the number of failures.

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
<td><code class="command" data-options="nota">notable</code></td>
<td>display graph only; suppress display of table</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="g">graph</code></td>
<td>present the table graphically, as well as in tabular form</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="by">by(groupvar)</code></td>
<td>produce separate tables (or graphs) for each value of <var class="command">groupvar</var></td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="t">test</code></td>
<td>report chi-squared measure of differences between groups (2 tests)</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="overlay">overlay</code></td>
<td>overlay plots on the same graph</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="su">survival</code></td>
<td>display survival table; the default</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="f">failure</code></td>
<td>display cumulative failure table</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="h">hazard</code></td>
<td>display hazard table</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="ci">ci</code></td>
<td>graph confidence interval</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="l">level(#)</code></td>
<td>set confidence level; default is <code class="command">level(95)</code></td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="noa">noadjust</code></td>
<td>suppress actuarial adjustment to the number at risk</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="tv">tvid(varname)</code></td>
<td>subject ID variable to use with time-varying parameters</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command">intervals:(</code><code class="command">w</code>|<var class="command">numlist</var><code class="command">)</code></td>
<td>time intervals in which data are to be aggregated for tables</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command">saving:(</code><var class="command">filename</var>[<code class="command">,</code> <code class="command">replace</code>]<code class="command">)</code></td>
<td>save the life-table data to <var class="command">filename</var>; use <code class="command" data-options="replace">replace</code> to overwrite existing <var class="command">filename</var></td>
</tr>
</tbody>
<tbody>
<tr class="odd section">
<td colspan="3">Plot</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="ploto">plotopts(plot_options)</code></td>
<td>affect rendition of the plotted line and plotted points</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command">plot</code>
<ul>
</ul>
<code class="command">opts(</code><var class="command">plot_options</var><code class="command">)</code></td>
<td>affect rendition of the <var class="command">#</var>th plotted line and plotted points; available only with <code class="command" data-options="overlay">overlay</code></td>
</tr>
</tbody>
<tbody>
<tr class="odd section">
<td colspan="3">CI plot</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="ciop">ciopts(rspike_options)</code></td>
<td>affect rendition of the confidence intervals</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command">ci</code>
<ul>
</ul>
<code class="command">opts(</code><var class="command">rspike_options</var><code class="command">)</code></td>
<td>affect rendition of the <var class="command">#</var>th confidence interval; available only with <code class="command" data-options="overlay">overlay</code></td>
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
<td colspan="3">Y axis, X axis, Titles, Legend, Overall</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><var class="command">twoway_options</var></td>
<td>any options other than <code class="command">by()</code> documented in [<strong>[G-3]</strong> <em>twoway_options</em>](http://www.stata.com/help.cgi?twoway_options)</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="byop">byopts(byopts)</code></td>
<td>how subgraphs are combined, labeled, etc.</td>
</tr>
</tbody>
</table>

| plot\_options |                   | Description                                |
|---------------|-------------------|--------------------------------------------|
|               | `connect_options` | change look of lines or connecting method  |
|               | `marker_options`  | change look of markers (color, size, etc.) |

`fweight`s are allowed; see
[<strong>weight</strong>](http://www.stata.com/help.cgi?weight).
