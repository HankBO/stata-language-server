## Syntax

`sem` ... \[`,` ... `covstructure(variables, structure)` ...\]

`gsem` ... \[`,` ... `covstructure(variables, structure)` ...\]

where `variables` is one of

1\. a list of (a subset of the) exogenous variables (`sem`) or latent
exogenous variable (`gsem`) in your model, for instance,

`. sem ..., ... covstruct(x1 x2, structure)`

`. sem ..., ... covstruct(L1 L2, structure)`

`. gsem ..., ... covstruct(L1 L2, structure)`

2\. `_OEx`, meaning all observed exogenous variables in your model
(`sem` only)

3\. `_LEx`, meaning all latent exogenous variables in your model
(including any multilevel latent exogenous variables in the case of
`gsem`)

4\. `_Ex`, meaning all exogenous variables in your model (`sem` only)

or where `variables` is one of

1\. a list of (a subset of the) error variables in your model, for
example,

`. sem ..., ... covstruct(e.y1 e.y2 e.Aspect, structure)`

2\. `e._OEn`, meaning all error variables associated with observed
endogenous variables in your model

3\. `e._LEn`, meaning all error variables associated with latent
endogenous variables in your model

4\. `e._En`, meaning all error variables in your model

and where `structure` is

<table class="standard">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><var class="command">structure</var></td>
<td>Description <span>{p2line None}_</td>
</tr>
<tr class="even">
<td><code class="command" data-options="diag">diagonal</code></td>
<td>all variances unrestricted</td>
</tr>
<tr class="odd">
<td></td>
<td>all covariances fixed at <code class="command">0</code></td>
</tr>
<tr class="even">
<td><code class="command" data-options="un">unstructured</code></td>
<td>all variances unrestricted</td>
</tr>
<tr class="odd">
<td></td>
<td>all covariances unrestricted</td>
</tr>
<tr class="even">
<td><code class="command" data-options="id">identity</code></td>
<td>all variances equal</td>
</tr>
<tr class="odd">
<td></td>
<td>all covariances fixed at <code class="command">0</code></td>
</tr>
<tr class="even">
<td><code class="command" data-options="ex">exchangeable</code></td>
<td>all variances equal</td>
</tr>
<tr class="odd">
<td></td>
<td>all covariances equal</td>
</tr>
<tr class="even">
<td><code class="command" data-options="zero">zero</code></td>
<td>all variances fixed at <code class="command">0</code></td>
</tr>
<tr class="odd">
<td></td>
<td>all covariances fixed at <code class="command">0</code></td>
</tr>
<tr class="even">
<td>* <code class="command" data-options="pat">pattern(matname)</code></td>
<td>covariances (variances) unrestricted if matname[i,j]
<ul>
</ul>
<code class="command">.</code></td>
</tr>
<tr class="odd">
<td></td>
<td>covariances (variances) equal if matname[i,j] = matname[k,l]</td>
</tr>
<tr class="even">
<td>+ <code class="command" data-options="fix">fixed(matname)</code></td>
<td>covariances (variances) unrestricted if matname[i,j]
<ul>
</ul>
<code class="command">.</code></td>
</tr>
<tr class="odd">
<td></td>
<td>covariances (variances) fixed at matname[i,j] otherwise <span>{p2line None}_
(*) Only elements in the lower triangle of <var class="command">matname</var> are used. All values in <var class="command">matname</var> are interpreted as the [<strong>floor()</strong>](http://www.stata.com/help.cgi?floor()) of the value if noninteger values appear. Row and column stripes of <var class="command">matname</var> are ignored.</td>
</tr>
</tbody>
</table>

(+) Only elements on the lower triangle of `matname` are used. Row and
column stripes of `matname` are ignored.
