## Syntax

`joinby`
\[[varlist](http://www.stata.com/help.cgi?varlist)\]
`using filename` \[`, options`\]

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
<td colspan="3">Options</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td>When observations match:</td>
<td></td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="update">update</code></td>
<td>replace missing data in memory with values from <var class="command">filename</var></td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="replace">replace</code></td>
<td>replace all data in memory with values from <var class="command">filename</var></td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td>When observations do not match:</td>
<td></td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="unm">unmatched</code><code class="command">(</code><code class="command" data-options="n">none</code><code class="command">)</code></td>
<td>ignore all; the default</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="unm">unmatched</code><code class="command">(</code><code class="command" data-options="b">both</code><code class="command">)</code></td>
<td>include from both datasets</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="unm">unmatched</code><code class="command">(</code><code class="command" data-options="m">master</code><code class="command">)</code></td>
<td>include from data in memory</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="unm">unmatched</code><code class="command">(</code><code class="command" data-options="u">using</code><code class="command">)</code></td>
<td>include from data in <var class="command">filename</var></td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="_merge(varname)">_merge(varname)</code></td>
<td><var class="command">varname</var> marks source of resulting observation; default is <code class="command" data-options="_merge">_merge</code></td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="nol">nolabel</code></td>
<td>do not copy value-label definitions from <var class="command">filename</var></td>
</tr>
</tbody><tfoot>
<tr class="even footnote">
<td colspan="3"><span>{nobreak None}_ <var class="command">varlist</var> may not contain [<strong>strL</strong>](http://www.stata.com/help.cgi?data%20types)s. <span>{p2colreset None}_<span>{nobreak None}_ <span data-options="menu">{marker menu}_<span>{nobreak None}_ <span>{title None:Menu}_ <span>{phang None}_ <strong>Data &gt; Combine datasets &gt; Form all pairwise combinations within groups</strong> <span data-options="description">{marker description}_<span>{nobreak None}_ <span>{title None:Description}_ <span>{pstd None}_ <code class="command">joinby</code> joins, within groups formed by [varlist](http://www.stata.com/help.cgi?varlist), observations of the dataset in memory with <var class="command">filename</var>, a Stata-format dataset. By join we mean to form all pairwise combinations. <var class="command">filename</var> is required to be sorted by <var class="command">varlist</var>. If <var class="command">filename</var> is specified without an extension, <code class="command">.dta</code> is assumed. <span>{pstd None}_ If <var class="command">varlist</var> is not specified, <code class="command">joinby</code> takes as <var class="command">varlist</var> the set of variables common to the dataset in memory and in <var class="command">filename</var>. <span>{pstd None}_ Observations unique to one or the other dataset are ignored unless <code class="command" data-options="unmatched()">unmatched()</code> specifies differently. Whether you load one dataset and join the other or vice versa makes no difference in the number of resulting observations. <span>{pstd None}_ If there are common variables between the two datasets, however, the combined dataset will contain the values from the master data for those observations. This behavior can be modified with the <code class="command" data-options="update">update</code> and <code class="command" data-options="replace">replace</code> options. <span data-options="linkspdf">{marker linkspdf}_<span>{nobreak None}_ <span>{title None:Links to PDF documentation}_ <a href="http://www.stata.com/manuals14/djoinbyquickstart.pdf">Quick start</a> <a href="http://www.stata.com/manuals14/djoinbyremarksandexamples.pdf">Remarks and examples</a> <span>{pstd None}_ The above sections are not included in this help file. <span data-options="options">{marker options}_<span>{nobreak None}_ <span>{title None:Options}_ <span>{dlgtab None:Options}_ <span>{phang None}_ <code class="command" data-options="update">update</code> varies the action that <code class="command">joinby</code> takes when an observation is matched. By default, values from the master data are retained when the same variables are found in both datasets. If <code class="command" data-options="update">update</code> is specified, however, the values from the using dataset are retained where the master dataset contains missing. <span>{phang None}_ <code class="command" data-options="replace">replace</code>, allowed with <code class="command" data-options="update">update</code> only, specifies that nonmissing values in the master dataset be replaced with corresponding values from the using dataset. A nonmissing value, however, will never be replaced with a missing value. <span>{phang None}_ <code class="command" data-options="unmatched">unmatched</code><code class="command">(</code><code class="command" data-options="none">none</code>|<code class="command" data-options="both">both</code>|<code class="command" data-options="master">master</code>|<code class="command" data-options="using">using</code><code class="command">)</code> specifies whether observations unique to one of the datasets are to be kept, with the variables from the other dataset set to missing. Valid values are
<code class="command" data-options="none">none</code><span data-options="4">{space 4}_ignore all unmatched observations (default)</td>
</tr>
<tr class="odd footnote">
<td colspan="3"><code class="command" data-options="both">both</code><span data-options="4">{space 4}_include unmatched observations from the master and using data</td>
</tr>
<tr class="even footnote">
<td colspan="3"><code class="command" data-options="master">master</code><span data-options="2">{space 2}_include unmatched observations from the master data</td>
</tr>
<tr class="odd footnote">
<td colspan="3"><code class="command" data-options="using">using</code><span data-options="3">{space 3}_include unmatched observations from the using data <span>{phang None}_ <code class="command" data-options="_merge(varname)">_merge(varname)</code> specifies the name of the variable that will mark the source of the resulting observation. The default name is <code class="command">_merge(_merge)</code>. To preserve compatibility with earlier versions of <code class="command">joinby</code>, <code class="command">_merge</code> is generated only if <code class="command">unmatched</code> is specified. <span>{phang None}_ <code class="command">nolabel</code> prevents Stata from copying the value-label definitions from the dataset on disk into the dataset in memory. Even if you do not specify this option, label definitions from the disk dataset do not replace label definitions already in memory. <span data-options="example">{marker example}_<span>{nobreak None}_ <span>{title None:Example}_ <span>{pstd None}_Setup</td>
</tr>
<tr class="even footnote">
<td colspan="3"><code class="command">. webuse child</code></td>
</tr>
<tr class="odd footnote">
<td colspan="3"><code class="command">. describe</code></td>
</tr>
<tr class="even footnote">
<td colspan="3"><code class="command">. list</code></td>
</tr>
<tr class="odd footnote">
<td colspan="3"><code class="command">. webuse parent</code></td>
</tr>
<tr class="even footnote">
<td colspan="3"><code class="command">. describe</code></td>
</tr>
<tr class="odd footnote">
<td colspan="3"><code class="command">. list, sep(0)</code></td>
</tr>
<tr class="even footnote">
<td colspan="3"><code class="command">. sort family_id</code> <span>{pstd None}_Join information on parents from data in memory with information on children from data at http://www.stata-press.com</td>
</tr>
<tr class="odd footnote">
<td colspan="3"><code class="command">. joinby family_id using</code> <code class="command">http://www.stata-press.com/data/r15/child</code> <span>{pstd None}_Describe the resulting dataset</td>
</tr>
<tr class="even footnote">
<td colspan="3"><code class="command">. describe</code> <span>{pstd None}_List the resulting data</td>
</tr>
<tr class="odd footnote">
<td colspan="3"><code class="command">. list, sepby(family_id) abbrev(12)</code></td>
</tr>
</tfoot>

</table>
