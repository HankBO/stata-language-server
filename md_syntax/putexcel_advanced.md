## Syntax

Set workbook for export

`putexcel set`
[<var class="command">filename</var><strong></strong>](http://www.stata.com/help.cgi?filename)
\[`,`
[<var class="command">set_options</var><strong></strong>](putexcel%20advanced##setopts)\]

Specify formatting and output

`putexcel`
[<var class="command">spec</var><strong></strong>](putexcel%20advanced##spec)\_1
\[`spec_2` \[...\]\] \[`,`
[<var class="command">export_options</var><strong></strong>](putexcel%20advanced##exptopts)
[<var class="command">format_options</var><strong></strong>](putexcel%20advanced##fmtopts)\]

Close current Excel file and write file to disk

`putexcel close`

Describe current export settings

`putexcel describe`

Clear current export settings

`putexcel clear`

`spec` may be `ul_cell` or `cellrange` of the form `ul_cell:lr_cell`
if no output is to be written or may be one of the following
[<strong>output types</strong>](putexcel%20advanced##output):

`ul_cell=expul_cell:lr_cell=expul_cell=matrix(name)ul_cell=picture(filename)ul_cell=formula(formula)ul_cell=returnsetul_cell=etable`

`ul_cell` is a valid Excel upper-left cell specified using standard
Excel notation, and `lr_cell` is a valid Excel lower-right cell. If you
specify `ul_cell` as the output location multiple times, the rightmost
specification is the one written to the Excel file.

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
