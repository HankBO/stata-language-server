## Syntax

`ivregress estimator`
[depvar](http://www.stata.com/help.cgi?depvar)
\[`varlist1`\] `(varlist2 = varlist_iv)` <span
class="command">\[`if`\] \[`in`\]_ \[`weight`\] \[`, options`\]

`varlist1` is the list of exogenous variables.

`varlist2` is the list of endogenous variables.

`varlist_iv` is the list of exogenous variables used with `varlist1` as
instruments for `varlist2`.

| estimator |        | Description                                   |
|-----------|--------|-----------------------------------------------|
|           | `2sls` | two-stage least squares (2SLS)                |
|           | `liml` | limited-information maximum likelihood (LIML) |
|           | `gmm`  | generalized method of moments (GMM)           |

| Options |              | Description                |
|---------|--------------|----------------------------|
| Model   |              |                            |
|         | `noconstant` | suppress constant term     |
|         | `hascons`    | has user-supplied constant |

<table class="syntab">
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<tbody>
<tr class="odd section">
<td colspan="3" data-options="3 4 4 2"># GMM</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="wmat">wmatrix(wmtype)</code></td>
<td><var class="command">wmtype</var> may be <code class="command" data-options="r">robust</code>, <code class="command" data-options="cl">cluster</code> <var class="command">clustvar</var>, <code class="command" data-options="hac">hac</code> [<var class="command">kernel</var><strong></strong>](#kernel), or <code class="command" data-options="un">unadjusted</code></td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="c">center</code></td>
<td>center moments in weight matrix computation</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="i">igmm</code></td>
<td>use iterative instead of two-step GMM estimator</td>
</tr>
<tr class="odd" style="has_footnote">
<td>*</td>
<td><code class="command" data-options="eps(#)">eps(#)</code></td>
<td>specify # for parameter convergence criterion; default is <code class="command">eps(1e-6)</code></td>
</tr>
<tr class="even" style="has_footnote">
<td>*</td>
<td><code class="command" data-options="weps(#)">weps(#)</code></td>
<td>specify # for weight matrix convergence criterion; default is <code class="command">weps(1e-6)</code></td>
</tr>
<tr class="odd" style="has_footnote">
<td>*</td>
<td><var class="command">optimization_options</var></td>
<td>control the optimization process; seldom used</td>
</tr>
</tbody>
<tbody>
<tr class="odd section">
<td colspan="3">SE/Robust</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="vce(vcetype)">vce(vcetype)</code></td>
<td><var class="command">vcetype</var> may be <code class="command" data-options="un">unadjusted</code>, <code class="command" data-options="r">robust</code>, <code class="command" data-options="cl">cluster</code> <var class="command">clustvar</var>, <code class="command" data-options="boot">bootstrap</code>, <code class="command" data-options="jack">jackknife</code>, or <code class="command" data-options="hac">hac</code> [<var class="command">kernel</var><strong></strong>](#kernel)</td>
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
<td><code class="command" data-options="first">first</code></td>
<td>report first-stage regression</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="small">small</code></td>
<td>make degrees-of-freedom adjustments and report small-sample statistics</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="nohe">noheader</code></td>
<td>display only the coefficient table</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="dep">depname(depname)</code></td>
<td>substitute dependent variable name</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="ef">eform(string)</code></td>
<td>report exponentiated coefficients and use <var class="command">string</var> to label them</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><var class="command">display_options</var></td>
<td>control columns and column formats, row spacing, line width, display of omitted variables and base and empty cells, and factor-variable labeling</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="per">perfect</code></td>
<td>do not check for collinearity between endogenous regressors and excluded instruments</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="coefl">coeflegend</code></td>
<td>display legend instead of statistics</td>
</tr>
</tbody><tfoot>
<tr class="odd footnote">
<td colspan="3"># These options may be specified only when <code class="command">gmm</code> is specified.</td>
</tr>
<tr class="even footnote">
<td colspan="3">* These options may be specified only when <code class="command">igmm</code> is specified.</td>
</tr>
<tr class="odd footnote">
<td colspan="3"><var class="command">varlist1</var>, <var class="command">varlist2</var>, and <var class="command">varlist_iv</var> may contain factor variables; see [<strong>fvvarlist</strong>](http://www.stata.com/help.cgi?fvvarlist).</td>
</tr>
<tr class="even footnote">
<td colspan="3"><var class="command">depvar</var>, <var class="command">varlist1</var>, <var class="command">varlist2</var>, and <var class="command">varlist_iv</var> may contain time-series operators; see [<strong>tsvarlist</strong>](http://www.stata.com/help.cgi?tsvarlist).</td>
</tr>
<tr class="odd footnote">
<td colspan="3"><code class="command">bootstrap</code>, <code class="command">by</code>, <code class="command">fmm</code>, <code class="command">jackknife</code>, <code class="command">rolling</code>, <code class="command">statsby</code>, and <code class="command">svy</code> are allowed; see [<strong>prefix</strong>](http://www.stata.com/help.cgi?prefix). For more details, see [<strong>[FMM]</strong> fmm ivregress](http://www.stata.com/help.cgi?fmm_ivregress).</td>
</tr>
<tr class="even footnote">
<td colspan="3">Weights are not allowed with the [<strong>bootstrap</strong>](http://www.stata.com/help.cgi?bootstrap) prefix.</td>
</tr>
<tr class="odd footnote">
<td colspan="3"><code class="command">aweight</code>s are not allowed with the [<strong>jackknife</strong>](http://www.stata.com/help.cgi?jackknife) prefix.</td>
</tr>
<tr class="even footnote">
<td colspan="3"><code class="command">hascons</code>, <code class="command">vce()</code>, <code class="command">noheader</code>, <code class="command">depname()</code>, and weights are not allowed with the [<strong>svy</strong>](http://www.stata.com/help.cgi?svy) prefix.</td>
</tr>
<tr class="odd footnote">
<td colspan="3"><code class="command">aweight</code>s, <code class="command">fweight</code>s, <code class="command">iweight</code>s, and <code class="command">pweight</code>s are allowed; see [<strong>weight</strong>](http://www.stata.com/help.cgi?weight).</td>
</tr>
<tr class="even footnote">
<td colspan="3"><code class="command" data-options="perfect">perfect</code> and <code class="command" data-options="coeflegend">coeflegend</code> do not appear in the dialog box.</td>
</tr>
<tr class="odd footnote">
<td colspan="3">See [<strong>[R]</strong> ivregress postestimation](http://www.stata.com/help.cgi?ivregress_postestimation) for features available after estimation. <span data-options="menu">{marker menu}_<span>{nobreak None}_ <span>{title None:Menu}_ <span>{phang None}_ <strong>Statistics &gt; Endogenous covariates &gt;</strong> <strong>Linear regression with endogenous covariates</strong> <span data-options="description">{marker description}_<span>{nobreak None}_ <span>{title None:Description}_ <span>{pstd None}_ <code class="command">ivregress</code> fits linear models where one or more of the regressors are endogenously determined. <code class="command">ivregress</code> supports estimation via two-stage least squares (2SLS), limited-information maximum likelihood (LIML), and generalized method of moments (GMM). <span data-options="linkspdf">{marker linkspdf}_<span>{nobreak None}_ <span>{title None:Links to PDF documentation}_ [<strong>[R] estimation options</strong>](http://www.stata.com/manuals14/rivregressquickstart.pdf">Quick start</a> <a href="http://www.stata.com/manuals14/rivregressremarksandexamples.pdf">Remarks and examples</a> <a href="http://www.stata.com/manuals14/rivregressmethodsandformulas.pdf">Methods and formulas</a> <span>{pstd None}_ The above sections are not included in this help file. <span data-options="options">{marker options}_<span>{nobreak None}_ <span>{title None:Options}_ <span>{dlgtab None:Model}_ <span>{phang None}_ <code class="command" data-options="noconstant">noconstant</code>; see <a href="estimation%20options##noconstant). <span>{phang None}_ <code class="command" data-options="hascons">hascons</code> indicates that a user-defined constant or its equivalent is specified among the independent variables. <span>{dlgtab None:GMM}_ <span data-options="wmatrix">{marker wmatrix}_<span>{nobreak None}_ <span>{phang None}_ <code class="command" data-options="wmatrix(wmtype)">wmatrix(wmtype)</code> specifies the type of weighting matrix to be used in conjunction with the GMM estimator. <span>{pmore None}_ Specifying <code class="command">wmatrix(robust)</code> requests a weighting matrix that is optimal when the error term is heteroskedastic. <code class="command">wmatrix(robust)</code> is the default. <span>{pmore None}_ Specifying <code class="command">wmatrix(cluster</code> <var class="command">clustvar</var><code class="command">)</code> requests a weighting matrix that accounts for arbitrary correlation among observations within clusters identified by <var class="command">clustvar</var>. <span data-options="kernel">{marker kernel}_<span>{nobreak None}_ <span>{pmore None}_ Specifying <code class="command">wmatrix(hac</code> <var class="command">kernel</var> <var class="command">#</var><code class="command">)</code> requests a heteroskedasticity- and autocorrelation-consistent (HAC) weighting matrix using the specified kernel (see below) with <var class="command">#</var> lags. The bandwidth of a kernel is equal to <var class="command">#</var> + 1. <span>{pmore None}_ Specifying <code class="command">wmatrix(hac</code> <var class="command">kernel</var> <code class="command">opt</code> [<var class="command">#</var>]<code class="command">)</code> requests an HAC weighting matrix using the specified kernel, and the lag order is selected using Newey and West's ([<strong>1994</strong>](#NW1994)) optimal lag-selection algorithm. <var class="command">#</var> is an optional tuning parameter that affects the lag order selected; see the <a href="http://www.stata.com/manuals14/rivregressmethodsandformulaswmatrixopt.pdf">discussion</a> in <strong>[R] ivregress</strong>. <span>{pmore None}_ Specifying <code class="command">wmatrix(hac</code> <var class="command">kernel</var><code class="command">)</code> requests an HAC weighting matrix using the specified kernel and <var class="command">N</var>-2 lags, where <var class="command">N</var> is the sample size. <span>{pmore None}_ There are three kernels available for HAC weighting matrices, and you may request each one by using the name used by statisticians or the name perhaps more familiar to economists:
<code class="command" data-options="ba">bartlett</code> or <code class="command" data-options="nw">nwest</code> requests the Bartlett (Newey-West) kernel;
<code class="command" data-options="pa">parzen</code> or <code class="command" data-options="ga">gallant</code> requests the Parzen ([<strong>Gallant 1987</strong>](#G1987)) kernel; and
<code class="command" data-options="qu">quadraticspectral</code> or <code class="command" data-options="an">andrews</code> requests the quadratic spectral ([<strong>Andrews 1991</strong>](#A1991)) kernel. <span>{pmore None}_ Specifying <code class="command">wmatrix(unadjusted)</code> requests a weighting matrix that is suitable when the errors are homoskedastic. The GMM estimator with this weighting matrix is equivalent to the 2SLS estimator. <span>{phang None}_ <code class="command" data-options="center">center</code> requests that the sample moments be centered (demeaned) when computing GMM weight matrices. By default, centering is not done. <span>{phang None}_ <code class="command" data-options="igmm">igmm</code> requests that the iterative GMM estimator be used instead of the default two-step GMM estimator. Convergence is declared when the relative change in the parameter vector from one iteration to the next is less than <code class="command">eps()</code> or the relative change in the weight matrix is less than <code class="command">weps()</code>. <span>{phang None}_ <code class="command" data-options="eps(#)">eps(#)</code> specifies the convergence criterion for successive parameter estimates when the iterative GMM estimator is used. The default is <code class="command">eps(1e-6)</code>. Convergence is declared when the relative difference between successive parameter estimates is less than <code class="command">eps()</code> and the relative difference between successive estimates of the weighting matrix is less than <code class="command">weps()</code>. <span>{phang None}_ <code class="command" data-options="weps(#)">weps(#)</code> specifies the convergence criterion for successive estimates of the weighting matrix when the iterative GMM estimator is used. The default is <code class="command">weps(1e-6)</code>. Convergence is declared when the relative difference between successive parameter estimates is less than <code class="command">eps()</code> and the relative difference between successive estimates of the weighting matrix is less than <code class="command">weps()</code>. <span data-options="optimization_options">{marker optimization_options}_<span>{nobreak None}_ <span>{phang None}_ <var class="command">optimization_options</var>: <code class="command">iterate()</code>, [
<ul>
</ul>
]<code class="command" data-options="lo">log</code>. <code class="command">iterate()</code> specifies the maximum number of iterations to perform in conjunction with the iterative GMM estimator. The default is 16,000 or the number set using [<strong>set maxiter</strong>](http://www.stata.com/help.cgi?set%20maxiter). <code class="command" data-options="log">log</code>/<code class="command" data-options="nolog">nolog</code> specifies whether to show the iteration log. These options are seldom used. <span>{dlgtab None:SE/Robust}_ <span>{phang None}_ <code class="command" data-options="vce(vcetype)">vce(vcetype)</code> specifies the type of standard error reported, which includes types that are robust to some kinds of misspecification (<code class="command">robust</code>), that allow for intragroup correlation (<code class="command">cluster</code> <var class="command">clustvar</var>), and that use bootstrap or jackknife methods (<code class="command">bootstrap</code>, <code class="command">jackknife</code>); see [<var class="command">vce_option</var><strong>[R]</strong>](http://www.stata.com/help.cgi?vce_option) .</td>
</tr>
</tfoot>

</table>

`vce(unadjusted)`, the default for `2sls` and `liml`, specifies that an
unadjusted (nonrobust) VCE matrix be used. The default for `gmm` is
based on the `wmtype` specified in the `wmatrix()` option; see
[<var class="command">wmtype</var>)<strong>wmatrix(</strong>](#wmatrix)
above. If `wmatrix()` is specified with `gmm` but `vce()` is not, then
`vcetype` is set equal to `wmtype`. To override this behavior and obtain
an unadjusted (nonrobust) VCE matrix, specify `vce(unadjusted)`.

`ivregress` also allows the following:

`vce(hac kernel` \[`#` \| `opt` \[`#`\]\]`)` specifies that an HAC
covariance matrix be used. The syntax used with
`vce(hac kernel ...)` is identical to that used with
`wmatrix(hac kernel ... )`; see
[<var class="command">wmtype</var>)<strong>wmatrix(</strong>](#wmatrix)
above.

### Reporting

`level(#)`; see
[<strong>[R] estimation options</strong>](estimation%20options##level()).

`first` requests that the first-stage regression results be displayed.

`small` requests that the degrees-of-freedom adjustment `N`/(`N`-`k`) be
made to the variance-covariance matrix of parameters and that
small-sample `F` and `t` statistics be reported, where `N` is the sample
size and `k` is the number of parameters estimated. By default, no
degrees-of-freedom adjustment is made, and Wald and `z` statistics are
reported. Even with this option, no degrees-of-freedom adjustment is
made to the weighting matrix when the GMM estimator is used.

`noheader` suppresses the display of the summary statistics at the top
of the output, displaying only the coefficient table.

`depname(depname)` is used only in programs and ado-files that use
`ivregress` to fit models other than instrumental-variables regression.
`depname()` may be specified only at estimation time. `depname` is
recorded as the identity of the dependent variable, even though the
estimates are calculated using
[depvar](http://www.stata.com/help.cgi?depvar).
This method affects the labeling of the output -- not the results
calculated -- but could affect later calculations made by `predict`,
where the residual would be calculated as deviations from `depname`
rather than `depvar`. `depname()` is most typically used when `depvar`
is a temporary variable (see
[<strong>[P]</strong> macro](http://www.stata.com/help.cgi?macro))
used as a proxy for `depname`.

`eform(string)` is used only in programs and ado-files that use
`ivregress` to fit models other than instrumental-variables regression.
`eform()` specifies that the coefficient table be displayed in
"exponentiated form", as defined in
[<strong>[R] maximize</strong>](http://www.stata.com/help.cgi?maximize),
and that `string` be used to label the exponentiated coefficients in the
table.

`display_options`: `noci`, `nopvalues`, `noomitted`, `vsquish`,
`noemptycells`, `baselevels`, `allbaselevels`, `nofvlabel`, `fvwrap(#)`,
`fvwrapon(style)`, `cformat(%fmt)`, `pformat(%fmt)`, `sformat(%fmt)`,
and `nolstretch`; see
[<strong>[R] estimation options</strong>](estimation%20options##display_options).

The following options are available with `ivregress` but are not shown
in the dialog box:

`perfect` requests that `ivregress` not check for collinearity between
the endogenous regressors and excluded instruments, allowing one to
specify "perfect" instruments. This option cannot be used with the LIML
estimator. This option may be required when using `ivregress` to
implement other estimators.

`coeflegend`; see
[<strong>[R] estimation options</strong>](estimation%20options##coeflegend).
