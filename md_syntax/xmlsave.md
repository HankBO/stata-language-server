## Syntax

Export dataset in memory to XML format

`xmlsave filename` _\[`if`\] \[`in`\]_
\[`, xmlsave_options`\]

Export subset of dataset in memory to XML format

`xmlsave`
[varlist](http://www.stata.com/help.cgi?varlist)
`using filename` _\[`if`\] \[`in`\]_ \[`,`
`xmlsave_options`\]

Import XML-format dataset

`xmluse filename` \[`, xmluse_options`\]

| xmlsave\_options |                  | Description                                  |
|------------------|------------------|----------------------------------------------|
| Main             |                  |                                              |
|                  | `doctype(dta)`   | save XML file by using Stata's `.dta` format |
|                  | `doctype(excel)` | save XML file by using Excel XML format      |
|                  | `dtd`            | include Stata DTD in XML file                |
|                  | `legible`        | format XML to be more legible                |
|                  | `replace`        | overwrite existing `filename`                |

| xmluse\_options |                                 | Description                                     |
|-----------------|---------------------------------|-------------------------------------------------|
|                 | `doctype(dta)`                  | load XML file by using Stata's `.dta` format    |
|                 | `doctype(excel)`                | load XML file by using Excel XML format         |
|                 | `sheet("sheetname")`        | Excel worksheet to load                         |
|                 | `cells(upper-left:lower-right)` | Excel cell range to load                        |
|                 | `datestring`                    | import Excel dates as strings                   |
|                 | `allstring`                     | import all Excel data as strings                |
|                 | `firstrow`                      | treat first row of Excel data as variable names |
|                 | `missing`                       | treat inconsistent Excel types as missing       |
|                 | `nocompress`                    | do not compress Excel data                      |
|                 | `clear`                         | replace data in memory                          |
