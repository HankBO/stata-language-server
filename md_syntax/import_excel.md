## Syntax

Load an Excel file

`import excel` \[`using`\] `filename` \[`, import_excel_options`\]

Load subset of variables from an Excel file

`import excel extvarlist using filename` \[`,`
`import_excel_options`\]

Describe contents of an Excel file

`import excel` \[`using`\] `filename`, `describe`

Save data in memory to an Excel file

`export excel` \[`using`\] `filename` _\[`if`\]
\[`in`\]_ \[`, export_excel_options`\]

Save subset of variables in memory to an Excel file

`export excel`
\[[varlist](http://www.stata.com/help.cgi?varlist)\]
`using filename` _\[`if`\] \[`in`\]_ \[`,`
`export_excel_options`\]

| import\_excel\_options |                                        | Description                                                                                            |
|------------------------|----------------------------------------|--------------------------------------------------------------------------------------------------------|
|                        | `sheet("sheetname")`                   | Excel worksheet to load                                                                                |
|                        | `cellrange([start][:end])`             | Excel cell range to load                                                                               |
|                        | `firstrow`                             | treat first row of Excel data as variable names                                                        |
|                        | `case(preserve`\|`lower`\|`upper)` | preserve the case (the default) or read variable names as lowercase or uppercase when using `firstrow` |
|                        | `allstring`\[`("format")`\]        | import all Excel data as strings; optionally, specify the numeric display format                       |
|                        | `clear`                                | replace data in memory                                                                                 |

{p\_end None}

|                                                                           |     |     |
|---------------------------------------------------------------------------|-----|-----|
| `allstring("format")` and `locale()` do not appear in the dialog box. |     |     |

| export\_excel\_options |                                        | Description                                                                 |
|------------------------|----------------------------------------|-----------------------------------------------------------------------------|
| Main                   |                                        |                                                                             |
|                        | `sheet("sheetname")`               | save to Excel worksheet                                                     |
|                        | `cell(start)`                          | start (upper-left) cell in Excel to begin saving to                         |
|                        | `sheetmodify`                          | modify Excel worksheet                                                      |
|                        | `sheetreplace`                         | replace Excel worksheet                                                     |
|                        | `firstrow(variables`\|`varlabels)` | save variable names or variable labels to first row                         |
|                        | `nolabel`                              | export values instead of value labels                                       |
|                        | `keepcellfmt`                          | when writing data, preserve the cell style and format of existing worksheet |
|                        | `replace`                              | overwrite Excel file                                                        |
| Advanced               |                                        |                                                                             |
|                        | `datestring("datetime_format")`    | save dates as strings with a `datetime_format`                              |
|                        | `missing("repval")`                | save missing values as `repval`                                             |

{p\_end None}

|                                               |     |     |
|-----------------------------------------------|-----|-----|
| `locale()` does not appear in the dialog box. |     |     |

`extvarlist` specifies variable names of imported columns. An
`extvarlist` is one or more of any of the following:

`varnamevarname=columnname`

Example: `import excel make mpg weight price using auto.xlsx, clear`

imports columns A, B, C, and D from the Excel file `auto.xlsx`.

Example: `import excel make=A mpg=B price=D using auto.xlsx, clear`

imports columns A, B, and D from the Excel file `auto.xlsx`. Column C
and any columns after D are skipped.
