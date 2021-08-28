## Syntax

`matlist matrix_exp` \[`, style_options general_options`\]

`matlist matrix_exp , cspec(cspec) rspec(rspec)`
\[`general_options`\]

|                                                                                                |                                                                  |
|------------------------------------------------------------------------------------------------|------------------------------------------------------------------|
| <span options="style_options_table">{marker style\_options\_table}_`style_options`       | Description {p2line None}                                        |
| `lines(lstyle)`                                                                                | lines style; default between headers/labels and data             |
| `border(bspec)`                                                                                | border style; default none                                       |
| `border`                                                                                       | same as `border(all)`                                            |
| `format(%fmt)`                                                                                 | display format; default is `format(%9.0g)`                       |
| `twidth(#)`                                                                                    | row-label width; default is `twidth(12)`                         |
| `left(#)`                                                                                      | left indent for tables; default is `left(0)`                     |
| `right(#)`                                                                                     | right indent for tables; default is `right(0)` {p2line None}     |
| <span options="lstyle">{marker lstyle}_`lstyle`                                          | Lines are drawn ... {p2line None}                                |
| `oneline`                                                                                      | between headers/labels and data; default with no equations       |
| `eq`                                                                                           | between equations; default when equations are present            |
| `rowtotal`                                                                                     | same as `oneline` plus line before last row                      |
| `coltotal`                                                                                     | same as `oneline` plus line before last column                   |
| `rctotal`                                                                                      | same as `oneline` plus line before last row and column           |
| `rows`                                                                                         | between all rows; between row labels and data                    |
| `columns`                                                                                      | between all columns; between column header and data              |
| `cells`                                                                                        | between all rows and columns                                     |
| `none`                                                                                         | suppress all lines {p2line None}                                 |
| <span options="bspec">{marker bspec}_`bspec`                                             | Border lines are drawn ... {p2line None}                         |
| `none`                                                                                         | no border lines are drawn; the default                           |
| `all`                                                                                          | around all four sides                                            |
| `rows`                                                                                         | at the top and bottom                                            |
| `columns`                                                                                      | at the left and right                                            |
| `left`                                                                                         | at the left                                                      |
| `right`                                                                                        | at the right                                                     |
| `top`                                                                                          | at the top                                                       |
| `bottom`                                                                                       | at the bottom {p2line None}                                      |
| <span options="general_options_table">{marker general\_options\_table}_`general_options` | Description {p2line None}                                        |
| `title(string)`                                                                                | title displayed above table                                      |
| `tindent(#)`                                                                                   | indent title `#` spaces                                          |
| `rowtitle(string)`                                                                             | title to display above row names                                 |
| `names:(rows)`                                                                             | display row names                                                |
| `names:(columns)`                                                                          | display column names                                             |
| `names:(all)`                                                                              | display row and column names; the default                        |
| `names:(none)`                                                                             | suppress row and column names                                    |
| `nonames`                                                                                      | same as `names(none)`                                            |
| `showcoleq(ceq)`                                                                               | specify how column equation names are displayed                  |
| `roweqonly`                                                                                    | display only row equation names                                  |
| `coleqonly`                                                                                    | display only column equation names                               |
| `colorcoleq(txt`\|`res)`                                                                   | display mode (color) for column equation names; default is `txt` |
| `keepcoleq`                                                                                    | keep columns of the same equation together                       |
| `aligncolnames(ralign)`                                                                    | right-align column names                                         |
| `aligncolnames(lalign)`                                                                    | left-align column names                                          |
| `aligncolnames(center)`                                                                    | center column names                                              |
| `noblank`                                                                                      | suppress blank line before tables                                |
| `nohalf`                                                                                       | display full matrix even if symmetric                            |
| `nodotz`                                                                                       | display missing value `.z` as blank                              |
| `underscore`                                                                                   | display underscores as blanks in row and column names            |
| `linesize(#)`                                                                                  | overrule `linesize` setting {p2line None}                        |
| <span options="ceq">{marker ceq}_`ceq`                                                   | Equation names are displayed {p2line None}                       |
| `first`                                                                                        | over the first column only; the default                          |
| `each`                                                                                         | over each column                                                 |
| `combined`                                                                                     | centered over all associated columns                             |
| `lcombined`                                                                                    | left-aligned over all associated columns                         |
| `rcombined`                                                                                    | right-aligned over all associated columns {p2line None}          |
