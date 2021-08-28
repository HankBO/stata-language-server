## Syntax

Kao test

`xtcointtest kao`
[depvar](http://www.stata.com/help.cgi?depvar)
[varlist](http://www.stata.com/help.cgi?varlist)
_\[`if`\] \[`in`\]_ \[`, kao_options`\]

Pedroni test

`xtcointtest pedroni`
[depvar](http://www.stata.com/help.cgi?depvar)
[varlist](http://www.stata.com/help.cgi?varlist)
_\[`if`\] \[`in`\]_ \[`, pedroni_options`\]

Westerlund test

`xtcointtest westerlund`
[depvar](http://www.stata.com/help.cgi?depvar)
[varlist](http://www.stata.com/help.cgi?varlist)
_\[`if`\] \[`in`\]_ \[`,`
`westerlund_options`\]

| kao\_options |                | Description                                                   |
|--------------|----------------|---------------------------------------------------------------|
| Main         |                |                                                               |
|              | `lags(lspec)`  | specify lag structure for augmented Dickey-Fuller regressions |
|              | `kernel(spec)` | specify method to estimate long-run variance                  |
|              | `demean`       | subtract cross-sectional means                                |

| pedroni\_options |                               | Description                                                                                                          |
|------------------|-------------------------------|----------------------------------------------------------------------------------------------------------------------|
| Main             |                               |                                                                                                                      |
|                  | `ar(panelspecific`\|`same)` | specify autoregressive parameter as panel specific or as the same for all panels; `ar(panelspecific)` is the default |
|                  | `trend`                       | include panel-specific time trends                                                                                   |
|                  | `noconstant`                  | suppress panel-specific means                                                                                        |
|                  | `lags(lspec)`                 | specify lag structure for augmented Dickey-Fuller regressions                                                        |
|                  | `kernel(kspec)`               | specify method to estimate long-run variance                                                                         |
|                  | `demean`                      | subtract cross-sectional means                                                                                       |

| westerlund\_options |              | Description                                                             |
|---------------------|--------------|-------------------------------------------------------------------------|
| Main                |              |                                                                         |
|                     | `somepanels` | use alternative hypothesis of cointegration in some panels; the default |
|                     | `allpanels`  | use alternative hypothesis of cointegration in all panels               |
|                     | `trend`      | include panel-specific time trends                                      |
|                     | `demean`     | subtract cross-sectional means                                          |

`lspec` is

|     |            |                                                               |
|-----|------------|---------------------------------------------------------------|
|     | `#`        | number of lags of series; `1` is the default                  |
|     | `aic #`  | Akaike information criterion (AIC) with up to `#` lags        |
|     | `bic #`  | Bayesian information criterion (BIC) with up to `#` lags      |
|     | `hqic #` | Hannan-Quinn information criterion (HQIC) with up to `#` lags |

`kspec` is

|     |                             |                                                   |
|-----|-----------------------------|---------------------------------------------------|
|     | `bartlett nwest`          | Bartlett kernel with Newey-West lags; the default |
|     | `bartlett #`              | Bartlett kernel with up to `#` lags               |
|     | `parzen nwest`            | Parzen kernel with Newey-West lags                |
|     | `parzen #`                | Parzen kernel with up to `#` lags                 |
|     | `quadraticspectral nwest` | quadratic spectral kernel with Newey-West lags    |
|     | `quadraticspectral #`     | quadratic spectral kernel with up to `#` lags     |
