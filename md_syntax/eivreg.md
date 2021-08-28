## Syntax

`eivreg`
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
<td><code class="command">reliab(</code><var class="command">indepvar</var> <var class="command">#</var> [<var class="command">indepvar # </var>[...]]<code class="command">)</code></td>
<td></td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td></td>
<td>specify measurement reliability for each <var class="command">indepvar</var> measured with error</td>
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
<td><var class="command">display_options</var></td>
<td>control columns and column formats, row spacing, line width, display of omitted variables and base and empty cells, and factor-variable labeling</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="coefl">coeflegend</code></td>
<td>display legend instead of statistics</td>
</tr>
</tbody><tfoot>
<tr class="even footnote">
<td colspan="3"><var class="command">indepvars</var> may contain factor variables; see [<strong>fvvarlist</strong>](http://www.stata.com/help.cgi?fvvarlist).</td>
</tr>
<tr class="odd footnote">
<td colspan="3"><code class="command" data-options="bootstrap">bootstrap</code>, <code class="command" data-options="by">by</code>, <code class="command" data-options="jackknife">jackknife</code>, <code class="command" data-options="rolling">rolling</code>, and <code class="command" data-options="statsby">statsby</code> are allowed; see [<strong>prefix</strong>](http://www.stata.com/help.cgi?prefix).</td>
</tr>
<tr class="even footnote">
<td colspan="3">Weights are not allowed with the [<strong>bootstrap</strong>](http://www.stata.com/help.cgi?bootstrap) prefix.</td>
</tr>
<tr class="odd footnote">
<td colspan="3"><code class="command">aweight</code>s are not allowed with the [<strong>jackknife</strong>](http://www.stata.com/help.cgi?jackknife) prefix.</td>
</tr>
<tr class="even footnote">
<td colspan="3"><code class="command">aweight</code>s and <code class="command">fweight</code>s are allowed; see [<strong>weight</strong>](http://www.stata.com/help.cgi?weight).</td>
</tr>
<tr class="odd footnote">
<td colspan="3"><code class="command" data-options="coeflegend">coeflegend</code> does not appear in the dialog box.</td>
</tr>
<tr class="even footnote">
<td colspan="3">See [<strong>[R]</strong> eivreg postestimation](http://www.stata.com/help.cgi?eivreg_postestimation) for features available after estimation. <span data-options="menu">{marker menu}_<span>{nobreak None}_ <span>{title None:Menu}_ <span>{phang None}_ <strong>Statistics &gt; Linear models and related &gt; Errors-in-variables regression</strong> <span data-options="description">{marker description}_<span>{nobreak None}_ <span>{title None:Description}_ <span>{pstd None}_ <code class="command">eivreg</code> fits errors-in-variables regression models when one or more of the independent variables are measured with error. To use <code class="command">eivreg</code>, you must have an estimate of each independent variable's reliability or assume it is measured without error. <span data-options="linkspdf">{marker linkspdf}_<span>{nobreak None}_ <span>{title None:Links to PDF documentation}_ <a href="http://www.stata.com/manuals14/reivregquickstart.pdf">Quick start</a> <a href="http://www.stata.com/manuals14/reivregremarksandexamples.pdf">Remarks and examples</a> <a href="http://www.stata.com/manuals14/reivregmethodsandformulas.pdf">Methods and formulas</a> <span>{pstd None}_ The above sections are not included in this help file. <span data-options="options">{marker options}_<span>{nobreak None}_ <span>{title None:Options}_ <span>{dlgtab None:Model}_ <span>{phang None}_ <code class="command">reliab(</code><var class="command">indepvar</var> <var class="command">#</var> [<var class="command">indepvar # </var>[...]]<code class="command">)</code> specifies the measurement reliability for each independent variable measured with error. Reliabilities are specified as pairs consisting of an independent variable name (a name that appears in <var class="command">indepvars</var>) and the corresponding reliability r, 0 &lt; r
<ul>
</ul>
1. Independent variables for which no reliability is specified are assumed to have reliability 1. If the option is not specified, all variables are assumed to have reliability 1, and the result is thus the same as that produced by <code class="command">regress</code> (the ordinary least-squares results). <span>{dlgtab None:Reporting}_ <span>{phang None}_ <code class="command" data-options="level(#)">level(#)</code>; see [<strong>[R] estimation options</strong>](estimation%20options##level()). <span data-options="display_options">{marker display_options}_<span>{nobreak None}_ <span>{phang None}_ <var class="command">display_options</var>: <code class="command" data-options="noci">noci</code>, <code class="command" data-options="nopv">nopvalues</code>, <code class="command" data-options="noomit">noomitted</code>, <code class="command" data-options="vsquish">vsquish</code>, <code class="command" data-options="noempty">noemptycells</code>, <code class="command" data-options="base">baselevels</code>, <code class="command" data-options="allbase">allbaselevels</code>, <code class="command" data-options="nofvlab">nofvlabel</code>, <code class="command" data-options="fvwrap(#)">fvwrap(#)</code>, <code class="command" data-options="fvwrapon(style)">fvwrapon(style)</code>, <code class="command" data-options="cformat(%fmt)">cformat(%fmt)</code>, <code class="command" data-options="pformat(%fmt)">pformat(%fmt)</code>, <code class="command" data-options="sformat(%fmt)">sformat(%fmt)</code>, and <code class="command" data-options="nolstretch">nolstretch</code>; see [<strong>[R] estimation options</strong>](estimation%20options##display_options).</td>
</tr>
</tfoot>

</table>

The following option is available with `eivreg` but is not shown in the
dialog box:

`coeflegend`; see
[<strong>[R] estimation options</strong>](estimation%20options##coeflegend).
