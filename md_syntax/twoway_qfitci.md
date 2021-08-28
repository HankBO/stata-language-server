## Syntax

`twoway qfitci yvar xvar` _\[`if`\]
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
<td><code class="command">stdp</code></td>
<td>CIs from SE of prediction; the default</td>
</tr>
<tr class="odd">
<td><code class="command">stdf</code></td>
<td>CIs from SE of forecast</td>
</tr>
<tr class="even">
<td><code class="command">stdr</code></td>
<td>CIs from SE of residual; seldom specified</td>
</tr>
<tr class="odd">
<td><code class="command">level(</code><var class="command">#</var><code class="command">)</code></td>
<td>set confidence level; default is <code class="command">level(95)</code></td>
</tr>
<tr class="even">
<td><code class="command">range:(</code><var class="command">#</var> <var class="command">#</var><code class="command">)</code></td>
<td>range over which predictions are calculated</td>
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
<td><code class="command">nofit</code></td>
<td>do not plot the prediction</td>
</tr>
<tr class="even">
<td><code class="command">fitplot:(</code><var class="command">plottype</var><code class="command">)</code></td>
<td>how to plot fit; default is <code class="command">fitplot(line)</code></td>
</tr>
<tr class="odd">
<td><code class="command">ciplot:(</code><var class="command">plottype</var><code class="command">)</code></td>
<td>how to plot CIs; default is <code class="command">ciplot(rarea)</code></td>
</tr>
<tr class="even">
<td><var class="command">fcline_options</var></td>
<td>change look of predicted line</td>
</tr>
<tr class="odd">
<td><var class="command">fitarea_options</var></td>
<td>change look of CI</td>
</tr>
<tr class="even">
<td><var class="command">axis_choice_options</var></td>
<td>associate plot with alternative axis</td>
</tr>
<tr class="odd">
<td><var class="command">twoway_options</var></td>
<td>titles, legends, axes, added lines and text, by, regions, name, aspect ratio, etc. <span>{p2line None}_
Options <code class="command">range()</code>, <code class="command">estopts()</code>, <code class="command">predopts()</code>, <code class="command">n()</code>, and <code class="command">level()</code> are <var class="command">rightmost</var>; <code class="command">atobs</code>, <code class="command">nofit</code>, <code class="command">fitplot()</code>, <code class="command">ciplot()</code>, <code class="command">stdp</code>, <code class="command">stdf</code>, and <code class="command">stdr</code> are <var class="command">unique</var>; see [<strong>repeated options</strong>](http://www.stata.com/help.cgi?repeated%20options).
<var class="command">yvar</var> and <var class="command">xvar</var> may contain time-series operators; see [<strong>tsvarlist</strong>](http://www.stata.com/help.cgi?tsvarlist). <span data-options="weight">{marker weight}_
<code class="command">aweight</code>s, <code class="command">fweight</code>s, and <code class="command">pweight</code>s are allowed. Weights, if specified, affect estimation but not how the weighted results are plotted. See [<strong>weight</strong>](http://www.stata.com/help.cgi?weight).</td>
</tr>
</tbody>
</table>
