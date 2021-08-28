## Syntax

Check proportional-hazards assumption:

Log-log plot of survival

`stphplot` \[`if`\] `,` {`by(varname)` \|
`strata(varname)`} \[`stphplot_options`\]

Kaplan-Meier and predicted survival plot

`stcoxkm` \[`if`\] `, by(varname)` \[`stcoxkm_options`\]

Using Schoenfeld residuals

`estat phtest` \[`, phtest_options`\]

<table id="stphplot_options" class="syntab">
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">stphplot_options</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd section">
<td colspan="3">Main</td>
</tr>
<tr class="even" style="has_footnote">
<td>*</td>
<td><code class="command" data-options="by(varname)">by(varname)</code></td>
<td>fit separate Cox models; the default</td>
</tr>
<tr class="odd" style="has_footnote">
<td>*</td>
<td><code class="command" data-options="str">strata(varname)</code></td>
<td>fit stratified Cox model</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="adj">adjust(varlist)</code></td>
<td>adjust to average values of <var class="command">varlist</var></td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="z">zero</code></td>
<td>adjust to zero values of <var class="command">varlist</var>; use with <code class="command" data-options="adjust()">adjust()</code></td>
</tr>
</tbody>
<tbody>
<tr class="odd section">
<td colspan="3">Options</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="noneg">nonegative</code></td>
<td>plot ln<span data-options="-(">{c -(}_-ln(survival)<span data-options=")-">{c )-}_</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="nolnt">nolntime</code></td>
<td>plot curves against analysis time</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="nosh">noshow</code></td>
<td>do not show st setting information</td>
</tr>
</tbody>
<tbody>
<tr class="odd section">
<td colspan="3">Plot</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command">plot</code>
<ul>
</ul>
<code class="command">opts(</code>[<var class="command">stphplot_plot_options</var><strong></strong>](#stphplot_plot_options)<code class="command">)</code></td>
<td>affect rendition of the <var class="command">#</var>th connected line and <var class="command">#</var>th plotted points</td>
</tr>
</tbody>
<tbody>
<tr class="odd section">
<td colspan="3">Add plots</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="&quot;addplot(addplot_option:plot)&quot;">"addplot(plot)</code></td>
<td>add other plots to the generated graph</td>
</tr>
</tbody>
<tbody>
<tr class="odd section">
<td colspan="3">Y axis, X axis, Titles, Legend, Overall</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><var class="command">twoway_options</var></td>
<td>any options other than <code class="command" data-options="by()">by()</code> documented in [<strong>[G-3]</strong> <em>twoway_options</em>](http://www.stata.com/help.cgi?twoway_options)</td>
</tr>
</tbody><tfoot>
<tr class="even footnote">
<td colspan="3">* Either <code class="command" data-options="by(varname)">by(varname)</code> or <code class="command" data-options="strata(varname)">strata(varname)</code> is required with <code class="command">stphplot</code>.</td>
</tr>
</tfoot>

</table>

| stphplot\_plot\_options |                  | Description                                |
|-------------------------|------------------|--------------------------------------------|
|                         | `cline_options`  | change look of lines or connecting method  |
|                         | `marker_options` | change look of markers (color, size, etc.) |

<table id="stcoxkm_options" class="syntab">
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">stcoxkm_options</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd section">
<td colspan="3">Main</td>
</tr>
<tr class="even" style="has_footnote">
<td>*</td>
<td><code class="command" data-options="by(varname)">by(varname)</code></td>
<td>report the nominal or ordinal covariate</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command">ties(</code><code class="command">breslow)</code></td>
<td>use Breslow method to handle tied failures</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command">ties(</code><code class="command">efron)</code></td>
<td>use Efron method to handle tied failures</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command">ties(exactm)</code></td>
<td>use exact marginal-likelihood method to handle tied failures</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command">ties(exactp)</code></td>
<td>use exact partial-likelihood method to handle tied failures</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="sep">separate</code></td>
<td>draw separate plot for predicted and observed curves</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="nosh">noshow</code></td>
<td>do not show st setting information</td>
</tr>
</tbody>
<tbody>
<tr class="odd section">
<td colspan="3">Observed plot</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="obsop">obsopts(stcoxkm_plot_options)</code></td>
<td>affect rendition of the observed curve</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command">obs</code>
<ul>
</ul>
<code class="command">opts(</code>[<var class="command">stcoxkm_plot_options</var><strong></strong>](#stcoxkm_plot_options)<code class="command">)</code></td>
<td>affect rendition of the <var class="command">#</var>th observed curve; not allowed with <code class="command" data-options="separate">separate</code></td>
</tr>
</tbody>
<tbody>
<tr class="odd section">
<td colspan="3">Predicted plot</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="predop">predopts(stcoxkm_plot_options)</code></td>
<td>affect rendition of the predicted curve</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command">pred</code>
<ul>
</ul>
<code class="command">opts(</code>[<var class="command">stcoxkm_plot_options</var><strong></strong>](#stcoxkm_plot_options)<code class="command">)</code></td>
<td>affect rendition of the <var class="command">#</var>th predicted curve; not allowed with <code class="command" data-options="separate">separate</code></td>
</tr>
</tbody>
<tbody>
<tr class="odd section">
<td colspan="3">Add plots</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="&quot;addplot(addplot_option:plot)&quot;">"addplot(plot)</code></td>
<td>add other plots to the generated graph</td>
</tr>
</tbody>
<tbody>
<tr class="odd section">
<td colspan="3">Y axis, X axis, Titles, Legend, Overall</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><var class="command">twoway_options</var></td>
<td>any options other than <code class="command" data-options="by()">by()</code> documented in [<strong>[G-3]</strong> <em>twoway_options</em>](http://www.stata.com/help.cgi?twoway_options)</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="byop">byopts(byopts)</code></td>
<td>how subgraphs are combined, labeled, etc.</td>
</tr>
</tbody><tfoot>
<tr class="even footnote">
<td colspan="3">* <code class="command" data-options="by(varname)">by(varname)</code> is required with <code class="command">stcoxkm</code>.</td>
</tr>
</tfoot>

</table>

| stcoxkm\_plot\_options |                   | Description                                |
|------------------------|-------------------|--------------------------------------------|
|                        | `connect_options` | change look of connecting method           |
|                        | `marker_options`  | change look of markers (color, size, etc.) |

You must `stset` your data before using `stphplot` and `stcoxkm`; see
[<strong>[ST]</strong> stset](http://www.stata.com/help.cgi?stset).

`fweight`s, `iweight`s, and `pweight`s may be specified using `stset`;
see
[<strong>[ST]</strong> stset](http://www.stata.com/help.cgi?stset).

| phtest\_options                                                  |                           | Description                                                                                                                                                           |
|------------------------------------------------------------------|---------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Main                                                             |                           |                                                                                                                                                                       |
|                                                                  | `log`                     | use natural logarithm time-scaling function                                                                                                                           |
|                                                                  | `km`                      | use 1-KM product-limit estimate as the time-scaling function                                                                                                          |
|                                                                  | `rank`                    | use rank of analysis time as the time-scaling function                                                                                                                |
|                                                                  | `time(varname)`           | use `varname` containing a monotone transformation of analysis time as the time-scaling function                                                                      |
|                                                                  | `plot(varname)`           | plot smoothed, scaled Schoenfeld residuals versus time                                                                                                                |
|                                                                  | `bwidth(#)`               | use bandwidth of `#`; default is `bwidth(0.8)`                                                                                                                        |
|                                                                  | `detail`                  | test proportional-hazards assumption separately for each covariate                                                                                                    |
| Scatterplot                                                      |                           |                                                                                                                                                                       |
|                                                                  | `marker_options`          | change look of markers (color, size, etc.)                                                                                                                            |
|                                                                  | `marker_label_options`    | add marker labels; change look or position                                                                                                                            |
| Smoothed line                                                    |                           |                                                                                                                                                                       |
|                                                                  | `lineopts(cline_options)` | affect rendition of the smoothed line                                                                                                                                 |
| Y axis, X axis, Titles, Legend, Overall                          |                           |                                                                                                                                                                       |
|                                                                  | `twoway_options`          | any options other than `by()` documented in [<strong>[G-3]</strong> <em>twoway_options</em>](http://www.stata.com/help.cgi?twoway_options) |
| `estat phtest` is not appropriate after estimation with `svy`. |                           |                                                                                                                                                                       |
