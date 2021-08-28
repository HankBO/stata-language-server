## Syntax

|                 |                                             |
|-----------------|---------------------------------------------|
| `marginstyle`   | Description {p2line None}                   |
| `zero`          | no margin                                   |
| `tiny`          | tiny margin, all four sides (smallest)      |
| `vsmall`        |                                             |
| `small`         |                                             |
| `medsmall`      |                                             |
| `medium`        |                                             |
| `medlarge`      |                                             |
| `large`         |                                             |
| `vlarge`        | very large margin, all four sides (largest) |
| `bottom`        | `medium` on the bottom                      |
| `top`           | `medium` on the top                         |
| `top_bottom`    | `medium` on bottom and top                  |
| `left`          | `medium` on the left                        |
| `right`         | `medium` on the right                       |
| `sides`         | `medium` on left and right                  |
| `# # # #` | specified margins; left, right, bottom, top |
| `marginexp`     | specified margin or margins {p2line None}   |

where `marginexp` is one or more elements of the form

{`lrbt`<span options=")-">{c
)-}_`<space>+-=#`

such as

`l=5l=5 r=5l+5l+5 r=7.2  b-2 t+1`

In both the `# # # #` syntax and the <span options="-(">{c
-(}_`l`\|`r`\|`b`\|`t`<span options=")-">{c
)-}_\[`+`\|`-`\|`=`\]`#` syntax, `#` is interpreted as a
percentage of the minimum of the width and height of the graph. Thus a
distance of 5 is the same in both the vertical and horizontal
directions.

When you apply margins to rotated textboxes, the terms left, right,
bottom, and top refer to the box before rotation; see
[<strong>[G-3]</strong> <em>textbox_options</em>](http://www.stata.com/help.cgi?textbox_options).

Other `marginstyles` may be available; type

`.`**`. graph query marginstyle`**

to obtain the complete list of `marginstyles` installed on your
computer. If other `marginstyles` do exist, they are merely names
associated with `# # # #` margins.
