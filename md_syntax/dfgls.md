## Syntax

`dfgls`
[varname](http://www.stata.com/help.cgi?varname)
_\[`if`\] \[`in`\]_ \[`, options`\]

| Options                                                                                                                                             |             | Description                                                                                                                             |
|-----------------------------------------------------------------------------------------------------------------------------------------------------|-------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Main                                                                                                                                                |             |                                                                                                                                         |
|                                                                                                                                                     | `maxlag(#)` | use `#` as the highest lag order for Dickey-Fuller GLS regressions                                                                      |
|                                                                                                                                                     | `notrend`   | series is stationary around a mean instead of around a linear time trend                                                                |
|                                                                                                                                                     | `ers`       | present interpolated critical values from [<strong>Elliott, Rothenberg, and Stock (1996)</strong>](#ERS1996) |
| You must `tsset` your data before using `dfgls`; see [<strong>[TS]</strong> tsset](http://www.stata.com/help.cgi?tsset). |             |                                                                                                                                         |
| `varname` may contain time-series operators; see [<strong>tsvarlist</strong>](http://www.stata.com/help.cgi?tsvarlist).  |             |                                                                                                                                         |
