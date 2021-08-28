## Syntax

`gsem paths` ...`,` ... `lclass(lcname #` \[`, base(#)`\]`)`
`lcinvariant(pclassname)`

| lclass\_options |                           | Description                                             |
|-----------------|---------------------------|---------------------------------------------------------|
|                 | `lclass()`                | fit model with latent classes                           |
|                 | `lcinvariant(pclassname)` | specify parameters that are equal across latent classes |

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
<td><code class="command" data-options="errv">errvar</code></td>
<td>covariances of errors</td>
</tr>
<tr class="odd">
<td><code class="command" data-options="scale">scale</code></td>
<td>scaling parameters <span>{p2line None}_</td>
</tr>
<tr class="even">
<td><code class="command" data-options="all">all</code></td>
<td>all the above</td>
</tr>
<tr class="odd">
<td><code class="command" data-options="none">none</code></td>
<td>none of the above <span>{p2line None}_
<code class="command">lcinvariant(errvar scale)</code> is the default if <code class="command" data-options="lcinvariant()">lcinvariant()</code> is not specified.</td>
</tr>
</tbody>
</table>
