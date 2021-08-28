## Syntax

Slices as totals or percentages of each variable

`graph pie`
[varlist](http://www.stata.com/help.cgi?varlist)
_\[`if`\] \[`in`\]_ \[`weight`\] \[`,`
`options`\]

Slices as totals or percentages within `over()` categories

`graph pie`
[varname](http://www.stata.com/help.cgi?varname)
_\[`if`\] \[`in`\]_ \[`weight`\]`,`
`over(`[varname](http://www.stata.com/help.cgi?varname)`)`
\[`options`\]

Slices as frequencies within `over()` categories

`graph pie` _\[`if`\] \[`in`\]_
\[`weight`\]`,`
`over(`[varname](http://www.stata.com/help.cgi?varname)`)`
\[`options`\]

|           |                                                                                                                                                                                                                                                                                                                                                                                    |
|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `options` | Description {p2line None} {p2coldent None:\* }`over(`[varname](http://www.stata.com/help.cgi?varname)`)`slices are distinct values of `varname` {synopt None: }`missing`do not ignore missing values of [varname](http://www.stata.com/help.cgi?varname) {synopt None: }`allcategories`include all categories in the dataset |

`cw`

casewise treatment of missing values

`noclockwise`

counterclockwise pie chart

`angle0(#)`

angle of first slice; default is `angle(90)`

`sort`

put slices in size order

`sort(varname)`

put slices in `varname` order

`descending`

reverse default or specified order

`pie:(...)`

look of slice, including explosion

`plabel(...)`

labels to appear on the slice

`ptext:(...)`

text to appear on the pie

`intensity(`\[`*`\]`#)`

color intensity of slices

`line(line_options)`

outline of slices

**[<strong>legend(...)</strong>](http://www.stata.com/help.cgi?legend_options)**

legend explaining slices

`std_options`

titles, saving to disk

[<strong>by(</strong><var class="command">varlist</var><strong>, ...)</strong>](http://www.stata.com/help.cgi?by_option)

repeat for subgroups

slice styles before recycle

\* `over(varname)` is required in syntaxes 2 and 3.

The syntax of the `pie()` option is

`pie:(`{`numlist`\|`_all`<span
options=")-">{c )-}_ \[`, pie_subopts`\]`)`

|                             |                                          |
|-----------------------------|------------------------------------------|
| `pie_subopts`               | Description {p2line None}                |
| `explode`                   | explode slice by `relativesize`=3.8      |
| `explode(relativesize)` | explode slice by `relativesize`          |
| `color(colorstyle)`     | color and opacity of slice {p2line None} |

The syntax of the `plabel()` option is

`plabel:(`{`#`\|`_all`<span
options=")-">{c )-}_ <span options="-(">{c
-(}_`sum`\|`percent`\|`name`\|`"text"`<span options=")-">{c
)-}_ \[`, plabel_subopts`\]`)`

|                                                                                                                                                   |                                       |
|---------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------|
| `plabel_subopts`                                                                                                                                  | Description {p2line None}             |
| `format:(`[<strong>%</strong><var class="command">fmt</var><strong></strong>](http://www.stata.com/help.cgi?format)`)` | display format for `sum` or `percent` |
| `gap(relativesize)`                                                                                                                           | additional radial distance            |
| `textbox_options`                                                                                                                                 | look of label {p2line None}           |

The syntax for the `ptext()` option is

`ptext:(#_a #_r "text"` \[`"text"` ...\] \[`#_a #_r`
...\] \[`, ptext_subopts`\]`)`

|                   |                                  |
|-------------------|----------------------------------|
| `ptext_subopts`   | Description {p2line None}        |
| `textbox_options` | look of added text {p2line None} |

`aweight`s, `fweight`s, and `pweight`s are allowed; see
[<strong>weight</strong>](http://www.stata.com/help.cgi?weight).
