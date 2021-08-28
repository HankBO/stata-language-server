## Syntax

Basic syntax

`heckman`
[depvar](http://www.stata.com/help.cgi?depvar)
\[[indepvars](http://www.stata.com/help.cgi?indepvars)\]`,`
`select(varlist_s)` \[`twostep`\]

`heckman`
[depvar](http://www.stata.com/help.cgi?depvar)
\[[indepvars](http://www.stata.com/help.cgi?indepvars)\]`,`
`select(depvar_s = varlist_s)` \[`twostep`\]

Full syntax for maximum likelihood estimates only

`heckman`
[depvar](http://www.stata.com/help.cgi?depvar)
\[[indepvars](http://www.stata.com/help.cgi?indepvars)\]
_\[`if`\] \[`in`\]_ \[`weight`\]`,`
`select(`\[`depvar_s =`\] `varlist_s` \[`, noconstant`
`offset(varname_o)`\]`)` \[`heckman_ml_options`\]

Full syntax for Heckman's two-step consistent estimates only

`heckman`
[depvar](http://www.stata.com/help.cgi?depvar)
\[[indepvars](http://www.stata.com/help.cgi?indepvars)\]
_\[`if`\] \[`in`\]_`, twostep`
`select(`\[`depvar_s =`\] `varlist_s` \[`, noconstant`\]`)`
\[`heckman_ts_options`\]

<table id="heckman_ml_options" class="syntab">
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">heckman_ml_options</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd section">
<td colspan="3">Model</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="ml">mle</code></td>
<td>use maximum likelihood estimator; the default</td>
</tr>
<tr class="odd" style="has_footnote">
<td>*</td>
<td><code class="command" data-options="sel">select()</code></td>
<td>specify selection equation: dependent and independent variables; whether to have constant term and offset variable</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="nocons">noconstant</code></td>
<td>suppress constant term</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="off">offset(varname)</code></td>
<td>include <var class="command">varname</var> in model with coefficient constrained to 1</td>
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
<td><code class="command" data-options="fir">first</code></td>
<td>report first-step probit estimates</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="lrmodel">lrmodel</code></td>
<td>perform the likelihood-ratio model test instead of the default Wald test</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="ns">nshazard(newvar)</code></td>
<td>generate nonselection hazard variable</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="m">mills(newvar)</code></td>
<td>synonym for <code class="command" data-options="nshazard()">nshazard()</code></td>
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
<td colspan="3">* <code class="command" data-options="select()">select()</code> is required. The full specification is<br />
<code class="command" data-options="sel">select</code><code class="command">(</code>[<var class="command">depvar_s</var> <code class="command">=</code>] <var class="command">varlist_s</var> [<code class="command">,</code> <code class="command" data-options="nocons">noconstant</code> <code class="command" data-options="off">offset(varname_o)</code>]<code class="command">)</code>.</td>
</tr>
</tfoot>

</table>

<table id="heckman_ts_options" class="syntab">
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">heckman_ts_options</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd section">
<td colspan="3">Model</td>
</tr>
<tr class="even" style="has_footnote">
<td>*</td>
<td><code class="command" data-options="two">twostep</code></td>
<td>produce two-step consistent estimate</td>
</tr>
<tr class="odd" style="has_footnote">
<td>*</td>
<td><code class="command" data-options="sel">select()</code></td>
<td>specify selection equation: dependent and independent variables; whether to have constant term</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="nocons">noconstant</code></td>
<td>suppress constant term</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="rhos">rhosigma</code></td>
<td>truncate rho to [-1,1] with consistent Sigma</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="rhot">rhotrunc</code></td>
<td>truncate rho to [-1,1]</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="rhol">rholimited</code></td>
<td>truncate rho in limited cases</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="rhof">rhoforce</code></td>
<td>do not truncate rho</td>
</tr>
</tbody>
<tbody>
<tr class="odd section">
<td colspan="3">SE</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="vce(vcetype)">vce(vcetype)</code></td>
<td><var class="command">vcetype</var> may be <code class="command" data-options="conventional">conventional</code>, <code class="command" data-options="boot">bootstrap</code>, or <code class="command" data-options="jack">jackknife</code></td>
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
<td><code class="command" data-options="fir">first</code></td>
<td>report first-step probit estimates</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="ns">nshazard(newvar)</code></td>
<td>generate nonselection hazard variable</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="m">mills(newvar)</code></td>
<td>synonym for <code class="command" data-options="nshazard()">nshazard()</code></td>
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
<td colspan="3">* <code class="command" data-options="twostep">twostep</code> and <code class="command" data-options="select()">select()</code> are required. The full specification is<br />
<code class="command" data-options="sel">select</code><code class="command">(</code>[<var class="command">depvar_s</var> <code class="command">=</code>] <var class="command">varlist_s</var> [<code class="command">,</code> <code class="command" data-options="nocons">noconstant</code>]<code class="command">)</code>.</td>
</tr>
</tfoot>

</table>

`indepvars` and `varlist_s` may contain factor variables; see
[<strong>fvvarlist</strong>](http://www.stata.com/help.cgi?fvvarlist).

`depvar`, `indepvars`, `varlist_s`, and `depvar_s` may contain
time-series operators; see
[<strong>tsvarlist</strong>](http://www.stata.com/help.cgi?tsvarlist).

`bayes`, `bootstrap`, `by`, `fp`, `jackknife`, `rolling`, `statsby`, and
`svy` are allowed; see
[<strong>prefix</strong>](http://www.stata.com/help.cgi?prefix).
For more details, see
[<strong>[BAYES]</strong> bayes: heckman](http://www.stata.com/help.cgi?bayes_heckman).

Weights are not allowed with the
[<strong>bootstrap</strong>](http://www.stata.com/help.cgi?bootstrap)
prefix.

`twostep`, `vce()`, `first`, `lrmodel`, and weights are not allowed with
the
[<strong>svy</strong>](http://www.stata.com/help.cgi?svy)
prefix.

`pweight`s, `fweight`s, and `iweight`s are allowed with maximum
likelihood estimation; see
[<strong>weight</strong>](http://www.stata.com/help.cgi?weight).
No weights are allowed if `twostep` is specified.

`coeflegend` does not appear in the dialog box.

See
[<strong>[R]</strong> heckman postestimation](http://www.stata.com/help.cgi?heckman_postestimation)
for features available after estimation.
