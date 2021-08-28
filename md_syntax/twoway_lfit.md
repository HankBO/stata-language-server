## Syntax

`twoway lfit yvar xvar` _\[`if`\]
\[`in`\]_ \[`weight`\] \[`, options`\]

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
<td><code class="command">range:(</code><var class="command">#</var> <var class="command">#</var><code class="command">)</code></td>
<td>range over which predictions calculated</td>
</tr>
<tr class="odd">
<td><code class="command">n(</code><var class="command">#</var><code class="command">)</code></td>
<td>number of prediction points</td>
</tr>
<tr class="even">
<td><code class="command">atobs</code></td>
<td>calculate predictions at <var class="command">xvar</var></td>
</tr>
<tr class="odd">
<td><code class="command">estopts:(</code><var class="command">regress_options</var><code class="command">)</code></td>
<td>options for <code class="command">regress</code></td>
</tr>
<tr class="even">
<td><code class="command">predopts:(</code><var class="command">predict_options</var><code class="command">)</code></td>
<td>options for <code class="command">predict</code></td>
</tr>
<tr class="odd">
<td><var class="command">cline_options</var></td>
<td>change look of predicted line</td>
</tr>
<tr class="even">
<td><var class="command">axis_choice_options</var></td>
<td>associate plot with alternative axis</td>
</tr>
<tr class="odd">
<td><var class="command">twoway_options</var></td>
<td>titles, legends, axes, added lines and text, by, regions, name, aspect ratio, etc. <span>{p2line None}_
All options are <var class="command">rightmost</var>; see [<strong>repeated options</strong>](http://www.stata.com/help.cgi?repeated%20options).
<var class="command">yvar</var> and <var class="command">xvar</var> may contain time-series operators; see [<strong>tsvarlist</strong>](http://www.stata.com/help.cgi?tsvarlist). <span data-options="weight">{marker weight}_
<code class="command">aweight</code>s, <code class="command">fweight</code>s, and <code class="command">pweight</code>s are allowed. Weights, if specified, affect estimation but not how the weighted results are plotted. See [<strong>weight</strong>](http://www.stata.com/help.cgi?weight).</td>
</tr>
</tbody>
</table>
