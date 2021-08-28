## Syntax

<table class="standard">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><var class="command">added_text_options</var></td>
<td>Description <span>{p2line None}_</td>
</tr>
<tr class="even">
<td><code class="command">text(</code><var class="command">text_arg</var><code class="command">)</code></td>
<td>add text at specified <var class="command">y</var> <var class="command">x</var></td>
</tr>
<tr class="odd">
<td><code class="command">ttext(</code><var class="command">text_arg</var><code class="command">)</code></td>
<td>add text at specified <var class="command">y</var> <var class="command">t</var> <span>{p2line None}_
The above options are <var class="command">merged-implicit</var>; see [<strong>repeated options</strong>](http://www.stata.com/help.cgi?repeated%20options).</td>
</tr>
</tbody>
</table>

where `text_arg` is

`loc_and_textloc_and_text,textoptions`

and where `loc_and_text` is

`#_y#_x"text""text"`

`text` may contain Unicode characters and SMCL tags to render
mathematical symbols, italics, etc.; see
[<strong>[G-4]</strong> <em>text</em>](http://www.stata.com/help.cgi?graph_text).

<table class="standard">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><var class="command">textoptions</var></td>
<td>Description <span>{p2line None}_</td>
</tr>
<tr class="even">
<td><code class="command">yaxis:(</code><var class="command">#</var><code class="command">)</code></td>
<td>how to interpret <var class="command">#_y</var></td>
</tr>
<tr class="odd">
<td><code class="command">xaxis:(</code><var class="command">#</var><code class="command">)</code></td>
<td>how to interpret <var class="command">#_x</var></td>
</tr>
<tr class="even">
<td><code class="command">placement:(</code><var class="command">compassdirstyle</var><code class="command">)</code></td>
<td>where to locate relative to <var class="command">#_y</var> <var class="command">#_x</var></td>
</tr>
<tr class="odd">
<td><var class="command">textbox_options</var></td>
<td>look of text <span>{p2line None}_
<code class="command">placement()</code> is also a textbox option, but ignore the description of <code class="command">placement()</code> found there in favor of the one below.</td>
</tr>
</tbody>
</table>
