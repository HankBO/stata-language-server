## Syntax

`gsem paths` ...`,` ... `group_options`

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
<td><code class="command" data-options="cons">cons</code></td>
<td>intercepts and cutpoints</td>
</tr>
<tr class="odd">
<td><code class="command" data-options="coef">coef</code></td>
<td>fixed coefficients</td>
</tr>
<tr class="even">
<td><code class="command" data-options="load">loading</code></td>
<td>latent variable coefficients</td>
</tr>
<tr class="odd">
<td><code class="command" data-options="errv">errvar</code></td>
<td>covariances of errors</td>
</tr>
<tr class="even">
<td><code class="command" data-options="scale">scale</code></td>
<td>scaling parameters</td>
</tr>
<tr class="odd">
<td><code class="command" data-options="mean">means</code></td>
<td>means of exogenous variables</td>
</tr>
<tr class="even">
<td><code class="command" data-options="cov">covex</code></td>
<td>covariances of exogenous latent variables <span>{p2line None}_</td>
</tr>
<tr class="odd">
<td><code class="command" data-options="all">all</code></td>
<td>all the above</td>
</tr>
<tr class="even">
<td><code class="command" data-options="none">none</code></td>
<td>none of the above <span>{p2line None}_
<code class="command">ginvariant(cons coef loading)</code> is the default if <code class="command" data-options="ginvariant()">ginvariant()</code> is not specified.</td>
</tr>
</tbody>
</table>
