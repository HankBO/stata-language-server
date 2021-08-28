## Syntax

`twoway rarea y1var y2var xvar` _\[`if`\]
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
<td>vertical area plot; the default</td>
</tr>
<tr class="odd">
<td><code class="command">horizontal</code></td>
<td>horizontal area plot</td>
</tr>
<tr class="even">
<td><code class="command">cmissing:(</code><code class="command">y</code>|<code class="command">n</code><code class="command">)</code></td>
<td>missing values do not force gaps in area; default is <code class="command">cmissing(y)</code></td>
</tr>
<tr class="odd">
<td><code class="command">sort</code></td>
<td>sort by <var class="command">xvar</var>; recommended</td>
</tr>
<tr class="even">
<td><var class="command">area_options</var></td>
<td>change look of shaded areas</td>
</tr>
<tr class="odd">
<td><var class="command">axis_choice_options</var></td>
<td>associate plot with alternative axis</td>
</tr>
<tr class="even">
<td><var class="command">twoway_options</var></td>
<td>titles, legends, axes, added lines and text, by, regions, name, aspect ratio, etc. <span>{p2line None}_
All explicit options are <var class="command">unique</var>; see [<strong>repeated options</strong>](http://www.stata.com/help.cgi?repeated%20options).</td>
</tr>
</tbody>
</table>
