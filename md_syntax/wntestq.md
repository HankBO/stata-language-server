## Syntax

`wntestq`
[varname](http://www.stata.com/help.cgi?varname)
_\[`if`\] \[`in`\]_ \[`, lags(#)`\]

You must `tsset` your data before using `wntestq`; see
[<strong>[TS] tsset</strong>](http://www.stata.com/help.cgi?tsset).
Also the time series must be dense (nonmissing with no gaps in the time
variable) in the specified sample.

`varname` may contain time-series operators; see
[<strong>tsvarlist</strong>](http://www.stata.com/help.cgi?tsvarlist).
