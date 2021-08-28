## Syntax

\[`svy`\] `sdr exp_list` \[`,`
[<var class="command">svy_options</var><strong></strong>](svy%20sdr##svy_options)
[<var class="command">sdr_options</var><strong></strong>](svy%20sdr##sdr_options)
`eform_option`\] `: command`

`exp_list` specifies the statistics to be collected from the execution
of `command`. `exp_list` is required unless `command` has the `svyb`
program property, in which case `exp_list` defaults to `_b`; see
[<strong>[P]</strong> program properties](http://www.stata.com/help.cgi?program_properties).

| svy\_options                                                           |                                                                                                        | Description                                                                                                                                      |
|------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| if/in                                                                  |                                                                                                        |                                                                                                                                                  |
|                                                                        | `subpop(`\[[varname](http://www.stata.com/help.cgi?varname)\] \[`if`\]`)` | identify a subpopulation                                                                                                                         |
| Reporting                                                              |                                                                                                        |                                                                                                                                                  |
|                                                                        | `level(#)`                                                                                             | set confidence level; default is `level(95)`                                                                                                     |
|                                                                        | `noheader`                                                                                             | suppress table header                                                                                                                            |
|                                                                        | `nolegend`                                                                                             | suppress table legend                                                                                                                            |
|                                                                        | `noadjust`                                                                                             | do not adjust model Wald statistic                                                                                                               |
|                                                                        | `nocnsreport`                                                                                          | do not display constraints                                                                                                                       |
|                                                                        | `display_options`                                                                                      | control columns and column formats, row spacing, line width, display of omitted variables and base and empty cells, and factor-variable labeling |
|                                                                        | `coeflegend`                                                                                           | display legend instead of statistics                                                                                                             |
| `coeflegend` is not shown in the dialog boxes for estimation commands. |                                                                                                        |                                                                                                                                                  |

<table id="sdr_options" class="syntab">
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">sdr_options</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd section">
<td colspan="3">Options</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td>[<strong></strong>](http://www.stata.com/help.cgi?prefix_saving_option)
<ul>
</ul>
ving(<var class="command">filename</var>[<strong>,</strong> ...]<strong>)</strong></td>
<td>save results to <var class="command">filename</var>; save statistics in double precision; save results to <var class="command">filename</var> every <var class="command">#</var> replications</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="mse">mse</code></td>
<td>use MSE formula for variance</td>
</tr>
</tbody>
<tbody>
<tr class="odd section">
<td colspan="3">Reporting</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="v">verbose</code></td>
<td>display the full table legend</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="nodots">nodots</code></td>
<td>suppress replication dots</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="dots(#)">dots(#)</code></td>
<td>display dots every <var class="command">#</var> replications</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="noi">noisily</code></td>
<td>display any output from <var class="command">command</var></td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="tr">trace</code></td>
<td>trace <var class="command">command</var></td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="ti">title(text)</code></td>
<td>use <var class="command">text</var> as title for SDR results</td>
</tr>
</tbody>
<tbody>
<tr class="odd section">
<td colspan="3">Advanced</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="nodrop">nodrop</code></td>
<td>do not drop observations</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="reject(exp)">reject(exp)</code></td>
<td>identify invalid results</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="dof(#)">dof(#)</code></td>
<td>design degrees of freedom</td>
</tr>
</tbody><tfoot>
<tr class="odd footnote">
<td colspan="3"><code class="command">svy</code> requires that the survey design variables be identified using [<strong>svyset</strong>](http://www.stata.com/help.cgi?svyset).</td>
</tr>
<tr class="even footnote">
<td colspan="3"><var class="command">command</var> defines the estimation command to be executed. The [<strong>by</strong>](http://www.stata.com/help.cgi?by) prefix cannot be part of <var class="command">command</var>.</td>
</tr>
<tr class="odd footnote">
<td colspan="3">See [<strong>[SVY] svy postestimation</strong>](http://www.stata.com/help.cgi?svy%20postestimation) for features available after estimation.</td>
</tr>
<tr class="even footnote">
<td colspan="3">Warning: Using <code class="command">if</code> or <code class="command">in</code> restrictions will often not produce correct variance estimates for subpopulations. To compute estimates for subpopulations, use the <code class="command">subpop()</code> option.</td>
</tr>
<tr class="odd footnote">
<td colspan="3"><code class="command">svy</code> <code class="command">sdr</code> requires that the successive difference replicate weights be identified using [<strong>svyset</strong>](http://www.stata.com/help.cgi?svyset).</td>
</tr>
</tfoot>

</table>
