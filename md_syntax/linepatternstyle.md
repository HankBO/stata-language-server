## Syntax

<table class="standard">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><var class="command">linepatternstyle</var></td>
<td>Description <span>{p2line None}_</td>
</tr>
<tr class="even">
<td><code class="command">solid</code></td>
<td>solid line</td>
</tr>
<tr class="odd">
<td><code class="command">dash</code></td>
<td>dashed line</td>
</tr>
<tr class="even">
<td><code class="command">dot</code></td>
<td>dotted line</td>
</tr>
<tr class="odd">
<td><code class="command">dash_dot</code></td>
<td></td>
</tr>
<tr class="even">
<td><code class="command">shortdash</code></td>
<td></td>
</tr>
<tr class="odd">
<td><code class="command">shortdash_dot</code></td>
<td></td>
</tr>
<tr class="even">
<td><code class="command">longdash</code></td>
<td></td>
</tr>
<tr class="odd">
<td><code class="command">longdash_dot</code></td>
<td></td>
</tr>
<tr class="even">
<td><code class="command">blank</code></td>
<td>invisible line</td>
</tr>
<tr class="odd">
<td><code class="command">"</code><var class="command">formula</var><code class="command">"</code></td>
<td>e.g., <code class="command">"-."</code> or <code class="command">"--.."</code> etc. <span>{p2line None}_
A <var class="command">formula</var> is composed of any combination of</td>
</tr>
<tr class="even">
<td data-options="17 34 36 2"><code class="command">l</code></td>
<td>solid line</td>
</tr>
<tr class="odd">
<td data-options="17 34 36 2"><code class="command">_</code></td>
<td>(underscore) a long dash</td>
</tr>
<tr class="even">
<td data-options="17 34 36 2"><code class="command">-</code></td>
<td>(hyphen) a medium dash</td>
</tr>
<tr class="odd">
<td data-options="17 34 36 2"><code class="command">.</code></td>
<td>short dash (almost a dot)</td>
</tr>
<tr class="even">
<td data-options="17 34 36 2"><code class="command">#</code></td>
<td>small amount of blank space <span>{p2line None}_</td>
</tr>
</tbody>
</table>

For a palette displaying each of the above named line styles, type

`.`**`. palette linepalette`**`,scheme:(schemename)`

Other `linepatternstyles` may be available; type

`. . graph query linepatternstyle`

to obtain the complete list of `linepatternstyles` installed on your
computer.
