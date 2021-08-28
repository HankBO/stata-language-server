## Syntax

Create document for export

`putpdf begin` \[`, document_options`\]

Add paragraph to document

`putpdf paragraph` \[`, paragraph_options`\]

Add text to paragraph

`putpdf text (exp)` \[`, text_options`\]

Add image to paragraph

`putpdf image filename` \[`, image_options`\]

Add table to document

`putpdf table tablename = (nrows, ncols)` \[`,`
`table_options`\]

`putpdf table tablename = data(varlist)` <span
class="command">\[`if`\] \[`in`\]_ \[`, varnames obsno`
`table_options`\]

`putpdf table tablename = matrix(matname)` \[`, nformat(%fmt)`
`rownames colnames table_options`\]

`putpdf table tablename = mata(matname)` \[`, nformat(%fmt)`
`table_options`\]

`putpdf table tablename = etable`\[`(#`1 `#`2 ... `#n)`\]
\[`, table_options`\]

`putpdf table tablename = returnset` \[`, table_options`\]

Add content to cell

`putpdf table tablename(i,j) = (exp)` \[`,`
`cell_options`\]

`putpdf table tablename(i,j) = image(filename)` \[`,`
`cell_options`\]

`putpdf table tablename(i,j) = table(mem_tablename)`
\[`, cell_options`\]

Alter table layout

`putpdf table tablename(i,.), row_col_options`

`putpdf table tablename(.,j), row_col_options`

Customize format of cells or table

`putpdf table tablename(i,j)` \[`, cell_options`\]

`putpdftabletablename(numlist_i,.),cell_fmt_optionsputpdftabletablename(.,numlist_j),cell_fmt_optionsputpdftabletablename(numlist_i,numlist_j),cell_fmt_options`

`putpdf table tablename(.,.), cell_fmt_options`

Add page break to document

`putpdf pagebreak`

Add section break to document

`putpdf sectionbreak` \[`, section_options`\]

Describe current document

`putpdf describe`

Describe table

`putpdf describe tablename`

Close and save document

`putpdf save filename` \[`, replace`\]

Close without saving

`putpdf clear`

`tablename` specifies the name of a new table. The name must be a valid
name according to Stata's naming conventions; see <span
options="frnames">{findalias frnames}_.

| document\_options |                                     | Description                           |
|-------------------|-------------------------------------|---------------------------------------|
|                   | `pagesize(psize)`                   | set page size of document             |
|                   | `landscape`                         | set document orientation to landscape |
|                   | `font(fspec)`                       | set font, font size, and font color   |
|                   | `halign(hvalue)`                    | set horizontal alignment of document  |
|                   | `margin(type, #`\[`unit`\]`)` | set page margins of document          |
|                   | `bgcolor(color)`                    | set background color                  |

| paragraph\_options |                                           | Description                                       |
|--------------------|-------------------------------------------|---------------------------------------------------|
|                    | `font(fspec)`                             | set font, font size, and font color               |
|                    | `halign(hvalue)`                          | set paragraph alignment                           |
|                    | `valign(vvalue)`                          | set vertical alignment of characters on each line |
|                    | `indent(indenttype, #`\[`unit`\]`)` | set paragraph indentation                         |
|                    | `spacing(position, #`\[`unit`\]`)`  | set spacing between lines of text                 |
|                    | `bgcolor(color)`                          | set background color                              |

| text\_options |                                                     | Description                                     |
|---------------|-----------------------------------------------------|-------------------------------------------------|
|               | `nformat(%fmt)`                                     | specify numeric format for text                 |
|               | `font(fspec)`                                       | set font, font size, and font color             |
|               | `bold`                                              | format text as bold                             |
|               | `italic`                                            | format text as italic                           |
|               | `script(sub`|`super)` | set subscript or superscript formatting of text |
|               | `strikeout`                                         | strikeout text                                  |
|               | `underline`                                         | underline text                                  |
|               | `bgcolor(color)`                                    | set background color                            |
|               | `linebreak`\[`(#)`\]                            | add line breaks after text                      |
|               | `allcaps`                                           | format text as all caps                         |

| image\_options |                           | Description                 |
|----------------|---------------------------|-----------------------------|
|                | `width(#`\[`unit`\]`)`  | set image width             |
|                | `height(#`\[`unit`\]`)` | set image height            |
|                | `linebreak`\[`(#)`\]  | add line breaks after image |

