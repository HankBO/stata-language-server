## Syntax

`merge`
\[[varlist](http://www.stata.com/help.cgi?varlist)\]
`using filename` \[`filename ...`\] \[`, options`\]

| Options                                                                                                  |                  | Description                                                                                                                             |
|----------------------------------------------------------------------------------------------------------|------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Options                                                                                                  |                  |                                                                                                                                         |
|                                                                                                          | `keep(varlist)`  | keep only the specified variables from data in `filename`                                                                               |
|                                                                                                          | `_merge(newvar)` | `newvar` marks source of resulting observation; default is `_merge`                                                                     |
|                                                                                                          | `nolabel`        | do not copy value label definitions from `filename`                                                                                     |
|                                                                                                          | `nonotes`        | do not copy notes from `filename`                                                                                                       |
|                                                                                                          | `update`         | replace missing data in memory with data from `filename`                                                                                |
|                                                                                                          | `replace`        | replace nonmissing data in memory with data from `filename`                                                                             |
|                                                                                                          | `nokeep`         | drop observations in using dataset that do not match                                                                                    |
|                                                                                                          | `nosummary`      | drop summary variables when multiple `filenames` are specified                                                                          |
| \*                                                                                                       | `unique`         | match variables uniquely identify observations in both data in memory and in `filename`                                                 |
| \*                                                                                                       | `uniqmaster`     | match variables uniquely identify observations in memory                                                                                |
| \*                                                                                                       | `uniqusing`      | match variables uniquely identify observations in `filename`                                                                            |
| \*                                                                                                       | `sort`           | sort master and using datasets by match variables before merge; `sort` implies `unique` if `uniqmaster` or `uniqusing` is not specified |
| \* `unique`, `uniqmaster`, `uniqusing`, and `sort` require `varlist` (the match variables) be specified. |                  |                                                                                                                                         |
