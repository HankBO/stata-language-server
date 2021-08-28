## Syntax

`graph box`<span options="2">{space 2}_`yvars` <span
class="command">\[`if`\] \[`in`\]_ \[`weight`\] \[`, options`\]

`graph hbox yvars` _\[`if`\] \[`in`\]_
\[`weight`\] \[`, options`\]

where `yvars` is a
[varlist](http://www.stata.com/help.cgi?varlist)

|                                                                                                                                        |                                                      |
|----------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------|
| `options`                                                                                                                              | Description {p2line None}                            |
| [<var class="command">group_options</var><strong></strong>](graph%20box##group_options)                     | groups over which boxes are drawn                    |
| [<var class="command">yvar_options</var><strong></strong>](graph%20box##yvar_options)                       | variables that are the boxes                         |
| [<var class="command">boxlook_options</var><strong></strong>](graph%20box##boxlook_options)                 | how the boxes look                                   |
| [<var class="command">legending_options</var><strong></strong>](graph%20box##legending_options)             | how variables are labeled                            |
| [<var class="command">axis_options</var><strong></strong>](graph%20box##axis_options)                       | how numerical `y` axis is labeled                    |
| [<var class="command">title_and_other_options</var><strong></strong>](graph%20box##title_and_other_options) | titles, added text, aspect ratio, etc. {p2line None} |

|                                                                                                                                                                                                                |                                                     |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------|
| `group_options`                                                                                                                                                                                                | Description {p2line None}                           |
| `over:(`[varname](http://www.stata.com/help.cgi?varname)\[`,` [<var class="command">over_subopts</var><strong></strong>](graph%20box##over_subopts)\]`)` | categories; option may be repeated                  |
| `nofill`                                                                                                                                                                                                       | omit empty categories                               |
| `missing`                                                                                                                                                                                                      | keep missing value as category                      |
| `allcategories`                                                                                                                                                                                                | include all categories in the dataset {p2line None} |

|                |                                                                                     |
|----------------|-------------------------------------------------------------------------------------|
| `yvar_options` | Description {p2line None}                                                           |
| `ascategory`   | treat `yvars` as first `over()` group                                               |
| `asyvars`      | treat first `over()` group as `yvars`                                               |
| `cw`           | calculate variable statistics omitting missing values of any variable {p2line None} |

|                                     |                                                                                                                       |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| `boxlook_options`                   | Description {p2line None}                                                                                             |
| `nooutsides`                        | do not plot outside values                                                                                            |
| `box(#, barlook_options)`   | look of `#`th box                                                                                                     |
| `pcycle:(#)`                    | box styles before [<strong>pstyles</strong>](http://www.stata.com/help.cgi?pstyle) recycle |
| `intensity:(`\[`*`\]`#)`          | intensity of fill                                                                                                     |
| `lintensity:(`\[`*`\]`#)`         | intensity of outline                                                                                                  |
| `medtype:(line`\|`cline`\|`marker)` | how median is indicated in box                                                                                        |
| `medline:(line_options)`        | look of line if `medtype(cline)`                                                                                      |
| `medmarker:(marker_options)`    | look of marker if `medtype(marker)`                                                                                   |
| `cwhiskers`                         | use custom whiskers                                                                                                   |
| `lines:(line_options)`          | look of custom whiskers                                                                                               |
| `alsize(#)`                     | width of adjacent line; default is 67                                                                                 |
| `capsize:(#)`                   | height of cap on adjacent line; default is 0                                                                          |
| `marker:(#`, `marker_options`     | look of `#`th marker and label for                                                                                    |
| `marker_label_options)`           | outside values                                                                                                        |
| `outergap(`\[`*`\]`#)`            | gap between edge and first box and between last box and edge                                                          |
| `boxgap(#)`                     | gap between boxes; default is 33 {p2line None}                                                                        |

|                                                                                                                                    |                                                           |
|------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------|
| `legending_options`                                                                                                                | Description {p2line None}                                 |
| `legend_options`                                                                                                                   | control of `yvar` legend                                  |
| `nolabel`                                                                                                                          | use `yvar` names, not labels, in legend                   |
| `yvaroptions:(`[<var class="command">over_subopts</var><strong></strong>](graph%20box##over_subopts)`)` | `over_subopts` for `yvars`; seldom specified              |
| `showyvars`                                                                                                                        | label `yvars` on `x` axis; seldom specified {p2line None} |

|                                                                                                             |                                         |
|-------------------------------------------------------------------------------------------------------------|-----------------------------------------|
| `axis_options`                                                                                              | Description {p2line None}               |
| `yalternate`                                                                                                | put numerical `y` axis on right (top)   |
| `xalternate`                                                                                                | put categorical `x` axis on top (right) |
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

|                                                                                       |                                                      |
|---------------------------------------------------------------------------------------|------------------------------------------------------|
| `over_subopts`                                                                        | Description {p2line None}                            |
| `total`                                                                               | add total group                                      |
| `relabel:(# "text"` ...`)`                                                    | change axis labels                                   |
| `label:(cat_axis_label_options)`                                                  | rendition of labels                                  |
| `axis:(cat_axis_line_options)`                                                    | rendition of axis line                               |
| `gap(`\[`*`\]`#)`                                                                   | gap between boxes within `over()` category           |
| `sort(`[varname](http://www.stata.com/help.cgi?varname)`)` | put boxes in prespecified order                      |
| `sort(#)`                                                                         | put boxes in median order                            |
| `descending`                                                                          | reverse default or specified box order {p2line None} |

`aweight`s, `fweight`s, and `pweight`s are allowed; see
[<strong>weight</strong>](http://www.stata.com/help.cgi?weight)
and see note concerning weights in
[<strong>[D]</strong> collapse](http://www.stata.com/help.cgi?collapse).
