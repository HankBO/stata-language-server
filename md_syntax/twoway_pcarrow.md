## Syntax

Directional arrows

`twoway pcarrow` <span options="1">{space 1}_`y1var x1var`
`y2var x2var` _\[`if`\] \[`in`\]_ \[`,`
`options`\]

Bidirectional arrows

`twoway pcbarrow y1var x1var y2var x2var` <span
class="command">\[`if`\] \[`in`\]_ \[`, options`\]

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
<td><code class="command">mstyle:(</code><var class="command">markerstyle</var><code class="command">)</code></td>
<td>overall style of arrowhead</td>
</tr>
<tr class="odd">
<td><code class="command">msize:(</code><var class="command">markersizestyle</var><code class="command">)</code></td>
<td>size of arrowhead</td>
</tr>
<tr class="even">
<td><code class="command">mangle:(</code><var class="command">anglestyle</var><code class="command">)</code></td>
<td>angle of arrowhead</td>
</tr>
<tr class="odd">
<td><code class="command">barbsize:(</code><var class="command">markersizestyle</var><code class="command">)</code></td>
<td>size of filled portion of arrowhead</td>
</tr>
<tr class="even">
<td><code class="command">mcolor:(</code><var class="command">colorstyle</var><code class="command">)</code></td>
<td>color and opacity of arrowhead, inside and out</td>
</tr>
<tr class="odd">
<td><code class="command">mfcolor:(</code><var class="command">colorstyle</var><code class="command">)</code></td>
<td>arrowhead "fill" color and opacity</td>
</tr>
<tr class="even">
<td><code class="command">mlcolor:(</code><var class="command">colorstyle</var><code class="command">)</code></td>
<td>arrowhead outline color and opacity</td>
</tr>
<tr class="odd">
<td><code class="command">mlwidth:(</code><var class="command">linewidthstyle</var><code class="command">)</code></td>
<td>arrowhead outline thickness</td>
</tr>
<tr class="even">
<td><code class="command">mlstyle:(</code><var class="command">linestyle</var><code class="command">)</code></td>
<td>thickness and color</td>
</tr>
<tr class="odd">
<td><var class="command">line_options</var></td>
<td>change look of arrow shaft lines</td>
</tr>
<tr class="even">
<td><var class="command">marker_label_options</var></td>
<td>add marker labels; change look or position</td>
</tr>
<tr class="odd">
<td><code class="command">headlabel</code></td>
<td>label head of arrow, not tail</td>
</tr>
<tr class="even">
<td><code class="command">vertical</code></td>
<td>orient plot naturally; the default</td>
</tr>
<tr class="odd">
<td><code class="command">horizontal</code></td>
<td>orient plot transposing y and x values</td>
</tr>
<tr class="even">
<td><var class="command">axis_choice_options</var></td>
<td>associate plot with alternative axis</td>
</tr>
<tr class="odd">
<td><var class="command">twoway_options</var></td>
<td>titles, legends, axes, added lines and text, by, regions, name, aspect ratio, etc. <span>{p2line None}_
Most options are <var class="command">rightmost</var>, except <var class="command">axis_choice_options</var>, <code class="command">headlabel</code>, <code class="command">vertical</code>, and <code class="command">horizontal</code>, which are <var class="command">unique</var>, and <var class="command">twoway_options</var>, which are a mix of forms; see [<strong>repeated options</strong>](http://www.stata.com/help.cgi?repeated%20options).</td>
</tr>
</tbody>
</table>
