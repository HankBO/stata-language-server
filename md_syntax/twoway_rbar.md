## Syntax

`twoway rbar y1var y2var xvar` _\[`if`\]
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
<td>vertical bars; the default</td>
</tr>
<tr class="odd">
<td><code class="command">horizontal</code></td>
<td>horizontal bars</td>
</tr>
<tr class="even">
<td><code class="command">barwidth:(</code><var class="command">#</var><code class="command">)</code></td>
<td>width of bar in <var class="command">xvar</var> units</td>
</tr>
<tr class="odd">
<td><code class="command">mwidth</code></td>
<td>use <code class="command">msize()</code> rather than <code class="command">barwidth()</code></td>
</tr>
<tr class="even">
<td><code class="command">msize:(</code><var class="command">markersizestyle</var><code class="command">)</code></td>
<td>width of bar in [<strong>relative size</strong>](http://www.stata.com/help.cgi?relativesize) units</td>
</tr>
<tr class="odd">
<td><var class="command">barlook_options</var></td>
<td>change look of bars</td>
</tr>
<tr class="even">
<td><var class="command">axis_choice_options</var></td>
<td>associate plot with alternative axis</td>
</tr>
<tr class="odd">
<td><var class="command">twoway_options</var></td>
<td>titles, legends, axes, added lines and text, by, regions, name, aspect ratio, etc. <span>{p2line None}_
Options <code class="command">barwidth()</code>, <code class="command">mwidth</code>, and <code class="command">msize()</code> are <var class="command">rightmost</var>, and <code class="command">vertical</code> and <code class="command">horizontal</code> are <var class="command">unique</var>; see [<strong>repeated options</strong>](http://www.stata.com/help.cgi?repeated%20options).</td>
</tr>
</tbody>
</table>
