## Syntax

`mvtest normality`
[varlist](http://www.stata.com/help.cgi?varlist)
_\[`if`\] \[`in`\]_ \[`weight`\] \[`,`
`options`\]

| Options |                | Description                                            |
|---------|----------------|--------------------------------------------------------|
| Options |                |                                                        |
|         | `univariate`   | display tests for univariate normality (`sktest`)      |
|         | `bivariate`    | display tests for bivariate normality (Doornik-Hansen) |
|         | `stats(stats)` | statistics to be computed                              |

| stats |            | Description                              |
|-------|------------|------------------------------------------|
|       | `dhansen`  | Doornik-Hansen omnibus test; the default |
|       | `hzirkler` | Henze-Zirkler's consistent test          |
|       | `kurtosis` | Mardia's multivariate kurtosis test      |
|       | `skewness` | Mardia's multivariate skewness test      |
|       | `all`      | all tests listed here                    |

`bootstrap`, `by`, `jackknife`, `rolling`, and `statsby` are allowed;
see
[<strong>prefix</strong>](http://www.stata.com/help.cgi?prefix).

Weights are not allowed with the
[<strong>bootstrap</strong>](http://www.stata.com/help.cgi?bootstrap)
prefix.

`aweight`s are not allowed with the
[<strong>jackknife</strong>](http://www.stata.com/help.cgi?jackknife)
prefix.

`fweight`s are allowed; see
[<strong>weight</strong>](http://www.stata.com/help.cgi?weight).
