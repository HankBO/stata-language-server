## Syntax

<table class="standard">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><var class="command">marker_label_options</var></td>
<td>Description <span>{p2line None}_</td>
</tr>
<tr class="even">
<td><code class="command">mlabel(</code>[varname](http://www.stata.com/help.cgi?varname)<code class="command">)</code></td>
<td>specify marker variable</td>
</tr>
<tr class="odd">
<td><code class="command">mlabstyle:(</code><var class="command">markerlabelstyle</var><code class="command">)</code></td>
<td>overall style of label</td>
</tr>
<tr class="even">
<td><code class="command">mlabposition:(</code><var class="command">clockposstyle</var><code class="command">)</code></td>
<td>where to locate the label</td>
</tr>
<tr class="odd">
<td><code class="command">mlabvposition:(</code>[varname](http://www.stata.com/help.cgi?varname)<code class="command">)</code></td>
<td>where to locate the label 2</td>
</tr>
<tr class="even">
<td><code class="command">mlabgap:(</code><var class="command">relativesize</var><code class="command">)</code></td>
<td>gap between marker and label</td>
</tr>
<tr class="odd">
<td><code class="command">mlabangle:(</code><var class="command">anglestyle</var><code class="command">)</code></td>
<td>angle of label</td>
</tr>
<tr class="even">
<td><code class="command">mlabtextstyle:(</code><var class="command">textstyle</var><code class="command">)</code></td>
<td>overall style of text</td>
</tr>
<tr class="odd">
<td><code class="command">mlabsize:(</code><var class="command">textsizestyle</var><code class="command">)</code></td>
<td>size of label</td>
</tr>
<tr class="even">
<td><code class="command">mlabcolor:(</code><var class="command">colorstyle</var><code class="command">)</code></td>
<td>color and opacity of label <span>{p2line None}_
All options are <var class="command">rightmost</var>; see [<strong>repeated options</strong>](http://www.stata.com/help.cgi?repeated%20options).</td>
</tr>
</tbody>
</table>

Sometimes -- such as when used with `scatter` -- lists are allowed
inside the arguments. A list is a sequence of the elements separated by
spaces. Shorthands are allowed to make specifying the list easier; see
[<strong>[G-4]</strong> <em>stylelists</em>](http://www.stata.com/help.cgi?stylelists).
When lists are allowed, option `mlabel()` allows a
[varlist](http://www.stata.com/help.cgi?varlist)
in place of a
[varname](http://www.stata.com/help.cgi?varname).
