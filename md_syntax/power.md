## Syntax

Compute sample size

`power`
[<var class="command">method</var><strong></strong>](#method)
... \[`, power(numlist)`
[<var class="command">power_options</var><strong></strong>](#power_options)
...\]

Compute power

`power`
[<var class="command">method</var><strong></strong>](#method)
...`, n(numlist)`
\[[<var class="command">power_options</var><strong></strong>](#power_options)
...\]

Compute effect size and target parameter

`power`
[<var class="command">method</var><strong></strong>](#method)
...`, n(numlist) power(numlist)`
\[[<var class="command">power_options</var><strong></strong>](#power_options)
...\]

<table id="method" class="syntab">
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">method</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd section">
<td colspan="3">One sample</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td>[<strong>onemean</strong>](http://www.stata.com/help.cgi?power%20onemean)</td>
<td>One-sample mean test (one-sample t test)</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td>[](http://www.stata.com/help.cgi?power%20oneproportion)
<ul>
</ul>
ortion<strong></strong></td>
<td>One-sample proportion test</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td>[](http://www.stata.com/help.cgi?power%20onecorrelation)
<ul>
</ul>
elation<strong></strong></td>
<td>One-sample correlation test</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td>[](http://www.stata.com/help.cgi?power%20onevariance)
<ul>
</ul>
iance<strong></strong></td>
<td>One-sample variance test</td>
</tr>
</tbody>
<tbody>
<tr class="odd section">
<td colspan="3">Two independent samples</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td>[<strong>twomeans</strong>](http://www.stata.com/help.cgi?power%20twomeans)</td>
<td>Two-sample means test (two-sample t test)</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td>[](http://www.stata.com/help.cgi?power%20twoproportions)
<ul>
</ul>
ortions<strong></strong></td>
<td>Two-sample proportions test</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td>[](http://www.stata.com/help.cgi?power%20twocorrelations)
<ul>
</ul>
elations<strong></strong></td>
<td>Two-sample correlations test</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td>[](http://www.stata.com/help.cgi?power%20twovariances)
<ul>
</ul>
iances<strong></strong></td>
<td>Two-sample variances test</td>
</tr>
</tbody>
<tbody>
<tr class="odd section">
<td colspan="3">Two paired samples</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td>[](http://www.stata.com/help.cgi?power%20pairedmeans)
<ul>
</ul>
eans<strong></strong></td>
<td>Paired-means test (paired t test)</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td>[](http://www.stata.com/help.cgi?power%20pairedproportions)
<ul>
</ul>
oportions<strong></strong></td>
<td>Paired-proportions test (McNemar's test)</td>
</tr>
</tbody>
<tbody>
<tr class="odd section">
<td colspan="3">Analysis of variance</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td>[<strong>oneway</strong>](http://www.stata.com/help.cgi?power%20oneway)</td>
<td>One-way ANOVA</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td>[<strong>twoway</strong>](http://www.stata.com/help.cgi?power%20twoway)</td>
<td>Two-way ANOVA</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td>[<strong>repeated</strong>](http://www.stata.com/help.cgi?power%20repeated)</td>
<td>Repeated-measures ANOVA</td>
</tr>
</tbody>
<tbody>
<tr class="odd section">
<td colspan="3">Linear regression</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td>[<strong>oneslope</strong>](http://www.stata.com/help.cgi?power%20oneslope)</td>
<td>Slope test in a simple linear regression</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td>[](http://www.stata.com/help.cgi?power%20rsquared)
<ul>
</ul>
uared<strong></strong></td>
<td>R^2 test in a multiple linear regression</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td>[<strong>pcorr</strong>](http://www.stata.com/help.cgi?power%20pcorr)</td>
<td>Partial-correlation test in a multiple linear regression</td>
</tr>
</tbody>
<tbody>
<tr class="odd section">
<td colspan="3">Contingency tables</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td>[<strong>cmh</strong>](http://www.stata.com/help.cgi?power%20cmh)</td>
<td>Cochran-Mantel-Haenszel test (stratified 2 x 2 tables)</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td>[<strong>mcc</strong>](http://www.stata.com/help.cgi?power%20mcc)</td>
<td>Matched case-control studies</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td>[<strong>trend</strong>](http://www.stata.com/help.cgi?power%20trend)</td>
<td>Cochran-Armitage trend test (linear trend in J x 2 table)</td>
</tr>
</tbody>
<tbody>
<tr class="odd section">
<td colspan="3">Survival analysis</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td>[<strong>cox</strong>](http://www.stata.com/help.cgi?power%20cox)</td>
<td>Cox proportional hazards model</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td>[](http://www.stata.com/help.cgi?power%20exponential)
<ul>
</ul>
onential<strong></strong></td>
<td>Two-sample exponential test</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td>[](http://www.stata.com/help.cgi?power%20logrank)
<ul>
</ul>
rank<strong></strong></td>
<td>Log-rank test</td>
</tr>
</tbody>
<tbody>
<tr class="odd section">
<td colspan="3">Cluster randomized design (CRD)</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td>[<strong>onemean, cluster</strong>](http://www.stata.com/help.cgi?power%20onemean%20cluster)</td>
<td>One-sample mean test in a CRD</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td>[](http://www.stata.com/help.cgi?power%20oneproportion%20cluster)
<ul>
</ul>
ortion, cluster<strong></strong></td>
<td>One-sample proportion test in a CRD</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td>[<strong>twomeans, cluster</strong>](http://www.stata.com/help.cgi?power%20twomeans%20cluster)</td>
<td>Two-sample means test in a CRD</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td>[](http://www.stata.com/help.cgi?power%20twoproportions%20cluster)
<ul>
</ul>
ortions, cluster<strong></strong></td>
<td>Two-sample proportions test in a CRD</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td>[](http://www.stata.com/help.cgi?power%20logrank%20cluster)
<ul>
</ul>
rank, cluster<strong></strong></td>
<td>Log-rank test in a CRD</td>
</tr>
</tbody>
<tbody>
<tr class="odd section">
<td colspan="3">User-define methods</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td>[<var class="command">usermethod</var><strong></strong>](http://www.stata.com/help.cgi?power%20usermethod)</td>
<td>Add your own method to <code class="command">power</code></td>
</tr>
</tbody>
</table>

power\_options

Description

Main

INCLUDE help pss\_testmainopts1.ihlp

<table class="syntab">
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<tbody>
<tr class="odd" style="has_footnote">
<td>*</td>
<td><code class="command" data-options="n1(numlist)">n1(numlist)</code></td>
<td>sample size of the control group</td>
</tr>
<tr class="even" style="has_footnote">
<td>*</td>
<td><code class="command" data-options="n2(numlist)">n2(numlist)</code></td>
<td>sample size of the experimental group</td>
</tr>
<tr class="odd" style="has_footnote">
<td>*</td>
<td><code class="command" data-options="nrat">nratio(numlist)</code></td>
<td>ratio of sample sizes, <code class="command">N2/N1</code>; default is <code class="command">nratio(1)</code>, meaning equal group sizes</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command">compute(N1</code>|<code class="command">N2)</code></td>
<td>solve for <code class="command">N1</code> given <code class="command">N2</code> or for <code class="command">N2</code> given <code class="command">N1</code></td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="nfrac">nfractional</code></td>
<td>allow fractional sample size</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="dir">direction</code>(<code class="command" data-options="u">upper</code>|<code class="command" data-options="l">lower</code>)</td>
<td>direction of the effect for effect-size determination; default is <code class="command">direction(upper)</code>, which means that the postulated value of the parameter is larger than the hypothesized value</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="onesid">onesided</code></td>
<td>one-sided test; default is two sided</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="par">parallel</code></td>
<td>treat number lists in starred options or in command arguments as parallel when multiple values per option or argument are specified (do not enumerate all possible combinations of values)</td>
</tr>
</tbody>
<tbody>
<tr class="odd section">
<td colspan="3">Table</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td>[<code class="command"></code>
<ul>
</ul>
]<code class="command">table</code>[<code class="command">(</code><var class="command">tablespec</var><code class="command">)</code>]</td>
<td>suppress table or display results as a table; see [<strong>[PSS] power, table</strong>](http://www.stata.com/help.cgi?power%20table)</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command">saving(</code><var class="command">filename</var> [<code class="command">,</code> <code class="command">replace</code>]<code class="command">)</code></td>
<td>save the table data to <var class="command">filename</var>; use <code class="command">replace</code> to overwrite existing <var class="command">filename</var></td>
</tr>
</tbody>
<tbody>
<tr class="odd section">
<td colspan="3">Graph</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command">graph</code>[<code class="command">(</code>[<var class="command">graphopts</var><strong></strong>](power_optgraph##graphopts)<code class="command">)</code>]</td>
<td>graph results; see [<strong>[PSS] power, graph</strong>](http://www.stata.com/help.cgi?power_optgraph)</td>
</tr>
</tbody>
</table>

|                                                                                                                                                                                                                                                                                                                                                           |                 |                                                                      |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------|----------------------------------------------------------------------|
| Iteration                                                                                                                                                                                                                                                                                                                                                 |                 |                                                                      |
|                                                                                                                                                                                                                                                                                                                                                           | `init(#)`       | initial value of the estimated parameter; default is method specific |
|                                                                                                                                                                                                                                                                                                                                                           | `iterate(#)`    | maximum number of iterations; default is `iterate(500)`              |
|                                                                                                                                                                                                                                                                                                                                                           | `tolerance(#)`  | parameter tolerance; default is `tolerance(1e-12)`                   |
|                                                                                                                                                                                                                                                                                                                                                           | `ftolerance(#)` | function tolerance; default is `ftolerance(1e-12)`                   |
|                                                                                                                                                                                                                                                                                                                                                           | \[`no`\]`log`   | suppress or display iteration log                                    |
|                                                                                                                                                                                                                                                                                                                                                           | \[`no`\]`dots`  | suppress or display iterations as dots                               |
|                                                                                                                                                                                                                                                                                                                                                           | `notitle`       | suppress the title                                                   |
| \* Specifying a list of values in at least two starred options, or at least two command arguments, or at least one starred option and one argument results in computations for all possible combinations of the values; see [<strong>numlist</strong>](http://www.stata.com/help.cgi?numlist). Also see the `parallel` option. |                 |                                                                      |
| Options `n1()`, `n2()`, `nratio()`, and `compute()` are available only for two-independent-samples methods.                                                                                                                                                                                                                                               |                 |                                                                      |
| Iteration options are available only with computations requiring iteration.                                                                                                                                                                                                                                                                               |                 |                                                                      |
| `notitle` does not appear in the dialog box.                                                                                                                                                                                                                                                                                                              |                 |                                                                      |
