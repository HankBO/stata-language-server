## Syntax

`bayes` \[`, bayesopts`\] `: hetprobit`
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
<td><code class="command" data-options="col">collinear</code></td>
<td>keep collinear variables</td>
</tr>
</tbody>
<tbody>
<tr class="odd section">
<td colspan="3">Reporting</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><var class="command">display_options</var></td>
<td>control spacing, line width, and base and empty cells</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="l">level(#)</code></td>
<td>set credible level; default is <code class="command">level(95)</code></td>
</tr>
</tbody><tfoot>
<tr class="even footnote">
<td colspan="3">* <code class="command" data-options="het()">het()</code> is required. The full specification is<br />
<code class="command">het(</code><var class="command">varlist</var> [<code class="command">,</code> <code class="command" data-options="off">offset(varname_o)</code>]<code class="command">)</code>.</td>
</tr>
<tr class="odd footnote">
<td colspan="3"><var class="command">indepvars</var> and <var class="command">varlist</var> may contain factor variables; see [<strong>fvvarlist</strong>](http://www.stata.com/help.cgi?fvvarlist).</td>
</tr>
<tr class="even footnote">
<td colspan="3"><var class="command">depvar</var> and <var class="command">indepvars</var> may contain time-series operators; see [<strong>tsvarlist</strong>](http://www.stata.com/help.cgi?tsvarlist).</td>
</tr>
<tr class="odd footnote">
<td colspan="3"><code class="command">fweight</code>s are allowed; see [<strong>weight</strong>](http://www.stata.com/help.cgi?weight).</td>
</tr>
<tr class="even footnote">
<td colspan="3"><code class="command">bayes:</code> <code class="command">hetprobit,</code> <code class="command">level()</code> is equivalent to <code class="command">bayes,</code> <code class="command">clevel():</code> <code class="command">hetprobit</code>.</td>
</tr>
<tr class="odd footnote">
<td colspan="3">For a detailed description of <var class="command">options</var>, see [<var class="command">Options</var><strong></strong>](hetprobit##options) in [<strong>[R]</strong> hetprobit](http://www.stata.com/help.cgi?hetprobit).</td>
</tr>
</tfoot>

</table>

bayesopts

Description

[<strong>Priors</strong>](bayes##priors_options)

\*

`normalprior(#)`

specify standard deviation of default normal priors for regression
coefficients; default is `normalprior(100)`

INCLUDE help bayesmh\_prioropts

[<strong>Simulation</strong>](bayes##simulation_options)

INCLUDE help bayesmh\_simopts

[<strong>Blocking</strong>](bayes##blocking_options)

\*

`blocksize(#)`

maximum block size; default is `blocksize(50)`

INCLUDE help bayesmh\_blockopts

|     |              |                                    |
|-----|--------------|------------------------------------|
| \*  | `noblocking` | do not block parameters by default |

[<strong>Initialization</strong>](bayes##initialization_options)

INCLUDE help bayesmh\_initopts

|     |           |                                                                  |
|-----|-----------|------------------------------------------------------------------|
| \*  | `noisily` | display output from the estimation command during initialization |

[<strong>Adaptation</strong>](bayes##adaptation_options)

INCLUDE help bayesmh\_adaptopts

[<strong>Reporting</strong>](bayes##reporting_options)

INCLUDE help bayesecmd\_reportopts

[<strong>Advanced</strong>](bayes##advanced_options)

INCLUDE help bayesmh\_advancedopts

|                                                                                                                                                                                                                                                                                                                                      |     |     |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|-----|
| \* Starred options are specific to the `bayes` prefix; other options are common between `bayes` and [<strong>bayesmh</strong>](http://www.stata.com/help.cgi?bayesmh).                                                                                                                                    |     |     |
| Options `prior()` and `block()` can be repeated.                                                                                                                                                                                                                                                                                     |     |     |
| [<var class="command">priorspec</var><strong></strong>](bayesmh##priorspec) and [<var class="command">paramref</var><strong></strong>](bayesmh##paramref) are defined in [<strong>[BAYES]</strong> bayesmh](http://www.stata.com/help.cgi?bayesmh). |     |     |
| `paramref` may contain factor variables; see [<strong>fvvarlist</strong>](http://www.stata.com/help.cgi?fvvarlist).                                                                                                                                                                                       |     |     |
| See [<strong>[BAYES]</strong> bayesian postestimation](http://www.stata.com/help.cgi?bayesian_postestimation) for features available after estimation.                                                                                                                                                    |     |     |
| Model parameters are regression coefficients `{c -(}depvar:indepvars{c )-}` for the main regression and `{c -(}lnsigma2:varlist{c )-}` for the log-variance equation. Use the `dryrun` option to see the definitions of model parameters prior to estimation.                                                            |     |     |
| For a detailed description of `bayesopts`, see [<var class="command">Options</var><strong></strong>](bayes##options) in [<strong>[BAYES]</strong> bayes](http://www.stata.com/help.cgi?bayes).                                                                                 |     |     |
