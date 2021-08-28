## Syntax

<table class="standard">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><var class="command">legend_options</var></td>
<td>Description <span>{p2line None}_</td>
</tr>
<tr class="even">
<td><code class="command">legend:(</code>[<var class="command">contents</var>] [<var class="command">location</var>]<code class="command">)</code></td>
<td>standard legend, contents and location</td>
</tr>
<tr class="odd">
<td><code class="command">plegend:(</code>[<var class="command">contents</var>] [<var class="command">location</var>]<code class="command">)</code></td>
<td>[<strong>contourline</strong>](http://www.stata.com/help.cgi?twoway%20contourline) legend, contents and location</td>
</tr>
<tr class="even">
<td><code class="command">clegend:(</code>[<var class="command">suboptions</var>])</td>
<td>[<strong>contour</strong>](http://www.stata.com/help.cgi?twoway%20contour) plot legend; see [<strong>[G-3]</strong> <em>clegend_option</em>](http://www.stata.com/help.cgi?clegend_option) <span>{p2line None}_
<code class="command">legend()</code>, <code class="command">plegend()</code>, and <code class="command">clegend()</code> are <var class="command">merged-implicit</var>; see [<strong>repeated options</strong>](http://www.stata.com/help.cgi?repeated%20options).</td>
</tr>
</tbody>
</table>

where `contents` and `location` specify the contents and the location of
the legends.

<table id="contents" class="standard">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><var class="command">contents</var></td>
<td>Description <span>{p2line None}_</td>
</tr>
<tr class="even">
<td><code class="command">order(</code><var class="command">orderinfo</var><code class="command">)</code></td>
<td>which keys appear and their order</td>
</tr>
<tr class="odd">
<td><code class="command">label:(</code><var class="command">labelinfo</var><code class="command">)</code></td>
<td>override text for a key</td>
</tr>
<tr class="even">
<td><code class="command">holes:(</code><var class="command">numlist</var><code class="command">)</code></td>
<td>positions in legend to leave blank</td>
</tr>
<tr class="odd">
<td><code class="command">all</code></td>
<td>generate keys for all symbols</td>
</tr>
<tr class="even">
<td><code class="command">style:(</code><var class="command">legendstyle</var><code class="command">)</code></td>
<td>overall style of legend</td>
</tr>
<tr class="odd">
<td><code class="command">cols:(</code><var class="command">#</var><code class="command">)</code></td>
<td><var class="command">#</var> of keys per line</td>
</tr>
<tr class="even">
<td><code class="command">rows:(</code><var class="command">#</var><code class="command">)</code></td>
<td>or <var class="command">#</var> of rows</td>
</tr>
<tr class="odd">
<td>[<code class="command">no</code>]<code class="command">colfirst</code></td>
<td>"1, 2, 3" in row 1 or in column 1?</td>
</tr>
<tr class="even">
<td>[<code class="command">no</code>]<code class="command">textfirst</code></td>
<td>symbol-text or text-symbol?</td>
</tr>
<tr class="odd">
<td><code class="command">stack</code></td>
<td>symbol/text vertically stacked</td>
</tr>
<tr class="even">
<td><code class="command">rowgap:(</code><var class="command">relativesize</var><code class="command">)</code></td>
<td>gap between lines</td>
</tr>
<tr class="odd">
<td><code class="command">colgap:(</code><var class="command">relativesize</var><code class="command">)</code></td>
<td>gap between columns</td>
</tr>
<tr class="even">
<td><code class="command">symplacement:(</code><var class="command">compassdirstyle</var><code class="command">)</code></td>
<td>alignment/justification of key's symbol</td>
</tr>
<tr class="odd">
<td><code class="command">keygap:(</code><var class="command">relativesize</var><code class="command">)</code></td>
<td>gap between symbol-text</td>
</tr>
<tr class="even">
<td><code class="command">symysize:(</code><var class="command">relativesize</var><code class="command">)</code></td>
<td>height for key's symbol</td>
</tr>
<tr class="odd">
<td><code class="command">symxsize:(</code><var class="command">relativesize</var><code class="command">)</code></td>
<td>width for key's symbol</td>
</tr>
<tr class="even">
<td><code class="command">textwidth:(</code><var class="command">relativesize</var><code class="command">)</code></td>
<td>width for key's descriptive text</td>
</tr>
<tr class="odd">
<td><code class="command">forcesize</code></td>
<td>always respect <code class="command">symysize()</code>, <code class="command">symxsize()</code>, and <code class="command">textwidth()</code></td>
</tr>
<tr class="even">
<td><code class="command">bmargin:(</code><var class="command">marginstyle</var><code class="command">)</code></td>
<td>outer margin around legend</td>
</tr>
<tr class="odd">
<td><var class="command">textbox_options</var></td>
<td>other text characteristics</td>
</tr>
<tr class="even">
<td><var class="command">title_options</var></td>
<td>titles, subtitles, notes, captions</td>
</tr>
<tr class="odd">
<td><code class="command">region:(</code><var class="command">roptions</var><code class="command">)</code></td>
<td>borders and background shading <span>{p2line None}_
<code class="command">order()</code>, <code class="command">labels()</code>, <code class="command">holes()</code>, and <code class="command">all</code> have no effect on <code class="command">plegend()</code>.</td>
</tr>
</tbody>
</table>

<table id="location" class="standard">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><var class="command">location</var></td>
<td>Description <span>{p2line None}_</td>
</tr>
<tr class="even">
<td><code class="command">off</code> or <code class="command">on</code></td>
<td>suppress or force display of legend</td>
</tr>
<tr class="odd">
<td><code class="command">position:(</code><var class="command">clockposstyle</var><code class="command">)</code></td>
<td>where legend appears</td>
</tr>
<tr class="even">
<td><code class="command">ring(</code><var class="command">ringposstyle</var><code class="command">)</code></td>
<td>where legend appears (detail)</td>
</tr>
<tr class="odd">
<td><code class="command">bplacement:(</code><var class="command">compassdirstyle</var><code class="command">)</code></td>
<td>placement of legend when positioned in the plotregion</td>
</tr>
<tr class="even">
<td><code class="command">span</code></td>
<td>"centering" of legend</td>
</tr>
<tr class="odd">
<td><code class="command">at(</code><var class="command">#</var><code class="command">)</code></td>
<td>allowed with <code class="command">by()</code> only <span>{p2line None}_
See <var class="command">Where legends appear</var> under <var class="command">Remarks</var> below, and see [<strong>Positioning of titles</strong>](title_options##remarks3) in [<strong>[G-3]</strong> <em>title_options</em>](http://www.stata.com/help.cgi?title_options) for definitions of <var class="command">clockposstyle</var> and <var class="command">ringposstyle</var>.</td>
</tr>
</tbody>
</table>

`orderinfo`, the argument allowed by `legend(order())`, is defined as

{`#`\|`-`}
\[`"text"` {nobreak None} \[`"text"` ...\]\]

`labelinfo`, the argument allowed by `legend(label())`, is defined as

`# "text"` \[`"text"` ...\]

`roptions`, the arguments allowed by `legend(region())`, include

|                                   |                                                            |
|-----------------------------------|------------------------------------------------------------|
| `roptions`                        | Description {p2line None}                                  |
| `style:(areastyle)`           | overall style of region                                    |
| `color:(colorstyle)`          | line + fill color and opacity of region                    |
| `fcolor:(colorstyle)`         | fill color and opacity of region                           |
| `lstyle:(linestyle)`          | overall style of border                                    |
| `lcolor:(colorstyle)`         | color and opacity of border                                |
| `lwidth:(linewidthstyle)`     | thickness of border                                        |
| `lpattern:(linepatternstyle)` | border pattern (solid, dashed, etc.)                       |
| `lalign:(linealignmentstyle)` | border alignment (inside, outside, center)                 |
| `margin:(marginstyle)`        | margin between border and contents of legend {p2line None} |
