## Syntax

Maximum likelihood optimization

`mle_cmd ...` \[`, options`\]

Set default maximum iterations

`set maxiter #` \[`, permanently`\]

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
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="dif">difficult</code></td>
<td>use a different stepping algorithm in nonconcave regions</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="tech">technique(algorithm_spec)</code></td>
<td>maximization technique</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="iter">iterate(#)</code></td>
<td>perform maximum of <var class="command">#</var> iterations; default is <code class="command">iterate(16000)</code></td>
</tr>
<tr class="even">
<td class="normal"></td>
<td>[<code class="command">no</code>]<code class="command" data-options="lo">log</code></td>
<td>display an iteration log of the log likelihood; typically, the default</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="tr">trace</code></td>
<td>display current parameter vector in iteration log</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="grad">gradient</code></td>
<td>display current gradient vector in iteration log</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="showstep">showstep</code></td>
<td>report steps within an iteration in iteration log</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="hess">hessian</code></td>
<td>display current negative Hessian matrix in iteration log</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command">showtolerance</code></td>
<td>report the calculated result that is compared to the effective convergence criterion</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="tol">tolerance(#)</code></td>
<td>tolerance for the coefficient vector; see <var class="command">Options</var> for the defaults</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="ltol">ltolerance(#)</code></td>
<td>tolerance for the log likelihood; see <var class="command">Options</var> for the defaults</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="nrtol">nrtolerance(#)</code></td>
<td>tolerance for the scaled gradient; see <var class="command">Options</var> for the defaults</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="qtol">qtolerance(#)</code></td>
<td>when specified with algorithms <code class="command">bhhh</code>, <code class="command">dfp</code>, or <code class="command">bfgs</code>, the q-H matrix is used as the final check for convergence rather than <code class="command" data-options="nrtolerance()">nrtolerance()</code> and the H matrix; seldom used</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="nonrtol">nonrtolerance</code></td>
<td>ignore the <code class="command" data-options="nrtolerance()">nrtolerance()</code> option</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="from(init_specs)">from(init_specs)</code></td>
<td>initial values for the coefficients</td>
</tr>
</tbody><tfoot>
<tr class="even footnote">
<td colspan="3">where <var class="command">algorithm_spec</var> is
<var class="command">algorithm</var> [ <var class="command">#</var> [ <var class="command">algorithm</var> [<var class="command">#</var>] ] ... ]
<var class="command">algorithm</var> is <span data-options="-(">{c -(}_<code class="command" data-options="nr">nr</code> <span data-options="|">{c |}_ <code class="command" data-options="bhhh">bhhh</code> <span data-options="|">{c |}_ <code class="command" data-options="dfp">dfp</code> <span data-options="|">{c |}_ <code class="command" data-options="bfgs">bfgs</code><span data-options=")-">{c )-}_
and <var class="command">init_specs</var> is one of
<var class="command">matname</var> [<code class="command">,</code> <code class="command">skip</code> <code class="command">copy</code> ]</td>
</tr>
</tfoot>

</table>

{ \[`eqname:`\]`name = #` \|
`/eqname = #` } \[`...`\]

`#` \[`# ...`\]`, copy`
