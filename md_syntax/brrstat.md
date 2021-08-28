## Syntax

`brrstat`
\[[varlist](http://www.stata.com/help.cgi?varlist)\]
_\[`if`\] \[`in`\]_ \[`, options`\]

`brrstat` \[`namelist`\] \[`using filename`\] <span
class="command">\[`if`\] \[`in`\]_ \[`, options`\]

<table class="standard">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><var class="command">options</var></td>
<td>Description <span>{p2line None}_</td>
</tr>
<tr class="even">
<td><code class="command" data-options="notable">notable</code></td>
<td>suppress table of output</td>
</tr>
<tr class="odd">
<td><code class="command" data-options="noh">noheader</code></td>
<td>suppress table header</td>
</tr>
<tr class="even">
<td><code class="command" data-options="nol">nolegend</code></td>
<td>suppress table legend</td>
</tr>
<tr class="odd">
<td><code class="command" data-options="v">verbose</code></td>
<td>display the full table legend</td>
</tr>
<tr class="even">
<td><code class="command" data-options="l">level(#)</code></td>
<td>confidence level for CIs</td>
</tr>
<tr class="odd">
<td><code class="command" data-options="ti">title(text)</code></td>
<td>title for BRR results</td>
</tr>
<tr class="even">
<td><code class="command" data-options="s">stat(vector)</code></td>
<td>observed values</td>
</tr>
<tr class="odd">
<td><code class="command" data-options="mse">mse</code></td>
<td>use MSE formula for variance estimate <span>{p2line None}_
<code class="command">brrstat</code> shares the features of all estimation commands, except that <code class="command">mfx</code>, <code class="command">adjust</code>, <code class="command">predict</code>, and <code class="command">predictnl</code> are not allowed; see [<strong>estcom</strong>](http://www.stata.com/help.cgi?estcom).</td>
</tr>
</tbody>
</table>