| table\_options |                                                                                                      | Description                                         |
|----------------|------------------------------------------------------------------------------------------------------|-----------------------------------------------------|
|                | `memtable`                                                                                           | keep table in memory rather than add it to document |
|                | `width(#`\[`unit`|`%`\] | `matname)` | set table width                                     |
|                | `halign(hvalue)`                                                                                     | set table horizontal alignment                      |
|                | `indent(#`\[`unit)`                                                                              | set table indentation                               |
|                | `spacing(position, #`\[`unit`\]`)`                                                             | set spacing before or after table                   |
|                | `border(bspec)`                                                                                      | set pattern and color for border                    |
|                | `title(string)`                                                                                      | add a title to the table                            |
|                | `note(string)`                                                                                       | add notes to the table                              |

| cell\_options |                          | Description                                    |
|---------------|--------------------------|------------------------------------------------|
|               | `append`                 | append objects to current content of cell      |
|               | `rowspan(#)`             | merge cells vertically                         |
|               | `colspan(#)`             | merge cells horizontally                       |
|               | `span(#1, #2)`           | merge cells both horizontally and vertically   |
|               | `linebreak`\[`(#)`\] | add line breaks into the cell                  |
|               | `cell_fmt_options`       | options that control the look of cell contents |

| row\_col\_options |                                                                       | Description                                    |
|-------------------|-----------------------------------------------------------------------|------------------------------------------------|
|                   | `nosplit`                                                             | prevent row from breaking across pages         |
|                   | `addrows(#` \[`, before`|`after`\]`)` | add `#` rows in specified location             |
|                   | `addcols(#` \[`, before`|`after`\]`)` | add `#` columns in specified location          |
|                   | `drop`                                                                | drop specified row or column                   |
|                   | `cell_fmt_options`                                                    | options that control the look of cell contents |

| cell\_fmt\_options                                                                                                                                                                                                                                                                              |                                                     | Description                                     |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------|-------------------------------------------------|
|                                                                                                                                                                                                                                                                                                 | `margin(type, #`\[`unit`\]`)`                 | set margins                                     |
|                                                                                                                                                                                                                                                                                                 | `halign(hvalue)`                                    | set horizontal alignment                        |
|                                                                                                                                                                                                                                                                                                 | `valign(vvalue)`                                    | set vertical alignment                          |
|                                                                                                                                                                                                                                                                                                 | `border(bspec)`                                     | set pattern and color for border                |
|                                                                                                                                                                                                                                                                                                 | `bgcolor(color)`                                    | set background color                            |
|                                                                                                                                                                                                                                                                                                 | `nformat(%fmt)`                                     | specify numeric format for cell text            |
|                                                                                                                                                                                                                                                                                                 | `font(fspec)`                                       | set font, font size, and font color             |
|                                                                                                                                                                                                                                                                                                 | `bold`                                              | format text as bold                             |
|                                                                                                                                                                                                                                                                                                 | `italic`                                            | format text as italic                           |
| \*                                                                                                                                                                                                                                                                                              | `script(sub`|`super)` | set subscript or superscript formatting of text |
|                                                                                                                                                                                                                                                                                                 | `strikeout`                                         | strikeout text                                  |
|                                                                                                                                                                                                                                                                                                 | `underline`                                         | underline text                                  |
|                                                                                                                                                                                                                                                                                                 | `allcaps`                                           | format text as all caps                         |
|                                                                                                                                                                                                                                                                                                 | `landscape`                                         | set section orientation to landscape            |
|                                                                                                                                                                                                                                                                                                 | `font(fspec)`                                       | set font, font size, and font color             |
|                                                                                                                                                                                                                                                                                                 | `halign(hvalue)`                                    | set horizontal alignment of section             |
|                                                                                                                                                                                                                                                                                                 | `margin(type, #`\[`unit`\]`)`                 | set page margins of section                     |
|                                                                                                                                                                                                                                                                                                 | `bgcolor(color)`                                    | set background color                            |
| \* May only be specified when formatting a single cell. <span options="sectionopts">{marker sectionopts}_{nobreak None} <span options="28">{synoptset 28}_{nobreak None} {synopthdr None:section\_options} {synoptline None} {synopt None}`pagesize(psize)`set page size of section |                                                     |                                                 |

`fspec` is

`fontname` \[`, size` \[`, color`\]\]

`fontname` may be any supported font installed on the user's computer.
Base 14 fonts, Type 1 fonts, and TrueType fonts with an extension of
`.ttf` and `.ttc` are supported. TrueType fonts that cannot be embedded
may not used. If `fontname` includes spaces, then it must be enclosed in
double quotes. The default font is `Helvetica`.

`size` is a numeric value that represents font size measured in points.
The default is `11`.

`color` sets the text color.

`bspec` is

`bordername`\[`, bpattern` \[`, bcolor`\]\]

`bordername` specifies the location of the border.

`bpattern` is a keyword specifying the look of the border. Possible
patterns are `nil` and `single`. The default is `single`. To remove an
existing border, specify `nil` as the `bpattern`.

`bcolor` specifies the border color.

`unit` may be `in` (inch), `pt` (point), `cm` (centimeter), or `twip`
(twentieth of a point). An inch is equivalent to 72 points, 2.54
centimeters, or 1440 twips. The default is `in`.

`color` and `bcolor` may be one of the colors listed in the table of
colors in the
[<var class="command">Appendix</var><strong></strong>](#colors);
a valid RGB value in the form `### ### ###`, for example, `171 248 103`;
or a valid RRGGBB hex value in the form `######`, for example, `ABF867`.
