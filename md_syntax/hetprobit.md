## Syntax

`hetprobit`
[depvar](http://www.stata.com/help.cgi?depvar)
\[[indepvars](http://www.stata.com/help.cgi?indepvars)\]
_\[`if`\] \[`in`\]_ \[`weight`\]`,`
`het(`[varlist](http://www.stata.com/help.cgi?varlist)
\[`, offset(varname_o)`\]`)` \[`options`\]

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
<tr class="even" style="has_footnote">
<td>*</td>
<td><code class="command">het(</code>[varlist](http://www.stata.com/help.cgi?varlist)[...]<code class="command">)</code></td>
<td>independent variables to model the variance and possible offset variable</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="nocons">noconstant</code></td>
<td>suppress constant term</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="off">offset(varname)</code></td>
<td>include <var class="command">varname</var> in model with coefficient constrained to 1</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="asis">asis</code></td>
<td>retain perfect predictor variables</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command">constraints(</code><var class="command">constraints</var><code class="command">)</code></td>
<td>apply specified linear constraints</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="col">collinear</code></td>
<td>keep collinear variables</td>
</tr>
</tbody>
<tbody>
<tr class="odd section">
<td colspan="3">SE/Robust</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="vce(vcetype)">vce(vcetype)</code></td>
<td><var class="command">vcetype</var> may be <code class="command" data-options="oim">oim</code>, <code class="command" data-options="r">robust</code>, <code class="command" data-options="cl">cluster</code> <var class="command">clustvar</var>, <code class="command">opg</code>, <code class="command" data-options="boot">bootstrap</code>, or <code class="command" data-options="jack">jackknife</code></td>
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
<td><code class="command" data-options="lrmodel">lrmodel</code></td>
<td>perform the likelihood-ratio model test instead of the default Wald test</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="waldhet">waldhet</code></td>
<td>perform Wald test on variance</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="nocnsr">nocnsreport</code></td>
<td>do not display constraints</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><var class="command">display_options</var></td>
<td>control columns and column formats, row spacing, line width, display of omitted variables and base and empty cells, and factor-variable labeling</td>
</tr>
</tbody>
<tbody>
<tr class="odd section">
<td colspan="3">Maximization</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><var class="command">maximize_options</var></td>
<td>control the maximization process; seldom used</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="coefl">coeflegend</code></td>
<td>display legend instead of statistics</td>
</tr>
</tbody><tfoot>
<tr class="odd footnote">
<td colspan="3">* <code class="command" data-options="het()">het()</code> is required. The full specification is<br />
<code class="command">het(</code><var class="command">varlist</var> [<code class="command">,</code> <code class="command" data-options="off">offset(varname_o)</code>]<code class="command">)</code>.</td>
</tr>
<tr class="even footnote">
<td colspan="3"><var class="command">indepvars</var> and <var class="command">varlist</var> may contain factor variables; see [<strong>fvvarlist</strong>](http://www.stata.com/help.cgi?fvvarlist).</td>
</tr>
<tr class="odd footnote">
<td colspan="3"><var class="command">depvar</var>, <var class="command">indepvars</var>, and <var class="command">varlist</var> may contain time-series operators; see [<strong>tsvarlist</strong>](http://www.stata.com/help.cgi?tsvarlist).</td>
</tr>
<tr class="even footnote">
<td colspan="3"><code class="command">bayes</code>, <code class="command">bootstrap</code>, <code class="command">by</code>, <code class="command">fp</code>, <code class="command">jackknife</code>, <code class="command">rolling</code>, <code class="command">statsby</code>, and <code class="command">svy</code> are allowed; see [<strong>prefix</strong>](http://www.stata.com/help.cgi?prefix). For more details, see [<strong>[BAYES]</strong> bayes: hetprobit](http://www.stata.com/help.cgi?bayes_hetprobit).</td>
</tr>
<tr class="odd footnote">
<td colspan="3">Weights are not allowed with the [<strong>bootstrap</strong>](http://www.stata.com/help.cgi?bootstrap) prefix.</td>
</tr>
<tr class="even footnote">
<td colspan="3"><code class="command" data-options="vce()">vce()</code>, <code class="command" data-options="lrmodel">lrmodel</code>, and weights are not allowed with the [<strong>svy</strong>](http://www.stata.com/help.cgi?svy) prefix.</td>
</tr>
<tr class="odd footnote">
<td colspan="3"><code class="command" data-options="fweight">fweight</code>s, <code class="command" data-options="iweight">iweight</code>s, and <code class="command" data-options="pweight">pweight</code>s are allowed; see [<strong>weight</strong>](http://www.stata.com/help.cgi?weight).</td>
</tr>
<tr class="even footnote">
<td colspan="3"><code class="command" data-options="coeflegend">coeflegend</code> does not appear in the dialog box.</td>
</tr>
<tr class="odd footnote">
<td colspan="3">See [<strong>[R]</strong> hetprobit postestimation](http://www.stata.com/help.cgi?hetprobit_postestimation) for features available after estimation.</td>
</tr>
</tfoot>

</table>
