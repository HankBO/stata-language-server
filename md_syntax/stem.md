## Syntax

`stem`
[varname](http://www.stata.com/help.cgi?varname)
_\[`if`\] \[`in`\]_ \[`, options`\]

| Options                                                                                                      |               | Description                                     |
|--------------------------------------------------------------------------------------------------------------|---------------|-------------------------------------------------|
| Main                                                                                                         |               |                                                 |
|                                                                                                              | `prune`       | do not print stems that have no leaves          |
|                                                                                                              | `round(#)`    | round data to this value; default is `round(1)` |
|                                                                                                              | `truncate(#)` | truncate data to this value                     |
|                                                                                                              | `digits(#)`   | digits per leaf; default is `digits(1)`         |
|                                                                                                              | `lines(#)`    | number of stems per interval of 10^`digits`     |
|                                                                                                              | `width(#)`    | stem width; equal to (10^`digits`)/`width`      |
| `by` is allowed; see [<strong>[D]</strong> by](http://www.stata.com/help.cgi?by). |               |                                                 |
