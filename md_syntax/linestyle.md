## Syntax

|                            |                                                                                                                                                                                                                                                |
|----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `linestyle`                | Description {p2line None}                                                                                                                                                                                                                      |
| `foreground`               | borders, axes, etc., in foreground color                                                                                                                                                                                                       |
| `grid`                     | grid lines                                                                                                                                                                                                                                     |
| `minor_grid`               | a lesser grid line or same as `grid`                                                                                                                                                                                                           |
| `major_grid`               | a bolder grid line or same as `grid`                                                                                                                                                                                                           |
| `refline`                  | reference lines                                                                                                                                                                                                                                |
| `yxline`                   | `yline()` or `xline()`                                                                                                                                                                                                                         |
| `none`                     | nonexistent line                                                                                                                                                                                                                               |
| `p1` - `p15`               | used by first - fifteenth "line" plot                                                                                                                                                                                                          |
| `p1bar` - `p15bar`         | used by first - fifteenth "bar" plot                                                                                                                                                                                                           |
| `p1box` - `p15box`         | used by first - fifteenth "box" plot                                                                                                                                                                                                           |
| `p1area` - `p15area`       | used by first - fifteenth "area" plot                                                                                                                                                                                                          |
| `p1solid` - `p15solid`     | same as `p1` - `p15` but always solid                                                                                                                                                                                                          |
| `p1mark` - `p15mark`       | markers for first - fifteenth plot                                                                                                                                                                                                             |
| `p1boxmark` - `p15boxmark` | markers for outside values of box plots                                                                                                                                                                                                        |
| `p1dotmark` - `p15dotmark` | markers for dot plots                                                                                                                                                                                                                          |
| `p1other` - `p15other`     | "other" lines, such as [<strong>spikes</strong>](http://www.stata.com/help.cgi?twoway_spike) and [<strong>range plots</strong>](http://www.stata.com/help.cgi?twoway_rcap) {p2line None} |

Other `linestyles` may be available; type

`.`**`. graph query linestyle`**

to obtain the full list installed on your computer.
