## Syntax

`postrtoe` \[`prefix`\] \[`,` options\]

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
<td colspan="2"><code class="command"></code>
<ul>
</ul>
ro(<var class="command">namelist</var>|<code class="command">_all)</code></td>
<td>post only macros specified in <var class="command">namelist</var> or all macros</td>
</tr>
<tr class="even">
<td colspan="2"><code class="command"></code>
<ul>
</ul>
rix(<var class="command">namelist</var>|<code class="command">_all)</code></td>
<td>post only matrices specified in <var class="command">namelist</var> or all matrices</td>
</tr>
<tr class="odd">
<td colspan="2"><code class="command"></code>
<ul>
</ul>
lar(<var class="command">namelist</var>|<code class="command">_all)</code></td>
<td>post only scalars specified in <var class="command">namelist</var> or all scalars</td>
</tr>
<tr class="even">
<td colspan="2"><code class="command" data-options="nocle">noclear</code></td>
<td>do not clear current <code class="command">e()</code> stored results</td>
</tr>
<tr class="odd">
<td colspan="2"><code class="command" data-options="ren">rename</code></td>
<td>use the names obtained from the specified <var class="command">b</var> matrix as the labels for both the <code class="command">b</code> and <code class="command">V</code> estimation matrices</td>
</tr>
<tr class="even">
<td colspan="2"><code class="command" data-options="res">resize</code></td>
<td>replace <code class="command">e(b)</code>, <code class="command">e(V)</code>, and <code class="command">e(Cns)</code> with their <code class="command">r()</code> equivalents even if <code class="command">e()</code> and <code class="command">r()</code> results are not conformable</td>
</tr>
</tbody>
</table>
