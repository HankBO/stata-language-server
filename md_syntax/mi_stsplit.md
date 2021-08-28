## Syntax

To split at designated times

`mi stsplit`
[newvar](http://www.stata.com/help.cgi?newvar)
\[`if`\]`,` {`at(numlist)` \|
`every(#)`} \[`options`\]

<table class="syntab">
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">Options</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd section">
<td colspan="3">Main</td>
</tr>
<tr class="even" style="has_footnote">
<td>*</td>
<td><code class="command">at(</code><var class="command">numlist</var><code class="command">)</code></td>
<td>split at specified analysis times</td>
</tr>
<tr class="odd" style="has_footnote">
<td>*</td>
<td><code class="command">every(</code><var class="command">#</var><code class="command">)</code></td>
<td>split when analysis time is a multiple of <var class="command">#</var></td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command">after(</code><var class="command">spec</var><code class="command">)</code></td>
<td>use time since <var class="command">spec</var> instead of analysis time for <code class="command">at()</code> or <code class="command">every()</code></td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command">trim</code></td>
<td>exclude observations outside of range</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command">noupdate</code></td>
<td>see <strong>[<strong>[MI] noupdate option</strong>](http://www.stata.com/help.cgi?mi_noupdate_option)</strong></td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command">nopreserve</code></td>
<td>programmer's option</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command">strata(</code>[varlist](http://www.stata.com/help.cgi?varlist)<code class="command">)</code></td>
<td>perform splitting by failures within stratum, strata defined by <var class="command">varlist</var></td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command">riskset(</code>[newvar](http://www.stata.com/help.cgi?newvar)<code class="command">)</code></td>
<td>create risk-set ID variable</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command">noupdate</code></td>
<td>see <strong>[<strong>[MI] noupdate option</strong>](http://www.stata.com/help.cgi?mi_noupdate_option)</strong></td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command">nopreserve</code></td>
<td>programmer's option</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command">noupdate</code></td>
<td>see <strong>[<strong>[MI] noupdate option</strong>](http://www.stata.com/help.cgi?mi_noupdate_option)</strong></td>
</tr>
</tbody><tfoot>
<tr class="odd footnote">
<td colspan="3">* <code class="command">at()</code> or <code class="command">every()</code> is required.</td>
</tr>
<tr class="even footnote">
<td colspan="3"><code class="command">nopreserve</code> is not included in the dialog box. <span>{phang None}_ To split at failure times
<code class="command">mi</code> <code class="command">stsplit</code> [<var class="command">if</var>]<code class="command">,</code> <code class="command">at(</code><code class="command" data-options="f">failures)</code> [<var class="command">options</var>] <span data-options="20 tabbed">{synoptset 20 tabbed}_<span>{nobreak None}_ <span>{synopthdr None}_ <span>{synoptline None}_ <span>{syntab None:Main}_ <span>{p2coldent None:* }<code class="command">at(failures)</code>_split at times of observed failures</td>
</tr>
<tr class="odd footnote">
<td colspan="3">* <code class="command">at()</code> is required.</td>
</tr>
<tr class="even footnote">
<td colspan="3"><code class="command">nopreserve</code> is not included in the dialog box. <span>{phang None}_ To join episodes
<code class="command">mi</code> <code class="command">stjoin</code> [<code class="command">,</code> <var class="command">options</var>] <span data-options="20 tabbed">{synoptset 20 tabbed}_<span>{nobreak None}_ <span>{synopthdr None}_ <span>{synoptline None}_ <span>{syntab None:Main}_ <span>{synopt None}<code class="command">censored(</code><var class="command">numlist</var><code class="command">)</code>_values of failure that indicate no event</td>
</tr>
</tfoot>

</table>
