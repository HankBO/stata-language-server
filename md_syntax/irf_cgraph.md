## Syntax

`irf cgraph (spec_1)` \[`(spec_2)` ... \[`(spec_N)`\]\] \[`,`
`options`\]

where `(spec_k)` is

`(irfname impulsevar responsevar stat` \[`, spec_options`\]`)`

`irfname` is the name of a set of IRF results in the active IRF file.
`impulsevar` should be specified as an endogenous variable for all
statistics except `dm` and `cdm`; for those, specify as an exogenous
variable. `responsevar` is an endogenous variable name. `stat` is one or
more statistics from the list below:

<table id="stat" class="standard">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><var class="command">stat</var></td>
<td>Description <span>{p2line None}_ <span>{syntab None:Main}_</td>
</tr>
<tr class="even">
<td><code class="command">irf</code></td>
<td>impulse-response function</td>
</tr>
<tr class="odd">
<td><code class="command">oirf</code></td>
<td>orthogonalized impulse-response function</td>
</tr>
<tr class="even">
<td><code class="command">dm</code></td>
<td>dynamic-multiplier function</td>
</tr>
<tr class="odd">
<td><code class="command">cirf</code></td>
<td>cumulative impulse-response function</td>
</tr>
<tr class="even">
<td><code class="command">coirf</code></td>
<td>cumulative orthogonalized impulse-response function</td>
</tr>
<tr class="odd">
<td><code class="command">cdm</code></td>
<td>cumulative dynamic-multiplier function</td>
</tr>
<tr class="even">
<td><code class="command">fevd</code></td>
<td>Cholesky forecast-error variance decomposition</td>
</tr>
<tr class="odd">
<td><code class="command">sirf</code></td>
<td>structural impulse-response function</td>
</tr>
<tr class="even">
<td><code class="command">sfevd</code></td>
<td>structural forecast-error variance decomposition <span>{p2line None}_
Notes: (1) No statistic may appear more than once.
(2) If confidence intervals are included (the default), only two statistics may be included.
(3) If confidence intervals are suppressed (option <code class="command">noci</code>), up to four statistics may be included.</td>
</tr>
</tbody>
</table>

| options                                 |                   | Description                                                                                                                                                           |
|-----------------------------------------|-------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Main                                    |                   |                                                                                                                                                                       |
|                                         | `set(filename)`   | make `filename` active                                                                                                                                                |
| Options                                 |                   |                                                                                                                                                                       |
|                                         | `combine_options` | affect appearance of combined graph                                                                                                                                   |
| Y axis, X axis, Titles, Legend, Overall |                   |                                                                                                                                                                       |
|                                         | `twoway_options`  | any options other than `by()` documented in [<strong>[G-3]</strong> <em>twoway_options</em>](http://www.stata.com/help.cgi?twoway_options) |

|                                                              |                |                                                    |
|--------------------------------------------------------------|----------------|----------------------------------------------------|
| \*                                                           | `spec_options` | level, steps, and rendition of plots and their CIs |
|                                                              | `individual`   | graph each combination individually                |
| \* `spec_options` appear on multiple tabs in the dialog box. |                |                                                    |
| `individual` does not appear in the dialog box.              |                |                                                    |

<table id="spec_options" class="syntab">
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">spec_options</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd section">
<td colspan="3">Main</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="noci">noci</code></td>
<td>suppress confidence bands</td>
</tr>
</tbody>
<tbody>
<tr class="odd section">
<td colspan="3">Options</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="l">level(#)</code></td>
<td>set confidence level; default is <code class="command">level(95)</code></td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="lst">lstep(#)</code></td>
<td>use <var class="command">#</var> for first step</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="ust">ustep(#)</code></td>
<td>use <var class="command">#</var> for maximum step</td>
</tr>
</tbody>
<tbody>
<tr class="odd section">
<td colspan="3">Plots</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command">plot</code><var class="command"></var>
<ul>
</ul>
<code class="command">opts(</code><var class="command">cline_options</var><code class="command">)</code></td>
<td>affect rendition of the line plotting the # <var class="command">stat</var></td>
</tr>
</tbody>
<tbody>
<tr class="odd section">
<td colspan="3">CI plots</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command">ci</code><var class="command"></var>
<ul>
</ul>
<code class="command">opts(</code><var class="command">area_options</var><code class="command">)</code></td>
<td>affect rendition of the confidence interval for the <var class="command">#</var> <var class="command">stat</var></td>
</tr>
</tbody><tfoot>
<tr class="odd footnote">
<td colspan="3"><var class="command">spec_options</var> may be specified within a graph specification, globally, or in both. When specified in a graph specification, the <var class="command">spec_options</var> affect only the specification in which they are used. When supplied globally, the <var class="command">spec_options</var> affect all graph specifications. When supplied in both places, options in the graph specification take precedence.</td>
</tr>
</tfoot>

</table>
