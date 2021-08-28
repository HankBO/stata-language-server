## Syntax

`axis_scale_options` are a subset of `axis_options`; see
[<strong>[G-3]</strong> <em>axis_options</em>](http://www.stata.com/help.cgi?axis_options).

<table class="standard">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><var class="command">axis_scale_options</var></td>
<td>Description <span>{p2line None}_</td>
</tr>
<tr class="even">
<td><code class="command">yscale:(</code><var class="command">axis_suboptions</var><code class="command">)</code></td>
<td>how <var class="command">y</var> axis looks</td>
</tr>
<tr class="odd">
<td><code class="command">xscale:(</code><var class="command">axis_suboptions</var><code class="command">)</code></td>
<td>how <var class="command">x</var> axis looks</td>
</tr>
<tr class="even">
<td><code class="command">tscale:(</code><var class="command">axis_suboptions</var><code class="command">)</code></td>
<td>how <var class="command">t</var> (time) axis looks</td>
</tr>
<tr class="odd">
<td><code class="command">zscale:(</code><var class="command">axis_suboptions</var><code class="command">)</code></td>
<td>how contour legend axis looks <span>{p2line None}_
The above options are <var class="command">merged-implicit</var>; see [<strong>repeated options</strong>](http://www.stata.com/help.cgi?repeated%20options).</td>
</tr>
<tr class="even">
<td><var class="command">axis_suboptions</var></td>
<td>Description <span>{p2line None}_</td>
</tr>
<tr class="odd">
<td><code class="command">axis:(</code><var class="command">#</var><code class="command">)</code></td>
<td>which axis to modify; <code class="command">1</code>
<ul>
</ul>
<var class="command">#</var>
<ul>
</ul>
<code class="command">9</code></td>
</tr>
<tr class="even">
<td>[<code class="command">no</code>]<code class="command">log</code></td>
<td>use logarithmic scale</td>
</tr>
<tr class="odd">
<td>[<code class="command">no</code>]<code class="command">reverse</code></td>
<td>reverse scale to run from max to min</td>
</tr>
<tr class="even">
<td><code class="command">range:(</code><var class="command">numlist</var><code class="command">)</code></td>
<td>expand range of axis</td>
</tr>
<tr class="odd">
<td><code class="command">range:(</code><var class="command">datelist</var><code class="command">)</code></td>
<td>expand range of <var class="command">t</var> axis (<code class="command">tscale()</code> only)</td>
</tr>
<tr class="even">
<td><code class="command">off</code> and <code class="command">on</code></td>
<td>suppress/force display of axis</td>
</tr>
<tr class="odd">
<td><code class="command">fill</code></td>
<td>allocate space for axis even if <code class="command">off</code></td>
</tr>
<tr class="even">
<td><code class="command">alt</code></td>
<td>move axis from left to right or from top to bottom</td>
</tr>
<tr class="odd">
<td><code class="command">fextend</code></td>
<td>extend axis line through plot region and plot region's margin</td>
</tr>
<tr class="even">
<td><code class="command">extend</code></td>
<td>extend axis line through plot region</td>
</tr>
<tr class="odd">
<td><code class="command">noextend</code></td>
<td>do not extend axis line at all</td>
</tr>
<tr class="even">
<td><code class="command">noline</code></td>
<td>do not draw axis line</td>
</tr>
<tr class="odd">
<td><code class="command">line</code></td>
<td>force drawing of axis line</td>
</tr>
<tr class="even">
<td><code class="command">titlegap:(</code><var class="command">relativesize</var><code class="command">)</code></td>
<td>margin between axis title and tick labels</td>
</tr>
<tr class="odd">
<td><code class="command">outergap:(</code><var class="command">relativesize</var><code class="command">)</code></td>
<td>margin outside axis title</td>
</tr>
<tr class="even">
<td><code class="command">lstyle:(</code><var class="command">linestyle</var><code class="command">)</code></td>
<td>overall style of axis line</td>
</tr>
<tr class="odd">
<td><code class="command">lcolor:(</code><var class="command">colorstyle</var><code class="command">)</code></td>
<td>color and opacity of axis line</td>
</tr>
<tr class="even">
<td><code class="command">lwidth:(</code><var class="command">linewidthstyle</var><code class="command">)</code></td>
<td>thickness of axis line</td>
</tr>
<tr class="odd">
<td><code class="command">lpattern:(</code><var class="command">linepatternstyle</var><code class="command">)</code></td>
<td>axis pattern (solid, dashed, etc.) <span>{p2line None}_</td>
</tr>
</tbody>
</table>
