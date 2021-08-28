## Syntax

Compute sample size

`power oneproportion p0 pa` \[`, power(numlist) options`\]

Compute power

`power oneproportion p0 pa, n(numlist)` \[`options`\]

Compute effect size and target proportion

`power oneproportion p0, n(numlist) power(numlist)`
\[`options`\]

where `p0` is the null (hypothesized) proportion or the value of the
proportion under the null hypothesis, and `pa` is the alternative
(target) proportion or the value of the proportion under the alternative
hypothesis. `p0` and `pa` may each be specified either as one number or
as a list of values in parentheses (see
[<strong>numlist</strong>](http://www.stata.com/help.cgi?numlist)).

| options                                                                                                                                                                                                                                                                                                                                                   |                                       | Description                                                                                                                                                                                |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                                                                                                                                                                                                                                                                                                           | `test(test)`                          | specify the type of test; default is `test(score)`                                                                                                                                         |
| Main                                                                                                                                                                                                                                                                                                                                                      |                                       |                                                                                                                                                                                            |
| \*                                                                                                                                                                                                                                                                                                                                                        | `alpha(numlist)`                      | significance level; default is `alpha(0.05)`                                                                                                                                               |
| \*                                                                                                                                                                                                                                                                                                                                                        | `power(numlist)`                      | power; default is `power(0.8)`                                                                                                                                                             |
| \*                                                                                                                                                                                                                                                                                                                                                        | `beta(numlist)`                       | probability of type II error; default is `beta(0.2)`                                                                                                                                       |
| \*                                                                                                                                                                                                                                                                                                                                                        | `n(numlist)`                          | sample size; required to compute power or effect size                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                           | `nfractional`                         | allow fractional sample size                                                                                                                                                               |
| \*                                                                                                                                                                                                                                                                                                                                                        | `diff(numlist)`                       | difference between the alternative proportion and the null proportion, `pa`-`p0`; specify instead of the alternative proportion `pa`                                                       |
|                                                                                                                                                                                                                                                                                                                                                           | `critvalues`                          | show critical values for the binomial test                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                           | `continuity`                          | apply continuity correction to the normal approximation of the discrete distribution                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                           | `direction`(`upper`\|`lower`)         | direction of the effect for effect-size determination; default is `direction(upper)`, which means that the postulated value of the parameter is larger than the hypothesized value         |
|                                                                                                                                                                                                                                                                                                                                                           | `onesided`                            | one-sided test; default is two sided                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                           | `parallel`                            | treat number lists in starred options or in command arguments as parallel when multiple values per option or argument are specified (do not enumerate all possible combinations of values) |
| Table                                                                                                                                                                                                                                                                                                                                                     |                                       |                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                           | \[`no`\]`table`\[`(tablespec)`\]  | suppress table or display results as a table; see [<strong>[PSS]</strong> power, table](http://www.stata.com/help.cgi?power_opttable)                           |
|                                                                                                                                                                                                                                                                                                                                                           | `saving(filename`\[`, replace`\]`)` | save the table data to `filename`; use `replace` to overwrite existing `filename`                                                                                                          |
| Graph                                                                                                                                                                                                                                                                                                                                                     |                                       |                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                           | `graph`\[`(graphopts)`\]          | graph results; see [<strong>[PSS]</strong> power, graph](http://www.stata.com/help.cgi?power_optgraph)                                                          |
| Iteration                                                                                                                                                                                                                                                                                                                                                 |                                       |                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                           | `init(#)`                             | initial value for sample size or proportion                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                           | `iterate(#)`                          | maximum number of iterations; default is `iterate(500)`                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                           | `tolerance(#)`                        | parameter tolerance; default is `tolerance(1e-12)`                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                           | `ftolerance(#)`                       | function tolerance; default is `ftolerance(1e-12)`                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                           | \[`no`\]`log`                         | suppress or display iteration log                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                           | \[`no`\]`dots`                        | suppress or display iterations as dots                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                           | `cluster`                             | perform computations for a CRD; see [<strong>[PSS]</strong> power oneproportion, cluster](http://www.stata.com/help.cgi?power_oneproportion_cluster)            |
|                                                                                                                                                                                                                                                                                                                                                           | `notitle`                             | suppress the title                                                                                                                                                                         |
| \* Specifying a list of values in at least two starred options, or at least two command arguments, or at least one starred option and one argument results in computations for all possible combinations of the values; see [<strong>numlist</strong>](http://www.stata.com/help.cgi?numlist). Also see the `parallel` option. |                                       |                                                                                                                                                                                            |
| `cluster` and `notitle` do not appear in the dialog box.                                                                                                                                                                                                                                                                                                  |                                       |                                                                                                                                                                                            |

<table id="testspec" class="syntab">
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">test</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="score">score</code></td>
<td>score test; the default</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="wald">wald</code></td>
<td>Wald test</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="binom">binomial</code></td>
<td>binomial test</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="alpha_a">alpha_a</code></td>
<td>observed significance level</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="power">power</code></td>
<td>power</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="beta">beta</code></td>
<td>type II error probability</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="N">N</code></td>
<td>number of subjects</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="delta">delta</code></td>
<td>effect size</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="p0">p0</code></td>
<td>null proportion</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="pa">pa</code></td>
<td>alternative proportion</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="diff">diff</code></td>
<td>difference between the alternative and null proportions</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="C_l">C_l</code></td>
<td>lower critical value</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="C_u">C_u</code></td>
<td>upper critical value</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="target">target</code></td>
<td>target parameter; synonym for <code class="command">pa</code></td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="_all">_all</code></td>
<td>display all supported columns</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command"> r(alpha)</code></td>
<td>significance level</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command"> r(alpha_a)</code></td>
<td>actual significance level of the binomial method</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command"> r(power)</code></td>
<td>power</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command"> r(beta)</code></td>
<td>probability of a type II error</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command"> r(delta)</code></td>
<td>effect size</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command"> r(N)</code></td>
<td>sample size</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command"> r(nfractional)</code></td>
<td><code class="command">1</code> if <code class="command">nfractional</code> is specified, <code class="command">0</code> otherwise</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command"> r(onesided)</code></td>
<td><code class="command">1</code> for a one-sided test, <code class="command">0</code> otherwise</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command"> r(p0)</code></td>
<td>proportion under the null hypothesis</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command"> r(pa)</code></td>
<td>proportion under the alternative hypothesis</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command"> r(diff)</code></td>
<td>difference between the alternative and null proportions</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command"> r(C_l)</code></td>
<td>lower critical value of the binomial distribution</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command"> r(C_u)</code></td>
<td>upper critical value of the binomial distribution</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command"> r(continuity)</code></td>
<td><strong>1</strong> if continuity correction is used; <strong>0</strong> otherwise</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command">r(separator)</code></td>
<td>number of lines between separator lines in the table</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command">r(divider)</code></td>
<td><code class="command">1</code> if <code class="command">divider</code> is requested in the table, <code class="command">0</code> otherwise</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command"> r(init)</code></td>
<td>initial value for sample size or proportion</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command"> r(maxiter)</code></td>
<td>maximum number of iterations</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command"> r(iter)</code></td>
<td>number of iterations performed</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command"> r(tolerance)</code></td>
<td>requested parameter tolerance</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command"> r(deltax)</code></td>
<td>final parameter tolerance achieved</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command"> r(ftolerance)</code></td>
<td>requested distance of the objective function from zero</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command"> r(function)</code></td>
<td>final distance of the objective function from zero</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command"> r(converged)</code></td>
<td><code class="command">1</code> if iteration algorithm converged, <code class="command">0</code> otherwise</td>
</tr>
</tbody><tfoot>
<tr class="even footnote">
<td colspan="3"><code class="command">test()</code> does not appear in the dialog box. The dialog box selected is determined by the <code class="command">test()</code> specification. <span data-options="tablespec">{marker tablespec}_<span>{nobreak None}_ <span>{pstd None}_ where <var class="command">tablespec</var> is
<var class="command">column</var>[<code class="command">:</code><var class="command">label</var>] [<var class="command">column</var>[<code class="command">:</code><var class="command">label</var>] [...]] [<code class="command">,</code> <var class="command">tableopts</var>] <span>{pstd None}_ <var class="command">column</var> is one of the columns defined below, and <var class="command">label</var> is a column label (may contain quotes and compound quotes). <span data-options="30">{synoptset 30}_<span>{nobreak None}_ <span data-options="column">{marker column}_<span>{nobreak None}_ <span>{synopthdr None:column}_ <span>{synoptline None}_ <span>{synopt None}<code class="command" data-options="alpha">alpha</code>_significance level</td>
</tr>
<tr class="odd footnote">
<td colspan="3">Column <code class="command">beta</code> is shown in the default table in place of column <code class="command">power</code> if specified.</td>
</tr>
<tr class="even footnote">
<td colspan="3">Column <code class="command">diff</code> is shown in the default table if specified.</td>
</tr>
<tr class="odd footnote">
<td colspan="3">Columns <code class="command">alpha_a</code>, <code class="command">C_l</code>, and <code class="command">C_u</code> are available when the <code class="command">test(binomial)</code> option is specified.</td>
</tr>
<tr class="even footnote">
<td colspan="3">Columns <code class="command">C_l</code> and <code class="command">C_u</code> are shown in the default table, if the <code class="command">critvalues</code> option is specified. <span data-options="menu">{marker menu}_<span>{nobreak None}_ <span>{title None:Menu}_ <span>{phang None}_ <strong>Statistics &gt; Power and sample size</strong> <span data-options="description">{marker description}_<span>{nobreak None}_ <span>{title None:Description}_ <span>{pstd None}_ <code class="command">power</code> <code class="command">oneproportion</code> computes sample size, power, or target proportion for a one-sample proportion test. By default, it computes sample size for given power and the values of the proportion parameters under the null and alternative hypotheses. Alternatively, it can compute power for given sample size and values of the null and alternative proportions or the target proportion for given sample size, power, and the null proportion. For power and sample-size analysis in a cluster randomized design, see [<strong>[PSS]</strong> power oneproportion, cluster](http://www.stata.com/help.cgi?power_oneproportion_cluster). Also see [<strong>[PSS]</strong> power](http://www.stata.com/help.cgi?power) for a general introduction to the <code class="command">power</code> command using hypothesis tests. <span data-options="linkspdf">{marker linkspdf}_<span>{nobreak None}_ <span>{title None:Links to PDF documentation}_ [<strong>[PSS]</strong> power](http://www.stata.com/manuals14/psspoweroneproportionquickstart.pdf">Quick start</a> <a href="http://www.stata.com/manuals14/psspoweroneproportionremarksandexamples.pdf">Remarks and examples</a> <a href="http://www.stata.com/manuals14/psspoweroneproportionmethodsandformulas.pdf">Methods and formulas</a> <span>{pstd None}_ The above sections are not included in this help file. <span data-options="options">{marker options}_<span>{nobreak None}_ <span>{title None:Options}_ <span>{phang None}_ <code class="command" data-options="test(test)">test(test)</code> specifies the type of the test for power and sample-size computations. <var class="command">test</var> is one of <code class="command">score</code>, <code class="command">wald</code>, or <code class="command">binomial</code>. <span>{pmore None}_ <code class="command">score</code> requests computations for the score test. This is the default test. <span>{pmore None}_ <code class="command">wald</code> requests computations for the Wald test. This corresponds to computations using the value of the alternative proportion instead of the default null proportion in the formula for the standard error of the estimator of the proportion. <span>{pmore None}_ <code class="command">binomial</code> requests computations for the binomial test. The computation using the binomial distribution is not available for sample-size and effect-size determinations; see <a href="http://www.stata.com/manuals14/psspoweroneproportionremarksandexamplesex7.pdf">example 7</a> for details. Iteration options are not allowed with this test. <span>{dlgtab None:Main}_ <span>{phang None}_ <code class="command">alpha()</code>, <code class="command">power()</code>, <code class="command">beta()</code>, <code class="command">n()</code>, <code class="command">nfractional</code>; see <a href="power##mainopts). The <code class="command" data-options="nfractional">nfractional</code> option is allowed only for sample-size determination. <span>{phang None}_ <code class="command" data-options="diff(numlist)">diff(numlist)</code> specifies the difference between the alternative proportion and the null proportion, <var class="command">pa</var> - <var class="command">p0</var>. You can specify either the alternative proportion <var class="command">pa</var> as a command argument or the difference between the two proportions in <code class="command">diff()</code>. If you specify <code class="command" data-options="diff(#)">diff(#)</code>, the alternative proportion is computed as <var class="command">pa</var> = <var class="command">p0</var> + <var class="command">#</var>. This option is not allowed with the effect-size determination. <span>{phang None}_ <code class="command" data-options="critvalues">critvalues</code> requests that the critical values be reported when the computation is based on the binomial distribution. <span>{phang None}_ <code class="command" data-options="continuity">continuity</code> requests that continuity correction be applied to the normal approximation of the discrete distribution. <code class="command" data-options="continuity">continuity</code> cannot be specified with <code class="command">test(binomial)</code>. <span>{phang None}_ <code class="command">direction()</code>, <code class="command">onesided</code>, <code class="command">parallel</code>; see [<strong>[PSS]</strong> power](power##mainopts). <span>{dlgtab None:Table}_ <span>{phang None}_ <code class="command">table</code>, <code class="command" data-options="table()">table()</code>, <code class="command">notable</code>; see [<strong>[PSS]</strong> power, table](http://www.stata.com/help.cgi?power_opttable). <span>{phang None}_ <code class="command">saving()</code>; see [<strong>[PSS] power</strong>](power##saving()). <span>{dlgtab None:Graph}_ <span>{phang None}_ <code class="command">graph</code>, <code class="command">graph()</code>; see [<strong>[PSS]</strong> power, graph](http://www.stata.com/help.cgi?power_optgraph). Also see the [<strong>[PSS]</strong> power](http://www.stata.com/manuals14/psspoweroneproportionsyntaxcolumn.pdf">column</a> table in <strong>[PSS] power oneproportion</strong> for a list of symbols used by the graphs. <span>{dlgtab None:Iteration}_ <span>{phang None}_ <code class="command" data-options="init(#)">init(#)</code> specifies the initial value of the sample size for the sample-size determination or the initial value of the proportion for the effect-size determination. <span>{phang None}_ <code class="command">iterate()</code>, <code class="command">tolerance()</code>, <code class="command">ftolerance()</code>, <code class="command">log</code>, <code class="command">nolog</code>, <code class="command">dots</code>, <code class="command">nodots</code>; see <a href="power##iteropts). <span>{pstd None}_ The following options are available with <code class="command">power oneproportion</code> but are not shown in the dialog box: <span>{phang None}_ <code class="command" data-options="cluster">cluster</code>; see [<strong>[PSS]</strong> power oneproportion, cluster](http://www.stata.com/help.cgi?power_oneproportion_cluster). <span>{phang None}_ <code class="command">notitle</code>; see [<strong>[PSS]</strong> power](power##reportopts). <span data-options="remarks">{marker remarks}_<span>{nobreak None}_ <span>{title None:Remarks: Using power oneproportion}_ <span>{pstd None}_ <code class="command">power oneproportion</code> computes sample size, power, or target proportion for a one-sample proportion test. All computations are performed for a two-sided hypothesis test where, by default, the significance level is set to 0.05. You may change the significance level by specifying the <code class="command">alpha()</code> option. You can specify the <code class="command">onesided</code> option to request a one-sided test. <span>{pstd None}_ To compute sample size, you must specify the proportions under the null and alternative hypotheses, <var class="command">p0</var> and <var class="command">pa</var>, respectively, and, optionally, the power of the test in the <code class="command">power()</code> option. The default power is set to 0.8. <span>{pstd None}_ To compute power, you must specify the sample size in the <code class="command">n()</code> option and the proportions under the null and alternative hypotheses, <var class="command">p0</var> and <var class="command">pa</var>, respectively. <span>{pstd None}_ Instead of the alternative proportion <var class="command">pa</var>, you may specify the difference <var class="command">pa</var> - <var class="command">p0</var> between the alternative proportion and null proportion in the <code class="command">diff()</code> option when computing sample size or power. <span>{pstd None}_ To compute effect size, the difference between the alternative and null proportions, and target proportion, you must specify the sample size in the <code class="command">n()</code> option, the power in the <code class="command">power()</code> option, the null proportion <var class="command">p0</var>, and, optionally, the direction of the effect. The direction is upper by default, <code class="command">direction(upper)</code>, which means that the target proportion is assumed to be larger than the specified null value. You can change the direction to lower, which means that the target proportion is assumed to be smaller than the specified null value, by specifying the <code class="command">direction(lower)</code> option. <span>{pstd None}_ By default, all computations are based on a large-sample z test of the proportion, which uses a normal distribution as the sampling distribution of the test statistic. For power determination, you can request a small-sample binomial test by specifying the <code class="command">binomial</code> option. The binomial test is not available for the sample-size and effect-size determinations; see [<strong>[PSS]</strong> power](http://www.stata.com/manuals14/psspoweroneproportionremarksandexamplesex7.pdf">example 7</a> for details. <span>{pstd None}_ By default, the computed sample size is rounded up. You can specify the <code class="command">nfractional</code> option to see the corresponding fractional sample size; see <a href="http://www.stata.com/manuals14/pssunbalanceddesignsremarksandexamplesfractionalsamplesizes.pdf">PSS unbalanceddesignsRemarksandexamplesFractionalsamplesizes<var class="command">Fractional sample sizes</var></a> in <strong>[PSS] unbalanced designs</strong> for an example. The <code class="command">nfractional</code> option is allowed only for sample-size determination. <span>{pstd None}_ Some of <code class="command">power oneproportion</code>'s computations require iteration. For example, for a large-sample z test, sample size for a two-sided test is obtained by iteratively solving a nonlinear power equation. The default initial value for the sample size for the iteration procedure is obtained using a closed-form one-sided formula. If desired, it may be changed by specifying the <code class="command">init()</code> option. See <a href="http://www.stata.com/help.cgi?power) for the descriptions of other options that control the iteration procedure. <span data-options="examples">{marker examples}_<span>{nobreak None}_ <span>{title None:Examples}_ <span>{title None:Examples: Computing sample size}_ <span>{pstd None}_ Compute the sample size required to detect a proportion of 0.2 given a proportion of 0.1 under the null hypothesis using a two-sided test; assume a 5% significance level and 80% power (the defaults)</td>
</tr>
<tr class="odd footnote">
<td colspan="3"><code class="command">. power oneproportion 0.1 0.2</code> <span>{pstd None}_ Same as above, using the <code class="command">diff()</code> option to specify the difference in proportions under the null and alternative hypotheses</td>
</tr>
<tr class="even footnote">
<td colspan="3"><code class="command">. power oneproportion 0.1, diff(0.1)</code> <span>{pstd None}_ Same as first example, using a power of 90%</td>
</tr>
<tr class="odd footnote">
<td colspan="3"><code class="command">. power oneproportion 0.1 0.2, power(0.9)</code> <span>{pstd None}_ Same as first example, using a one-sided test and a 1% significance level</td>
</tr>
<tr class="even footnote">
<td colspan="3"><code class="command">. power oneproportion 0.1 0.2, alpha(0.01) onesided</code> <span>{pstd None}_ Compute sample size for a range of alternative proportions and powers, graphing the results</td>
</tr>
<tr class="odd footnote">
<td colspan="3"><code class="command">. power oneproportion 0.1 (0.2(0.1)0.9), power(0.8 0.9) graph</code> <span>{title None:Examples: Computing power}_ <span>{pstd None}_ For a sample of 50 subjects, compute the power of a two-sided test to detect a proportion of 0.2 given a null mean of 0.1; assume a 5% significance level (the default)</td>
</tr>
<tr class="even footnote">
<td colspan="3"><code class="command">. power oneproportion 0.1 0.2, n(50)</code> <span>{pstd None}_ Same as above, assuming a binomial test will be used</td>
</tr>
<tr class="odd footnote">
<td colspan="3"><code class="command">. power oneproportion 0.1 0.2, n(50) test(binomial)</code> <span>{pstd None}_ Compute powers for a range of alternative proportions and sample sizes, graphing the results</td>
</tr>
<tr class="even footnote">
<td colspan="3"><code class="command">. power oneproportion 0.1 (0.2 0.5 0.7 0.9), n(5(1)15) graph</code> <span>{title None:Examples: Computing target proportion}_ <span>{pstd None}_ Compute the minimum value of the proportion exceeding 0.1 that can be detected using a two-sided test in a sample of 50 subjects with 80% power; assume a 5% significance level (the default)</td>
</tr>
<tr class="odd footnote">
<td colspan="3"><code class="command">. power oneproportion 0.1, n(50) power(0.8)</code> <span>{pstd None}_ Same as above</td>
</tr>
<tr class="even footnote">
<td colspan="3"><code class="command">. power oneproportion 0.1, n(50) power(0.8) direction(upper)</code> <span>{pstd None}_ Same as above, using a Wald test rather than the default score test</td>
</tr>
<tr class="odd footnote">
<td colspan="3"><code class="command">. power oneproportion 0.1, n(50) power(0.8) test(wald)</code> <span>{pstd None}_ Compute the maximum proportion less than 0.1 that can be detected</td>
</tr>
<tr class="even footnote">
<td colspan="3"><code class="command">. power oneproportion 0.1, n(50) power(0.8)</code> <code class="command">direction(lower) test(wald)</code> <span data-options="video">{marker video}_<span>{nobreak None}_ <span>{title None:Video examples}_ <span>{phang None}_ [<strong>Sample-size calculation for comparing a sample proportion to a reference value</strong>](https://www.youtube.com/watch?v=SMl0BTSpC3Q&amp;list=UUVk4G4nEtBS4tLOyHqustDA) <span>{phang None}_ [<strong>Power calculation for comparing a sample proportion to a reference value</strong>](https://www.youtube.com/watch?v=178LFlzwJlI&amp;list=UUVk4G4nEtBS4tLOyHqustDA) <span>{phang None}_ [<strong>Minimum detectable effect size for comparing a sample proportion to a reference value using Stata</strong>](https://www.youtube.com/watch?v=i2r-OgXP4gY&amp;list=UUVk4G4nEtBS4tLOyHqustDA) <span data-options="stored_results">{marker stored_results}_<span>{nobreak None}_ <span>{title None:Stored results}_ <span>{pstd None}_ <code class="command">power oneproportion</code> stores the following in <code class="command">r()</code>: <span data-options="20 tabbed">{synoptset 20 tabbed}_<span>{nobreak None}_ <span data-options="5 20 24 2">{p2col 5 20 24 2: Scalars}_</td>
</tr>
</tfoot>

</table>

|        |                |                                |
|--------|----------------|--------------------------------|
| Macros |                |                                |
|        | `r(type)`      | `test`                         |
|        | `r(method)`    | `oneproportion`                |
|        | `r(test)`      | `score`, `wald`, or `binomial` |
|        | `r(direction)` | `upper` or `lower`             |
|        | `r(columns)`   | displayed table columns        |
|        | `r(labels)`    | table column labels            |
|        | `r(widths)`    | table column widths            |
|        | `r(formats)`   | table column formats           |

|          |                |                  |
|----------|----------------|------------------|
| Matrices |                |                  |
|          | `r(pss_table)` | table of results |
