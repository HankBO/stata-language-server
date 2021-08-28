## Syntax

`psdensity` _\[`type`\] \[_ `newvar_sd`
`newvar_f` _\[`if`\] \[`in`\]_ \[`,`
`options`\]

where `newvar_sd` is the name of the variable that will contain the
estimated spectral density and `newvar_f` is the name of the new
variable that will contain the frequencies at which the spectral density
estimate is computed.

| options |              | Description                                                                                                    |
|---------|--------------|----------------------------------------------------------------------------------------------------------------|
|         | `pspectrum`  | estimate the power spectrum rather than the spectral density                                                   |
|         | `range(a b)` | limit the frequency range to \[a,b)                                                                            |
|         | `cycle(#)`   | estimate the spectral density from the specified stochastic cycle; only allowed after `ucm`                    |
|         | `smemory`    | estimate the spectral density of the short-memory component of the ARFIMA process; only allowed after `arfima` |
