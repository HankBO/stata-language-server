## Syntax

`twoway function` \[\[`y`\]=\] `f`(`x`) _\[`if`\]
\[`in`\]_ \[`, options`\]

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
<td><code class="command">range:(</code><var class="command">#</var> <var class="command">#</var><code class="command">)</code></td>
<td>plot over <code class="command">x</code> = <var class="command">#</var> to <var class="command">#</var></td>
</tr>
<tr class="odd">
<td><code class="command" data-options="ra">range(varname)</code></td>
<td>plot over <code class="command">x</code> = min to max of <var class="command">varname</var></td>
</tr>
<tr class="even">
<td><code class="command">n(</code><var class="command">#</var><code class="command">)</code></td>
<td>evaluate at <var class="command">#</var> points; default is 300</td>
</tr>
<tr class="odd">
<td><code class="command">droplines:(</code><var class="command">numlist</var><code class="command">)</code></td>
<td>draw lines to axis at specified <code class="command">x</code> values</td>
</tr>
<tr class="even">
<td><code class="command">base(</code><var class="command">#</var><code class="command">)</code></td>
<td>base value for <code class="command">dropline()</code>; default is 0</td>
</tr>
<tr class="odd">
<td><code class="command">horizontal</code></td>
<td>draw plot horizontally</td>
</tr>
<tr class="even">
<td><code class="command">yvarformat:(</code>[<strong>%</strong><var class="command">fmt</var><strong></strong>](http://www.stata.com/help.cgi?format)<code class="command">)</code></td>
<td>display format for <code class="command">y</code></td>
</tr>
<tr class="odd">
<td><code class="command">xvarformat:(</code>[<strong>%</strong><var class="command">fmt</var><strong></strong>](http://www.stata.com/help.cgi?format)<code class="command">)</code></td>
<td>display format for <code class="command">x</code></td>
</tr>
<tr class="even">
<td><var class="command">cline_options</var></td>
<td>change look of plotted line</td>
</tr>
<tr class="odd">
<td><var class="command">axis_choice_options</var></td>
<td>associate plot with alternative axis</td>
</tr>
<tr class="even">
<td><var class="command">twoway_options</var></td>
<td>titles, legends, axes, added lines and text, by, regions, name, aspect ratio, etc. <span>{p2line None}_
All explicit options are <var class="command">rightmost</var>, except <code class="command">horizontal</code>, which is <var class="command">unique</var>; see [<strong>repeated options</strong>](http://www.stata.com/help.cgi?repeated%20options).
<code class="command">if</code> <var class="command">exp</var> and <code class="command">in</code> <var class="command">range</var> play no role unless option <code class="command">range(</code><var class="command">varname</var><code class="command">)</code> is specified.
In the above syntax diagram, <var class="command">f</var>(<code class="command">x</code>) stands for an <var class="command">exp</var>ression in terms of <code class="command">x</code>.</td>
</tr>
</tbody>
</table>
