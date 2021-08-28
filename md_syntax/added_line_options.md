## Syntax

<table class="standard">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><var class="command">added_line_options</var></td>
<td>description <span>{p2line None}_</td>
</tr>
<tr class="even">
<td><code class="command">yline:(</code><var class="command">linearg</var><code class="command">)</code></td>
<td>add horizontal lines at specified <var class="command">y</var> values</td>
</tr>
<tr class="odd">
<td><code class="command">xline:(</code><var class="command">linearg</var><code class="command">)</code></td>
<td>add vertical lines at specified <var class="command">x</var> values</td>
</tr>
<tr class="even">
<td><code class="command">tline:(</code><var class="command">time_linearg</var><code class="command">)</code></td>
<td>add vertical lines at specified <var class="command">t</var> values <span>{p2line None}_
<code class="command">yline()</code>, <code class="command">xline()</code>, and <code class="command">tline()</code> are <var class="command">merged-implicit</var>; see [<strong>repeated options</strong>](http://www.stata.com/help.cgi?repeated%20options) and see [<strong>Interpretation of repeated options</strong>](#remarks2) below.</td>
</tr>
</tbody>
</table>

where `linearg` is

`numlist` \[`, suboptions`\]

For a description of `numlist`, see
[<strong>numlist</strong>](http://www.stata.com/help.cgi?numlist).

and `time_linearg` is

`datelist` \[`, suboptions`\]

For a description of `datelist`, see
[<strong>datelist</strong>](http://www.stata.com/help.cgi?datelist).

<table class="standard">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><var class="command">suboptions</var></td>
<td>description <span>{p2line None}_</td>
</tr>
<tr class="even">
<td><code class="command">axis:(</code><var class="command">#</var><code class="command">)</code></td>
<td>which axis to use, 1
<ul>
</ul>
#
<ul>
</ul>
9</td>
</tr>
<tr class="odd">
<td><code class="command">style:(</code><var class="command">addedlinestyle</var><code class="command">)</code></td>
<td>overall style of added line</td>
</tr>
<tr class="even">
<td>[<code class="command">no</code>]<code class="command">extend</code></td>
<td>extend line through plot region's margins</td>
</tr>
<tr class="odd">
<td><code class="command">lstyle:(</code><var class="command">linestyle</var><code class="command">)</code></td>
<td>overall style of line</td>
</tr>
<tr class="even">
<td><code class="command">lpattern:(</code><var class="command">linepatternstyle</var><code class="command">)</code></td>
<td>line pattern (solid, dashed, etc.)</td>
</tr>
<tr class="odd">
<td><code class="command">lwidth:(</code><var class="command">linewidthstyle</var><code class="command">)</code></td>
<td>thickness of line</td>
</tr>
<tr class="even">
<td><code class="command">lalign:(</code><var class="command">linealignmentstyle</var><code class="command">)</code></td>
<td>outline alignment (inside, outside, center)</td>
</tr>
<tr class="odd">
<td><code class="command">lcolor:(</code><var class="command">colorstyle</var><code class="command">)</code></td>
<td>color and opacity of line <span>{p2line None}_</td>
</tr>
</tbody>
</table>
