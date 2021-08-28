## Syntax

Declaring a `_tab` object:

`.obj` = `._tab.new` \[`, options` \]

Setting default parameters:

`.obj.reset` \[`, options` \]

`.obj.width`

{nobreak None}

`width_1width_k,noreformat.obj.titlefmt`

{nobreak None}

`sfmt_1sfmt_k.obj.strfmt`

{nobreak None}

`sfmt_1sfmt_k.obj.numfmt`

{nobreak None}

`nfmt_1nfmt_k.obj.pad`

{nobreak None}

`##.obj.ignore`

{nobreak None}

`item_1item_k.obj.titlecolor`

{nobreak None}

`color_1color_k.obj.strcolor`

{nobreak None}

`color_1color_k.obj.numcolor`

{nobreak None}

`color_1color_k`

Displaying table elements:

`.obj.sep` \[`, top middle bottom` \]

`.obj.titles`

{nobreak None}

`title_1title_k.obj.row`

{nobreak None}

`element_1element_k`

Miscellaneous information:

`.obj.width_of_table`

Post table information to `r()`:

`.obj.post_results`

|                        |                                                                                                                    |
|------------------------|--------------------------------------------------------------------------------------------------------------------|
| `options`              | Description {p2line None}                                                                                          |
| `width(#)`             | default column width; default is 12                                                                                |
| `columns(#)`           | number of columns; default is 2                                                                                    |
| `lmargin(#)`           | left margin; default is 2                                                                                          |
| `tcolor(color)`        | default color for titles; default is `text`                                                                        |
| `ncolor(color)`        | default color for numbers; default is `input`                                                                      |
| `scolor(color)`        | default color for strings; default is `text`                                                                       |
| `lcolor(color)`        | color of the separator lines; default is `text`                                                                    |
| `tfmt(sfmt)`           | default title format                                                                                               |
| `nfmt(nfmt)`           | default numeric format                                                                                             |
| `sfmt(sfmt)`           | default string format                                                                                              |
| `nocommas`             | do not use comma in default numeric formats; default behavior                                                      |
| `commas`               | use comma in default numeric formats                                                                               |
| `ignore(item)`         | ignore `item` if supplied as an argument to `.row`                                                                 |
| `separator(#)`         | automatically separate every `#` rows; default is 0, no separator                                                  |
| `puttab(name)`         | name for Mata object used by `post_results`; default is `_putTab`                                                  |
| `clear(clear_options)` | clear the specified parameters                                                                                     |
| `clear`                | synonym for `clear(all)` {p2line None}                                                                             |
| `clear_options`        | Description {p2line None}                                                                                          |
| `widths`               | clear the column widths                                                                                            |
| `tcolors`              | clear the title colors                                                                                             |
| `ncolors`              | clear the number colors                                                                                            |
| `scolors`              | clear the string colors                                                                                            |
| `tfmts`                | clear the title formats                                                                                            |
| `nfmts`                | clear the number formats                                                                                           |
| `sfmts`                | clear the string formats                                                                                           |
| `paddings`             | clear the column paddings                                                                                          |
| `vseparators`          | remove the vertical separators                                                                                     |
| `rows`                 | reset the row counter to zero                                                                                      |
| `columns`              | reset the column starting positions                                                                                |
| `fmts`                 | reset the default formats                                                                                          |
| `all`                  | shortcut for specifying all the above {p2line None}                                                                |
| Column arguments       | Description {p2line None}                                                                                          |
| `width_#`              | column width                                                                                                       |
| `title_#`              | column title                                                                                                       |
| `nfmt_#`               | numeric format; see [<strong>[D]</strong> format](http://www.stata.com/help.cgi?format) |
| `sfmt_#`               | string format; see [<strong>[D]</strong> format](http://www.stata.com/help.cgi?format)  |
| `color_#`              | `text` (or `txt`), `error`, `result`, or `input`                                                                   |
| `item_#`               | string or value, including a missing value                                                                         |
| `element_#`            | quoted string or expression {p2line None}                                                                          |

Note when the column argument is `.` or `""`, the default value is used.
For `element_#` in `.row`, `""` (the empty string) causes nothing to be
displayed for the specific column, but `.` is interpreted as a missing
value resulting from an expression.
