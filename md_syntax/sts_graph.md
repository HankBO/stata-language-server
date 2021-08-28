## Syntax

`sts graph` _\[`if`\] \[`in`\]_ \[`,`
`options`\]

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
<td><code class="command" data-options="sur">survival</code></td>
<td>graph Kaplan-Meier survivor function; the default</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="fail">failure</code></td>
<td>graph Kaplan-Meier failure function</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="cumh">cumhaz</code></td>
<td>graph Nelson-Aalen cumulative hazard function</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="haz">hazard</code></td>
<td>graph smoothed hazard estimate</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="by(varlist)">by(varlist)</code></td>
<td>estimate and graph separate functions for each group formed by <var class="command">varlist</var></td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="ad">adjustfor(varlist)</code></td>
<td>adjust the estimates to zero values of <var class="command">varlist</var></td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="st">strata(varlist)</code></td>
<td>stratify on different groups of <var class="command">varlist</var></td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="sep">separate</code></td>
<td>show curves on separate graphs; default is to show curves one on top of another</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="ci">ci</code></td>
<td>show pointwise confidence bands</td>
</tr>
</tbody>
<tbody>
<tr class="odd section">
<td colspan="3">At-risk table</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command">risktable</code></td>
<td>show table of number at risk beneath graph</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="riskt">risktable(risk_spec)</code></td>
<td>show customized table of number at risk beneath graph</td>
</tr>
</tbody>
<tbody>
<tr class="odd section">
<td colspan="3">Options</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="l">level(#)</code></td>
<td>set confidence level; default is <code class="command">level(95)</code></td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="per(#)">per(#)</code></td>
<td>units to be used in reported rates</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="nosh">noshow</code></td>
<td>do not show st setting information</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="tma">tmax(#)</code></td>
<td>show graph for t &lt;= <var class="command">#</var></td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="tmi">tmin(#)</code></td>
<td>show graph for t &gt;= <var class="command">#</var></td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="noori">noorigin</code></td>
<td>begin survival (failure) curve at first exit time; default is to begin at t = 0</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command">width(</code><var class="command">#</var>[<var class="command">#</var>...]<code class="command">)</code></td>
<td>override default bandwidth(s)</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="k">kernel(kernel)</code></td>
<td>kernel function; use with <code class="command" data-options="hazard">hazard</code></td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="nob">noboundary</code></td>
<td>no boundary correction; use with <code class="command" data-options="hazard">hazard</code></td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="lost">lost</code></td>
<td>show number lost</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="e">enter</code></td>
<td>show number entered and number lost</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="atr">atrisk</code></td>
<td>show numbers at risk at beginning of each interval</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command">censored(</code><code class="command" data-options="s">single)</code></td>
<td>show one hash mark at each censoring time, no matter what number is censored</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command">censored(</code><code class="command" data-options="n">number)</code></td>
<td>show one hash mark at each censoring time and number censored above hash mark</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command">censored(</code><code class="command" data-options="m">multiple)</code></td>
<td>show multiple hash marks for multiple censoring at the same time</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="censo">censopts(hash_options)</code></td>
<td>affect rendition of hash marks</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="lostop">lostopts(marker_label_options)</code></td>
<td>affect rendition of numbers lost</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="atriskop">atriskopts(marker_label_options)</code></td>
<td>affect rendition of numbers at risk</td>
</tr>
</tbody>
<tbody>
<tr class="odd section">
<td colspan="3">Plot</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="ploto">plotopts(cline_options)</code></td>
<td>affect rendition of plotted lines</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command">plot</code>
<ul>
</ul>
<code class="command">opts(</code><var class="command">cline_options</var><code class="command">)</code></td>
<td>affect rendition of <var class="command">#</var>th plotted line; may not be combined with <code class="command" data-options="separate">separate</code></td>
</tr>
</tbody>
<tbody>
<tr class="odd section">
<td colspan="3">CI plot</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="ciop">ciopts(area_options)</code></td>
<td>affect rendition of confidence bands</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command">ci</code>
<ul>
</ul>
<code class="command">opts(</code><var class="command">area_options</var><code class="command">)</code></td>
<td>affect rendition of <var class="command">#</var>th confidence band; may not be combined with <code class="command" data-options="separate">separate</code></td>
</tr>
</tbody>
<tbody>
<tr class="odd section">
<td colspan="3">Add plots</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="&quot;addplot(addplot_option:plot)&quot;">"addplot(plot)</code></td>
<td>add other plots to the generated graph</td>
</tr>
</tbody>
<tbody>
<tr class="odd section">
<td colspan="3">Y axis, X axis, Titles, Legend, Overall</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><var class="command">twoway_options</var></td>
<td>any options documented in [<strong>[G-3]</strong> <em>twoway_options</em>](http://www.stata.com/help.cgi?twoway_options)</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="byop">byopts(byopts)</code></td>
<td>how subgraphs are combined, labeled, etc.</td>
</tr>
</tbody>
</table>

where `risk_spec` is

\[`numlist`\]\[`, table_options group(group)`\]

`numlist` specifies the points at which the number at risk is to be
evaluated, `table_options` customizes the table of number at risk, and
`group(group)` specifies a specific group/row for `table_options` to be
applied.

| table\_options |                                                   | Description                                               |
|----------------|---------------------------------------------------|-----------------------------------------------------------|
| Main           |                                                   |                                                           |
|                | `axis_label_options`                              | control table by using axis labeling options; seldom used |
|                | `order`**(**`order_spec`**)**                     | select which rows appear and their order                  |
|                | `righttitles`                                     | place titles on right side of the table                   |
|                | `failevents`                                      | show number failed in the at-risk table                   |
|                | `text_options`                                    | affect rendition of table elements and titles             |
| Row titles     |                                                   |                                                           |
|                | `rowtitle(`\[`text`\]\[`, rtext_options`\]`)` | change title for a row                                    |
| Title          |                                                   |                                                           |
|                | `title(`\[`text`\]\[`, ttext_options`\]`)`    | change overall table title                                |

where `order_spec` is

`#` \[**"**`text`**"** \[**"**`text`**"** ...\]\] \[...\]

| text\_options                                |                                     | Description                                    |
|----------------------------------------------|-------------------------------------|------------------------------------------------|
|                                              | `size(textsizestyle)`               | size of text                                   |
|                                              | `color(colorstyle)`                 | color of text                                  |
|                                              | `justification(justificationstyle)` | text left-justified, centered, right-justified |
|                                              | `format(%fmt)`                      | format values per **%**`fmt`                   |
|                                              | `topgap(relativesize)`              | margin above rows                              |
|                                              | `bottomgap(relativesize)`           | margin beneath rows                            |
|                                              | `style(textstyle)`                  | overall style of text                          |
| `style()` does not appear in the dialog box. |                                     |                                                |

| rtext\_options                               |                                     | Description                                    |
|----------------------------------------------|-------------------------------------|------------------------------------------------|
|                                              | `size(textsizestyle)`               | size of text                                   |
|                                              | `color(colorstyle)`                 | color of text                                  |
|                                              | `justification(justificationstyle)` | text left-justified, centered, right-justified |
|                                              | `at(#)`                             | override x position of titles                  |
|                                              | `topgap(relativesize)`              | margin above rows                              |
|                                              | `style(textstyle)`                  | overall style of text                          |
| `style()` does not appear in the dialog box. |                                     |                                                |

| ttext\_options                               |                                     | Description                                    |
|----------------------------------------------|-------------------------------------|------------------------------------------------|
|                                              | `size(textsizestyle)`               | size of text                                   |
|                                              | `color(colorstyle)`                 | color of text                                  |
|                                              | `justification(justificationstyle)` | text left-justified, centered, right-justified |
|                                              | `at(#)`                             | override x position of titles                  |
|                                              | `topgap(relativesize)`              | margin above rows                              |
|                                              | `bottomgap(relativesize)`           | margin beneath rows                            |
|                                              | `style(textstyle)`                  | overall style of text                          |
| `style()` does not appear in the dialog box. |                                     |                                                |

| group |           | Description                                                |
|-------|-----------|------------------------------------------------------------|
|       | `#rownum` | specify group by row number in table                       |
|       | `value`   | specify group by value of group                            |
|       | `label`   | specify group by text of value label associated with group |

| hash\_options |                        | Description                                                                                                                                                                                           |
|---------------|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|               | `line_options`         | change look of dropped lines                                                                                                                                                                          |
|               | `marker_label_options` | add marker labels; any options documented in [<strong>[G-3]</strong> <em>marker_label_options</em>](http://www.stata.com/help.cgi?marker_label_options), except `mlabel()` |

`risktable()` may be repeated and is `merged-explicit`; see
[<strong>repeated options</strong>](http://www.stata.com/help.cgi?repeated%20options).

You must `stset` your data before using `sts graph`; see
[<strong>[ST]</strong> stset](http://www.stata.com/help.cgi?stset).

`fweight`s, `iweight`s, and `pweight`s may be specified using `stset`;
see
[<strong>[ST]</strong> stset](http://www.stata.com/help.cgi?stset).
