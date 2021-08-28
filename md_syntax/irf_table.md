## Syntax

`irf table` \[`stat`\] \[`, options`\]

<table id="stat" class="standard">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><var class="command">stat</var></td>
<td>Description <span>{p2line None}_ <span>{syntab None:Main}_</td>
</tr>
<tr class="even">
<td><code class="command">irf</code></td>
<td>impulse-response function</td>
</tr>
<tr class="odd">
<td><code class="command">oirf</code></td>
<td>orthogonalized impulse-response function</td>
</tr>
<tr class="even">
<td><code class="command">dm</code></td>
<td>dynamic-multiplier function</td>
</tr>
<tr class="odd">
<td><code class="command">cirf</code></td>
<td>cumulative impulse-response function</td>
</tr>
<tr class="even">
<td><code class="command">coirf</code></td>
<td>cumulative orthogonalized impulse-response function</td>
</tr>
<tr class="odd">
<td><code class="command">cdm</code></td>
<td>cumulative dynamic-multiplier function</td>
</tr>
<tr class="even">
<td><code class="command">fevd</code></td>
<td>Cholesky forecast-error variance decomposition</td>
</tr>
<tr class="odd">
<td><code class="command">sirf</code></td>
<td>structural impulse-response function</td>
</tr>
<tr class="even">
<td><code class="command">sfevd</code></td>
<td>structural forecast-error variance decomposition <span>{p2line None}_
If <var class="command">stat</var> is not specified, all statistics are included, unless option <code class="command">nostructural</code> is also specified, in which case <code class="command">sirf</code> and <code class="command">sfevd</code> are excluded. You may specify more than one <var class="command">stat</var>.</td>
</tr>
</tbody>
</table>

| Options |                       | Description                                                     |
|---------|-----------------------|-----------------------------------------------------------------|
| Main    |                       |                                                                 |
|         | `set(filename)`       | make `filename` active                                          |
|         | `irf(irfnames)`       | use `irfnames` IRF result sets                                  |
|         | `impulse(impulsevar)` | use `impulsevar` as impulse variables                           |
|         | `response(endogvars)` | use endogenous variables as response variables                  |
|         | `individual`          | make an individual table for each result set                    |
|         | `title("text")`   | use `text` for overall table title                              |
| Options |                       |                                                                 |
|         | `level(#)`            | set confidence level; default is `level(95)`                    |
|         | `noci`                | suppress confidence intervals                                   |
|         | `stderror`            | include standard errors in the tables                           |
|         | `nostructural`        | suppress `sirf` and `sfevd` from the default list of statistics |
|         | `step(#)`             | use common maximum step horizon `#` for all tables              |
