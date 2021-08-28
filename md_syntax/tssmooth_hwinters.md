## Syntax

`tssmooth hwinters` _\[`type`\] \[_
[newvar](http://www.stata.com/help.cgi?newvar)
`= exp` _\[`if`\] \[`in`\]_ \[`,`
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
<td colspan="3">Main</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command">replace</code></td>
<td>replace [newvar](http://www.stata.com/help.cgi?newvar) if it already exists</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="p">parms(#a #b)</code></td>
<td>use <var class="command">#a</var> and <var class="command">#b</var> as smoothing parameters</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="sa">samp0(#)</code></td>
<td>use <var class="command">#</var> observations to obtain initial values for recursion</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command">s0(</code><var class="command">#</var>cons <var class="command">#</var>lt<code class="command">)</code></td>
<td>use <var class="command">#</var>cons and <var class="command">#</var>lt as initial values for recursion</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="f">forecast(#)</code></td>
<td>use <var class="command">#</var> periods for the out-of-sample forecast</td>
</tr>
</tbody>
<tbody>
<tr class="odd section">
<td colspan="3">Options</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="d">diff</code></td>
<td>alternative initial-value specification; see <var class="command">Options</var></td>
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
<td><code class="command" data-options="fr">from(#a #b)</code></td>
<td>use <var class="command">#a</var> and <var class="command">#b</var> as starting values for the parameters</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command">r(N)</code></td>
<td>number of observations</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command">r(alpha)</code></td>
<td>alpha smoothing parameter</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command">r(beta)</code></td>
<td>beta smoothing parameter</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command">r(rss)</code></td>
<td>sum-of-squared errors</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command">r(prss)</code></td>
<td>penalized sum-of-squared errors, if <code class="command">parms()</code> not specified</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command">r(rmse)</code></td>
<td>root mean squared error</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command">r(N_pre)</code></td>
<td>number of observations used in calculating starting values</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command">r(s2_0)</code></td>
<td>initial value for linear term</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command">r(s1_0)</code></td>
<td>initial value for constant term</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command">r(linear)</code></td>
<td>final value of linear term</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command">r(constant)</code></td>
<td>final value of constant term</td>
</tr>
</tbody><tfoot>
<tr class="odd footnote">
<td colspan="3">You must <code class="command">tsset</code> your data before using <code class="command">tssmooth hwinters</code>; [<strong>[TS] tsset</strong>](http://www.stata.com/help.cgi?tsset).</td>
</tr>
<tr class="even footnote">
<td colspan="3"><var class="command">exp</var> may contain time-series operators; see [<strong>tsvarlist</strong>](http://www.stata.com/help.cgi?tsvarlist). <span data-options="menu">{marker menu}_<span>{nobreak None}_ <span>{title None:Menu}_ <span>{phang None}_ <strong>Statistics &gt; Time series &gt; Smoothers/univariate forecasters &gt;</strong> <strong>Holt-Winters nonseasonal smoothing</strong> <span data-options="description">{marker description}_<span>{nobreak None}_ <span>{title None:Description}_ <span>{pstd None}_ <code class="command">tssmooth hwinters</code> is used in smoothing or forecasting a series that can be modeled as a linear trend in which the intercept and the coefficient on time vary over time. <span data-options="linkspdf">{marker linkspdf}_<span>{nobreak None}_ <span>{title None:Links to PDF documentation}_ [newvar](http://www.stata.com/manuals14/tstssmoothhwintersquickstart.pdf">Quick start</a> <a href="http://www.stata.com/manuals14/tstssmoothhwintersremarksandexamples.pdf">Remarks and examples</a> <a href="http://www.stata.com/manuals14/tstssmoothhwintersmethodsandformulas.pdf">Methods and formulas</a> <span>{pstd None}_ The above sections are not included in this help file. <span data-options="options">{marker options}_<span>{nobreak None}_ <span>{title None:Options}_ <span>{dlgtab None:Main}_ <span>{phang None}_ <code class="command" data-options="replace">replace</code> replaces <a href="http://www.stata.com/help.cgi?newvar) if it already exists. <span>{phang None}_ <code class="command" data-options="parms(#a #b)">parms(#a #b)</code>, <code class="command">0</code>
<ul>
</ul>
<var class="command">#a</var>
<ul>
</ul>
<code class="command">1</code> and <span class="nowrap"><code class="command">0</code> _
<ul>
</ul>
<var class="command">#b</var>
<ul>
</ul>
<code class="command">1</code>, specifies the parameters. If <code class="command" data-options="parms()">parms()</code> is not specified, the values are chosen by an iterative process to minimize the in-sample sum-of-squared prediction errors. <span>{pmore None}_ If you experience difficulty converging (many iterations and "not concave" messages), try using <code class="command" data-options="from()">from()</code> to provide better starting values. <span>{phang None}_ <code class="command" data-options="samp0(#)">samp0(#)</code> and <code class="command">s0(</code><var class="command">#</var>cons <var class="command">#</var>lt<code class="command">)</code> specify how the initial values <var class="command">#</var>cons and <var class="command">#</var>lt for the recursion are obtained. <span>{pmore None}_ By default, initial values are obtained by fitting a linear regression with a time trend using the first half of the observations in the dataset. <span>{pmore None}_ <code class="command" data-options="samp0(#)">samp0(#)</code> specifies that the first <var class="command">#</var> observations be used in that regression. <span>{pmore None}_ <code class="command">s0(</code><var class="command">#</var>cons <var class="command">#</var>lt<code class="command">)</code> specifies that <var class="command">#</var>cons and <var class="command">#</var>lt be used as initial values. <span>{phang None}_ <code class="command" data-options="forecast(#)">forecast(#)</code> specifies the number of periods for the out-of-sample prediction; <span class="nowrap"><code class="command">0</code> _
<ul>
</ul>
<var class="command">#</var>
<ul>
</ul>
<code class="command">500</code>. The default is <code class="command">forecast(0)</code>, which is equivalent to not performing an out-of-sample forecast. <span>{dlgtab None:Options}_ <span>{phang None}_ <span data-options="diff">{marker diff}_<span>{nobreak None}_ <code class="command" data-options="diff">diff</code> specifies that the linear term is obtained by averaging the first difference of <var class="command">exp_t</var> and the intercept is obtained as the difference of <var class="command">exp</var> in the first observation and the mean of <code class="command" data-options="D">D</code>.<var class="command">exp_t</var>. <span>{pmore None}_ If the <code class="command" data-options="diff">diff</code> option is not specified, a linear regression of <var class="command">exp_t</var> on a constant and <var class="command">t</var> is fit. <span>{dlgtab None:Maximization}_ <span>{phang None}_ <span data-options="maximize_options">{marker maximize_options}_<span>{nobreak None}_ <var class="command">maximize_options</var> controls the process for solving for the optimal alpha and beta when <code class="command" data-options="parms()">parms()</code> is not specified. <span>{pmore None}_ <var class="command">maximize_options</var>: <code class="command" data-options="nodif">nodifficult</code>, <code class="command" data-options="tech">technique(algorithm_spec)</code>, <code class="command" data-options="iter">iterate(#)</code>, [<code class="command"></code>
<ul>
</ul>
]<code class="command" data-options="lo">log</code>, <code class="command" data-options="tr">trace</code>, <code class="command" data-options="grad">gradient</code>, <code class="command" data-options="showstep">showstep</code>, <code class="command" data-options="hess">hessian</code>, <code class="command" data-options="showtol">showtolerance</code>, <code class="command" data-options="tol">tolerance(#)</code>, <code class="command" data-options="ltol">ltolerance(#)</code>, <code class="command" data-options="nrtol">nrtolerance(#)</code>, and <code class="command" data-options="nonrtol">nonrtolerance</code>; see [<strong>[R]</strong> maximize](http://www.stata.com/help.cgi?maximize). These options are seldom used. <span>{phang None}_ <code class="command" data-options="from(#a #b)">from(#a #b)</code>, <code class="command">0</code> &lt; <var class="command">#a</var> &lt; <code class="command">1</code> and <code class="command">0</code> &lt; <var class="command">#b</var> &lt; <code class="command">1</code>, specifies starting values from which the optimal values of alpha and beta will be obtained. If <code class="command" data-options="from()">from()</code> is not specified, <code class="command">from(.5 .5)</code> is used. <span data-options="examples">{marker examples}_<span>{nobreak None}_ <span>{title None:Examples}_ <span>{pstd None}_Setup</td>
</tr>
<tr class="odd footnote">
<td colspan="3"><code class="command">. webuse bsales</code> <span>{pstd None}_Perform Holt-Winters nonseasonal smoothing on <code class="command">sales</code></td>
</tr>
<tr class="even footnote">
<td colspan="3"><code class="command">. tssmooth hwinters hw1=sales</code> <span>{pstd None}_Same as above, but use .7 and .3 as smoothing parameters</td>
</tr>
<tr class="odd footnote">
<td colspan="3"><code class="command">. tssmooth hwinters hw2=sales, parms(.7 .3)</code> <span>{pstd None}_Same as above, but perform out-of-sample forecast using 3 periods</td>
</tr>
<tr class="even footnote">
<td colspan="3"><code class="command">. tssmooth hwinters hw3=sales, parms(.7 .3) forecast(3)</code> <span data-options="results">{marker results}_<span>{nobreak None}_ <span>{title None:Stored results}_ <span>{pstd None}_ <code class="command">tssmooth hwinters</code> stores the following in <code class="command">r()</code>: <span data-options="15 tabbed">{synoptset 15 tabbed}_<span>{nobreak None}_ <span data-options="5 15 19 2">{p2col 5 15 19 2: Scalars}_</td>
</tr>
</tfoot>

</table>

|        |               |                                      |
|--------|---------------|--------------------------------------|
| Macros |               |                                      |
|        | `r(method)`   | smoothing method                     |
|        | `r(exp)`      | expression specified                 |
|        | `r(timevar)`  | time variables specified in `tsset`  |
|        | `r(panelvar)` | panel variables specified in `tsset` |
