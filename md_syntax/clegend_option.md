## Syntax

<table class="standard">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><var class="command">clegend_option</var></td>
<td>Description <span>{p2line None}_</td>
</tr>
<tr class="even">
<td><code class="command">clegend:(</code>[<var class="command">suboptions</var>]<code class="command">)</code></td>
<td>contour-legend contents, appearance, and location <span>{p2line None}_
<code class="command">clegend()</code> is <var class="command">merged-implicit</var>; see [<strong>repeated options</strong>](http://www.stata.com/help.cgi?repeated%20options).</td>
</tr>
</tbody>
</table>

| suboptions                |                        | Description           |
|---------------------------|------------------------|-----------------------|
| Contour legend appearance |                        |                       |
|                           | `width(relativesize)`  | width of contour key  |
|                           | `height(relativesize)` | height of contour key |

|                             |                                                                  |
|-----------------------------|------------------------------------------------------------------|
| `altaxis`                   | move the contour key's axis to the other side of the contour key |
| `bmargin:(marginstyle)` | outer margin around legend                                       |
| `title_options`             | titles, subtitles, notes, captions                               |
| `region:(roptions)`     | borders and background shading                                   |

Contour legend location

suppress or force display of legend where legend appears where legend
appears (detail) placement of legend when positioned in the plotregion
allowed with only overall style of region line and fill color of region
fill color of region overall style of border color of border thickness
of border border pattern (solid, dashed, etc.) line alignment (inside,
outside, center) margin between border and contents of legend

See `Where contour legends appear` under `Remarks` below, and see
`Positioning of titles` in
[<strong>[G-3]</strong> <em>title_options</em>](http://www.stata.com/help.cgi?title_options)
for definitions of `clockposstyle` and `ringposstyle`. <span
options="roptions">{marker roptions}_{nobreak None} {p2col
None}`roptions`Description
