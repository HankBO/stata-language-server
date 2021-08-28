## Syntax

`diflogistic`
[varlist](http://www.stata.com/help.cgi?varlist)
_\[`if`\] \[`in`\]_
\[[<var class="command">weight</var><strong></strong>](#weight)\]`,`
`group(varname)` \[`options`\]

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
<tr class="odd section">
<td colspan="3">Main</td>
</tr>
<tr class="even" style="has_footnote">
<td>*</td>
<td><code class="command" data-options="gr">group(varname)</code></td>
<td>specify variable that identifies groups</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="total(varname)">total(varname)</code></td>
<td>specify total score variable</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="items">items(varlist_i)</code></td>
<td>calculate logistic regression test for items in <var class="command">varlist_i</var> only</td>
</tr>
</tbody>
<tbody>
<tr class="odd section">
<td colspan="3">Reporting</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="maxp(#)">maxp(#)</code></td>
<td>display only items with <span class="nowrap">p-value _
<ul>
</ul>
<var class="command">#</var></td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="sf">sformat(%fmt)</code></td>
<td>display format for chi-squared values; default is <code class="command">sformat(%9.2f)</code></td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="pf">pformat(%fmt)</code></td>
<td>display format for p-values; default is <code class="command">pformat(%9.4f)</code></td>
</tr>
</tbody><tfoot>
<tr class="odd footnote">
<td colspan="3">* <code class="command" data-options="group()">group()</code> is required.</td>
</tr>
<tr class="even footnote">
<td colspan="3"><code class="command" data-options="fweight">fweight</code>s are allowed; see [<strong>weight</strong>](http://www.stata.com/help.cgi?weight). <span data-options="menu_irt">{marker menu_irt}_<span>{nobreak None}_ <span>{title None:Menu}_ <span>{phang None}_ <strong>Statistics &gt; IRT (item response theory)</strong></td>
</tr>
</tfoot>

</table>
