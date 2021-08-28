## Syntax

`sunflower yvar xvar` _\[`if`\] \[`in`\]_
\[`weight`\] \[`, options`\]

| options                                     |                  | Description                                                                                                                                         |
|---------------------------------------------|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| Main                                        |                  |                                                                                                                                                     |
|                                             | `nograph`        | do not show graph                                                                                                                                   |
|                                             | `notable`        | do not show summary table; implied when `by()` is specified                                                                                         |
|                                             | `marker_options` | affect rendition of markers drawn at the plotted points                                                                                             |
| Bins/Petals                                 |                  |                                                                                                                                                     |
|                                             | `binwidth(#)`    | width of the hexagonal bins                                                                                                                         |
|                                             | `binar(#)`       | aspect ratio of the hexagonal bins                                                                                                                  |
|                                             | `bin_options`    | affect rendition of hexagonal bins                                                                                                                  |
|                                             | `light(#)`       | minimum observations for a light sunflower; default is `light(3)`                                                                                   |
|                                             | `dark(#)`        | minimum observations for a dark sunflower; default is `dark(13)`                                                                                    |
|                                             | `xcenter(#)`     | `x`-coordinate of the reference bin                                                                                                                 |
|                                             | `ycenter(#)`     | `y`-coordinate of the reference bin                                                                                                                 |
|                                             | `petalweight(#)` | observations in a dark sunflower petal                                                                                                              |
|                                             | `petallength(#)` | length of sunflower petal as a percentage                                                                                                           |
|                                             | `petal_options`  | affect rendition of sunflower petals                                                                                                                |
|                                             | `flowersonly`    | show petals only; do not render bins                                                                                                                |
|                                             | `nosinglepetal`  | suppress single petals                                                                                                                              |
| Add plots                                   |                  |                                                                                                                                                     |
|                                             | `"addplot(plot)` | add other plots to generated graph                                                                                                                  |
| Y axis, X axis, Titles, Legend, Overall, By |                  |                                                                                                                                                     |
|                                             | `twoway_options` | any options documented in [<strong>[G-3]</strong> <em>twoway_options</em>](http://www.stata.com/help.cgi?twoway_options) |

| bin\_options |                                                                    | Description                    |
|--------------|--------------------------------------------------------------------|--------------------------------|
|              | \[`l`|`d`\]`bstyle(areastyle)`       | overall look of hexagonal bins |
|              | \[`l`|`d`\]`bcolor(colorstyle)`      | outline and fill color         |
|              | \[`l`|`d`\]`bfcolor(colorstyle)`     | fill color                     |
|              | \[`l`|`d`\]`blstyle(linestyle)`      | overall look of outline        |
|              | \[`l`|`d`\]`blcolor(colorstyle)`     | outline color                  |
|              | \[`l`|`d`\]`blwidth(linewidthstyle)` | thickness of outline           |

| petal\_options |                                                                    | Description                       |
|----------------|--------------------------------------------------------------------|-----------------------------------|
|                | \[`l`|`d`\]`flstyle(linestyle)`      | overall style of sunflower petals |
|                | \[`l`|`d`\]`flcolor(colorstyle)`     | color of sunflower petals         |
|                | \[`l`|`d`\]`flwidth(linewidthstyle)` | thickness of sunflower petals     |

All options are `rightmost`; see `repeated_options`.

`fweight`s are allowed; see
[<strong>weight</strong>](http://www.stata.com/help.cgi?weight).
