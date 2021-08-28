## Syntax

<table class="standard">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><var class="command">title_options</var></td>
<td>Description <span>{p2line None}_</td>
</tr>
<tr class="even">
<td><code class="command">title:(</code><var class="command">tinfo</var><code class="command">)</code></td>
<td>overall title</td>
</tr>
<tr class="odd">
<td><code class="command">subtitle:(</code><var class="command">tinfo</var><code class="command">)</code></td>
<td>subtitle of title</td>
</tr>
<tr class="even">
<td><code class="command">note(</code><var class="command">tinfo</var><code class="command">)</code></td>
<td>note about graph</td>
</tr>
<tr class="odd">
<td><code class="command">caption:(</code><var class="command">tinfo</var><code class="command">)</code></td>
<td>explanation of graph</td>
</tr>
<tr class="even">
<td><code class="command">t1title:(</code><var class="command">tinfo</var><code class="command">)</code><span data-options="2">{space 2}_<code class="command">t2title:(</code><var class="command">tinfo</var><code class="command">)</code></td>
<td>rarely used</td>
</tr>
<tr class="odd">
<td><code class="command">b1title:(</code><var class="command">tinfo</var><code class="command">)</code><span data-options="2">{space 2}_<code class="command">b2title:(</code><var class="command">tinfo</var><code class="command">)</code></td>
<td>rarely used</td>
</tr>
<tr class="even">
<td><code class="command">l1title:(</code><var class="command">tinfo</var><code class="command">)</code><span data-options="2">{space 2}_<code class="command">l2title:(</code><var class="command">tinfo</var><code class="command">)</code></td>
<td>vertical text</td>
</tr>
<tr class="odd">
<td><code class="command">r1title:(</code><var class="command">tinfo</var><code class="command">)</code><span data-options="2">{space 2}_<code class="command">r2title:(</code><var class="command">tinfo</var><code class="command">)</code></td>
<td>vertical text <span>{p2line None}_
The above options are <var class="command">merged-explicit</var>; see [<strong>repeated options</strong>](http://www.stata.com/help.cgi?repeated%20options).<br />
<span data-options="-(">{c -(}_<code class="command">t</code>|<code class="command">b</code>|<code class="command">l</code>|<code class="command">r</code><span data-options=")-">{c )-}_<span data-options="-(">{c -(}_<code class="command">1</code>|<code class="command">2</code><span data-options=")-">{c )-}_<code class="command">title()</code> are allowed with <code class="command">graph</code> <code class="command">twoway</code> only.</td>
</tr>
</tbody>
</table>

where `tinfo` is

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
<td><code class="command">prefix</code> and <code class="command">suffix</code></td>
<td>add to title text</td>
</tr>
<tr class="odd">
<td><code class="command">position:(</code><var class="command">clockposstyle</var><code class="command">)</code></td>
<td>position of title -- side</td>
</tr>
<tr class="even">
<td><code class="command">ring(</code><var class="command">ringposstyle</var><code class="command">)</code></td>
<td>position of title -- distance</td>
</tr>
<tr class="odd">
<td><code class="command">span</code></td>
<td>"centering" of title</td>
</tr>
<tr class="even">
<td><var class="command">textbox_options</var></td>
<td>rendition of title <span>{p2line None}_
Option <code class="command">position()</code> is not allowed with <span data-options="-(">{c -(}_<code class="command">t</code>|<code class="command">b</code>|<code class="command">l</code>|<code class="command">r</code><span data-options=")-">{c )-}_<span data-options="-(">{c -(}_<code class="command">1</code>|<code class="command">2</code><span data-options=")-">{c )-}_<code class="command">title()</code>.</td>
</tr>
</tbody>
</table>

Examples include

`title("My graph")` note(`"includes both "high" and "low" priced items"') `title("First line" "Second line")title("Third line", suffix)title("Fourth line" "Fifth line", suffix)`

The definition of `ringposstyle` and the default positioning of titles
is

||`ringposstyle`

------------------------------------------------------------------------

<span options="+">{c +}_

------------------------------------------------------------------------

<span options="TLC">{c TLC}_

------------------------------------------------------------------------

<span options="TRC">{c TRC}_|<span
options="|">{c \|}_|<span
options="|">{c \|}_|<span
options="|">{c \|}_|<span
options="|">{c \|}_|<span
options="|">{c \|}_|<span
options="|">{c \|}_|<span
options="|">{c \|}_<span options="TLC">{c TLC}_

------------------------------------------------------------------------

<span options="TRC">{c TRC}_|<span
options="|">{c \|}_|<span
options="|">{c \|}_|<span
options="|">{c \|}_|<span
options="|">{c \|}_|<span
options="|">{c \|}_|<span
options="|">{c \|}_|<span
options="|">{c \|}_|<span
options="|">{c \|}_|<span
options="|">{c \|}_|`plot region`|<span
options="|">{c \|}_|<span
options="|">{c \|}_|<span
options="|">{c \|}_|<span
options="|">{c \|}_|<span
options="|">{c \|}_|<span
options="|">{c \|}_|<span
options="|">{c \|}_|<span
options="|">{c \|}_|<span
options="|">{c \|}_|<span
options="BLC">{c BLC}_

------------------------------------------------------------------------

<span options="BRC">{c BRC}_|<span
options="|">{c \|}_|<span
options="|">{c \|}_|<span
options="|">{c \|}_|<span
options="|">{c \|}_|<span
options="|">{c \|}_|<span
options="|">{c \|}_|<span
options="|">{c \|}_|<span
options="|">{c \|}_|<span
options="BLC">{c BLC}_

------------------------------------------------------------------------

<span options="BRC">{c
BRC}_[<strong>scheme</strong>](http://www.stata.com/help.cgi?schemes)
