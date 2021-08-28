## Syntax

Graph by panel

`xtline`
[varlist](http://www.stata.com/help.cgi?varlist)
_\[`if`\] \[`in`\]_ \[`, panel_options`\]

Overlaid panels

`xtline`
[varname](http://www.stata.com/help.cgi?varname)
_\[`if`\] \[`in`\]_`, overlay`
\[`overlaid_options`\]

| panel\_options                             |                  | Description                                                                                                                                                           |
|--------------------------------------------|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Main                                       |                  |                                                                                                                                                                       |
|                                            | `"i(varname_i)`  | use `varname_i` as the panel ID variable                                                                                                                              |
|                                            | `"t(varname_t)`  | use `varname_t` as the time variable                                                                                                                                  |
| Plot                                       |                  |                                                                                                                                                                       |
|                                            | `cline_options`  | affect rendition of the plotted points connected by lines                                                                                                             |
| Add plots                                  |                  |                                                                                                                                                                       |
|                                            | `"addplot(plot)` | add other plots to the generated graph                                                                                                                                |
| Y axis, Time axis, Titles, Legend, Overall |                  |                                                                                                                                                                       |
|                                            | `twoway_options` | any options other than `by()` documented in [<strong>[G-3]</strong> <em>twoway_options</em>](http://www.stata.com/help.cgi?twoway_options) |
|                                            | `byopts(byopts)` | affect appearance of the combined graph                                                                                                                               |

<table id="overlaid" class="syntab">
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">overlaid_options</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd section">
<td colspan="3">Main</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="ov">overlay</code></td>
<td>overlay each panel on the same graph</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="&quot;i(varname:varname_i)&quot;">"i(varname_i)</code></td>
<td>use <var class="command">varname_i</var> as the panel ID variable</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="&quot;t(varname:varname_t)&quot;">"t(varname_t)</code></td>
<td>use <var class="command">varname_t</var> as the time variable</td>
</tr>
</tbody>
<tbody>
<tr class="odd section">
<td colspan="3">Plots</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command">plot</code>
<ul>
</ul>
<code class="command" data-options="&quot;opts(cline_options:cline_options)&quot;">"opts(cline_options)</code></td>
<td>affect rendition of the <var class="command">#</var> panel line</td>
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
<td colspan="3">Y axis, Time axis, Titles, Legend, Overall</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><var class="command">twoway_options</var></td>
<td>any options other than <code class="command" data-options="by()">by()</code> documented in [<strong>[G-3]</strong> <em>twoway_options</em>](http://www.stata.com/help.cgi?twoway_options)</td>
</tr>
</tbody>
</table>

A panel variable and a time variable must be specified. Use `xtset` (see
[<strong>[XT] xtset</strong>](http://www.stata.com/help.cgi?xtset))
or specify the `i()` and `t()` options. The `t()` option allows
noninteger values for the time variable, whereas `xtset` does not.
