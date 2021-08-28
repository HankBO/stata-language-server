## Syntax

Interactive version

`nlsur (depvar_1=`&lt;`sexp_1`&gt;`)`
`(depvar_2=`&lt;`sexp_2`&gt;`)` ... _\[`if`\]
\[`in`\]_ \[`weight`\] \[`, options`\]

Programmed substitutable expression version

`nlsur sexp_prog : depvar_1 depvar_2` ...
\[[varlist](http://www.stata.com/help.cgi?varlist)\]
_\[`if`\] \[`in`\]_ \[`weight`\] \[`,`
`options`\]

Function evaluator program version

`nlsur func_prog @ depvar_1 depvar_2` ...
\[[varlist](http://www.stata.com/help.cgi?varlist)\]
_\[`if`\] \[`in`\]_ \[`weight`\] `,`
`nequations(#)` <span options="-(">{c
-(}_`parameters(namelist)`|`nparameters(#)`} \[`options`\]

where

`depvar_j` is the dependent variable for equation `j`;

`<sexp>_j` is the substitutable expression for equation `j`;

`sexp_prog` is a substitutable expression program; and

`func_prog` is a function evaluator program.

<table id="options_table" class="syntab">
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
<td><code class="command" data-options="fgnls">fgnls</code></td>
<td>use two-step FGNLS estimator; the default</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="ifgnls">ifgnls</code></td>
<td>use iterative FGNLS estimator</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="nls">nls</code></td>
<td>use NLS estimator</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="va">variables(varlist)</code></td>
<td>variables in model</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="in">initial(initial_values)</code></td>
<td>initial values for parameters</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="neq">nequations(#)</code></td>
<td>number of equations in model (function evaluator program version only)</td>
</tr>
<tr class="even" style="has_footnote">
<td>*</td>
<td><code class="command" data-options="param">parameters(namelist)</code></td>
<td>parameters in model (function evaluator program version only)</td>
</tr>
<tr class="odd" style="has_footnote">
<td>*</td>
<td><code class="command" data-options="nparam">nparameters(#)</code></td>
<td>number of parameters in model (function evaluator program version only)</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><var class="command">sexp_options</var></td>
<td>options for substitutable expression program</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><var class="command">func_options</var></td>
<td>options for function evaluator program</td>
</tr>
</tbody>
<tbody>
<tr class="odd section">
<td colspan="3">SE/Robust</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command">vce(</code><var class="command">vcetype</var><code class="command">)</code></td>
<td><var class="command">vcetype</var> may be <code class="command" data-options="gnr">gnr</code>, <code class="command" data-options="r">robust</code>, <code class="command" data-options="cl">cluster</code> <var class="command">clustvar</var>, <code class="command" data-options="boot">bootstrap</code>, or <code class="command" data-options="jack">jackknife</code></td>
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
<td><code class="command" data-options="title">title(string)</code></td>
<td>display <var class="command">string</var> as title above the table of parameter estimates</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="title2">title2(string)</code></td>
<td>display <var class="command">string</var> as subtitle</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><var class="command">display_options</var></td>
<td>control columns and column formats and line width</td>
</tr>
</tbody>
<tbody>
<tr class="odd section">
<td colspan="3">Optimization</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><var class="command">optimization_options</var></td>
<td>control the optimization process; seldom used</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="eps(#)">eps(#)</code></td>
<td>specify <var class="command">#</var> for convergence criteria; default is <code class="command">eps(1e-5)</code></td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="ifgnlsi">ifgnlsiterate(#)</code></td>
<td>set maximum number of FGNLS iterations</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="ifgnlseps(#)">ifgnlseps(#)</code></td>
<td>specify <var class="command">#</var> for FGNLS convergence criterion; default is <code class="command">ifgnlseps(1e-10)</code></td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="del">delta(#)</code></td>
<td>specify stepsize <var class="command">#</var> for computing derivatives; default is <code class="command">delta(4e-7)</code></td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="nocons">noconstants</code></td>
<td>no equations have constant terms</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="h">hasconstants(namelist)</code></td>
<td>use <var class="command">namelist</var> as constant terms</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="coefl">coeflegend</code></td>
<td>display legend instead of statistics</td>
</tr>
</tbody><tfoot>
<tr class="even footnote">
<td colspan="3">* You must specify <code class="command" data-options="parameters(namelist)">parameters(namelist)</code>, <code class="command" data-options="nparameters(#)">nparameters(#)</code>, or both.</td>
</tr>
<tr class="odd footnote">
<td colspan="3"><code class="command">bootstrap</code>, <code class="command">by</code>, <code class="command">jackknife</code>, <code class="command">rolling</code>, and <code class="command">statsby</code> are allowed; see [<strong>prefix</strong>](http://www.stata.com/help.cgi?prefix).</td>
</tr>
<tr class="even footnote">
<td colspan="3">Weights are not allowed with the [<strong>bootstrap</strong>](http://www.stata.com/help.cgi?bootstrap) prefix.</td>
</tr>
<tr class="odd footnote">
<td colspan="3"><code class="command">aweight</code>s are not allowed with the [<strong>jackknife</strong>](http://www.stata.com/help.cgi?jackknife) prefix.</td>
</tr>
<tr class="even footnote">
<td colspan="3"><code class="command">aweight</code>s, <code class="command">fweight</code>s, <code class="command">iweight</code>s, and <code class="command">pweight</code>s are allowed; see [<strong>weight</strong>](http://www.stata.com/help.cgi?weight).</td>
</tr>
<tr class="odd footnote">
<td colspan="3"><code class="command" data-options="coeflegend">coeflegend</code> does not appear in the dialog box.</td>
</tr>
<tr class="even footnote">
<td colspan="3">See [<strong>[R]</strong> nlsur postestimation](http://www.stata.com/help.cgi?nlsur_postestimation) for features available after estimation. <span data-options="menu">{marker menu}_<span>{nobreak None}_ <span>{title None:Menu}_ <span>{phang None}_ <strong>Statistics &gt; Linear models and related &gt; Multiple-equation models &gt;</strong> <strong>Nonlinear seemingly unrelated regression</strong> <span data-options="description">{marker description}_<span>{nobreak None}_ <span>{title None:Description}_ <span>{pstd None}_ <code class="command">nlsur</code> fits a system of nonlinear equations by feasible generalized nonlinear least squares (FGNLS). With the interactive version of the command, you enter the system of equations directly on the command line or in the dialog box by using [<strong>substitutable expressions</strong>](#subexp). If you have a system that you use regularly, you can write a [<strong>substitutable expression program</strong>](#subexppr) and use the second syntax to avoid having to reenter the system every time. The function evaluator program version gives you the most flexibility in exchange for increased complexity; with this version, your program is given a vector of parameters and a variable list, and your program computes the system of equations. <span>{pstd None}_ When you write a substitutable expression program or a function evaluator program, the first five letters of the name must be <code class="command">nlsur</code>. <var class="command">sexp_prog</var> and <var class="command">func_prog</var> refer to the name of the program without the first five letters. For example, if you wrote a function evaluator program named <code class="command">nlsurregss</code>, you would type <code class="command">nlsur regss @ ...</code> to estimate the parameters. <span data-options="linkspdf">{marker linkspdf}_<span>{nobreak None}_ <span>{title None:Links to PDF documentation}_ [<var class="command">sexp_prog</var><strong></strong>](http://www.stata.com/manuals14/rnlsurquickstart.pdf">Quick start</a> <a href="http://www.stata.com/manuals14/rnlsurremarksandexamples.pdf">Remarks and examples</a> <a href="http://www.stata.com/manuals14/rnlsurmethodsandformulas.pdf">Methods and formulas</a> <span>{pstd None}_ The above sections are not included in this help file. <span data-options="options">{marker options}_<span>{nobreak None}_ <span>{title None:Options}_ <span>{dlgtab None:Model}_ <span>{phang None}_ <code class="command" data-options="fgnls">fgnls</code> requests the two-step FGNLS estimator; this is the default. <span>{phang None}_ <code class="command" data-options="ifgnls">ifgnls</code> requests the iterative FGNLS estimator. For the nonlinear systems estimator, this is equivalent to maximum likelihood estimation. <span>{phang None}_ <code class="command" data-options="nls">nls</code> requests the nonlinear least-squares (NLS) estimator. <span>{phang None}_ <code class="command" data-options="variables(varlist)">variables(varlist)</code> specifies the variables in the system. <code class="command" data-options="nlsur">nlsur</code> ignores observations for which any of these variables has missing values. If you do not specify <code class="command" data-options="variables()">variables()</code>, <code class="command">nlsur</code> issues an error message if the estimation sample contains any missing values. <span data-options="initial_values">{marker initial_values}_ <span>{phang None}_ <code class="command" data-options="initial(initial_values)">initial(initial_values)</code> specifies the initial values to begin the estimation. You can specify a 1 x k matrix, where k is the total number of parameters in the system, or you can specify a parameter name, its initial value, another parameter name, its initial value, and so on. For example, to initialize <code class="command" data-options="alpha">alpha</code> to 1.23 and <code class="command" data-options="delta">delta</code> to 4.57, you would type <span>{pmore2 None}_ <code class="command">nlsur ... , initial(alpha 1.23 delta 4.57) ...</code> <span>{pmore None}_ Initial values declared using this option override any that are declared within substitutable expressions. If you specify a matrix, the values must be in the same order in which the parameters are declared in your model. <code class="command">nlsur</code> ignores the row and column names of the matrix. <span>{phang None}_ <code class="command" data-options="nequations(#)">nequations(#)</code> specifies the number of equations in the system. <span>{phang None}_ <code class="command" data-options="parameters(namelist)">parameters(namelist)</code> specifies the names of the parameters in the system. The names of the parameters must adhere to the naming conventions of Stata's variables; see <span data-options="frnames">{findalias frnames}_. If you specify both <code class="command" data-options="parameters()">parameters()</code> and <code class="command" data-options="nparameters()">nparameters()</code>, the number of names in the former must match the number specified in the latter. <span>{phang None}_ <code class="command" data-options="nparameters(#)">nparameters(#)</code> specifies the number of parameters in the system. If you do not specify names with the <code class="command" data-options="parameters()">parameters()</code> option, <code class="command">nlsur</code> names them <code class="command">b1</code>, <code class="command">b2</code>, ..., <code class="command">b</code><var class="command">#</var>. If you specify both <code class="command" data-options="parameters()">parameters()</code> and <code class="command" data-options="nparameters()">nparameters()</code>, the number of names in the former must match the number specified in the latter. <span>{phang None}_ <var class="command">sexp_options</var> refer to any options allowed by your <a href="#subexppr). <span>{phang None}_ <var class="command">func_options</var> refer to any options allowed by your [<var class="command">func_prog</var><strong></strong>](#func_prog). <span data-options="vcetype">{marker vcetype}_<span>{nobreak None}_ <span>{dlgtab None:SE/Robust}_ <span>{phang None}_ <code class="command" data-options="vce(vcetype)">vce(vcetype)</code> specifies the type of standard error reported, which includes types that are derived from asymptotic theory (<code class="command">gnr</code>), that are robust to some kinds of misspecification (<code class="command">robust</code>), that allow for intragroup correlation (<code class="command">cluster</code> <var class="command">clustvar</var>), and that use bootstrap or jackknife methods (<code class="command">bootstrap</code>, <code class="command">jackknife</code>); see [<var class="command">vce_option</var><strong>[R]</strong>](http://www.stata.com/help.cgi?vce_option) . <span>{pmore None}_ <code class="command">vce(gnr)</code>, the default, uses the conventionally derived variance estimator for nonlinear models fit using Gauss-Newton regression. <span>{dlgtab None:Reporting}_ <span>{phang None}_ <code class="command" data-options="level(#)">level(#)</code>; see [<strong>[R] estimation options</strong>](estimation%20options##level()). <span>{phang None}_ <code class="command" data-options="title">title(string)</code> specifies an optional title that will be displayed just above the table of parameter estimates. <span>{phang None}_ <code class="command" data-options="title2">title2(string)</code> specifies an optional subtitle that will be displayed between the title specified in <code class="command" data-options="title()">title()</code> and the table of parameter estimates. If <code class="command" data-options="title2()">title2()</code> is specified but <code class="command" data-options="title()">title()</code> is not, <code class="command" data-options="title2()">title2()</code> has the same effect as <code class="command" data-options="title()">title()</code>. <span data-options="display_options">{marker display_options}_<span>{nobreak None}_ <span>{phang None}_ <var class="command">display_options</var>: <code class="command" data-options="noci">noci</code>, <code class="command" data-options="nopv">nopvalues</code>, <code class="command" data-options="cformat(%fmt)">cformat(%fmt)</code>, <code class="command" data-options="pformat(%fmt)">pformat(%fmt)</code>, <code class="command" data-options="sformat(%fmt)">sformat(%fmt)</code>, and <code class="command" data-options="nolstretch">nolstretch</code>; see [<strong>[R] estimation options</strong>](estimation%20options##display_options). <span data-options="optimization_options">{marker optimization_options}_<span>{nobreak None}_ <span>{dlgtab None:Optimization}_ <span>{phang None}_ <var class="command">optimization_options</var>: <code class="command">iterate(</code><var class="command">#</var><code class="command">)</code>, [
<ul>
</ul>
]<code class="command">log</code>, <code class="command">trace</code>. <code class="command">iterate()</code> specifies the maximum number of iterations to use for NLS at each round of FGNLS estimation. This option is different from <code class="command" data-options="ifgnlsiterate()">ifgnlsiterate()</code>, which controls the maximum rounds of FGNLS estimation to use when the <code class="command" data-options="ifgnls">ifgnls</code> option is specified. <code class="command" data-options="log">log</code>/<code class="command" data-options="nolog">nolog</code> specifies whether to show the iteration log, and <code class="command" data-options="trace">trace</code> specifies that the iteration log should include the current parameter vector. <span>{phang None}_ <code class="command" data-options="eps(#)">eps(#)</code> specifies the convergence criterion for successive parameter estimates and for the residual sum of squares. The default is <code class="command">eps(1e-5)</code> (.00001). <code class="command" data-options="eps()">eps()</code> also specifies the convergence criterion for successive parameter estimates between rounds of iterative FGNLS estimation when <code class="command" data-options="ifgnls">ifgnls</code> is specified. <span>{phang None}_ <code class="command" data-options="ifgnlsiterate(#)">ifgnlsiterate(#)</code> specifies the maximum number of FGNLS iterations to perform. The default is the number set using [<strong>set maxiter</strong>](http://www.stata.com/help.cgi?set%20maxiter), which is 16,000 by default. To use this option, you must also specify the <code class="command" data-options="ifgnls">ifgnls</code> option. <span>{phang None}_ <code class="command" data-options="ifgnlseps(#)">ifgnlseps(#)</code> specifies the convergence criterion for successive estimates of the error covariance matrix during iterative FGNLS estimation. The default is <code class="command">ifgnlseps(1e-10)</code>. To use this option, you must also specify the <code class="command" data-options="ifgnls">ifgnls</code> option. <span>{phang None}_ <code class="command" data-options="delta(#)">delta(#)</code> specifies the relative change in a parameter to be used in computing the numeric derivatives. The derivative for parameter b_i is computed as <span data-options="-(">{c -(}_f_i(x_i,b_1,b_2,...,b_i + d, b_[i+1],...) - f_i(x_i, b_1,b_2,...,b_i, b_[i+1],...)<span data-options=")-">{c )-}_/d, where d is delta*(b_i + delta). The default is <code class="command">delta(4e-7)</code>. <span>{phang None}_ <code class="command" data-options="noconstants">noconstants</code> indicates that none of the equations in the system includes constant terms. This option is generally not needed, even if there are no constant terms in the system; though in rare cases without this option, <code class="command">nlsur</code> may claim that there is one or more constant terms even if there are none. <span>{phang None}_ <code class="command" data-options="hasconstants(namelist)">hasconstants(namelist)</code> indicates the parameters that are to be treated as constant terms in the system of equations. The number of elements of <var class="command">namelist</var> must equal the number of equations in the system. The <var class="command">i</var>th entry of <var class="command">namelist</var> specifies the constant term in the <var class="command">i</var>th equation. If an equation does not include a constant term, specify a period (<code class="command">.</code>) instead of a parameter name. This option is seldom needed with the interactive and programmed substitutable expression versions, because in those cases <code class="command">nlsur</code> can almost always find the constant terms automatically. <span>{pstd None}_ The following option is available with <code class="command">nlsur</code> but is not shown in the dialog box: <span>{phang None}_ <code class="command" data-options="coeflegend">coeflegend</code>; see [<strong>[R] estimation options</strong>](estimation%20options##coeflegend). <span data-options="remarks">{marker remarks}_<span>{nobreak None}_ <span>{title None:Remarks}_ <span>{pstd None}_ Remarks are presented under the following headings: [<strong>Substitutable expressions</strong>](#subexp) [<strong>Examples</strong>](#examples_sexp) [<strong>Substitutable expression programs</strong>](#subexppr) [<strong>Example</strong>](#example_sexp_progs) [<strong>Function evaluator programs</strong>](#func_prog) <span data-options="subexp">{marker subexp}_<span>{nobreak None}_ <span>{title None:Substitutable expressions}_ <span>{pstd None}_ You use substitutable expressions with the interactive and programmed substitutable expression versions of <code class="command">nlsur</code> to define your system of equations. Substitutable expressions are just like any other mathematical expression in Stata, except that the parameters of your model are bound in braces. <span>{pstd None}_ You specify a substitutable expression for each equation in your system, and you must follow three rules: <span>{phang2 None}_ 1. Parameters of the model are bound in braces: <code class="command">{c -(}b0{c )-}</code>, <code class="command">{c -(}param{c )-}</code>, etc. <span>{phang2 None}_ 2. Initial values are given by including an equal sign and the initial value inside the braces: <code class="command">{c -(}b1=1.267{c )-}</code>, <code class="command"> {c -(}gamma=3{c )-}</code>, etc. If you do not specify an initial value, that parameter is initialized to zero. The <code class="command">initial()</code> option overrides initial values provided in substitutable expressions. <span>{phang2 None}_ 3. Linear combinations can be included using the notation <code class="command">{c -(}</code><var class="command">eqname</var><code class="command">:</code><var class="command">varlist</var><code class="command">{c )-}</code>: <span>{pmore3 None}_ <code class="command">{c -(}xb:mpg price weight{c )-}</code> is equivalent to</td>
</tr>
<tr class="odd footnote">
<td colspan="3"><code class="command">{c -(}xb_mpg{c )-}*mpg + </code> <code class="command">{c -(}xb_price{c )-}*price + </code> <code class="command">{c -(}xb_weight{c )-}*weight</code> <span data-options="examples_sexp">{marker examples_sexp}_<span>{nobreak None}_ <span>{title None:Examples}_ <span>{phang2 None}_ 1. To fit the system of equations <span>{pmore3 None}_ y1 = a1 + b1*x^g1 <span>{pmore3 None}_ y2 = a2 + b2*x^g2 <span>{pmore2 None}_ by iterative FGNLS, where a1, a2, b1, b2, g1, and g2 are parameters and 1 is a reasonable starting value for both g1 and g2, you would type <span>{pmore3 None}_ <code class="command">. nlsur (y1 = {c -(}a1{c )-} + {c -(}b1{c )-}*x^{c -(}g1=1{c )-}) (y2 = {c -(}a2{c )-} + {c -(}b2{c )-}*x^{c -(}g2=1{c )-}), ifgnls</code> <span>{phang2 None}_ 2. <code class="command">nlsur</code> makes imposing cross-equation parameter restrictions easy. Say that you want to fit a pair of exponential growth equations with the restriction that the constant terms in the two equations are equal, <span>{pmore3 None}_ y1 = a + b1*b2^x <span>{pmore3 None}_ y2 = a + c1*c2^x <span>{pmore2 None}_ where a, b1, b2, c1, and c2 are the parameters. To fit this model, you would type <span>{pmore3 None}_ <code class="command">. nlsur (y1 = {c -(}a{c )-} + {c -(}b1{c )-}*{c -(}b2{c )-}^x) (y2 = {c -(}a{c )-} + {c -(}c1{c )-}*{c -(}c2{c )-}^x)</code></td>
</tr>
</tfoot>

</table>
