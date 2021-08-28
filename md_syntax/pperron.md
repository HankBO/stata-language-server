## Syntax

`pperron`
[varname](http://www.stata.com/help.cgi?varname)
_\[`if`\] \[`in`\]_ \[`, options`\]

| Options                                                                                                                                               |              | Description                      |
|-------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|----------------------------------|
| Main                                                                                                                                                  |              |                                  |
|                                                                                                                                                       | `noconstant` | suppress constant term           |
|                                                                                                                                                       | `trend`      | include trend term in regression |
|                                                                                                                                                       | `regress`    | display regression table         |
|                                                                                                                                                       | `lags(#)`    | use `#` Newey-West lags          |
| You must `tsset` your data before using `pperron`; see [<strong>[TS] tsset</strong>](http://www.stata.com/help.cgi?tsset). |              |                                  |
| `varname` may contain time-series operators; see [<strong>tsvarlist</strong>](http://www.stata.com/help.cgi?tsvarlist).    |              |                                  |
