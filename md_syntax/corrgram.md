## Syntax

Autocorrelations, partial autocorrelations, and portmanteau (Q)
statistics

`corrgram`
[varname](http://www.stata.com/help.cgi?varname)
_\[`if`\] \[`in`\]_ \[`,`
`corrgram_options`\]

Graph autocorrelations with confidence intervals

`ac`
[varname](http://www.stata.com/help.cgi?varname)
_\[`if`\] \[`in`\]_ \[`, ac_options`\]

Graph partial autocorrelations with confidence intervals

`pac`
[varname](http://www.stata.com/help.cgi?varname)
_\[`if`\] \[`in`\]_ \[`, pac_options`\]

| corrgram\_options |           | Description                                                       |
|-------------------|-----------|-------------------------------------------------------------------|
| Main              |           |                                                                   |
|                   | `lags(#)` | calculate `#` autocorrelations                                    |
|                   | `noplot`  | suppress character-based plots                                    |
|                   | `yw`      | calculate partial autocorrelations by using Yule-Walker equations |

ac\_options

Description

Main

`lags(#)`

calculate `#` autocorrelations

`generate(newvar)`

generate a variable to hold the autocorrelations

`level(#)`

set confidence level; default is `level(95)`

`fft`

calculate autocorrelation by using Fourier transforms

Plot

change look of dropped lines change look of markers (color, size, etc.)
add marker labels; change look or position

CI plot

`ciopts(area_options)`

affect rendition of the confidence bands

Add plots

`"addplot(plot)`

add other plots to the generated graph

Y axis, X axis, Titles, Legend, Overall

`twoway_options`

any options other than `by()` documented in
[<strong>[G-3]</strong> <em>twoway_options</em>](http://www.stata.com/help.cgi?twoway_options)

pac\_options

Description

Main

`lags(#)`

calculate `#` partial autocorrelations

`generate(newvar)`

generate a variable to hold the partial autocorrelations

`yw`

calculate partial autocorrelations by using Yule-Walker equations

`level(#)`

set confidence level; default is `level(95)`

Plot

change look of dropped lines change look of markers (color, size, etc.)
add marker labels; change look or position

CI plot

`ciopts(area_options)`

affect rendition of the confidence bands

SRV plot

`srv`

include standardized residual variances in graph

`srvopts(marker_options)`

affect rendition of the plotted standardized residual variances (SRVs)

Add plots

`"addplot(plot)`

add other plots to the generated graph

Y axis, X axis, Titles, Legend, Overall

`twoway_options`

any options other than `by()` documented in
[<strong>[G-3]</strong> <em>twoway_options</em>](http://www.stata.com/help.cgi?twoway_options)

You must `tsset` your data before using `corrgram`, `ac`, or `pac`; see
[<strong>[TS]</strong> tsset](http://www.stata.com/help.cgi?tsset).
Also, the time series must be dense (nonmissing and no gaps in the time
variable) in the sample if you specify the `fft` option.

`varname` may contain time-series operators; see
[<strong>tsvarlist</strong>](http://www.stata.com/help.cgi?tsvarlist).
