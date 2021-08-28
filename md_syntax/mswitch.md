## Syntax

Markov-switching dynamic regression

`mswitch dr`
[depvar](http://www.stata.com/help.cgi?depvar)
\[`nonswitch_varlist`\] _\[`if`\] \[`in`\]_
\[`,`
[<var class="command">options</var><strong></strong>](#mswitch_options)\]

Markov-switching autoregression (AR)

`mswitch ar`
[depvar](http://www.stata.com/help.cgi?depvar)
\[`nonswitch_varlist`\]`, ar(numlist)`
\[[<var class="command">msar_options</var><strong></strong>](#msar_options)
[<var class="command">options</var><strong></strong>](#mswitch_options)\]

`nonswitch_varlist` is a list of variables with state-invariant
coefficients.

| options      |                                               | Description                                                                                                                                      |
|--------------|-----------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| Main         |                                               |                                                                                                                                                  |
|              | `states(#)`                                   | specify number of states; default is `states(2)`                                                                                                 |
|              | `switch(`\[`varlist`\]\[`, noconstant`\]`)` | specify variables with switching coefficients; by default, the constant term is state dependent unless `switch(, noconstant)` is specified       |
|              | `constant`                                    | allow a state-invariant constant term; may be specified only with `switch(, noconstant)`                                                         |
|              | `varswitch`                                   | specify state-dependent variance parameters; by default, the variance parameter is constant across all states                                    |
|              | `p0(type)`                                    | specify initial unconditional probabilities where `type` is one of `transition`, `fixed`, or `smoothed`; the default is `p0(transition)`         |
|              | `constraints(numlist)`                        | apply specified linear constraints                                                                                                               |
| SE/Robust    |                                               |                                                                                                                                                  |
|              | `vce(vcetype)`                                | `vcetype` may be `oim` or `robust`                                                                                                               |
| Reporting    |                                               |                                                                                                                                                  |
|              | `level(#)`                                    | set confidence level; default is `level(95)`                                                                                                     |
|              | `nocnsreport`                                 | do not display constraints                                                                                                                       |
|              | `display_options`                             | control columns and column formats, row spacing, line width, display of omitted variables and base and empty cells, and factor-variable labeling |
| EM options   |                                               |                                                                                                                                                  |
|              | `emiterate(#)`                                | specify the number of expectation-maximization (EM) iterations; default is `emiterate(10)`                                                       |
|              | `emlog`                                       | show EM iteration log                                                                                                                            |
|              | `emdots`                                      | show EM iterations as dots                                                                                                                       |
| Maximization |                                               |                                                                                                                                                  |
|              | `maximize_options`                            | control the maximization process                                                                                                                 |
|              | `coeflegend`                                  | display legend instead of statistics                                                                                                             |

<table id="msar_options" class="syntab">
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">msar_options</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd section">
<td colspan="3">Model</td>
</tr>
<tr class="even" style="has_footnote">
<td>*</td>
<td><code class="command" data-options="ar(numlist)">ar(numlist)</code></td>
<td>specify the number of AR terms</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command">arswitch</code></td>
<td>specify state-dependent AR coefficients</td>
</tr>
</tbody><tfoot>
<tr class="even footnote">
<td colspan="3">* <code class="command" data-options="ar(numlist)">ar(numlist)</code> is required.
You must <code class="command" data-options="tsset">tsset</code> your data before using <code class="command" data-options="mswitch">mswitch</code>; see [<strong>[TS]</strong> tsset](http://www.stata.com/help.cgi?tsset).</td>
</tr>
<tr class="odd footnote">
<td colspan="3"><var class="command">varlist</var> and <var class="command">nonswitch_varlist</var> may contain factor variables; see [<strong>fvvarlist</strong>](http://www.stata.com/help.cgi?fvvarlist).</td>
</tr>
<tr class="even footnote">
<td colspan="3"><var class="command">depvar</var>, <var class="command">nonswitch_varlist</var>, and <var class="command">varlist</var> may contain time-series operators; see [<strong>tsvarlist</strong>](http://www.stata.com/help.cgi?tsvarlist).</td>
</tr>
<tr class="odd footnote">
<td colspan="3"><code class="command" data-options="by">by</code>, <code class="command" data-options="rolling">rolling</code>, and <code class="command" data-options="statsby">statsby</code> are allowed; see [<strong>prefix</strong>](http://www.stata.com/help.cgi?prefix).</td>
</tr>
<tr class="even footnote">
<td colspan="3"><code class="command" data-options="coeflegend">coeflegend</code> does not appear in the dialog box.</td>
</tr>
<tr class="odd footnote">
<td colspan="3">See [<strong>[TS]</strong> mswitch postestimation](http://www.stata.com/help.cgi?mswitch_postestimation) for features available after estimation.</td>
</tr>
</tfoot>

</table>
