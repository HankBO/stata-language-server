## Syntax

`axis_title_options` are a subset of `axis_options`; see
[<strong>[G-3]</strong> <em>axis_options</em>](http://www.stata.com/help.cgi?axis_options).
`axis_title_options` control the titling of an axis.

<table class="standard">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><var class="command">axis_title_options</var></td>
<td>Description <span>{p2line None}_</td>
</tr>
<tr class="even">
<td><code class="command">ytitle:(</code><var class="command">axis_title</var><code class="command">)</code></td>
<td>specify <var class="command">y</var> axis title</td>
</tr>
<tr class="odd">
<td><code class="command">xtitle:(</code><var class="command">axis_title</var><code class="command">)</code></td>
<td>specify <var class="command">x</var> axis title</td>
</tr>
<tr class="even">
<td><code class="command">ttitle:(</code><var class="command">axis_title</var><code class="command">)</code></td>
<td>specify <var class="command">t</var> (time) axis title</td>
</tr>
<tr class="odd">
<td><code class="command">ztitle:(</code><var class="command">axis_title</var><code class="command">)</code></td>
<td>specify contour legend axis title <span>{p2line None}_
The above options are <var class="command">merged-explicit</var>; see [<strong>repeated options</strong>](http://www.stata.com/help.cgi?repeated%20options).</td>
</tr>
</tbody>
</table>

where `axis_title` is

`"string"` \[`"string"` \[...\]\] \[`, suboptions`\]

`string` may contain Unicode characters and SMCL tags to render
mathematical symbols, italics, etc.; see
[<strong>[G-4]</strong> <em>text</em>](http://www.stata.com/help.cgi?graph_text).

<table class="standard">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><var class="command">suboptions</var></td>
<td>Description <span>{p2line None}_</td>
</tr>
<tr class="even">
<td><code class="command">axis(</code><var class="command">#</var><code class="command">)</code></td>
<td>which axis, <code class="command">1</code>
<ul>
</ul>
<var class="command">#</var>
<ul>
</ul>
<code class="command">9</code></td>
</tr>
<tr class="odd">
<td><code class="command">prefix</code></td>
<td>combine options</td>
</tr>
<tr class="even">
<td><code class="command">suffix</code></td>
<td>combine options</td>
</tr>
<tr class="odd">
<td><var class="command">textbox_options</var></td>
<td>control details of text appearance; see [<strong>[G-3]</strong> <em>textbox_options</em>](http://www.stata.com/help.cgi?textbox_options) <span>{p2line None}_</td>
</tr>
</tbody>
</table>
