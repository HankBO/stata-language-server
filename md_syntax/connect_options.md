## Syntax

<table class="standard">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><var class="command">connect_options</var></td>
<td>Description <span>{p2line None}_</td>
</tr>
<tr class="even">
<td><code class="command">connect:(</code><var class="command">connectstyle</var><code class="command">)</code></td>
<td>how to connect points</td>
</tr>
<tr class="odd">
<td><code class="command">sort</code>[<code class="command">(</code>[varlist](http://www.stata.com/help.cgi?varlist)<code class="command">)</code>]</td>
<td>how to sort before connecting</td>
</tr>
<tr class="even">
<td><code class="command">cmissing:(</code><span data-options="-(">{c -(}_<code class="command">y</code>|<code class="command">n</code><span data-options=")-">{c )-}_ ...<code class="command">)</code></td>
<td>missing values are ignored</td>
</tr>
<tr class="odd">
<td><code class="command">lpattern:(</code><var class="command">linepatternstyle</var><code class="command">)</code></td>
<td>line pattern (solid, dashed, etc.)</td>
</tr>
<tr class="even">
<td><code class="command">lwidth:(</code><var class="command">linewidthstyle</var><code class="command">)</code></td>
<td>thickness of line</td>
</tr>
<tr class="odd">
<td><code class="command">lcolor:(</code><var class="command">colorstyle</var><code class="command">)</code></td>
<td>color and opacity of line</td>
</tr>
<tr class="even">
<td><code class="command">lalign:(</code><var class="command">linealignmentstyle</var><code class="command">)</code></td>
<td>line alignment (inside, outside, center)</td>
</tr>
<tr class="odd">
<td><code class="command">lstyle:(</code><var class="command">linestyle</var><code class="command">)</code></td>
<td>overall style of line</td>
</tr>
<tr class="even">
<td><code class="command">pstyle:(</code><var class="command">pstyle</var><code class="command">)</code></td>
<td>overall plot style, including linestyle</td>
</tr>
<tr class="odd">
<td>[<strong>recast(</strong><var class="command">newplottype</var><strong>)</strong>](http://www.stata.com/help.cgi?advanced_options)</td>
<td>advanced; treat plot as <var class="command">newplottype</var> <span>{p2line None}_
All options are <var class="command">rightmost</var>; see [<strong>repeated options</strong>](http://www.stata.com/help.cgi?repeated%20options). If both <code class="command">sort</code> and <code class="command">sort(</code><var class="command">varlist</var><code class="command">)</code> are specified, <code class="command">sort</code> is ignored and <code class="command">sort(</code><var class="command">varlist</var><code class="command">)</code> is honored.</td>
</tr>
</tbody>
</table>
