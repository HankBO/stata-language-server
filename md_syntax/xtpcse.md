## Syntax

`xtpcse`
[depvar](http://www.stata.com/help.cgi?depvar)
\[[indepvars](http://www.stata.com/help.cgi?indepvars)\]
_\[`if`\] \[`in`\]_ \[`weight`\] \[`,`
`options`\]

<table class="syntab">
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">Options</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd section">
<td colspan="3">Model</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="nocons">noconstant</code></td>
<td>suppress constant term</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="c">correlation</code><code class="command">(</code>
<ul>
</ul>
ndependent)</td>
<td>use independent autocorrelation structure</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="c">correlation</code><code class="command">(</code>
<ul>
</ul>
r1)</td>
<td>use AR1 autocorrelation structure</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="c">correlation</code><code class="command">(</code>
<ul>
</ul>
sar1)</td>
<td>use panel-specific AR1 autocorrelation structure</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="rho">rhotype(calc)</code></td>
<td>specify method to compute autocorrelation parameter; seldom used</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="np1">np1</code></td>
<td>weight panel-specific autocorrelations by panel sizes</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="het">hetonly</code></td>
<td>assume panel-level heteroskedastic errors</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="i">independent</code></td>
<td>assume independent errors across panels</td>
</tr>
</tbody>
<tbody>
<tr class="odd section">
<td colspan="3">by/if/in</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="ca">casewise</code></td>
<td>include only observations with complete cases</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="p">pairwise</code></td>
<td>include all available observations with nonmissing pairs</td>
</tr>
</tbody>
<tbody>
<tr class="odd section">
<td colspan="3">SE</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="nmk">nmk</code></td>
<td>normalize standard errors by N-k instead of N</td>
</tr>
</tbody>
<tbody>
<tr class="odd section">
<td colspan="3">Reporting</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="l">level(#)</code></td>
<td>set confidence level; default is <code class="command">level(95)</code></td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="d">detail</code></td>
<td>report list of gaps in time series</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><var class="command">display_options</var></td>
<td>control columns and column formats, row spacing, line width, display of omitted variables and base and empty cells, and factor-variable labeling</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="coefl">coeflegend</code></td>
<td>display legend instead of statistics</td>
</tr>
</tbody><tfoot>
<tr class="even footnote">
<td colspan="3">A panel variable and a time variable must be specified; use [<strong>xtset</strong>](http://www.stata.com/help.cgi?xtset).</td>
</tr>
<tr class="odd footnote">
<td colspan="3"><var class="command">indepvars</var> may contain factor variables; see [<strong>fvvarlist</strong>](http://www.stata.com/help.cgi?fvvarlist).</td>
</tr>
<tr class="even footnote">
<td colspan="3"><var class="command">depvar</var> and <var class="command">indepvars</var> may contain time-series operators; see [<strong>tsvarlist</strong>](http://www.stata.com/help.cgi?tsvarlist).</td>
</tr>
<tr class="odd footnote">
<td colspan="3"><code class="command" data-options="by">by</code> and <code class="command" data-options="statsby">statsby</code> are allowed; see [<strong>prefix</strong>](http://www.stata.com/help.cgi?prefix).</td>
</tr>
<tr class="even footnote">
<td colspan="3"><code class="command" data-options="iweight">iweight</code>s and <code class="command" data-options="aweight">aweight</code>s are allowed; see [<strong>weight</strong>](http://www.stata.com/help.cgi?weight).</td>
</tr>
<tr class="odd footnote">
<td colspan="3"><code class="command" data-options="coeflegend">coeflegend</code> does not appear in the dialog box.</td>
</tr>
<tr class="even footnote">
<td colspan="3">See [<strong>[XT]</strong> xtpcse postestimation](http://www.stata.com/help.cgi?xtpcse_postestimation) for features available after estimation.</td>
</tr>
</tfoot>

</table>
