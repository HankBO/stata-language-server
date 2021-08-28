## Syntax

`twoway fpfitci yvar xvar` _\[`if`\]
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
<td><var class="command">fpfit_options</var></td>
<td>any of the option of [<strong>[G-2]</strong> graph twoway fpfit](http://www.stata.com/help.cgi?twoway_fpfit)</td>
</tr>
<tr class="odd">
<td><code class="command">level(</code><var class="command">#</var><code class="command">)</code></td>
<td>set confidence level; default is <code class="command">level(95)</code></td>
</tr>
<tr class="even">
<td><code class="command">nofit</code></td>
<td>prevent plotting the prediction</td>
</tr>
<tr class="odd">
<td><code class="command">fitplot:(</code><var class="command">plottype</var><code class="command">)</code></td>
<td>how to plot fit; default is <code class="command">fitplot(line)</code></td>
</tr>
<tr class="even">
<td><code class="command">ciplot:(</code><var class="command">plottype</var><code class="command">)</code></td>
<td>how to plot CIs; default is <code class="command">ciplot(rarea)</code></td>
</tr>
<tr class="odd">
<td><var class="command">fcline_options</var></td>
<td>change look of predicted line</td>
</tr>
<tr class="even">
<td><var class="command">fitarea_options</var></td>
<td>change look of CI</td>
</tr>
<tr class="odd">
<td><var class="command">axis_choice_options</var></td>
<td>associate plot with alternative axis</td>
</tr>
<tr class="even">
<td><var class="command">twoway_options</var></td>
<td>titles, legends, axes, added lines and text, by, regions, name, aspect ratio, etc. <span>{p2line None}_
Option <code class="command">level()</code> is <var class="command">rightmost</var>; <code class="command">nofit</code>, <code class="command">fitplot()</code>, and <code class="command">ciplot()</code> are <var class="command">unique</var>; see [<strong>repeated options</strong>](http://www.stata.com/help.cgi?repeated%20options). <span data-options="weight">{marker weight}_
<code class="command">aweight</code>s, <code class="command">fweight</code>s, and <code class="command">pweight</code>s are allowed. Weights, if specified, affect estimation but not how the weighted results are plotted. See [<strong>weight</strong>](http://www.stata.com/help.cgi?weight).</td>
</tr>
</tbody>
</table>
