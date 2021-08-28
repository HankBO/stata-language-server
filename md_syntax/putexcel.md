## Syntax

Set workbook for export

`putexcel set filename` \[`,`
[<var class="command">set_options</var><strong></strong>](#setopts)\]

Write expression to Excel

`putexcel`
[<var class="command">ul_cell</var><strong></strong>](#ulcell)
`=`
[<var class="command">exp</var><strong></strong>](http://www.stata.com/help.cgi?exp)
\[`,`
[<var class="command">export_options</var><strong></strong>](#exptopts)
[<var class="command">format_options</var><strong></strong>](#fmtopts)\]

Export Stata matrix to Excel

`putexcel`
[<var class="command">ul_cell</var><strong></strong>](#ulcell)
`= matrix(name)` \[`,`
[<var class="command">export_options</var><strong></strong>](#exptopts)
[<var class="command">format_options</var><strong></strong>](#fmtopts)\]

Export Stata graph, path diagram, or other picture to Excel

`putexcel`
[<var class="command">ul_cell</var><strong></strong>](#ulcell)
`= picture(filename)`

Export returned results to Excel

`putexcel`
[<var class="command">ul_cell</var><strong></strong>](#ulcell)
`= returnset` \[`,`
[<var class="command">export_options</var><strong></strong>](#exptopts)\]

Write formula to Excel

`putexcel`
[<var class="command">ul_cell</var><strong></strong>](#ulcell)
`= formula(formula)` \[`,`
[<var class="command">export_options</var><strong></strong>](#exptopts)\]

Format cells

`putexcel`
[<var class="command">cellrange</var><strong></strong>](#cellrange)`,`
`overwritefmt`
[<var class="command">format_options</var><strong></strong>](#fmtopts)

Add the coefficient table from the last estimation command to Excel file

`putexcel`
[<var class="command">ul_cell</var><strong></strong>](#ulcell)
`= etable`\[`(#`1 `#`2 ... `#n)`\]

Close current Excel file and write file to disk

`putexcel close`

Describe current export settings

`putexcel describe`

Clear current export settings

`putexcel clear`

`ul_cell` is a valid Excel upper-left cell specified using standard
Excel notation, for example, `A1` or `D4`.

`cellrange` is `ul_cell` or `ul_cell:lr_cell`, where `lr_cell` is a
valid Excel lower-right cell, for example, `A1`, `A1:D1`, `A1:A4`, or
`A1:D4`.

| set\_options |                                        | Description                                                  |
|--------------|----------------------------------------|--------------------------------------------------------------|
|              | `sheet(sheetname` \[`, replace`\]`)` | specify the worksheet to use; default is the first worksheet |
|              | `modify`                               | modify Excel file                                            |
|              | `open`                                 | open Excel file in memory                                    |
|              | `replace`                              | overwrite Excel file                                         |

| export\_options |                 | Description                                                                                                |
|-----------------|-----------------|------------------------------------------------------------------------------------------------------------|
| Main            |                 |                                                                                                            |
|                 | `overwritefmt`  | overwrite existing cell formatting when exporting new content                                              |
|                 | `asdate`        | convert Stata date (`%td`-formatted) `exp` to an Excel date                                                |
|                 | `asdatetime`    | convert Stata datetime (`%tc`-formatted) `exp` to an Excel datetime                                        |
|                 | `asdatenum`     | convert Stata date `exp` to an Excel date number, preserving the cell's format                             |
|                 | `asdatetimenum` | convert Stata datetime `exp` to an Excel datetime number, preserving the cell's format                     |
|                 | `names`         | also write row names and column names for matrix `name`; may not be combined with `rownames` or `colnames` |
|                 | `rownames`      | also write matrix row names for matrix `name`; may not be combined with `names` or `colnames`              |
|                 | `colnames`      | also write matrix column names for matrix `name`; may not be combined with `names` or `rownames`           |
|                 | `colwise`       | write results in `returnset` to consecutive columns instead of rows                                        |

| format\_options |                                                             | Description                                       |
|-----------------|-------------------------------------------------------------|---------------------------------------------------|
| Number          |                                                             |                                                   |
|                 | `nformat(excelnfmt)`                                        | specify format for numbers                        |
| Alignment       |                                                             |                                                   |
|                 | `left`                                                      | left-align text                                   |
|                 | `hcenter`                                                   | center text horizontally                          |
|                 | `right`                                                     | right-align text                                  |
|                 | `top`                                                       | vertically align text with the top                |
|                 | `vcenter`                                                   | center text vertically                            |
|                 | `bottom`                                                    | vertically align text with the bottom             |
|                 | `txtindent(#)`                                              | indent text by `#` spaces; default is 0           |
|                 | `txtrotate(#)`                                              | rotate text by `#` degrees; default is 0          |
|                 | \[`no`\]`txtwrap`                                           | wrap text within each cell                        |
|                 | \[`no`\]`shrinkfit`                                         | shrink text to fit the cell width                 |
|                 | `merge`                                                     | merge cells in `cellrange`                        |
|                 | `unmerge`                                                   | separate merged cells identified by `ul_cell`     |
| Font            |                                                             |                                                   |
|                 | `font(fontname` \[`, size` \[`, color`\]\]`)`         | specify font, font size, and font color           |
|                 | \[`no`\]`italic`                                            | format text as italic                             |
|                 | \[`no`\]`bold`                                              | format text as bold                               |
|                 | \[`no`\]`underline`                                         | underline text in the specified cells             |
|                 | \[`no`\]`strikeout`                                         | strikeout text in the specified cells             |
|                 | `script(sub`\|`super`\|`none)`                              | specify subscript or superscript formatting       |
| Border          |                                                             |                                                   |
|                 | `border(border` \[`, style` \[`, color`\]\]`)`        | specify horizontal and vertical cell border style |
|                 | `dborder(direction` \[`, style` \[`, color`\]\]`)`    | specify diagonal cell border style                |
| Fill            |                                                             |                                                   |
|                 | `fpattern(pattern` \[`, fgcolor` \[`, bgcolor`\]\]`)` | specify fill pattern for cells                    |
