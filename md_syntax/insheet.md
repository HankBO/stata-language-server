## Syntax

`insheet`
\[[varlist](http://www.stata.com/help.cgi?varlist)\]
`using filename` \[`, options`\]

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
<td>[<code class="command">no</code>]<code class="command" data-options="d">double</code></td>
<td>override default storage type</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="t">tab</code></td>
<td>tab-delimited data</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="c">comma</code></td>
<td>comma-delimited data</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command">delimiter("</code><var class="command">char</var><code class="command">")</code></td>
<td>use <var class="command">char</var> as delimiter</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="clear">clear</code></td>
<td>replace data in memory</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="case">case</code></td>
<td>preserve variable name's case</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td>[<code class="command"></code>
<ul>
</ul>
]<code class="command" data-options="n">names</code></td>
<td>variable names are included on the first line of the file</td>
</tr>
</tbody><tfoot>
<tr class="even footnote">
<td colspan="3">[<code class="command" data-options="no">no</code>]<code class="command" data-options="names">names</code> does not appear in the dialog box</td>
</tr>
</tfoot>

</table>
