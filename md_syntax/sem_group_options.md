## Syntax

`sem paths` ...`,` ... `group_options`

| group\_options |                          | Description                                     |
|----------------|--------------------------|-------------------------------------------------|
|                | `group(varname)`         | fit model for different groups                  |
|                | `ginvariant(pclassname)` | specify parameters that are equal across groups |

<table id="pclassname" class="standard">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><var class="command">pclassname</var></td>
<td>Description <span>{p2line None}_</td>
</tr>
<tr class="even">
<td><code class="command" data-options="scoe">scoef</code></td>
<td>structural coefficients</td>
</tr>
<tr class="odd">
<td><code class="command" data-options="scon">scons</code></td>
<td>structural intercepts</td>
</tr>
<tr class="even">
<td><code class="command" data-options="mcoe">mcoef</code></td>
<td>measurement coefficients</td>
</tr>
<tr class="odd">
<td><code class="command" data-options="mcon">mcons</code></td>
<td>measurement intercepts</td>
</tr>
<tr class="even">
<td><code class="command" data-options="serr">serrvar</code></td>
<td>covariances of structural errors</td>
</tr>
<tr class="odd">
<td><code class="command" data-options="merr">merrvar</code></td>
<td>covariances of measurement errors</td>
</tr>
<tr class="even">
<td><code class="command" data-options="smer">smerrcov</code></td>
<td>covariances between structural and measurement errors</td>
</tr>
<tr class="odd">
<td><code class="command" data-options="mean">meanex</code></td>
<td>means of exogenous variables</td>
</tr>
<tr class="even">
<td><code class="command" data-options="cov">covex</code></td>
<td>covariances of exogenous variables <span>{p2line None}_</td>
</tr>
<tr class="odd">
<td><code class="command" data-options="all">all</code></td>
<td>all the above</td>
</tr>
<tr class="even">
<td><code class="command" data-options="none">none</code></td>
<td>none of the above <span>{p2line None}_
<code class="command">ginvariant(mcoef mcons)</code> is the default if <code class="command" data-options="ginvariant()">ginvariant()</code> is not specified.</td>
</tr>
</tbody>
</table>

`meanex`, `covex`, and `all` exclude the observed exogenous variables
(that is, they include only the latent exogenous variables) unless you
specify the `noxconditional` option or the `noxconditional` option is
otherwise implied; see
[<strong>[SEM] sem option noxconditional</strong>](http://www.stata.com/help.cgi?sem_option_noxconditional).
This is what you would desire in most cases.
