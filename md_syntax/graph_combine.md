## Syntax

`graph combine name` \[`name` ...\] \[`, options`\]

|              |                                            |
|--------------|--------------------------------------------|
| `name`       | Description {p2line None}                  |
| `simplename` | name of graph in memory                    |
| `name.gph` | name of graph stored on disk               |
| `"name"` | name of graph stored on disk {p2line None} |

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
<td><code class="command">colfirst</code></td>
<td>display down columns</td>
</tr>
<tr class="odd">
<td><code class="command">rows:(</code><var class="command">#</var><code class="command">)</code> | <code class="command">cols:(</code><var class="command">#</var><code class="command">)</code></td>
<td>display in <var class="command">#</var> rows or <var class="command">#</var> columns</td>
</tr>
<tr class="even">
<td><code class="command">holes:(</code><var class="command">numlist</var><code class="command">)</code></td>
<td>positions to leave blank</td>
</tr>
<tr class="odd">
<td><code class="command">iscale(</code>[<code class="command">*</code>]<var class="command">#</var><code class="command">)</code></td>
<td>size of text and markers</td>
</tr>
<tr class="even">
<td><code class="command">altshrink</code></td>
<td>alternate scaling of text, etc.</td>
</tr>
<tr class="odd">
<td><code class="command">imargin(</code><var class="command">marginstyle</var><code class="command">)</code></td>
<td>margins for individual graphs</td>
</tr>
<tr class="even">
<td><code class="command">ycommon</code></td>
<td>give <var class="command">y</var> axes common scales</td>
</tr>
<tr class="odd">
<td><code class="command">xcommon</code></td>
<td>give <var class="command">x</var> axes common scales</td>
</tr>
<tr class="even">
<td><var class="command">title_options</var></td>
<td>titles to appear on combined graph</td>
</tr>
<tr class="odd">
<td><var class="command">region_options</var></td>
<td>outlining, shading, aspect ratio</td>
</tr>
<tr class="even">
<td><code class="command">commonscheme</code></td>
<td>put graphs on common scheme</td>
</tr>
<tr class="odd">
<td>[](http://www.stata.com/help.cgi?scheme_option)
<ul>
</ul>
eme(<var class="command">schemename</var>)<strong></strong></td>
<td>overall look</td>
</tr>
<tr class="even">
<td>[<strong>nodraw</strong>](http://www.stata.com/help.cgi?nodraw_option)</td>
<td>suppress display of combined graph</td>
</tr>
<tr class="odd">
<td>[<strong>name(</strong><var class="command">name</var><strong>, ...)</strong>](http://www.stata.com/help.cgi?name_option)</td>
<td>specify name for combined graph</td>
</tr>
<tr class="even">
<td>[<strong>saving(</strong><var class="command">filename</var><strong>, ...)</strong>](http://www.stata.com/help.cgi?saving_option)</td>
<td>save combined graph in file <span>{p2line None}_</td>
</tr>
</tbody>
</table>
