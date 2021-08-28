## Syntax

`tssmooth dexponential` _\[`type`\] \[_
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
<td><code class="command" data-options="replace">replace</code></td>
<td>replace [newvar](http://www.stata.com/help.cgi?newvar) if it already exists</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="p">parms(#a)</code></td>
<td>use <var class="command">#a</var> as smoothing parameter</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="sa">samp0(#)</code></td>
<td>use <var class="command">#</var> observations to obtain initial values for recursion</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="s0(#1 #2)">s0(#1 #2)</code></td>
<td>use <var class="command">#1</var> and <var class="command">#2</var> as initial values for recursions</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="f">forecast(#)</code></td>
<td>use <var class="command">#</var> periods for the out-of-sample forecast</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command">r(N)</code></td>
<td>number of observations</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command">r(alpha)</code></td>
<td>alpha smoothing parameter</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command">r(rss)</code></td>
<td>sum-of-squared errors</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command">r(rmse)</code></td>
<td>root mean squared error</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command">r(N_pre)</code></td>
<td>number of observations used in calculating starting values, if starting values calculated</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command">r(s2_0)</code></td>
<td>initial value for linear term, i.e., S_0^[2]</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command">r(s1_0)</code></td>
<td>initial value for constant term, i.e., S_0</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command">r(linear)</code></td>
<td>final value of linear term</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command">r(constant)</code></td>
<td>final value of constant term</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command">r(period)</code></td>
<td>period, if filter is seasonal</td>
</tr>
</tbody><tfoot>
<tr class="odd footnote">
<td colspan="3">You must <code class="command">tsset</code> your data before using <code class="command">tssmooth dexponential</code>; see [<strong>[TS] tsset</strong>](http://www.stata.com/help.cgi?tsset).</td>
</tr>
<tr class="even footnote">
<td colspan="3"><var class="command">exp</var> may contain time-series operators; see [<strong>tsvarlist</strong>](http://www.stata.com/help.cgi?tsvarlist). <span data-options="menu">{marker menu}_<span>{nobreak None}_ <span>{title None:Menu}_ <span>{phang None}_ <strong>Statistics &gt; Time series &gt; Smoothers/univariate forecasters &gt;</strong> <strong>Double-exponential smoothing</strong> <span data-options="description">{marker description}_<span>{nobreak None}_ <span>{title None:Description}_ <span>{pstd None}_ <code class="command">tssmooth dexponential</code> models the trend of a variable whose difference between changes from the previous values is serially correlated. More precisely, it models a variable whose second difference follows a low-order, moving-average process. <span data-options="linkspdf">{marker linkspdf}_<span>{nobreak None}_ <span>{title None:Links to PDF documentation}_ [newvar](http://www.stata.com/manuals14/tstssmoothdexponentialquickstart.pdf">Quick start</a> <a href="http://www.stata.com/manuals14/tstssmoothdexponentialremarksandexamples.pdf">Remarks and examples</a> <a href="http://www.stata.com/manuals14/tstssmoothdexponentialmethodsandformulas.pdf">Methods and formulas</a> <span>{pstd None}_ The above sections are not included in this help file. <span data-options="options">{marker options}_<span>{nobreak None}_ <span>{title None:Options}_ <span>{dlgtab None:Main}_ <span>{phang None}_ <code class="command" data-options="replace">replace</code> replaces <a href="http://www.stata.com/help.cgi?newvar) if it already exists. <span>{phang None}_ <code class="command" data-options="parms(#a)">parms(#a)</code> specifies the parameter alpha for the double-exponential smoothers; <span class="nowrap"><code class="command">0</code> &lt; <var class="command">#a</var> &lt; <code class="command">1</code>_. If <code class="command" data-options="parms(#a)">parms(#a)</code> is not specified, the smoothing parameter is chosen to minimize the in-sample sum-of-squared forecast errors. <span>{phang None}_ <code class="command" data-options="samp0(#)">samp0(#)</code> and <code class="command" data-options="s0(#1 #2)">s0(#1 #2)</code> are mutually exclusive ways of specifying the initial values for the recursion. <span>{pmore None}_ By default, initial values are obtained by fitting a linear regression with a time trend, using the first half of the observations in the dataset; see <a href="http://www.stata.com/manuals14/tstssmoothdexponentialremarksandexamples.pdf">TS tssmoothdexponentialRemarksandexamples<var class="command">Remarks and examples</var></a> in <strong>[TS] tssmooth dexponential</strong>. <span>{pmore None}_ <code class="command" data-options="samp0(#)">samp0(#)</code> specifies that the first <var class="command">#</var> be used in that regression. <span>{pmore None}_ <code class="command" data-options="s0(#1 #2)">s0(#1 #2)</code> specifies that <var class="command">#1</var> <var class="command">#2</var> be used as initial values. <span>{phang None}_ <code class="command" data-options="forecast(#)">forecast(#)</code> specifies the number of periods for the out-of-sample prediction; <span class="nowrap"><code class="command">0</code> _
<ul>
</ul>
<var class="command">#</var>
<ul>
</ul>
<code class="command">500</code>. The default is <code class="command">forecast(0)</code>, which is equivalent to not performing an out-of-sample forecast. <span data-options="examples">{marker examples}_<span>{nobreak None}_ <span>{title None:Examples}_ <span>{pstd None}_Setup</td>
</tr>
<tr class="odd footnote">
<td colspan="3"><code class="command">. webuse sales2</code> <span>{pstd None}_Perform double-exponential smoothing on <code class="command">sales</code></td>
</tr>
<tr class="even footnote">
<td colspan="3"><code class="command">. tssmooth dexponential double sm2a=sales</code> <span>{pstd None}_Same as above, but use .7 as smoothing parameter</td>
</tr>
<tr class="odd footnote">
<td colspan="3"><code class="command">. tssmooth dexponential double sm2b=sales, p(.7)</code> <span>{pstd None}_Same as above, but use 1031 and 1031 as initial values for recursions</td>
</tr>
<tr class="even footnote">
<td colspan="3"><code class="command">. tssmooth dexponential double sm2c=sales, p(.7) s0(1031 1031)</code> <span>{pstd None}_Same as above, but perform out-of-sample forecast using 4 periods</td>
</tr>
<tr class="odd footnote">
<td colspan="3"><code class="command">. tssmooth dexponential double sm2d=sales, p(.7) s0(1031 1031)</code> <code class="command">forecast(4)</code> <span data-options="results">{marker results}_<span>{nobreak None}_ <span>{title None:Stored results}_ <span>{pstd None}_ <code class="command">tssmooth dexponential</code> stores the following in <code class="command">r()</code>: <span data-options="15 tabbed">{synoptset 15 tabbed}_<span>{nobreak None}_ <span data-options="5 15 19 2">{p2col 5 15 19 2: Scalars}_</td>
</tr>
</tfoot>

</table>

|        |               |                                     |
|--------|---------------|-------------------------------------|
| Macros |               |                                     |
|        | `r(method)`   | smoothing method                    |
|        | `r(exp)`      | expression specified                |
|        | `r(timevar)`  | time variable specified in `tsset`  |
|        | `r(panelvar)` | panel variable specified in `tsset` |
