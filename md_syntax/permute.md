## Syntax

Compute permutation test

`permute permvar exp_list` \[`, options`\] `: command`

Report saved results

`permute`
\[[varlist](http://www.stata.com/help.cgi?varlist)\]
\[`using filename`\] \[`, display_options`\]

<table id="options_table" class="syntab">
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
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="r">reps(#)</code></td>
<td>perform <var class="command">#</var> random permutations; default is <code class="command">reps(100)</code></td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="le">left</code>|<code class="command" data-options="ri">right</code></td>
<td>compute one-sided p-values; default is two-sided</td>
</tr>
</tbody>
<tbody>
<tr class="odd section">
<td colspan="3">Options</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="str">strata(varlist)</code></td>
<td>permute within strata</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td>[<strong></strong>](http://www.stata.com/help.cgi?prefix_saving_option)
<ul>
</ul>
ving(<var class="command">filename</var><strong>, ...)</strong></td>
<td>save results to <var class="command">filename</var>; save statistics in double precision; save results to <var class="command">filename</var> every <var class="command">#</var> replications</td>
</tr>
</tbody>
<tbody>
<tr class="odd section">
<td colspan="3">Reporting</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="l">level(#)</code></td>
<td>set confidence level; default is <code class="command">level(95)</code></td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="noh">noheader</code></td>
<td>suppress table header</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="nol">nolegend</code></td>
<td>suppress table legend</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="v">verbose</code></td>
<td>display full table legend</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="nodrop">nodrop</code></td>
<td>do not drop observations</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="nodots">nodots</code></td>
<td>suppress replication dots</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="dots(#)">dots(#)</code></td>
<td>display dots every <var class="command">#</var> replications</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="noi">noisily</code></td>
<td>display any output from <var class="command">command</var></td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="tr">trace</code></td>
<td>trace <var class="command">command</var></td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="ti">title(text)</code></td>
<td>use <var class="command">text</var> as title for permutation results</td>
</tr>
</tbody>
<tbody>
<tr class="odd section">
<td colspan="3">Advanced</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="eps(#)">eps(#)</code></td>
<td>numerical tolerance; seldom used</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="nowarn">nowarn</code></td>
<td>do not warn when <code class="command">e(sample)</code> is not set</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="force">force</code></td>
<td>do not check for <var class="command">weights</var> or <code class="command">svy</code> commands; seldom used</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="reject(exp)">reject(exp)</code></td>
<td>identify invalid results</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="seed(#)">seed(#)</code></td>
<td>set random-number seed to <var class="command">#</var></td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="l">level(#)</code></td>
<td>set confidence level; default is <code class="command">level(95)</code></td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="noh">noheader</code></td>
<td>suppress table header</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="nol">nolegend</code></td>
<td>suppress table legend</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="v">verbose</code></td>
<td>display full table legend</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="ti">title(text)</code></td>
<td>use <var class="command">text</var> as title for results</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="eps(#)">eps(#)</code></td>
<td>numerical tolerance; seldom used</td>
</tr>
</tbody><tfoot>
<tr class="even footnote">
<td colspan="3"><var class="command">weights</var> are not allowed in <var class="command">command</var>. <span data-options="23">{synoptset 23}_<span>{nobreak None}_ <span data-options="display_options">{marker display_options}_<span>{nobreak None}_ <span>{synopthdr None:display_options}_ <span>{synoptline None}_ <span>{synopt None}<code class="command" data-options="le">left</code>|<code class="command" data-options="ri">right</code>_compute one-sided p-values; default is two-sided</td>
</tr>
</tfoot>

</table>
