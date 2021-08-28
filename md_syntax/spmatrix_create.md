## Syntax

`spmatrix create contiguity spmatname` <span
class="command">\[`if`\] \[`in`\]_ \[`,`
[<var class="command">contoptions</var><strong></strong>](#contoptions)
[<var class="command">stdoptions</var><strong></strong>](#stdoptions)\]

`spmatrix create idistance spmatname` <span
class="command">\[`if`\] \[`in`\]_ \[`,`
[<var class="command">idistoption</var><strong></strong>](#idistoption)
[<var class="command">stdoptions</var><strong></strong>](#stdoptions)\]

`spmatname` is a weighting matrix name.

| contoptions |                       | Description                          |
|-------------|-----------------------|--------------------------------------|
|             | `rook`                | share a border and not just a vertex |
|             | `first`               | first-order neighbors                |
|             | `second`\[`(#)`\] | second-order neighbors               |

<table id="idistoption" class="syntab">
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">idistoption</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="vtrunc">vtruncate(#)</code></td>
<td>set (i,j) element to 0 if 1/distance
<ul>
</ul>
<var class="command">#</var></td>
</tr>
</tbody>
</table>

| stdoptions |                        | Description                                             |
|------------|------------------------|---------------------------------------------------------|
|            | `normalize(normalize)` | type of normalization; default is `normalize(spectral)` |
|            | `replace`              | replace existing weighting matrix                       |
