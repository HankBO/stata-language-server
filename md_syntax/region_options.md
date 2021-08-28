## Syntax

<table class="standard">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><var class="command">region_options</var></td>
<td>Description <span>{p2line None}_</td>
</tr>
<tr class="even">
<td><code class="command">ysize:(</code><var class="command">#</var><code class="command">)</code></td>
<td>height of <var class="command">available area</var> (in inches)</td>
</tr>
<tr class="odd">
<td><code class="command">xsize:(</code><var class="command">#</var><code class="command">)</code></td>
<td>width of <var class="command">available area</var> (in inches)</td>
</tr>
<tr class="even">
<td><code class="command">graphregion:(</code><var class="command">suboptions</var><code class="command">)</code></td>
<td>attributes of <var class="command">graph region</var></td>
</tr>
<tr class="odd">
<td><code class="command">plotregion:(</code><var class="command">suboptions</var><code class="command">)</code></td>
<td>attributes of <var class="command">plot region</var> <span>{p2line None}_
Options <code class="command">ysize()</code> and <code class="command">xsize()</code> are <var class="command">unique</var>; options <code class="command">graphregion()</code> and <code class="command">plotregion()</code> are <var class="command">merged-implicit</var>; see [<strong>repeated options</strong>](http://www.stata.com/help.cgi?repeated%20options).</td>
</tr>
</tbody>
</table>

|                                    |                                                      |
|------------------------------------|------------------------------------------------------|
| `suboptions`                       | Description {p2line None}                            |
| `style:(areastyle)`            | overall style of outer region                        |
| `color:(colorstyle)`           | line and fill color and opacity of outer region      |
| `fcolor:(colorstyle)`          | fill color and opacity of outer region               |
| `lstyle:(linestyle)`           | overall style of outline                             |
| `lcolor:(colorstyle)`          | color and opacity of outline                         |
| `lwidth:(linewidthstyle)`      | thickness of outline                                 |
| `lpattern:(linepatternstyle)`  | outline pattern (solid, dashed, etc.)                |
| `lalign:(linealignmentstyle)`  | outline alignment (inside, outside, center)          |
| `istyle:(areastyle)`           | overall style of inner region                        |
| `icolor:(colorstyle)`          | line and fill color and opacity of inner region      |
| `ifcolor:(colorstyle)`         | fill color and opacity of inner region               |
| `ilstyle:(linestyle)`          | overall style of outline                             |
| `ilcolor:(colorstyle)`         | color and opacity of outline                         |
| `ilwidth:(linewidthstyle)`     | thickness of outline                                 |
| `ilpattern:(linepatternstyle)` | outline pattern (solid, dashed, etc.)                |
| `ilalign:(linealignmentstyle)` | outline alignment (inside, outside, center)          |
| `margin:(marginstyle)`         | margin between inner and outer regions {p2line None} |

The `available area`, `graph region`, and `plot region` are defined

<span options="TLC">{c TLC}_

------------------------------------------------------------------------

<span options="TRC">{c TRC}_|`(outer graph region)margin`||<span options="TLC">{c
TLC}_

------------------------------------------------------------------------

<span options="TRC">{c TRC}_|<span
options="|">{c \|}_|`(inner graph region)`|<span
options="|">{c \|}_`titles appear outside`||||`the borders of outer`<span
options="|">{c \|}_|<span
options="TLC">{c TLC}_

------------------------------------------------------------------------

<span options="TRC">{c TRC}_|<span
options="|">{c \|}_`plot region`|||`(outer plot region)margin`||||||<span options="TLC">{c
TLC}_

------------------------------------------------------------------------

<span options="TRC">{c TRC}_|<span
options="|">{c \|}_|

`axes appear on the`

||<span
options="|">{c \|}_|<span
options="|">{c \|}_|<span
options="|">{c \|}_|`borders of the outer`|<span
options="|">{c \|}_|<span
options="|">{c \|}_|<span
options="|">{c \|}_|<span
options="|">{c \|}_`plot region`||||||||||||`(inner plot`<span
options="|">{c \|}_|<span
options="|">{c \|}_|

`plot appears in inner`

||<span
options="|">{c \|}_|`region)`<span
options="|">{c \|}_|<span
options="|">{c \|}_|`plot region`|<span
options="|">{c \|}_|<span
options="|">{c \|}_|<span
options="|">{c \|}_|<span
options="|">{c \|}_|<span
options="|">{c \|}_|<span
options="|">{c \|}_|<span
options="|">{c \|}_|<span
options="|">{c \|}_|<span
options="|">{c \|}_|<span
options="|">{c \|}_|<span
options="|">{c \|}_|<span
options="|">{c \|}_|<span
options="|">{c \|}_|<span
options="BLC">{c BLC}_

------------------------------------------------------------------------

<span options="BRC">{c BRC}_|<span
options="|">{c \|}_|

`Note: What are called`

||<span
options="|">{c \|}_`margin`|<span
options="|">{c \|}_|

`the "graph region" and`

||<span
options="BLC">{c BLC}_

------------------------------------------------------------------------

<span options="BRC">{c BRC}_|<span
options="|">{c \|}_

`the "plot region" are`

||<span
options="|">{c \|}_|

`sometimes the inner`

||<span
options="|">{c \|}_|

`and sometimes the`

|<span options="BLC">{c BLC}_

------------------------------------------------------------------------

<span options="BRC">{c BRC}_|

`outer regions.`

|`margin`|

<span options="BLC">{c BLC}_

------------------------------------------------------------------------

<span options="BRC">{c BRC}_{txt None}

`The available area and outer graph regionare almost coincident; they differ only bythe width of the border.The borders of the outer plot or graphregion are sometimes called the outerborders of the plot or graph region.`
