## Syntax

Levin-Lin-Chu test

`xtunitroot llc`
[varname](http://www.stata.com/help.cgi?varname)
_\[`if`\] \[`in`\]_ \[`, LLC_options`\]

Harris-Tzavalis test

`xtunitroot ht`
[varname](http://www.stata.com/help.cgi?varname)
_\[`if`\] \[`in`\]_ \[`, HT_options`\]

Breitung test

`xtunitroot breitung`
[varname](http://www.stata.com/help.cgi?varname)
_\[`if`\] \[`in`\]_ \[`,`
`Breitung_options`\]

Im-Pesaran-Shin test

`xtunitroot ips`
[varname](http://www.stata.com/help.cgi?varname)
_\[`if`\] \[`in`\]_ \[`, IPS_options`\]

Fisher-type tests (combining p-values)

`xtunitroot fisher`
[varname](http://www.stata.com/help.cgi?varname)
_\[`if`\] \[`in`\]_`,` <span options="-(">{c
-(}_`dfuller` | `pperron`<span
options=")-">{c )-}_ `lags(#)` \[`Fisher_options`\]

Hadri Lagrange multiplier stationarity test

`xtunitroot hadri`
[varname](http://www.stata.com/help.cgi?varname)
_\[`if`\] \[`in`\]_ \[`, Hadri_options`\]

| LLC\_options                                                                                                                                                                                 |                       | Description                                                         |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------|---------------------------------------------------------------------|
|                                                                                                                                                                                              | `trend`               | include a time trend                                                |
|                                                                                                                                                                                              | `noconstant`          | suppress panel-specific means                                       |
|                                                                                                                                                                                              | `demean`              | subtract cross-sectional means                                      |
|                                                                                                                                                                                              | `lags(lag_spec)`      | specify lag structure for augmented Dickey-Fuller (ADF) regressions |
|                                                                                                                                                                                              | `kernel(kernel_spec)` | specify method to estimate long-run variance                        |
| `lag_spec` is either a nonnegative integer or one of `aic`, `bic`, or `hqic` followed by a positive integer.                                                                                 |                       |                                                                     |
| `kernel_spec` takes the form `kernel maxlags`, where `kernel` is one of `bartlett`, `parzen`, or `quadraticspectral` and `maxlags` is either a positive number or one of `nwest` or `llc`. |                       |                                                                     |

| HT\_options |              | Description                       |
|-------------|--------------|-----------------------------------|
|             | `trend`      | include a time trend              |
|             | `noconstant` | suppress panel-specific means     |
|             | `demean`     | subtract cross-sectional means    |
|             | `altt`       | make small-sample adjustment to T |

| Breitung\_options |              | Description                            |
|-------------------|--------------|----------------------------------------|
|                   | `trend`      | include a time trend                   |
|                   | `noconstant` | suppress panel-specific means          |
|                   | `demean`     | subtract cross-sectional means         |
|                   | `robust`     | allow for cross-sectional dependence   |
|                   | `lags(#)`    | specify lag structure for prewhitening |

| IPS\_options                                                                                                 |                  | Description                               |
|--------------------------------------------------------------------------------------------------------------|------------------|-------------------------------------------|
|                                                                                                              | `trend`          | include a time trend                      |
|                                                                                                              | `demean`         | subtract cross-sectional means            |
|                                                                                                              | `lags(lag_spec)` | specify lag structure for ADF regressions |
| `lag_spec` is either a nonnegative integer or one of `aic`, `bic`, or `hqic` followed by a positive integer. |                  |                                           |

| Fisher\_options                               |                                                                                                                              | Description                                  |
|-----------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------|
| \*                                            | `dfuller`                                                                                                                    | use ADF unit-root tests                      |
| \*                                            | `pperron`                                                                                                                    | use Phillips-Perron unit-root tests          |
| \*                                            | `lags(#)`                                                                                                                    | specify lag structure for prewhitening       |
|                                               | `demean`                                                                                                                     | subtract cross-sectional means               |
|                                               | [<var class="command">dfuller_opts</var><strong></strong>](http://www.stata.com/help.cgi?dfuller) | any options allowed by the `dfuller` command |
|                                               | [<var class="command">pperron_opts</var><strong></strong>](http://www.stata.com/help.cgi?pperron) | any options allowed by the `pperron` command |
| \* Either `dfuller` or `pperron` is required. |                                                                                                                              |                                              |
| \* `lags(#)` is required.                     |                                                                                                                              |                                              |

| Hadri\_options                                                                                                                                     |                       | Description                                  |
|----------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------|----------------------------------------------|
|                                                                                                                                                    | `trend`               | include a time trend                         |
|                                                                                                                                                    | `demean`              | subtract cross-sectional means               |
|                                                                                                                                                    | `robust`              | allow for cross-sectional dependence         |
|                                                                                                                                                    | `kernel(kernel_spec)` | specify method to estimate long-run variance |
| `kernel_spec` takes the form `kernel` \[`#`\], where `kernel` is one of `bartlett`, `parzen`, or `quadraticspectral` and `#` is a positive number. |                       |                                              |

`varname` may contain time-series operators; see
[<strong>tsvarlist</strong>](http://www.stata.com/help.cgi?tsvarlist).
