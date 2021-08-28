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
<td><code class="command">pcycle:(</code><var class="command">#</var><code class="command">)</code></td>
<td>plots before [<strong>pstyles</strong>](http://www.stata.com/help.cgi?pstyle) recycle</td>
</tr>
<tr class="odd">
<td><code class="command">yvarlabel:(</code><var class="command">quoted_strings</var><code class="command">)</code></td>
<td>respecify <var class="command">y</var>-variable labels</td>
</tr>
<tr class="even">
<td><code class="command">xvarlabel:(</code><var class="command">quoted_string</var><code class="command">)</code></td>
<td>respecify <var class="command">x</var>-variable label</td>
</tr>
<tr class="odd">
<td><code class="command">yvarformat:(</code>[<strong>%</strong><var class="command">fmt</var><strong></strong>](http://www.stata.com/help.cgi?format) [...]<code class="command">)</code></td>
<td>respecify <var class="command">y</var>-variable formats</td>
</tr>
<tr class="even">
<td><code class="command">xvarformat:(</code>[<strong>%</strong><var class="command">fmt</var><strong></strong>](http://www.stata.com/help.cgi?format)<code class="command">)</code></td>
<td>respecify <var class="command">x</var>-variable format</td>
</tr>
<tr class="odd">
<td><code class="command" data-options="yoverhang">yoverhangs</code></td>
<td>adjust margins for <var class="command">y</var>-axis labels</td>
</tr>
<tr class="even">
<td><code class="command" data-options="xoverhang">xoverhangs</code></td>
<td>adjust margins for <var class="command">x</var>-axis labels</td>
</tr>
<tr class="odd">
<td><code class="command">recast(</code><var class="command">newplottype</var><code class="command">)</code></td>
<td>treat plot as <var class="command">newplottype</var> <span>{p2line None}_
The above options are <var class="command">rightmost</var>; see [<strong>repeated options</strong>](http://www.stata.com/help.cgi?repeated%20options).</td>
</tr>
</tbody>
</table>

where `quoted_string` is one quoted string and `quoted_strings` are one
or more quoted strings, such as

`"plot 1 label""plot 1 label""plot 2 label"`

<table class="standard">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><var class="command">newplottype</var></td>
<td>Description <span>{p2line None}_</td>
</tr>
<tr class="even">
<td><code class="command">scatter</code></td>
<td>treat as [<strong>graph twoway scatter</strong>](http://www.stata.com/help.cgi?graph%20twoway%20scatter)</td>
</tr>
<tr class="odd">
<td><code class="command">line</code></td>
<td>treat as [<strong>graph twoway line</strong>](http://www.stata.com/help.cgi?graph%20twoway%20line)</td>
</tr>
<tr class="even">
<td><code class="command">connected</code></td>
<td>treat as [<strong>graph twoway connected</strong>](http://www.stata.com/help.cgi?graph%20twoway%20connected)</td>
</tr>
<tr class="odd">
<td><code class="command">bar</code></td>
<td>treat as [<strong>graph twoway bar</strong>](http://www.stata.com/help.cgi?graph%20twoway%20bar)</td>
</tr>
<tr class="even">
<td><code class="command">area</code></td>
<td>treat as [<strong>graph twoway area</strong>](http://www.stata.com/help.cgi?graph%20twoway%20area)</td>
</tr>
<tr class="odd">
<td><code class="command">spike</code></td>
<td>treat as [<strong>graph twoway spike</strong>](http://www.stata.com/help.cgi?graph%20twoway%20spike)</td>
</tr>
<tr class="even">
<td><code class="command">dropline</code></td>
<td>treat as [<strong>graph twoway dropline</strong>](http://www.stata.com/help.cgi?graph%20twoway%20dropline)</td>
</tr>
<tr class="odd">
<td><code class="command">dot</code></td>
<td>treat as [<strong>graph twoway dot</strong>](http://www.stata.com/help.cgi?graph%20twoway%20dot)</td>
</tr>
<tr class="even">
<td><code class="command">rarea</code></td>
<td>treat as [<strong>graph twoway rarea</strong>](http://www.stata.com/help.cgi?graph%20twoway%20rarea)</td>
</tr>
<tr class="odd">
<td><code class="command">rbar</code></td>
<td>treat as [<strong>graph twoway rbar</strong>](http://www.stata.com/help.cgi?graph%20twoway%20rbar)</td>
</tr>
<tr class="even">
<td><code class="command">rspike</code></td>
<td>treat as [<strong>graph twoway rspike</strong>](http://www.stata.com/help.cgi?graph%20twoway%20rspike)</td>
</tr>
<tr class="odd">
<td><code class="command">rcap</code></td>
<td>treat as [<strong>graph twoway rcap</strong>](http://www.stata.com/help.cgi?graph%20twoway%20rcap)</td>
</tr>
<tr class="even">
<td><code class="command">rcapsym</code></td>
<td>treat as [<strong>graph twoway rcapsym</strong>](http://www.stata.com/help.cgi?graph%20twoway%20rcapsym)</td>
</tr>
<tr class="odd">
<td><code class="command">rline</code></td>
<td>treat as [<strong>graph twoway rline</strong>](http://www.stata.com/help.cgi?graph%20twoway%20rline)</td>
</tr>
<tr class="even">
<td><code class="command">rconnected</code></td>
<td>treat as [<strong>graph twoway rconnected</strong>](http://www.stata.com/help.cgi?graph%20twoway%20rconnected)</td>
</tr>
<tr class="odd">
<td><code class="command">rscatter</code></td>
<td>treat as [<strong>graph twoway rscatter</strong>](http://www.stata.com/help.cgi?graph%20twoway%20rscatter)</td>
</tr>
<tr class="even">
<td><code class="command">pcspike</code></td>
<td>treat as [<strong>graph twoway pcspike</strong>](http://www.stata.com/help.cgi?graph%20twoway%20pcspike)</td>
</tr>
<tr class="odd">
<td><code class="command">pccapsym</code></td>
<td>treat as [<strong>graph twoway pccapsym</strong>](http://www.stata.com/help.cgi?graph%20twoway%20pccapsym)</td>
</tr>
<tr class="even">
<td><code class="command">pcarrow</code></td>
<td>treat as [<strong>graph twoway pcarrow</strong>](http://www.stata.com/help.cgi?graph%20twoway%20pcarrow)</td>
</tr>
<tr class="odd">
<td><code class="command">pcbarrow</code></td>
<td>treat as [<strong>graph twoway pcbarrow</strong>](http://www.stata.com/help.cgi?graph%20twoway%20pcbarrow)</td>
</tr>
<tr class="even">
<td><code class="command">pcscatter</code></td>
<td>treat as [<strong>graph twoway pcscatter</strong>](http://www.stata.com/help.cgi?graph%20twoway%20pcscatter) <span>{p2line None}_
<var class="command">newplottypes</var> in each grouping (<code class="command">scatter</code> through <code class="command">dot</code>, <code class="command">rarea</code> though <code class="command">rscatter</code>, and <code class="command">pcspike</code> through <code class="command">pcscatter</code>) should be recast only among themselves.</td>
</tr>
</tbody>
</table>
