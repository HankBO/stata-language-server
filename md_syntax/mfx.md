## Syntax

`mfx` \[`compute`\] _\[`if`\] \[`in`\]_ \[`,`
`options`\]

`mfx replay` \[`, level(#)`\]

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
<td><code class="command" data-options="pred">predict(predict_option)</code></td>
<td>calculate marginal effects (elasticities) for <var class="command">predict_option</var></td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="var">varlist(varlist)</code></td>
<td>calculate marginal effects (elasticities) for <var class="command">varlist</var></td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="dydx">dydx</code></td>
<td>calculate marginal effects; the default</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="eyex">eyex</code></td>
<td>calculate elasticities in the form of d(lny)/d(lnx)</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="dyex">dyex</code></td>
<td>calculate elasticities in the form of d(y)/d(lnx)</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="eydx">eydx</code></td>
<td>calculate elasticities in the form of d(lny)/d(x)</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="nod">nodiscrete</code></td>
<td>treat dummy (indicator) variables as continuous</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="nos">nose</code></td>
<td>do not calculate standard errors</td>
</tr>
</tbody>
<tbody>
<tr class="odd section">
<td colspan="3">Model 2</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command">at(</code><var class="command">atlist</var><code class="command">)</code></td>
<td>calculate marginal effects (elasticities) at these values</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="noe">noesample</code></td>
<td>do not restrict calculation of means and medians to the estimation sample</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="now">nowght</code></td>
<td>ignore weights when calculating means and medians</td>
</tr>
</tbody>
<tbody>
<tr class="odd section">
<td colspan="3">Adv. model</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="nonl">nonlinear</code></td>
<td>do not use the linear method</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="force">force</code></td>
<td>calculate marginal effects and standard errors when it would otherwise refuse to do so</td>
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
<td><code class="command">diagnostics(beta)</code></td>
<td>report suitability of marginal-effect calculation</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command">diagnostics(vce)</code></td>
<td>report suitability of standard-error calculation</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command">diagnostics(all)</code></td>
<td>report all diagnostic information</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="tr">tracelvl(#)</code></td>
<td>report increasing levels of detail during calculations</td>
</tr>
</tbody><tfoot>
<tr class="odd footnote">
<td colspan="3"><span data-options="atlist">{marker atlist}_ where <var class="command">atlist</var> is <var class="command">numlist</var> or <var class="command">matname</var> or <span>{pin2 None}_ [<code class="command">mean</code><span data-options="|">{c |}_<code class="command">median</code><span data-options="|">{c |}_<code class="command">zero</code>] [[varname](http://www.stata.com/help.cgi?varname) <code class="command">=</code> <var class="command">#</var> [<code class="command">,</code> <var class="command">varname</var> <code class="command">=</code> <var class="command">#</var>] [...]] <span>{pin None}_ where <code class="command" data-options="mean">mean</code> is the default. <span>{title None:Menu}_ <span>{phang None}_ <strong>Statistics &gt; Postestimation &gt; Marginal effects or elasticities</strong> <span>{title None:Description}_ <span>{pstd None}_ <code class="command" data-options="mfx">mfx</code> numerically calculates the marginal effects or the elasticities and their standard errors after estimation. Exactly what <code class="command" data-options="mfx">mfx</code> can calculate is determined by the previous estimation command and the <code class="command" data-options="predict(predict_option)">predict(predict_option)</code> option. The values at which the marginal effects or elasticities are to be evaluated is determined by the <code class="command" data-options="at(atlist)">at(atlist)</code> option. By default, <code class="command" data-options="mfx">mfx</code> calculates the marginal effects or elasticities at the means of the independent variables by using the default prediction option associated with the previous estimation command. <span>{pstd None}_ Some disciplines use the term partial effects, rather than marginal effects, for what is computed by <code class="command">mfx</code>. <span>{pstd None}_ <code class="command" data-options="mfx replay">mfx replay</code> replays the results of the previous <code class="command" data-options="mfx">mfx</code> computation. <span>{title None:Options}_ <span>{dlgtab None:Model}_ <span>{phang None}_ <code class="command" data-options="predict(predict_option)">predict(predict_option)</code> specifies the function (that is, the form of y) for which to calculate the marginal effects or elasticities. The default is to use the default <code class="command" data-options="predict">predict</code> option of the preceding estimation command. To see which <code class="command" data-options="predict">predict</code> options are available, see <code class="command" data-options="help">help</code> for the particular estimation command. <span>{phang None}_ <code class="command" data-options="varlist(varlist)">varlist(varlist)</code> specifies the variables for which to calculate marginal effects (elasticities). The default is all variables. <span>{phang None}_<code class="command">dydx</code> specifies that marginal effects be calculated. This is the default. <span>{phang None}_ <code class="command" data-options="eyex">eyex</code> specifies that elasticities be calculated in the form of d(lny)/d(lnx) <span>{phang None}_ <code class="command" data-options="dyex">dyex</code> specifies that elasticities be calculated in the form of d(y)/d(lnx) <span>{phang None}_ <code class="command" data-options="eydx">eydx</code> specifies that elasticities be calculated in the form of d(lny)/d(x) <span>{phang None}_ <code class="command" data-options="nodiscrete">nodiscrete</code> treats dummy variables as continuous. A dummy variable is one that takes on the value 0 or 1 in the estimation sample. If <code class="command" data-options="nodiscrete">nodiscrete</code> is not specified, the marginal effect of a dummy variable is calculated as the discrete change in y as the dummy variable changes from 0 to 1. This option is irrelevant to the computation of the elasticities because all the dummy variables are treated as continuous when computing elasticities. <span>{phang None}_ <code class="command" data-options="nose">nose</code> specifies that standard errors of the marginal effects (elasticities) not be computed. <span>{dlgtab None:Model 2}_ <span>{phang None}_ <code class="command" data-options="at(atlist)">at(atlist)</code> specifies the values at which the marginal effects (elasticities) are to be calculated. The default is to calculate at the means of the independent variables. <span>{pmore None}_ <code class="command" data-options="at(numlist)">at(numlist)</code> specifies that the marginal effects (elasticities) be calculated at <var class="command">numlist</var>. For instance,
<code class="command">. sysuse auto</code></td>
</tr>
<tr class="even footnote">
<td colspan="3"><code class="command">. sureg (price disp weight) (mpg disp weight foreign)</code></td>
</tr>
<tr class="odd footnote">
<td colspan="3"><code class="command">. mfx, predict(xb eq(#2)) at(200 3000 0.5)</code> <span>{pmore None}_ computes the marginal effects for the second equation, setting <code class="command">disp</code>=200, <code class="command">weight</code>=3000, and <code class="command">foreign</code>=0.5. <span>{pmore None}_ The order of the values in the <var class="command">numlist</var> is the same as the variables in the preceding estimation command, from left to right, without repetition. For instance,
<code class="command">. sureg (price disp weight) (mpg foreign disp) </code></td>
</tr>
<tr class="even footnote">
<td colspan="3"><code class="command">. mfx, predict(xb) at(200 3000 0.5)</code> <span>{pmore None}_ <code class="command" data-options="at(matname)">at(matname)</code> specifies the points in a matrix format. The ordering of the variables is the same as that of <var class="command">numlist</var>. For instance,
<code class="command">. probit foreign mpg weight price</code></td>
</tr>
<tr class="odd footnote">
<td colspan="3"><code class="command">. matrix A = (21, 3000, 6000)</code></td>
</tr>
<tr class="even footnote">
<td colspan="3"><code class="command">. mfx, at(A)</code> <span>{pmore None}_ <code class="command">at(</code>[<code class="command" data-options="mean">mean</code> | <code class="command" data-options="median">median</code> | <code class="command" data-options="zero">zero</code>] [<var class="command">varname</var> <code class="command">=</code> <var class="command">#</var> [<code class="command">,</code> <var class="command">varname</var> <code class="command">=</code> <var class="command">#</var> [<var class="command">...</var>]]]<code class="command">)</code> specifies that the marginal effects (elasticities) be calculated at means, at medians of the independent variables, or at zeros. It also allows users to specify particular values for one or more independent variables, assuming that the rest are means, medians, or zeros.
<code class="command">. probit foreign mpg weight price</code></td>
</tr>
<tr class="odd footnote">
<td colspan="3"><code class="command">. mfx, at(mean mpg=30)</code> <span>{pmore None}_ <code class="command">at(</code>[varname](http://www.stata.com/help.cgi?varname) <code class="command">=</code> <var class="command">#</var> [<code class="command">,</code> <var class="command">varname</var> <code class="command">=</code> <var class="command">#</var> ] [...]<code class="command">)</code> specifies that the marginal effects or the elasticities be calculated at particular values for one or more independent variables, assuming that the rest are means.
<code class="command">. probit foreign mpg weight price</code></td>
</tr>
<tr class="even footnote">
<td colspan="3"><code class="command">. mfx, at(mpg=30)</code> <span>{phang None}_ <code class="command" data-options="noesample">noesample</code> affects <code class="command" data-options="at(atlist)">at(atlist)</code>, any offsets used in the preceding estimation, and the determination of dummy variables. It specifies that the whole dataset be considered instead of only those marked in the <code class="command">e(sample)</code> defined by the previous estimation command. <span>{phang None}_ <code class="command" data-options="nowght">nowght</code> affects only <code class="command" data-options="at(atlist)">at(atlist)</code> and offsets. It specifies that weights be ignored when calculating the means or medians for the <var class="command">atlist</var> and when calculating the means for any offsets. <span>{dlgtab None:Adv. model}_ <span>{phang None}_ <code class="command" data-options="nonlinear">nonlinear</code> specifies that y, the function to be calculated for the marginal effects or the elasticities, does not meet the linear-form restriction. By default, <code class="command" data-options="mfx">mfx</code> assumes that y meets the linear-form restriction, unless one or more dependent variables are shared by multiple equations or the previous estimation command was <code class="command">nl</code>. For instance, predictions after <span>{phang3 None}_ <code class="command">. heckman mpg price, sel(foreign=rep78)</code> <span>{pmore None}_ meet the linear-form restriction, but those after <span>{phang3 None}_ <code class="command">. heckman mpg price, sel(foreign=rep78 price)</code> <span>{pmore None}_ do not. If y meets the linear-form restriction, specifying <code class="command" data-options="nonlinear">nonlinear</code> should produce the same results as not specifying it. However, the nonlinear method is generally more time consuming. Most likely, you do not need to specify <code class="command" data-options="nonlinear">nonlinear</code> after an official Stata command. For user-written commands, if you are not sure whether y is of linear form, specifying <code class="command" data-options="nonlinear">nonlinear</code> is a safe choice. <span>{phang None}_ <code class="command" data-options="force">force</code> specifies that marginal effects and their standard errors be calculated when it would otherwise refuse to do so. Such cases arise, for instance, when the marginal effect is a function of a random quantity other than the coefficients of the model (for example, a residual). If you specify this option, there is no guarantee that the resulting marginal effects and standard errors are correct. <span>{dlgtab None:Reporting}_ <span>{phang None}_ <code class="command" data-options="level(#)">level(#)</code> specifies the confidence level, as a percentage, for confidence intervals. The default is <code class="command">level(95)</code> or as set by [<strong>set level</strong>](http://www.stata.com/help.cgi?set%20level). <span>{phang None}_ <code class="command" data-options="diagnostics(diaglist)">diagnostics(diaglist)</code> asks <code class="command" data-options="mfx">mfx</code> to display various diagnostic information. <span>{pmore None}_ <code class="command">diagnostics(beta)</code> shows the information used to determine whether the prediction option is suitable for computing marginal effects. <span>{pmore None}_ <code class="command">diagnostics(vce)</code> shows the information used to determine whether the prediction option is suitable for computing the standard errors of the marginal effects. <span>{pmore None}_ <code class="command">diagnostics(all)</code> shows all the above diagnostic information. <span>{phang None}_ <code class="command" data-options="tracelvl(#)">tracelvl(#)</code> shows increasing levels of detail during calculations. <var class="command">#</var> may be 1, 2, 3, or 4. Level 1 shows the marginal effects and standard errors as they are computed, and which method, either linear or nonlinear, was used. Level 2 shows, in addition, the components of the matrix of partial derivatives needed for each standard error as they are computed. Level 3 shows counts of iterations in obtaining a suitable finite difference for each numerical derivative. Level 4 shows the values of these finite differences. <span>{title None:Using mfx after nl}_ <span>{pstd None}_ You must specify the independent variables by using the <code class="command" data-options="variables()">variables()</code> option when using the interactive version of [<strong>nl</strong>](http://www.stata.com/help.cgi?nl) to obtain marginal effects. Otherwise, <code class="command">mfx</code> has no way of distinguishing the independent variables from the parameters of your model and will therefore exit with an error message. <span>{pstd None}_ Instead of typing <span>{phang2 None}_{cmd:. nl (mpg = <span>{b0 None}_ + <span>{b1 None}_*gear^{b2=1})} <span>{pstd None}_ type <span>{phang2 None}_{cmd:. nl (mpg = <span>{b0 None}_ + <span>{b1 None}_*gear^{b2=1}), variables(gear)} <span>{pstd None}_ If you use the programmed substitutable expression or function evaluator program versions of <code class="command">nl</code>, you do not need to use the <code class="command" data-options="variables()">variables()</code> option. <span>{title None:Examples}_ <span>{phang None}_<code class="command">. sysuse auto</code></td>
</tr>
<tr class="odd footnote">
<td colspan="3"><code class="command">. logit foreign mpg price</code></td>
</tr>
<tr class="even footnote">
<td colspan="3"><code class="command">. mfx, predict(p)</code></td>
</tr>
<tr class="odd footnote">
<td colspan="3"><code class="command">. mfx, predict(p) at(mpg = 20, price = 6000)</code></td>
</tr>
<tr class="even footnote">
<td colspan="3"><code class="command">. mfx, predict(p) at(20 6000)</code></td>
</tr>
</tfoot>

</table>

`. mlogit rep78 mpg displ`

`. mfx, predict(p outcome(2))`

`. mfx, predict(p outcome(2)) at(20 400) `

`. mfx, predict(p outcome(2)) varlist(mpg)`

`. heckman mpg weight length, sel(foreign = length displ)`

`. mfx, predict(xb)`

`. mfx, predict(xbsel)`

`. mfx, predict(yexpected) varlist(length) `

`. regress mpg length weight`

`. mfx, eyex`

`. mfx replay, level(90)`
