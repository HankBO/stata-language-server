## Syntax

`dfuller`
[varname](http://www.stata.com/help.cgi?varname)
_\[`if`\] \[`in`\]_ \[`, options`\]

| Options                                                                                                                                               |              | Description                          |
|-------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|--------------------------------------|
| Main                                                                                                                                                  |              |                                      |
|                                                                                                                                                       | `noconstant` | suppress constant term in regression |
|                                                                                                                                                       | `trend`      | include trend term in regression     |
|                                                                                                                                                       | `drift`      | include drift term in regression     |
|                                                                                                                                                       | `regress`    | display regression table             |
|                                                                                                                                                       | `lags(#)`    | include `#` lagged differences       |
| You must `tsset` your data before using `dfuller`; see [<strong>[TS]</strong> tsset](http://www.stata.com/help.cgi?tsset). |              |                                      |
| `varname` may contain time-series operators; see [<strong>tsvarlist</strong>](http://www.stata.com/help.cgi?tsvarlist).    |              |                                      |
