## Syntax

|                                                                                                     |                                                                                                                                                                                       |
|-----------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `by_option`                                                                                         | Description {p2line None}                                                                                                                                                             |
| `by(`[varlist](http://www.stata.com/help.cgi?varlist)\[`, byopts`\]`)` | repeat for by-groups {p2line None} `by()` is `merged-implicit`; see [<strong>repeated options</strong>](http://www.stata.com/help.cgi?repeated%20options). |

<table class="standard">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><var class="command">byopts</var></td>
<td>Description <span>{p2line None}_</td>
</tr>
<tr class="even">
<td><code class="command">total</code></td>
<td>add total group</td>
</tr>
<tr class="odd">
<td><code class="command">missing</code></td>
<td>add missing groups</td>
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
<td><code class="command">compact</code></td>
<td>synonym for <code class="command">style(compact)</code></td>
</tr>
<tr class="odd">
<td><code class="command">style(</code><var class="command">bystyle</var><code class="command">)</code></td>
<td>overall style of presentation</td>
</tr>
<tr class="even">
<td>[<code class="command">no</code>]<code class="command">edgelabel</code></td>
<td>label <var class="command">x</var> axes of edges</td>
</tr>
<tr class="odd">
<td>[<code class="command">no</code>]<code class="command">rescale</code></td>
<td>separate <var class="command">y</var> and <var class="command">x</var> scales for each group</td>
</tr>
<tr class="even">
<td>[<code class="command">no</code>]<code class="command">yrescale</code></td>
<td>separate <var class="command">y</var> scale for each group</td>
</tr>
<tr class="odd">
<td>[<code class="command">no</code>]<code class="command">xrescale</code></td>
<td>separate <var class="command">x</var> scale for each group</td>
</tr>
<tr class="even">
<td>[<code class="command">no</code>]<code class="command">iyaxes:</code></td>
<td>show individual <var class="command">y</var> axes</td>
</tr>
<tr class="odd">
<td>[<code class="command">no</code>]<code class="command">ixaxes:</code></td>
<td>show individual <var class="command">x</var> axes</td>
</tr>
<tr class="even">
<td>[<code class="command">no</code>]<code class="command">iytick:</code></td>
<td>show individual <var class="command">y</var>-axes ticks</td>
</tr>
<tr class="odd">
<td>[<code class="command">no</code>]<code class="command">ixtick:</code></td>
<td>show individual <var class="command">x</var>-axes ticks</td>
</tr>
<tr class="even">
<td>[<code class="command">no</code>]<code class="command">iylabel:</code></td>
<td>show individual <var class="command">y</var>-axes labels</td>
</tr>
<tr class="odd">
<td>[<code class="command">no</code>]<code class="command">ixlabel:</code></td>
<td>show individual <var class="command">x</var>-axes labels</td>
</tr>
<tr class="even">
<td>[<code class="command">no</code>]<code class="command">iytitle:</code></td>
<td>show individual <var class="command">y</var>-axes titles</td>
</tr>
<tr class="odd">
<td>[<code class="command">no</code>]<code class="command">ixtitle:</code></td>
<td>show individual <var class="command">x</var>-axes titles</td>
</tr>
<tr class="even">
<td><code class="command">imargin:(</code><var class="command">marginstyle</var><code class="command">)</code></td>
<td>margin between graphs</td>
</tr>
<tr class="odd">
<td><var class="command">legend_options</var></td>
<td>show legend and placement of legend</td>
</tr>
<tr class="even">
<td><var class="command">title_options</var></td>
<td>overall titles</td>
</tr>
<tr class="odd">
<td><var class="command">region_options</var></td>
<td>overall outlining, shading, and aspect <span>{p2line None}_
The <var class="command">title_options</var> and <var class="command">region_options</var> on the command on which <code class="command">by()</code> is appended will become the titles and regions for the individual by-groups.</td>
</tr>
</tbody>
</table>
