## Syntax

List business calendars used by the data in memory

`bcal check` \[`varlist`\] \[`, rc0`\]

List filenames and directories of available business calendars

`bcal dir` \[`pattern`\]

Describe the specified business calendar

`bcal describe calname`

Load the specified business calendar

`bcal load calname`

Create a business calendar from the current dataset

`bcal create filename` _\[`if`\]
\[`in`\]_ `, from(varname)` \[`bcal_create_options`\]

where

`varlist` is a list of variable names to be checked for whether they use
business calendars. If not specified, all variables are checked.

`pattern` is the name of a business calendar possibly containing
wildcards `*` and `?`. If `pattern` is not specified, all available
business calendar names are listed.

`calname` is the name of a business calendar either as a name or as a
datetime format; for example, `calname` could be `simple` or
`%tbsimple`.

`filename` is the name of the business calendar file created by `bcal`
`create`.

| bcal\_create\_options           |                                                      | Description                                                                                                                       |
|---------------------------------|------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| Main                            |                                                      |                                                                                                                                   |
| \*                              | `from(varname)`                                      | specify date variable for calendar                                                                                                |
|                                 | `generate(newvar)`                                   | generate `newvar` containing business dates                                                                                       |
|                                 | `excludemissing(varlist` \[`, any`\]`)`            | exclude observations with missing values in `varlist`                                                                             |
|                                 | `personal`                                           | save calendar file in your [<strong>PERSONAL</strong>](http://www.stata.com/help.cgi?sysdir) directory |
|                                 | `replace`                                            | replace file if it already exists                                                                                                 |
| Advanced                        |                                                      |                                                                                                                                   |
|                                 | `purpose(text)`                                      | describe purpose of calendar                                                                                                      |
|                                 | `dateformat(ymd`\|`ydm`\|`myd`\|`mdy`\|`dym`\|`dmy)` | specify date format in calendar file                                                                                              |
|                                 | `range(fromdate todate)`                             | specify range of calendar                                                                                                         |
|                                 | `centerdate(date)`                                   | specify center date of calendar                                                                                                   |
|                                 | `maxgap(#)`                                          | specify maximum gap allowed; default is 10 days                                                                                   |
| \* `from(varname)` is required. |                                                      |                                                                                                                                   |
