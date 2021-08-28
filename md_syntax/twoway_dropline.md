## Syntax

`twoway dropline yvar xvar` _\[`if`\]
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
<td>vertical dropped-line plot; the default</td>
</tr>
<tr class="odd">
<td><code class="command">horizontal</code></td>
<td>horizontal dropped-line plot</td>
</tr>
<tr class="even">
<td><code class="command">base(</code><var class="command">#</var><code class="command">)</code></td>
<td>value to drop to; default is 0</td>
</tr>
<tr class="odd">
<td><var class="command">marker_options</var></td>
<td>change look of markers (color, size, etc.)</td>
</tr>
<tr class="even">
<td><var class="command">marker_label_options</var></td>
<td>add marker labels; change look or position</td>
</tr>
<tr class="odd">
<td><var class="command">line_options</var></td>
<td>change look of dropped lines</td>
</tr>
<tr class="even">
<td><var class="command">axis_choice_options</var></td>
<td>associate plot with alternative axis</td>
</tr>
<tr class="odd">
<td><var class="command">twoway_options</var></td>
<td>titles, legends, axes, added lines and text, by, regions, name, aspect ratio, etc. <span>{p2line None}_
All explicit options are <var class="command">rightmost</var>, except <code class="command">vertical</code> and <code class="command">horizontal</code>, which are <var class="command">unique</var>; see [<strong>repeated options</strong>](http://www.stata.com/help.cgi?repeated%20options).</td>
</tr>
</tbody>
</table>
