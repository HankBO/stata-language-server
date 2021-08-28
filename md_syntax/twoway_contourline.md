## Syntax

`twoway contourline z y x` _\[`if`\]
\[`in`\]_ \[`, options`\]

| Options |                                                                                                                                                  | Description                                                                                                                                      |
|---------|--------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
|         | `ccuts:(numlist)`                                                                                                                            | list of values for contour lines or cuts                                                                                                         |
|         | `levels(#)`                                                                                                                                      | number of contour levels                                                                                                                         |
|         | `minmax`                                                                                                                                         | include contour lines for minimum and maximum of `z`                                                                                             |
|         | `format(`[<strong>%</strong><var class="command">fmt</var><strong></strong>](http://www.stata.com/help.cgi?format)`)` | display format for `ccuts()` or `levels()`                                                                                                       |
|         | `colorlines`                                                                                                                                     | display contour lines in different colors                                                                                                        |
|         | `crule(crule)`                                                                                                                                   | rule for creating contour-line colors                                                                                                            |
|         | `scolor(colorstyle)`                                                                                                                             | starting color for contour rule                                                                                                                  |
|         | `ecolor(colorstyle)`                                                                                                                             | ending color for contour rule                                                                                                                    |
|         | `ccolors:(colorstylelist)`                                                                                                                   | list of colors for contour lines                                                                                                                 |
|         | `clwidths:(linewidthstylelist)`                                                                                                              | list of widths for contour lines                                                                                                                 |
|         | `reversekey`                                                                                                                                     | reverse the order of the keys in [<strong>contour-line legend</strong>](http://www.stata.com/help.cgi?legend_options) |
|         | `interp(interpmethod)`                                                                                                                           | interpolation methods if (`z`, `y`, `x`) does not fill a regular grid                                                                            |

|                  |                                                                                                      |
|------------------|------------------------------------------------------------------------------------------------------|
| `twoway_options` | titles, legends, axes, added lines and text, by, regions, name, aspect ratio, etc. {synoptline None} |

| crule |             | Description                                                                                                                                                                                                                                                              |
|-------|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|       | `hue`       | use equally spaced [<strong>hues</strong>](http://www.stata.com/help.cgi?colorstyle) between `scolor()` and `ecolor()`; the default                                                                                                           |
|       | `chue`      | use equally spaced [<strong>hues</strong>](http://www.stata.com/help.cgi?colorstyle) between `scolor()` and `ecolor()`; unlike `hue`, it uses 360+`hue` of the `ecolor()` if the hue of the `ecolor()` is less than the hue of the `scolor()` |
|       | `intensity` | use equally spaced [<strong>intensities</strong>](http://www.stata.com/help.cgi?colorstyle) with `ecolor()` as the base; `scolor()` is ignored                                                                                                |
|       | `linear`    | use equally spaced interpolations of the [<strong>RGB</strong>](http://www.stata.com/help.cgi?colorstyle) values between `scolor()` and `ecolor()`                                                                                            |

| interpmethod |                   | Description                                  |
|--------------|-------------------|----------------------------------------------|
|              | `thinplatespline` | thin-plate-spline interpolation; the default |
|              | `shepard`         | Shepard interpolation                        |
|              | `none`            | no interpolation; plot data as is            |
