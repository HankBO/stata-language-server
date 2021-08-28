## Syntax

Split at designated times

`stsplit`
[newvar](http://www.stata.com/help.cgi?newvar)
\[`if`\]`,` {`at(numlist)` \|
`every(#)`} \[`stsplitDT_options`\]

Split at failure times

`stsplit` \[`if`\]`, at(failures)` \[`stsplitFT_options`\]

Join episodes

`stjoin` \[`, censored(numlist)`\]

<table id="stsplitDT_options" class="syntab">
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">stsplitDT_options</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd section">
<td colspan="3">Main</td>
</tr>
<tr class="even" style="has_footnote">
<td>*</td>
<td><code class="command" data-options="at(numlist)">at(numlist)</code></td>
<td>split records at specified analysis times</td>
</tr>
<tr class="odd" style="has_footnote">
<td>*</td>
<td><code class="command" data-options="ev">every(#)</code></td>
<td>split records when analysis time is a multiple of <var class="command">#</var></td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="af">after(spec)</code></td>
<td>use time since <var class="command">spec</var> for <code class="command" data-options="at()">at()</code> or <code class="command" data-options="every()">every()</code> rather than time since onset of risk</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="trim">trim</code></td>
<td>exclude observations outside of range</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="nopre">nopreserve</code></td>
<td>do not save original data; programmer's option</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="st">strata(varlist)</code></td>
<td>restrict splitting to failures within stratum defined by <var class="command">varlist</var></td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="r">riskset(newvar)</code></td>
<td>create a risk-set ID variable named <var class="command">newvar</var></td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="nopre">nopreserve</code></td>
<td>do not save original data; programmer's option</td>
</tr>
</tbody><tfoot>
<tr class="even footnote">
<td colspan="3">* Either <code class="command" data-options="at(numlist)">at(numlist)</code> or <code class="command" data-options="every(#)">every(#)</code> is required with <code class="command">stsplit</code> at designated times. <span data-options="18 tabbed">{synoptset 18 tabbed}_<span>{nobreak None}_ <span data-options="stsplitFT_options">{marker stsplitFT_options}_<span>{nobreak None}_ <span>{synopthdr None:stsplitFT_options}_ <span>{synoptline None}_ <span>{syntab None:Main}_ <span>{p2coldent None:* }<code class="command">at(</code><code class="command">failures)</code>_split at observed failure times</td>
</tr>
<tr class="odd footnote">
<td colspan="3">* <code class="command">at(failures)</code> is required with <code class="command">stsplit</code> at failure times.
You must <code class="command">stset</code> your dataset by using the <code class="command" data-options="id()">id()</code> option before using <code class="command">stsplit</code> or <code class="command">stjoin</code>; see [<strong>[ST]</strong> stset](http://www.stata.com/help.cgi?stset).</td>
</tr>
<tr class="even footnote">
<td colspan="3"><code class="command" data-options="nopreserve">nopreserve</code> does not appear in the dialog box.</td>
</tr>
</tfoot>

</table>
