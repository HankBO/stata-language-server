## Syntax

`tssmooth exponential` _\[`type`\] \[_
[newvar](http://www.stata.com/help.cgi?newvar)
`= exp` _\[`if`\] \[`in`\]_ \[`,`
`options`\]

| Options                                                                                                                                                            |               | Description                                                                                            |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|--------------------------------------------------------------------------------------------------------|
| Main                                                                                                                                                               |               |                                                                                                        |
|                                                                                                                                                                    | `replace`     | replace [newvar](http://www.stata.com/help.cgi?newvar) if it already exists |
|                                                                                                                                                                    | `parms(#a)`   | use `#a` as smoothing parameter                                                                        |
|                                                                                                                                                                    | `samp0(#)`    | use `#` observations to obtain initial value for recursion                                             |
|                                                                                                                                                                    | `s0(#)`       | use `#` as initial value for recursion                                                                 |
|                                                                                                                                                                    | `forecast(#)` | use `#` periods for the out-of-sample forecast                                                         |
| You must `tsset` your data before using `tssmooth exponential`; see [<strong>[TS] tsset</strong>](http://www.stata.com/help.cgi?tsset). |               |                                                                                                        |
| `exp` may contain time-series operators; see [<strong>tsvarlist</strong>](http://www.stata.com/help.cgi?tsvarlist).                     |               |                                                                                                        |
