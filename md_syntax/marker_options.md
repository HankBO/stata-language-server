## Syntax

<table class="standard">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><var class="command">marker_options</var></td>
<td>Description <span>{p2line None}_</td>
</tr>
<tr class="even">
<td><code class="command">msymbol:(</code><var class="command">symbolstyle</var><code class="command">)</code></td>
<td>shape of marker</td>
</tr>
<tr class="odd">
<td><code class="command">mcolor:(</code><var class="command">colorstyle</var><code class="command">)</code></td>
<td>color and opacity of marker, inside and out</td>
</tr>
<tr class="even">
<td><code class="command">msize:(</code><var class="command">markersizestyle</var><code class="command">)</code></td>
<td>size of marker</td>
</tr>
<tr class="odd">
<td><code class="command">msangle:(</code><var class="command">anglestyle</var><code class="command">)</code></td>
<td>angle of marker symbol</td>
</tr>
<tr class="even">
<td><code class="command">mfcolor:(</code><var class="command">colorstyle</var><code class="command">)</code></td>
<td>inside or "fill" color and opacity</td>
</tr>
<tr class="odd">
<td><code class="command">mlcolor:(</code><var class="command">colorstyle</var><code class="command">)</code></td>
<td>outline color and opacity</td>
</tr>
<tr class="even">
<td><code class="command">mlwidth:(</code><var class="command">linewidthstyle</var><code class="command">)</code></td>
<td>outline thickness</td>
</tr>
<tr class="odd">
<td><code class="command">mlalign:(</code><var class="command">linealignmentstyle</var><code class="command">)</code></td>
<td>outline alignment (inside, outside, center)</td>
</tr>
<tr class="even">
<td><code class="command">mlstyle:(</code><var class="command">linestyle</var><code class="command">)</code></td>
<td>thickness and color, overall style of outline</td>
</tr>
<tr class="odd">
<td><code class="command">mstyle:(</code><var class="command">markerstyle</var><code class="command">)</code></td>
<td>overall style of marker; all settings above</td>
</tr>
<tr class="even">
<td><code class="command">pstyle:(</code><var class="command">pstyle</var><code class="command">)</code></td>
<td>overall plot style, including markerstyle</td>
</tr>
<tr class="odd">
<td>[<strong>recast(</strong><var class="command">newplottype</var><strong>)</strong>](http://www.stata.com/help.cgi?advanced_options)</td>
<td>advanced; treat plot as <var class="command">newplottype</var> <span>{p2line None}_
All options are <var class="command">rightmost</var>; see [<strong>repeated options</strong>](http://www.stata.com/help.cgi?repeated%20options).</td>
</tr>
</tbody>
</table>

One example of each of the above is{cmd None}

{txt None}

Sometimes you may specify a list of elements, with the first element
applying to the first variable, the second to the second, and so on.
See, for instance,
[<strong>[G-2]</strong> graph twoway scatter](http://www.stata.com/help.cgi?scatter).
One example would be

`msymbol(O o p)mcolor(green blue black)msize(medium medium small)msangle(0 15 30)mfcolor(red red none)mlcolor(olive olive green)mlwidth(thick thin thick)mlalign(inside outside center)mstyle(p1 p2 p3)mlstyle(p1 p2 p3)`

For information about specifying lists, see
[<strong>[G-4]</strong> <em>stylelists</em>](http://www.stata.com/help.cgi?stylelists).
