## Syntax

`statsby` \[`exp_list`\] \[`, options` \]`: command`

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
<td><code class="command">by(</code>[<var class="command">varlist</var><strong></strong>](http://www.stata.com/help.cgi?varlist) [<code class="command">,</code> <code class="command">missing</code>]<code class="command">)</code></td>
<td>equivalent to interactive use of <code class="command">by</code> <var class="command">varlist</var><code class="command">:</code></td>
</tr>
</tbody>
<tbody>
<tr class="odd section">
<td colspan="3">Options</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="clear">clear</code></td>
<td>replace data in memory with results</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td>[<strong></strong>](http://www.stata.com/help.cgi?prefix_saving_option)
<ul>
</ul>
ving(<var class="command">filename</var><strong>, ...)</strong></td>
<td>save results to <var class="command">filename</var>; save statistics in double precision; save results to <var class="command">filename</var> every <var class="command">#</var> replications</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="t">total</code></td>
<td>include results for the entire dataset</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="s">subsets</code></td>
<td>include all combinations of subsets of groups</td>
</tr>
</tbody>
<tbody>
<tr class="odd section">
<td colspan="3">Reporting</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="nodots">nodots</code></td>
<td>suppress replication dots</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="dots(#)">dots(#)</code></td>
<td>display dots every <var class="command">#</var> replications</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="noi">noisily</code></td>
<td>display any output from <var class="command">command</var></td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="tr">trace</code></td>
<td>trace <var class="command">command</var></td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="nol">nolegend</code></td>
<td>suppress table legend</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="v">verbose</code></td>
<td>display the full table legend</td>
</tr>
</tbody>
<tbody>
<tr class="odd section">
<td colspan="3">Advanced</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="base">basepop</code><code class="command">(</code><var class="command">exp</var><code class="command">)</code></td>
<td>restrict initializing sample to <var class="command">exp</var>; seldom used</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="force">force</code></td>
<td>do not check for <code class="command">svy</code> commands; seldom used</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="forcedrop">forcedrop</code></td>
<td>retain only observations in by-groups when calling <var class="command">command</var>; seldom used</td>
</tr>
</tbody><tfoot>
<tr class="odd footnote">
<td colspan="3">* <code class="command" data-options="by()">by()</code> is required on the dialog box because <code class="command">statsby</code> is useful to the interactive user only when using <code class="command" data-options="by()">by()</code>.</td>
</tr>
<tr class="even footnote">
<td colspan="3">All weight types supported by <var class="command">command</var> are allowed except <code class="command">pweight</code>s; see [<strong>weight</strong>](http://www.stata.com/help.cgi?weight). <span data-options="menu">{marker menu}_<span>{nobreak None}_ <span>{title None:Menu}_ <span>{phang None}_ <strong>Statistics &gt; Other &gt; Collect statistics for a command across a by list</strong> <span data-options="description">{marker description}_<span>{nobreak None}_ <span>{title None:Description}_ <span>{pstd None}_ <code class="command">statsby</code> collects statistics from <var class="command">command</var> across a by list. Typing <span>{phang2 None}_ <code class="command">. statsby</code> <var class="command">exp_list</var> <code class="command">,</code> <code class="command" data-options="by(varname)">by(varname)</code><code class="command">:</code> <var class="command">command</var> <span>{pstd None}_ executes <var class="command">command</var> for each group identified by <var class="command">varname</var>, building a dataset of the associated values from the expressions in <var class="command">exp_list</var>. The resulting dataset replaces the current dataset, unless the <code class="command">saving()</code> option is supplied. <var class="command">varname</var> can refer to a numeric or a string variable. <span>{pstd None}_ <var class="command">command</var> defines the statistical command to be executed. Most Stata commands and user-written programs can be used with <code class="command">statsby</code>, as long as they follow [<strong>standard Stata syntax</strong>](http://www.stata.com/help.cgi?language) and allow the <strong>[<strong>if</strong>](http://www.stata.com/help.cgi?if)</strong> qualifier. The <code class="command">by</code> prefix cannot be part of <var class="command">command</var>. <span>{pstd None}_ <var class="command">exp_list</var> specifies the statistics to be collected from the execution of <var class="command">command</var>. The expressions in <var class="command">exp_list</var> follow the grammar given in <var class="command">exp_list</var>. If no expressions are given, <var class="command">exp_list</var> assumes a default depending upon whether <var class="command">command</var> changes results in <code class="command">e()</code> and <code class="command">r()</code>. If <var class="command">command</var> changes results in <code class="command">e()</code>, the default is <code class="command">_b</code>. If <var class="command">command</var> changes results in <code class="command">r()</code> (but not <code class="command">e()</code>), the default is all the scalars posted to <code class="command">r()</code>. It is an error not to specify an expression in <var class="command">exp_list</var> otherwise. <span data-options="linkspdf">{marker linkspdf}_<span>{nobreak None}_ <span>{title None:Links to PDF documentation}_ [<var class="command">varlist</var><strong></strong>](http://www.stata.com/manuals14/dstatsbyquickstart.pdf">Quick start</a> <a href="http://www.stata.com/manuals14/dstatsbyremarksandexamples.pdf">Remarks and examples</a> <span>{pstd None}_ The above sections are not included in this help file. <span data-options="options">{marker options}_<span>{nobreak None}_ <span>{title None:Options}_ <span>{dlgtab None:Main}_ <span>{phang None}_ <code class="command">by(</code><a href="http://www.stata.com/help.cgi?varlist) [<code class="command">, missing</code>]<code class="command">)</code> specifies a list of existing variables that would normally appear in the <code class="command">by</code> <var class="command">varlist</var><code class="command">:</code> section of the command if you were to issue the command interactively. By default, <code class="command">statsby</code> ignores groups in which one or more of the <code class="command">by()</code> variables is missing. Alternatively, <code class="command" data-options="missing">missing</code> causes missing values to be treated like any other values in the by-groups, and results from the entire dataset are included with use of the <code class="command" data-options="subsets">subsets</code> option. If <code class="command">by()</code> is not specified, <var class="command">command</var> will be run on the entire dataset. <var class="command">varlist</var> can contain both numeric and string variables. <span>{dlgtab None:Options}_ <span>{phang None}_ <code class="command" data-options="clear">clear</code> specifies that it is okay to replace the data in memory, even though the current data have not been saved to disk. <span>{phang None}_ <code class="command" data-options="saving">saving</code><code class="command">(</code><var class="command">filename</var> [<code class="command">,</code> <var class="command">suboptions</var>]<code class="command">)</code> creates a Stata data file (<code class="command">.dta</code> file) consisting of (for each statistic in <var class="command">exp_list</var>) a variable containing the replicates.</td>
</tr>
</tfoot>

</table>

See help `prefix_saving_option`, for details about `suboptions`.

`total` specifies that `command` be run on the entire dataset, in
addition to the groups specified in the `by()` option.

`subsets` specifies that `command` be run for each group defined by any
combination of the variables in the `by()` option.

### Reporting

`nodots` suppresses display of the replication dots. By default, one dot
character is printed for each by-group. A red \`x' is printed if
`command` returns with an error or one of the values in `exp_list` is
missing.

`dots(#)` displays dots every `#` replications. `dots(0)` is a synonym
for `nodots`.

`noisily` causes the output of `command` to be displayed for each
by-group. This option implies the `nodots` option.

`trace` causes a trace of the execution of `command` to be displayed.
This option implies the `noisily` option.

`nolegend` suppresses the display of the table legend, which identifies
the rows of the table with the expressions they represent.

`verbose` requests that the full table legend be displayed. By default,
coefficients and standard errors are not displayed.

### Advanced

`basepop(exp)` specifies a base population that `statsby` uses to
evaluate the `command` and to set up for collecting statistics. The
default base population is the entire dataset, or the dataset specified
by any
**[<strong>if</strong>](http://www.stata.com/help.cgi?if)**
or
**[<strong>in</strong>](http://www.stata.com/help.cgi?in)**
conditions specified on the `command`.

One situation where `basepop()` is useful is collecting statistics over
the panels of a panel dataset by using an estimator that works for time
series, but not panel data, for example,

`. statsby, by(mypanels) basepop(mypanels==2): arima ...`

`force` suppresses the restriction that `command` not be a `svy`
command. `statsby` does not perform subpopulation estimation for survey
data, so it should not be used with `svy`. `statsby` reports an error
when it encounters `svy` in `command` if the `force` option is not
specified. This option is seldom used, so use it only if you know what
you are doing.

`forcedrop` forces `statsby` to drop all observations except those in
each by-group before calling `command` for the group. This allows
`statsby` to work with user-written programs that completely ignore
**[<strong>if</strong>](http://www.stata.com/help.cgi?if)**
and
**[<strong>in</strong>](http://www.stata.com/help.cgi?in)**
but do not return an error when either is specified. `forcedrop` is
seldom used.
