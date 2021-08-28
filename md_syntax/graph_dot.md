## Syntax

`graph dot`<span options="2">{space 2}_`yvars` <span
class="command">\[`if`\] \[`in`\]_ \[`weight`\] \[`, options`\]

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

|                                                                                                                                        |                                                      |
|----------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------|
| `options`                                                                                                                              | Description {p2line None}                            |
| [<var class="command">group_options</var><strong></strong>](graph%20dot##group_options)                     | groups over which lines of dots are drawn            |
| [<var class="command">yvar_options</var><strong></strong>](graph%20dot##yvar_options)                       | variables that are the dots                          |
| [<var class="command">linelook_options</var><strong></strong>](graph%20dot##linelook_options)               | how the lines of dots look                           |
| [<var class="command">legending_options</var><strong></strong>](graph%20dot##legending_options)             | how `yvars` are labeled                              |
| [<var class="command">axis_options</var><strong></strong>](graph%20dot##axis_options)                       | how numerical `y` axis is labeled                    |
| [<var class="command">title_and_other_options</var><strong></strong>](graph%20dot##title_and_other_options) | titles, added text, aspect ratio, etc. {p2line None} |

|                                                                                                                                                                                                                |                                                     |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------|
| `group_options`                                                                                                                                                                                                | Description {p2line None}                           |
| `over:(`[varname](http://www.stata.com/help.cgi?varname)\[`,` [<var class="command">over_subopts</var><strong></strong>](graph%20dot##over_subopts)\]`)` | categories; option may be repeated                  |
| `nofill`                                                                                                                                                                                                       | omit empty categories                               |
| `missing`                                                                                                                                                                                                      | keep missing value as category                      |
| `allcategories`                                                                                                                                                                                                | include all categories in the dataset {p2line None} |

|                |                                                                                 |
|----------------|---------------------------------------------------------------------------------|
| `yvar_options` | Description {p2line None}                                                       |
| `ascategory`   | treat `yvars` as first `over()` group                                           |
| `asyvars`      | treat first `over()` group as `yvars`                                           |
| `percentages`  | show percentages within `yvars`                                                 |
| `cw`           | calculate `yvar` statistics omitting missing values of any `yvar` {p2line None} |

|                                       |                                                                                                                          |
|---------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| `linelook_options`                    | Description {p2line None}                                                                                                |
| `outergap(`\[`*`\]`#)`              | gap between top and first line and between last line and bottom                                                          |
| `linegap(#)`                      | gap between `yvar` lines; default is 0                                                                                   |
| `marker:(#, marker_options)`  | marker used for \#th `yvar` line                                                                                         |
| `pcycle:(#)`                      | marker styles before [<strong>pstyles</strong>](http://www.stata.com/help.cgi?pstyle) recycle |
| `linetype:(dot`\|`line`\|`rectangle)` | type of line                                                                                                             |
| `ndots:(#)`                       | \# of dots if `linetype(dot)`; default is 100                                                                            |
| `dots:(marker_options)`           | look if `linetype(dot)`                                                                                                  |
| `lines:(line_options)`            | look if `linetype(line)`                                                                                                 |
| `rectangles:(area_options)`       | look if `linetype(rectangle)`                                                                                            |
| `rwidth(relativesize)`            | rectangle width if `linetype(rectangle)`                                                                                 |
| \[`no`\]`extend:line`                 | whether line extends through plot region margins; `extendline` is usual default                                          |
| `lowextension(relativesize)`      | extend line through axis (advanced)                                                                                      |
| `highextension(relativesize)`     | extend line through axis (advanced) {p2line None}                                                                        |

|                                                                                                                                    |                                                           |
|------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------|
| `legending_options`                                                                                                                | Description {p2line None}                                 |
| `legend_options`                                                                                                                   | control of `yvar` legend                                  |
| `nolabel`                                                                                                                          | use `yvar` names, not labels, in legend                   |
| `yvaroptions:(`[<var class="command">over_subopts</var><strong></strong>](graph%20dot##over_subopts)`)` | `over_subopts` for `yvars`; seldom specified              |
| `showyvars`                                                                                                                        | label `yvars` on `x` axis; seldom specified {p2line None} |

|                                                                                                             |                                         |
|-------------------------------------------------------------------------------------------------------------|-----------------------------------------|
| `axis_options`                                                                                              | Description {p2line None}               |
| `yalternate`                                                                                                | put numerical `y` axis on right (top)   |
| `xalternate`                                                                                                | put categorical `x` axis on top (right) |
| `exclude0`                                                                                                  | do not force `y` axis to include 0      |
| `yreverse`                                                                                                  | reverse `y` axis                        |
| `axis_scale_options`                                                                                        | `y`-axis scaling and look               |
| `axis_label_options`                                                                                        | `y`-axis labeling                       |
| [<strong>ytitle(...)</strong>](http://www.stata.com/help.cgi?axis_title_options) | `y`-axis titling {p2line None}          |

|                                                                                                                                                     |                                        |
|-----------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------|
| `title_and_other_options`                                                                                                                           | Description {p2line None}              |
| [<strong>text(...)</strong>](http://www.stata.com/help.cgi?added_text_option)                                            | add text on graph; `x` range \[0,100\] |
| [<strong>yline(...)</strong>](http://www.stata.com/help.cgi?added_line_options)                                          | add `y` lines to graph                 |
| `aspect_option`                                                                                                                                     | constrain aspect ratio of plot region  |
| `std_options`                                                                                                                                       | titles, graph size, saving to disk     |
| [<strong>by(</strong><var class="command">varlist</var><strong>, ...)</strong>](http://www.stata.com/help.cgi?by_option) | repeat for subgroups {p2line None}     |

<span options="over_subopts">{marker over\_subopts}_ The
`over_subopts` -- used in
`over(`[varname](http://www.stata.com/help.cgi?varname)`,`
`over_subopts)` and, on rare occasion, in
`yvaroptions(over_subopts)` -- are

|                                                                                                  |                                                       |
|--------------------------------------------------------------------------------------------------|-------------------------------------------------------|
| `over_subopts`                                                                                   | Description {p2line None}                             |
| `relabel:(# "text"` ...`)`                                                               | change axis labels                                    |
| `label:(cat_axis_label_options)`                                                             | rendition of labels                                   |
| `axis:(cat_axis_line_options)`                                                               | rendition of axis line                                |
| `gap(`\[`*`\]`#)`                                                                              | gap between lines within `over()` category            |
| `sort(`[varname](http://www.stata.com/help.cgi?varname)`)`            | put lines in prespecified order                       |
| `sort(#)`                                                                                    | put lines in height order                             |
| `sort((stat)` [varname](http://www.stata.com/help.cgi?varname)`)` | put lines in derived order                            |
| `descending`                                                                                     | reverse default or specified line order {p2line None} |

`aweight`s, `fweight`s, and `pweight`s are allowed; see
[<strong>weight</strong>](http://www.stata.com/help.cgi?weight)
and see note concerning weights in
[<strong>[D]</strong> collapse](http://www.stata.com/help.cgi?collapse).
