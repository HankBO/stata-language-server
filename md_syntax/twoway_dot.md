## Syntax

`twoway dot yvar xvar` _\[`if`\]
\[`in`\]_ \[`, options`\]

<table class="standard">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><var class="command">options</var></td>
<td>Description <span>{p2line None}_</td>
</tr>
<tr class="even">
<td><code class="command">vertical</code></td>
<td>vertical bar plot; the default</td>
</tr>
<tr class="odd">
<td><code class="command">horizontal</code></td>
<td>horizontal bar plot</td>
</tr>
<tr class="even">
<td><code class="command">dotextend:(yes</code>|<code class="command">no)</code></td>
<td>dots extend beyond point</td>
</tr>
<tr class="odd">
<td><code class="command">base(</code><var class="command">#</var><code class="command">)</code></td>
<td>value to drop to if <code class="command">dotextend(no)</code></td>
</tr>
<tr class="even">
<td><code class="command">ndots:(</code><var class="command">#</var><code class="command">)</code></td>
<td><var class="command">#</var> of dots in full span of <var class="command">y</var> or <var class="command">x</var></td>
</tr>
<tr class="odd">
<td><code class="command">dstyle:(</code><var class="command">markerstyle</var><code class="command">)</code></td>
<td>overall marker style of dots</td>
</tr>
<tr class="even">
<td><code class="command">dsymbol:(</code><var class="command">symbolstyle</var><code class="command">)</code></td>
<td>marker symbol for dots</td>
</tr>
<tr class="odd">
<td><code class="command">dcolor:(</code><var class="command">colorstyle</var><code class="command">)</code></td>
<td>fill and outline color and opacity for dots</td>
</tr>
<tr class="even">
<td><code class="command">dfcolor:(</code><var class="command">colorstyle</var><code class="command">)</code></td>
<td>fill color and opacity for dots</td>
</tr>
<tr class="odd">
<td><code class="command">dsize:(</code><var class="command">markersizestyle</var><code class="command">)</code></td>
<td>size of dots</td>
</tr>
<tr class="even">
<td><code class="command">dlstyle:(</code><var class="command">linestyle</var><code class="command">)</code></td>
<td>overall outline style of dots</td>
</tr>
<tr class="odd">
<td><code class="command">dlcolor:(</code><var class="command">colorstyle</var><code class="command">)</code></td>
<td>outline color and opacity for dots</td>
</tr>
<tr class="even">
<td><code class="command">dlwidth:(</code><var class="command">linewidthstyle</var><code class="command">)</code></td>
<td>thickness of outline for dots</td>
</tr>
<tr class="odd">
<td><code class="command">dlalign:(</code><var class="command">linealignmentstyle</var><code class="command">)</code></td>
<td>alignment of outline for dots</td>
</tr>
<tr class="even">
<td><var class="command">scatter_options</var></td>
<td>any options other than <var class="command">connect_options</var> documented in [<strong>[G-2]</strong> graph twoway scatter](http://www.stata.com/help.cgi?scatter) <span>{p2line None}_
All options are <var class="command">rightmost</var>, except <code class="command">vertical</code> and <code class="command">horizontal</code>, which are <var class="command">unique</var>; see [<strong>repeated options</strong>](http://www.stata.com/help.cgi?repeated%20options).</td>
</tr>
</tbody>
</table>
