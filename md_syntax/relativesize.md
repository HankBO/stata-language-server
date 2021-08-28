## Syntax

<table class="standard">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><var class="command">relativesize</var></td>
<td>Description <span>{p2line None}_</td>
</tr>
<tr class="even">
<td><var class="command">#</var></td>
<td>specify size; size 100 = minimum of width and height of graph; <var class="command">#</var> must be &gt;= 0, depending on context</td>
</tr>
<tr class="odd">
<td><code class="command">*</code><var class="command">#</var></td>
<td>specify size change via multiplication; <code class="command">*1</code> means no change, <code class="command">*2</code> twice as large, <code class="command">*.5</code> half; <var class="command">#</var> must be &gt;= 0, depending on context <span>{p2line None}_
Negative sizes are allowed in certain contexts, such as for gaps; in other cases, such as the size of symbol, the size must be nonnegative, and negative sizes, if specified, are ignored.</td>
</tr>
</tbody>
</table>

Examples:  

<table class="standard">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><var class="command">example</var></td>
<td>Description <span>{p2line None}_</td>
</tr>
<tr class="even">
<td><code class="command">msize(2)</code></td>
<td>make marker diameter 2% of <var class="command">g</var></td>
</tr>
<tr class="odd">
<td><code class="command">msize(1.5)</code></td>
<td>make marker diameter 1.5% of <var class="command">g</var></td>
</tr>
<tr class="even">
<td><code class="command">msize(.5)</code></td>
<td>make marker diameter .5% of <var class="command">g</var></td>
</tr>
<tr class="odd">
<td><code class="command">msize(*2)</code></td>
<td>make marker size twice as large as default</td>
</tr>
<tr class="even">
<td><code class="command">msize(*1.5)</code></td>
<td>make marker size 1.5 times as large as default</td>
</tr>
<tr class="odd">
<td><code class="command">msize(*.5)</code></td>
<td>make marker size half as large as default</td>
</tr>
<tr class="even">
<td><code class="command">xsca(titlegap(2))</code></td>
<td>make gap 2% of <var class="command">g</var></td>
</tr>
<tr class="odd">
<td><code class="command">xsca(titlegap(.5))</code></td>
<td>make gap .5% of <var class="command">g</var></td>
</tr>
<tr class="even">
<td><code class="command">xsca(titlegap(-2))</code></td>
<td>make gap -2% of <var class="command">g</var></td>
</tr>
<tr class="odd">
<td><code class="command">xsca(titlegap(-.5))</code></td>
<td>make gap -.5% of <var class="command">g</var></td>
</tr>
<tr class="even">
<td><code class="command">xsca(titlegap(*2))</code></td>
<td>make gap twice as large as default</td>
</tr>
<tr class="odd">
<td><code class="command">xsca(titlegap(*.5))</code></td>
<td>make gap half as large as default</td>
</tr>
<tr class="even">
<td><code class="command">xsca(titlegap(*-2))</code></td>
<td>make gap -2 times as large as default</td>
</tr>
<tr class="odd">
<td><code class="command">xsca(titlegap(*-.5))</code></td>
<td>make gap -.5 times as large as default <span>{p2line None}_
where <var class="command">g</var> = min(width of graph, height of graph)</td>
</tr>
</tbody>
</table>
