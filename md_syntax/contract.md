## Syntax

`contract`
[varlist](http://www.stata.com/help.cgi?varlist)
_\[`if`\] \[`in`\]_ \[`weight`\] \[`,`
`options`\]

| Options                                                                                                                 |                    | Description                                                             |
|-------------------------------------------------------------------------------------------------------------------------|--------------------|-------------------------------------------------------------------------|
| Options                                                                                                                 |                    |                                                                         |
|                                                                                                                         | `freq(newvar)`     | name of frequency variable; default is `_freq`                          |
|                                                                                                                         | `cfreq(newvar)`    | create cumulative frequency variable                                    |
|                                                                                                                         | `percent(newvar)`  | create percentage variable                                              |
|                                                                                                                         | `cpercent(newvar)` | create cumulative percentage variable                                   |
|                                                                                                                         | `float`            | generate percentage variables as type `float`                           |
|                                                                                                                         | `format(format)`   | display format for new percentage variables; default is `format(%8.2f)` |
|                                                                                                                         | `zero`             | include combinations with frequency zero                                |
|                                                                                                                         | `nomiss`           | drop observations with missing values                                   |
| `fweight`s are allowed; see [<strong>weight</strong>](http://www.stata.com/help.cgi?weight). |                    |                                                                         |
