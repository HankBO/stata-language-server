## Syntax

`twoway histogram`
[varname](http://www.stata.com/help.cgi?varname)
_\[`if`\] \[`in`\]_ \[`weight`\] \[`,`
\[`discrete_options`\|`continuous_options`\] `common_options`\]

<table class="standard">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><var class="command">discrete_options</var></td>
<td>Description <span>{p2line None}_</td>
</tr>
<tr class="even">
<td><code class="command">discrete</code></td>
<td>specify that data are discrete</td>
</tr>
<tr class="odd">
<td><code class="command">width:(</code><var class="command">#</var><code class="command">)</code></td>
<td>width of bins in [varname](http://www.stata.com/help.cgi?varname) units</td>
</tr>
<tr class="even">
<td><code class="command">start(</code><var class="command">#</var><code class="command">)</code></td>
<td>theoretical minimum value <span>{p2line None}_</td>
</tr>
<tr class="odd">
<td><var class="command">continuous_options</var></td>
<td>Description <span>{p2line None}_</td>
</tr>
<tr class="even">
<td><code class="command">bin(</code><var class="command">#</var><code class="command">)</code></td>
<td><var class="command">#</var> of bins</td>
</tr>
<tr class="odd">
<td><code class="command">width:(</code><var class="command">#</var><code class="command">)</code></td>
<td>width of bins in [varname](http://www.stata.com/help.cgi?varname) units</td>
</tr>
<tr class="even">
<td><code class="command">start(</code><var class="command">#</var><code class="command">)</code></td>
<td>lower limit of first bin <span>{p2line None}_</td>
</tr>
<tr class="odd">
<td><var class="command">common_options</var></td>
<td>Description <span>{p2line None}_</td>
</tr>
<tr class="even">
<td><code class="command">density</code></td>
<td>draw as density; the default</td>
</tr>
<tr class="odd">
<td><code class="command">fraction</code></td>
<td>draw as fractions</td>
</tr>
<tr class="even">
<td><code class="command">frequency</code></td>
<td>draw as frequencies</td>
</tr>
<tr class="odd">
<td><code class="command">percent</code></td>
<td>draw as percents</td>
</tr>
<tr class="even">
<td><code class="command">vertical</code></td>
<td>vertical bars; the default</td>
</tr>
<tr class="odd">
<td><code class="command">horizontal</code></td>
<td>horizontal bars</td>
</tr>
<tr class="even">
<td><code class="command">gap(</code><var class="command">#</var><code class="command">)</code></td>
<td>reduce width of bars, 0
<ul>
</ul>
<var class="command">#</var>&lt;100</td>
</tr>
<tr class="odd">
<td><var class="command">barlook_options</var></td>
<td>change look of bars</td>
</tr>
<tr class="even">
<td><var class="command">axis_choice_options</var></td>
<td>associate plot with alternative axis</td>
</tr>
<tr class="odd">
<td><var class="command">twoway_options</var></td>
<td>titles, legends, axes, added lines and text, by, regions, name, aspect ratio, etc. <span>{p2line None}_</td>
</tr>
</tbody>
</table>

`fweight`s are allowed; see
[<strong>weight</strong>](http://www.stata.com/help.cgi?weight).
