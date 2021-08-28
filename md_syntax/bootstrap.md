## Syntax

`bootstrap exp_list` \[`, options eform_option`\] `:`
[<var class="command">command</var><strong></strong>](#command)

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
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="r">reps(#)</code></td>
<td>perform <var class="command">#</var> bootstrap replications; default is <code class="command">reps(50)</code></td>
</tr>
</tbody>
<tbody>
<tr class="odd section">
<td colspan="3">Options</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="str">strata(varlist)</code></td>
<td>variables identifying strata</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="si">size(#)</code></td>
<td>draw samples of size <var class="command">#</var>; default is [<strong>_N</strong>](http://www.stata.com/help.cgi?_N)</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="cl">cluster(varlist)</code></td>
<td>variables identifying resampling clusters</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="id">idcluster(newvar)</code></td>
<td>create new cluster ID variable</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td>[<strong></strong>](http://www.stata.com/help.cgi?prefix_saving_option)
<ul>
</ul>
ving(<var class="command">filename</var><strong>, ...)</strong></td>
<td>save results to <var class="command">filename</var>; save statistics in double precision; save results to <var class="command">filename</var> every <var class="command">#</var> replications</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="bca">bca</code></td>
<td>compute acceleration for BCa confidence intervals</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="tie">ties</code></td>
<td>adjust BC/BCa confidence intervals for ties</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="mse">mse</code></td>
<td>use MSE formula for variance estimation</td>
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
<td><code class="command" data-options="notable">notable</code></td>
<td>suppress table of results</td>
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
<td>display the full table legend</td>
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
<td>use <var class="command">text</var> as title for bootstrap results</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><var class="command">display_options</var></td>
<td>control columns and column formats, row spacing, line width, display of omitted variables and base and empty cells, and factor-variable labeling</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><var class="command">eform_option</var></td>
<td>display coefficient table in exponentiated form</td>
</tr>
</tbody>
<tbody>
<tr class="odd section">
<td colspan="3">Advanced</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="nodrop">nodrop</code></td>
<td>do not drop observations</td>
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
<td><code class="command" data-options="group(varname)">group(varname)</code></td>
<td>ID variable for groups within <code class="command" data-options="cluster()">cluster()</code></td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="jack">jackknifeopts(jkopts)</code></td>
<td>options for [<strong>jackknife</strong>](http://www.stata.com/help.cgi?jackknife)</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="coefl">coeflegend</code></td>
<td>display legend instead of statistics</td>
</tr>
</tbody><tfoot>
<tr class="even footnote">
<td colspan="3"><var class="command">command</var> is any command that follows standard Stata syntax. <var class="command">weights</var> are not allowed in <var class="command">command</var>.</td>
</tr>
<tr class="odd footnote">
<td colspan="3"><code class="command" data-options="group()">group()</code>, <code class="command" data-options="jackknifeopts()">jackknifeopts()</code>, and <code class="command" data-options="coeflegend">coeflegend</code> do not appear in the dialog box.</td>
</tr>
<tr class="even footnote">
<td colspan="3">See [<strong>[R]</strong> bootstrap postestimation](http://www.stata.com/help.cgi?bootstrap_postestimation) for features available after estimation. <span data-options="menu">{marker menu}_<span>{nobreak None}_ <span>{title None:Menu}_ <span>{phang None}_ <strong>Statistics &gt; Resampling &gt; Bootstrap estimation</strong> <span data-options="description">{marker description}_<span>{nobreak None}_ <span>{title None:Description}_ <span>{pstd None}_ <code class="command">bootstrap</code> performs nonparametric bootstrap estimation of specified statistics (or expressions) for a Stata command or a user-written program. Statistics are bootstrapped by resampling the data in memory with replacement. <code class="command">bootstrap</code> is designed for use with nonestimation commands, functions of coefficients, or user-written programs. To bootstrap coefficients, we recommend using the <code class="command">vce(bootstrap)</code> option when allowed by the estimation command. <span>{pstd None}_ <code class="command">bs</code> and <code class="command">bstrap</code> are synonyms for <code class="command">bootstrap</code>. <span data-options="linkspdf">{marker linkspdf}_<span>{nobreak None}_ <span>{title None:Links to PDF documentation}_ [<strong>Mooney and Duval (1993, 11)</strong>](http://www.stata.com/manuals14/rbootstrapquickstart.pdf">Quick start</a> <a href="http://www.stata.com/manuals14/rbootstrapremarksandexamples.pdf">Remarks and examples</a> <a href="http://www.stata.com/manuals14/rbootstrapmethodsandformulas.pdf">Methods and formulas</a> <span>{pstd None}_ The above sections are not included in this help file. <span data-options="options">{marker options}_<span>{nobreak None}_ <span>{title None:Options}_ <span>{dlgtab None:Main}_ <span>{phang None}_ <code class="command" data-options="reps(#)">reps(#)</code> specifies the number of bootstrap replications to be performed. The default is 50. A total of 50-200 replications are generally adequate for estimates of standard error and thus are adequate for normal-approximation confidence intervals; see <a href="#MD1993). Estimates of confidence intervals using the percentile or bias-corrected methods typically require 1,000 or more replications. <span>{dlgtab None:Options}_ <span>{phang None}_ <code class="command" data-options="strata(varlist)">strata(varlist)</code> specifies the variables that identify strata. If this option is specified, bootstrap samples are taken independently within each stratum. <span>{phang None}_ <code class="command" data-options="size(#)">size(#)</code> specifies the size of the samples to be drawn. The default is <code class="command" data-options="_N">_N</code>, meaning to draw samples of the same size as the data. If specified, <var class="command">#</var> must be less than or equal to the number of observations within <code class="command" data-options="strata()">strata()</code>. <span>{pmore None}_ If <code class="command" data-options="cluster()">cluster()</code> is specified, the default size is the number of clusters in the original dataset. For unbalanced clusters, resulting sample sizes will differ from replication to replication. For cluster sampling, <var class="command">#</var> must be less than or equal to the number of clusters within <code class="command" data-options="strata()">strata()</code>. <span>{phang None}_ <code class="command" data-options="cluster(varlist)">cluster(varlist)</code> specifies the variables that identify resampling clusters. If this option is specified, the sample drawn during each replication is a bootstrap sample of clusters. <span>{phang None}_ <code class="command" data-options="idcluster(newvar)">idcluster(newvar)</code> creates a new variable containing a unique identifier for each resampled cluster. This option requires that <code class="command" data-options="cluster()">cluster()</code> also be specified. <span>{phang None}_ <code class="command" data-options="saving">saving</code><code class="command">(</code><var class="command">filename</var> [<code class="command">,</code> <var class="command">suboptions</var>]<code class="command">)</code> creates a Stata data file (<code class="command">.dta</code> file) consisting of (for each statistic in <var class="command">exp_list</var>) a variable containing the replicates.</td>
</tr>
</tfoot>

</table>

See
[<strong>prefix_saving_option</strong>](http://www.stata.com/help.cgi?prefix_saving_option)
for details about `suboptions`.

`bca` specifies that `bootstrap` estimate the acceleration of each
statistic in `exp_list`. This estimate is used to construct BCa
confidence intervals. Type `estat bootstrap, bca` to display the BCa
confidence interval generated by the `bootstrap` command.

`ties` specifies that `bootstrap` adjust for ties in the replicate
values when computing the median bias used to construct BC and BCa
confidence intervals.

`mse` specifies that `bootstrap` compute the variance by using
deviations of the replicates from the observed value of the statistics
based on the entire dataset. By default, `bootstrap` computes the
variance by using deviations from the average of the replicates.

### Reporting

`level(#)`; see
[<strong>[R] estimation options</strong>](estimation%20options##level()).

`notable` suppresses the display of the table of results.

`noheader` suppresses the display of the table header. This option
implies `nolegend`. This option may also be specified when replaying
estimation results.

`nolegend` suppresses the display of the table legend. This option may
also be specified when replaying estimation results.

`verbose` specifies that the full table legend be displayed. By default,
coefficients and standard errors are not displayed. This option may also
be specified when replaying estimation results.

`nodots` suppresses display of the replication dots. By default, one dot
character is displayed for each successful replication. A red 'x' is
displayed if `command` returns an error or if one of the values in
`exp_list` is missing.

`dots(#)` displays dots every `#` replications. `dots(0)` is a synonym
for `nodots`.

`noisily` specifies that any output from `command` be displayed. This
option implies the `nodots` option.

`trace` causes a trace of the execution of `command` to be displayed.
This option implies the `noisily` option.

`title(text)` specifies a title to be displayed above the table of
bootstrap results. The default title is the title stored in `e(title)`
by an estimation command, or if `e(title)` is not filled in,
`Bootstrap results` is used. `title()` may also be specified when
replaying estimation results.

`display_options`: `noci`, `nopvalues`, `noomitted`, `vsquish`,
`noemptycells`, `baselevels`, `allbaselevels`, `nofvlabel`, `fvwrap(#)`,
`fvwrapon(style)`, `cformat(%fmt)`, `pformat(%fmt)`, `sformat(%fmt)`,
and `nolstretch`; see
[<strong>[R] estimation options</strong>](estimation%20options##display_options).

`eform_option` causes the coefficient table to be displayed in
exponentiated form; see
[<strong>[R]</strong> <em>eform_option</em>](http://www.stata.com/help.cgi?eform_option).
`command` determines which `eform_option` is allowed (`eform(string)`
and `eform` are always allowed).

### Advanced

`nodrop` prevents observations outside `e(sample)` and the `if` and `in`
qualifiers from being dropped before the data are resampled.

`nowarn` suppresses the display of a warning message when `command` does
not set `e(sample)`.

`force` suppresses the restriction that `command` not specify weights or
be a `svy` command. This is a rarely used option. Use it only if you
know what you are doing.

`reject(exp)` identifies an expression that indicates when results
should be rejected. When `exp` is true, the resulting values are reset
to missing values.

`seed(#)` sets the random-number seed. Specifying this option is
equivalent to typing the following command prior to calling `bootstrap`:

`. set seed #`

The following options are available with `bootstrap` but are not shown
in the dialog box:

`group(varname)` re-creates `varname` containing a unique identifier for
each group across the resampled clusters. This option requires that
`idcluster()` also be specified.

This option is useful for maintaining unique group identifiers when
sampling clusters with replacement. Suppose that cluster 1 contains 3
groups. If the `idcluster(newclid)` option is specified and cluster 1 is
sampled multiple times, `newclid` uniquely identifies each copy of
cluster 1. If `group(newgroupid)` is also specified, `newgroupid`
uniquely identifies each copy of each group.

`jackknifeopts(jkopts)` identifies options that are to be passed to
[<strong>jackknife</strong>](http://www.stata.com/help.cgi?jackknife)
when it computes the acceleration values for the BCa confidence
intervals. This option requires the `bca` option and is mostly used for
passing the `eclass`, `rclass`, or `n(#)` option to `jackknife`.

`coeflegend`; see
[<strong>[R] estimation options</strong>](estimation%20options##coeflegend).
