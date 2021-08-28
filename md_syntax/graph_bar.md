## Syntax

`graph bar`<span options="2">{space 2}_`yvars` <span
class="command">\[`if`\] \[`in`\]_ \[`weight`\] \[`, options`\]

`graph hbar yvars` _\[`if`\] \[`in`\]_
\[`weight`\] \[`, options`\]

`yvars`

`(asis)`
[varlist](http://www.stata.com/help.cgi?varlist)

`(percent)`
\[[varlist](http://www.stata.com/help.cgi?varlist)\]
\| `(count)`
\[[varlist](http://www.stata.com/help.cgi?varlist)\]

\[`(stat)`\]
[varname](http://www.stata.com/help.cgi?varname){nobreak
None}

`(stat)`

\[`(stat)`\]
[varlist](http://www.stata.com/help.cgi?varlist){nobreak
None}

`(stat)`

\[`(stat)`\]
\[`name=`\][varname](http://www.stata.com/help.cgi?varname)
\[...\]{nobreak None}

`(stat)stat`

`mean median p1 p2` ... `p99 sum count percent min max`

any of the other `stats` defined in
[<strong>[D]</strong> collapse](http://www.stata.com/help.cgi?collapse)

`yvars` is optional if the option `over(varname)` is specified.
`percent` is the default statistic, and percentages are calculated over
`varname`.

`mean` is the default when `varname` or `varlist` is specified and
`stat` is not specified. `p1` means the first percentile, `p2` means the
second percentile, and so on; `p50` means the same as `median`. `count`
means the number of nonmissing values of the specified variable.

|                                                                                                                            |                                                      |
|----------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------|
| `options`                                                                                                                  | Description {p2line None}                            |
| [<var class="command">group_options</var><strong></strong>](#group_options)                     | groups over which bars are drawn                     |
| [<var class="command">yvar_options</var><strong></strong>](#yvar_options)                       | variables that are the bars                          |
| [<var class="command">lookofbar_options</var><strong></strong>](#lookofbar_options)             | how the bars look                                    |
| [<var class="command">legending_options</var><strong></strong>](#legending_options)             | how `yvars` are labeled                              |
| [<var class="command">axis_options</var><strong></strong>](#axis_options)                       | how the numerical y axis is labeled                  |
| [<var class="command">title_and_other_options</var><strong></strong>](#title_and_other_options) | titles, added text, aspect ratio, etc. {p2line None} |

|                                                                                                                                                                                                                |                                                     |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------|
| `group_options`                                                                                                                                                                                                | Description {p2line None}                           |
| `over:(`[varname](http://www.stata.com/help.cgi?varname)\[`,` [<var class="command">over_subopts</var><strong></strong>](graph%20bar##over_subopts)\]`)` | categories; option may be repeated                  |
| `nofill`                                                                                                                                                                                                       | omit empty categories                               |
| `missing`                                                                                                                                                                                                      | keep missing value as category                      |
| `allcategories`                                                                                                                                                                                                | include all categories in the dataset {p2line None} |

|                |                                                                                 |
|----------------|---------------------------------------------------------------------------------|
| `yvar_options` | Description {p2line None}                                                       |
| `ascategory`   | treat `yvars` as first `over()` group                                           |
| `asyvars`      | treat first `over()` group as `yvars`                                           |
| `percentages`  | show percentages within `yvars`                                                 |
| `stack`        | stack the `yvar` bars                                                           |
| `cw`           | calculate `yvar` statistics omitting missing values of any `yvar` {p2line None} |

|                                   |                                                                                                                       |
|-----------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| `lookofbar_options`               | Description {p2line None}                                                                                             |
| `outergap(`\[`*`\]`#)`          | gap between edge and first bar and between last bar and edge                                                          |
| `bargap(#)`                   | gap between `yvar` bars; default is 0                                                                                 |
| `intensity:(`\[`*`\]`#)`        | intensity of fill                                                                                                     |
| `lintensity:(`\[`*`\]`#)`       | intensity of outline                                                                                                  |
| `pcycle:(#)`                  | bar styles before [<strong>pstyles</strong>](http://www.stata.com/help.cgi?pstyle) recycle |
| `bar(#, barlook_options)` | look of `#`th `yvar` bar {p2line None}                                                                                |

<table id="legending_options" class="standard">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><var class="command">legending_options</var></td>
<td>Description <span>{p2line None}_</td>
</tr>
<tr class="even">
<td><var class="command">legend_options</var></td>
<td>control of <var class="command">yvar</var> legend</td>
</tr>
<tr class="odd">
<td><code class="command">nolabel</code></td>
<td>use <var class="command">yvar</var> names, not labels, in legend</td>
</tr>
<tr class="even">
<td><code class="command">yvaroptions:(</code>[<var class="command">over_subopts</var><strong></strong>](graph%20bar##over_subopts)<code class="command">)</code></td>
<td><var class="command">over_subopts</var> for <var class="command">yvars</var>; seldom specified</td>
</tr>
<tr class="odd">
<td><code class="command">showyvars</code></td>
<td>label <var class="command">yvars</var> on x axis; seldom specified</td>
</tr>
<tr class="even">
<td>[<strong></strong>](http://www.stata.com/help.cgi?blabel_option)
<ul>
</ul>
el(...)<strong></strong></td>
<td>add labels to bars <span>{p2line None}_</td>
</tr>
</tbody>
</table>

<table id="axis_options" class="standard">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><var class="command">axis_options</var></td>
<td>Description <span>{p2line None}_</td>
</tr>
<tr class="even">
<td><code class="command">yalternate</code></td>
<td>put numerical y axis on right (top)</td>
</tr>
<tr class="odd">
<td><code class="command">xalternate</code></td>
<td>put categorical x axis on top (right)</td>
</tr>
<tr class="even">
<td><code class="command">exclude0</code></td>
<td>do not force y axis to include 0</td>
</tr>
<tr class="odd">
<td><code class="command">yreverse</code></td>
<td>reverse y axis</td>
</tr>
<tr class="even">
<td><var class="command">axis_scale_options</var></td>
<td>y-axis scaling and look</td>
</tr>
<tr class="odd">
<td><var class="command">axis_label_options</var></td>
<td>y-axis labeling</td>
</tr>
<tr class="even">
<td>[<strong></strong>](http://www.stata.com/help.cgi?axis_title_options)
<ul>
</ul>
tle(...)<strong></strong></td>
<td>y-axis titling <span>{p2line None}_</td>
</tr>
</tbody>
</table>

|                                                                                                                                                     |                                       |
|-----------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------|
| `title_and_other_options`                                                                                                                           | Description {p2line None}             |
| [<strong>text(...)</strong>](http://www.stata.com/help.cgi?added_text_option)                                            | add text on graph; x range \[0,100\]  |
| [<strong>yline(...)</strong>](http://www.stata.com/help.cgi?added_line_options)                                          | add y lines to graph                  |
| `aspect_option`                                                                                                                                     | constrain aspect ratio of plot region |
| `std_options`                                                                                                                                       | titles, graph size, saving to disk    |
| [<strong>by(</strong><var class="command">varlist</var><strong>, ...)</strong>](http://www.stata.com/help.cgi?by_option) | repeat for subgroups {p2line None}    |

<span options="over_subopts">{marker over\_subopts}_ The
`over_subopts` -- used in
`over(`[varname](http://www.stata.com/help.cgi?varname)`,`
`over_subopts)` and, on rare occasion, in
`yvaroptions(over_subopts)` -- are

|                                                                                                  |                                                    |
|--------------------------------------------------------------------------------------------------|----------------------------------------------------|
| `over_subopts`                                                                                   | Description {p2line None}                          |
| `relabel:(# "text"` ...`)`                                                               | change axis labels                                 |
| `label:(cat_axis_label_options)`                                                             | rendition of labels                                |
| `axis:(cat_axis_line_options)`                                                               | rendition of axis line                             |
| `gap(`\[`*`\]`#)`                                                                              | gap between bars within `over()` category          |
| `sort(`[varname](http://www.stata.com/help.cgi?varname)`)`            | put bars in prespecified order                     |
| `sort(#)`                                                                                    | put bars in height order                           |
| `sort((stat)` [varname](http://www.stata.com/help.cgi?varname)`)` | put bars in derived order                          |
| `descending`                                                                                     | reverse default or specified bar order             |
| `reverse`                                                                                        | reverse scale to run from max to min {p2line None} |

`aweight`s, `fweight`s, and `pweight`s are allowed; see
[<strong>weight</strong>](http://www.stata.com/help.cgi?weight)
and see note concerning weights in
[<strong>[D]</strong> collapse](http://www.stata.com/help.cgi?collapse).
