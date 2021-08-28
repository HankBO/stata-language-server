## Syntax

\[`twoway`\] `scatter`
[varlist](http://www.stata.com/help.cgi?varlist)
_\[`if`\] \[`in`\]_ \[`weight`\] \[`,`
`options`\]

where `varlist` is

`y_1y_2x`

|                          |                                                                                                  |
|--------------------------|--------------------------------------------------------------------------------------------------|
| `options`                | Description {p2line None}                                                                        |
| `marker_options`         | change look of markers (color, size, etc.)                                                       |
| `marker_label_options`   | add marker labels; change look or position                                                       |
| `connect_options`        | change look of lines or connecting method                                                        |
| `composite_style_option` | overall style of the plot                                                                        |
| `jitter_options`         | jitter marker positions using random noise                                                       |
| `axis_choice_options`    | associate plot with alternate axis                                                               |
| `twoway_options`         | titles, legends, axes, added lines and text, by, regions, name, aspect ratio, etc. {p2line None} |

|                                    |                                             |
|------------------------------------|---------------------------------------------|
| `marker_options`                   | Description {p2line None}                   |
| `msymbol:(symbolstylelist)`    | shape of marker                             |
| `mcolor:(colorstylelist)`      | color and opacity of marker, inside and out |
| `msize:(markersizestylelist)`  | size of marker                              |
| `msangle:(anglestyle)`         | angle of marker symbol                      |
| `mfcolor:(colorstylelist)`     | inside or "fill" color and opacity          |
| `mlcolor:(colorstylelist)`     | color and opacity of outline                |
| `mlwidth:(linewidthstylelist)` | thickness of outline                        |
| `mlalign:(linealignmentstyle)` | outline alignment (inside, outside, center) |
| `mlstyle:(linestylelist)`      | overall style of outline                    |
| `mstyle:(markerstylelist)`     | overall style of marker {p2line None}       |

|                                                                                                 |                                      |
|-------------------------------------------------------------------------------------------------|--------------------------------------|
| `marker_label_options`                                                                          | Description {p2line None}            |
| `mlabel(`[varlist](http://www.stata.com/help.cgi?varlist)`)`         | specify marker variables             |
| `mlabposition:(clockposlist)`                                                               | where to locate label                |
| `mlabvposition:(`[varname](http://www.stata.com/help.cgi?varname)`)` | where to locate label 2              |
| `mlabgap:(relativesizelist)`                                                                | gap between marker and label         |
| `mlabangle:(anglestylelist)`                                                                | angle of label                       |
| `mlabsize:(textsizestylelist)`                                                              | size of label                        |
| `mlabcolor:(colorstylelist)`                                                                | color and opacity of label           |
| `mlabtextstyle:(textstylelist)`                                                             | overall style of text                |
| `mlabstyle:(markerlabelstylelist)`                                                          | overall style of label {p2line None} |

|                                                                                             |                                          |
|---------------------------------------------------------------------------------------------|------------------------------------------|
| `connect_options`                                                                           | Description {p2line None}                |
| `connect:(connectstylelist)`                                                            | how to connect points                    |
| `sort`\[`(`[varlist](http://www.stata.com/help.cgi?varlist)`)`\] | how to order data before connecting      |
| `cmissing:(`{`y`\|`n`} ...`)` | missing values are ignored               |
| `lpattern:(linepatternstylelist)`                                                       | line pattern (solid, dashed, etc.)       |
| `lwidth:(linewidthstylelist)`                                                           | thickness of line                        |
| `lcolor:(colorstylelist)`                                                               | color and opacity of line                |
| `lalign:(linealignmentstyle)`                                                           | line alignment (inside, outside, center) |
| `lstyle:(linestylelist)`                                                                | overall style of line {p2line None}      |

<table id="composite_style_option" class="standard">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><var class="command">composite_style_option</var></td>
<td>Description <span>{p2line None}_</td>
</tr>
<tr class="even">
<td><code class="command">pstyle:(</code><var class="command">pstylelist</var><code class="command">)</code></td>
<td>all the <code class="command">...style()</code> options above <span>{p2line None}_
See <var class="command">Appendix: Styles and composite styles</var> under <var class="command">Remarks</var> below.</td>
</tr>
</tbody>
</table>

<table id="jitter_options" class="standard">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><var class="command">jitter_options</var></td>
<td>Description <span>{p2line None}_</td>
</tr>
<tr class="even">
<td><code class="command">jitter(</code><var class="command">relativesizelist</var><code class="command">)</code></td>
<td>perturb location of point</td>
</tr>
<tr class="odd">
<td><code class="command">jitterseed(</code><var class="command">#</var><code class="command">)</code></td>
<td>random-number seed for <code class="command">jitter()</code> <span>{p2line None}_
See <var class="command">Jittered markers</var> under <var class="command">Remarks</var> below.</td>
</tr>
</tbody>
</table>

|                             |                                     |
|-----------------------------|-------------------------------------|
| `axis_choice_options`       | Description {p2line None}           |
| `yaxis:(#` \[`#` ...\]`)` | which `y` axis to use               |
| `xaxis:(#` \[`#` ...\]`)` | which `x` axis to use {p2line None} |

|                                                                                                                                                              |                                           |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------|
| `twoway_options`                                                                                                                                             | Description {p2line None}                 |
| `added_line_options`                                                                                                                                         | draw lines at specified `y` or `x` values |
| `added_text_options`                                                                                                                                         | display text at specified (`y`,`x`) value |
| `axis_options`                                                                                                                                               | labels, ticks, grids, log scales          |
| `title_options`                                                                                                                                              | titles, subtitles, notes, captions        |
| `legend_options`                                                                                                                                             | legend explaining what means what         |
| [<strong>scale(</strong><var class="command">#</var><strong>)</strong>](http://www.stata.com/help.cgi?scale_option)               | resize text and markers                   |
| `region_options`                                                                                                                                             | outlining, shading, aspect ratio          |
| `aspect_option`                                                                                                                                              | constrain aspect ratio of plot region     |
| [<strong>scheme(</strong><var class="command">schemename</var><strong>)</strong>](http://www.stata.com/help.cgi?scheme_option)    | overall look                              |
| [<strong>play(</strong><var class="command">recordingname</var><strong>)</strong>](http://www.stata.com/help.cgi?play_option)     | play edits from `recordingname`           |
| [<strong>by(</strong><var class="command">varlist</var><strong>, ...)</strong>](http://www.stata.com/help.cgi?by_option)          | repeat for subgroups                      |
| [<strong>nodraw</strong>](http://www.stata.com/help.cgi?nodraw_option)                                                            | suppress display of graph                 |
| [<strong>name(</strong><var class="command">name</var><strong>, ...)</strong>](http://www.stata.com/help.cgi?name_option)         | specify name for graph                    |
| [<strong>saving(</strong><var class="command">filename</var><strong>, ...)</strong>](http://www.stata.com/help.cgi?saving_option) | save graph in file                        |
| `advanced_options`                                                                                                                                           | difficult to explain {p2line None}        |

`aweight`s, `fweight`s, and `pweight`s are allowed; see
[<strong>weight</strong>](http://www.stata.com/help.cgi?weight).
