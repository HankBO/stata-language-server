## Syntax

`separate`
[varname](http://www.stata.com/help.cgi?varname)
_\[`if`\] \[`in`\]_ `, by(groupvar` <span
options="|">{c \|}_ `exp)` \[`options`\]

| Options                                                  |                      | Description                                                                                                                                                   |
|----------------------------------------------------------|----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Main                                                     |                      |                                                                                                                                                               |
| \*                                                       | `by(groupvar)`       | categorize observations into groups defined by `groupvar`                                                                                                     |
| \*                                                       | `by(exp)`            | categorize observations into two groups defined by `exp`                                                                                                      |
| Options                                                  |                      |                                                                                                                                                               |
|                                                          | `generate(stubname)` | name new variables by suffixing values to `stubname`; default is to use [varname](http://www.stata.com/help.cgi?varname) as prefix |
|                                                          | `sequential`         | use as name suffix categories numbered sequentially from 1                                                                                                    |
|                                                          | `missing`            | create variables for the missing values                                                                                                                       |
|                                                          | `shortlabel`         | create shorter variable labels                                                                                                                                |
| \* Either `by(groupvar)` or `by(exp)` must be specified. |                      |                                                                                                                                                               |
