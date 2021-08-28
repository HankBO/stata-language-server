## Syntax

Quantile regression

`qreg`
[depvar](http://www.stata.com/help.cgi?depvar)
\[[indepvars](http://www.stata.com/help.cgi?indepvars)\]
_\[`if`\] \[`in`\]_ \[`weight`\] \[`,`
`qreg_options`\]

Interquantile range regression

`iqreg`
[depvar](http://www.stata.com/help.cgi?depvar)
\[[indepvars](http://www.stata.com/help.cgi?indepvars)\]
_\[`if`\] \[`in`\]_ \[`, iqreg_options`\]

Simultaneous-quantile regression

`sqreg`
[depvar](http://www.stata.com/help.cgi?depvar)
\[[indepvars](http://www.stata.com/help.cgi?indepvars)\]
_\[`if`\] \[`in`\]_ \[`, sqreg_options`\]

Bootstrapped quantile regression

`bsqreg`
[depvar](http://www.stata.com/help.cgi?depvar)
\[[indepvars](http://www.stata.com/help.cgi?indepvars)\]
_\[`if`\] \[`in`\]_ \[`, bsqreg_options`\]

| qreg\_options |                                         | Description                                                                                                                                      |
|---------------|-----------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| Model         |                                         |                                                                                                                                                  |
|               | `quantile(#)`                           | estimate `#` quantile; default is `quantile(.5)`                                                                                                 |
| SE/Robust     |                                         |                                                                                                                                                  |
|               | `vce(`\[`vcetype`\]`,` \[`vceopts`\]`)` | technique used to estimate standard errors                                                                                                       |
| Reporting     |                                         |                                                                                                                                                  |
|               | `level(#)`                              | set confidence level; default is `level(95)`                                                                                                     |
|               | `display_options`                       | control columns and column formats, row spacing, line width, display of omitted variables and base and empty cells, and factor-variable labeling |
| Optimization  |                                         |                                                                                                                                                  |
|               | `optimization_options`                  | control the optimization process; seldom used                                                                                                    |
|               | `wlsiter(#)`                            | attempt `#` weighted least-squares iterations before doing linear programming iterations                                                         |

| vcetype |          | Description                                       |
|---------|----------|---------------------------------------------------|
|         | `iid`    | compute the VCE assuming the residuals are i.i.d. |
|         | `robust` | compute the robust VCE                            |

| vceopts |             | Description                                    |
|---------|-------------|------------------------------------------------|
|         | `denmethod` | nonparametric density estimation technique     |
|         | `bwidth`    | bandwidth method used by the density estimator |

| denmethod |                            | Description                                                             |
|-----------|----------------------------|-------------------------------------------------------------------------|
|           | `fitted`                   | use the empirical quantile function using fitted values; the default    |
|           | `residual`                 | use the empirical residual quantile function                            |
|           | `kernel`\[`(kernel)`\] | use a nonparametric kernel density estimator; default is `epanechnikov` |

| bwidth |               | Description                            |
|--------|---------------|----------------------------------------|
|        | `hsheather`   | Hall-Sheather's bandwidth; the default |
|        | `bofinger`    | Bofinger's bandwidth                   |
|        | `chamberlain` | Chamberlain's bandwidth                |

| kernel |                | Description                               |
|--------|----------------|-------------------------------------------|
|        | `epanechnikov` | Epanechnikov kernel function; the default |
|        | `epan2`        | alternative Epanechnikov kernel function  |
|        | `biweight`     | biweight kernel function                  |
|        | `cosine`       | cosine trace kernel function              |
|        | `gaussian`     | Gaussian kernel function                  |
|        | `parzen`       | Parzen kernel function                    |
|        | `rectangle`    | rectangle kernel function                 |
|        | `triangle`     | triangle kernel function                  |

| iqreg\_options |                   | Description                                                                                                                                      |
|----------------|-------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| Model          |                   |                                                                                                                                                  |
|                | `quantiles(# #)`  | interquantile range; default is <span class="nowrap">`quantiles(.25 .75)`_                                                                 |
|                | `reps(#)`         | perform `#` bootstrap replications; default is `reps(20)`                                                                                        |
| Reporting      |                   |                                                                                                                                                  |
|                | `level(#)`        | set confidence level; default is `level(95)`                                                                                                     |
|                | `nodots`          | suppress display of the replication dots                                                                                                         |
|                | `display_options` | control columns and column formats, row spacing, line width, display of omitted variables and base and empty cells, and factor-variable labeling |

| sqreg\_options |                                      | Description                                                                                                                                      |
|----------------|--------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| Model          |                                      |                                                                                                                                                  |
|                | `quantiles(#`\[`#`\[`# ...`\]\]`)` | estimate `#` quantiles; default is `quantiles(.5)`                                                                                               |
|                | `reps(#)`                            | perform `#` bootstrap replications; default is `reps(20)`                                                                                        |
| Reporting      |                                      |                                                                                                                                                  |
|                | `level(#)`                           | set confidence level; default is `level(95)`                                                                                                     |
|                | `nodots`                             | suppress display of the replication dots                                                                                                         |
|                | `display_options`                    | control columns and column formats, row spacing, line width, display of omitted variables and base and empty cells, and factor-variable labeling |

| bsqreg\_options |                   | Description                                                                                                                                      |
|-----------------|-------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| Model           |                   |                                                                                                                                                  |
|                 | `quantile(#)`     | estimate `#` quantile; default is `quantile(.5)`                                                                                                 |
|                 | `reps(#)`         | perform `#` bootstrap replications; default is `reps(20)`                                                                                        |
| Reporting       |                   |                                                                                                                                                  |
|                 | `level(#)`        | set confidence level; default is `level(95)`                                                                                                     |
|                 | `display_options` | control columns and column formats, row spacing, line width, display of omitted variables and base and empty cells, and factor-variable labeling |

`indepvars` may contain factor variables; see
[<strong>fvvarlist</strong>](http://www.stata.com/help.cgi?fvvarlist).

`by`, `mi estimate`, `rolling`, and `statsby` are allowed with `qreg`,
`iqreg`, `sqreg`, and `bsqreg`; `mfp`, `nestreg`, and `stepwise` are
allowed with `qreg`; see
[<strong>prefix</strong>](http://www.stata.com/help.cgi?prefix).

`qreg` allows `fweight`s, `iweight`s, and `pweight`s; see
[<strong>weight</strong>](http://www.stata.com/help.cgi?weight).

See
[<strong>[R]</strong> qreg postestimation](http://www.stata.com/help.cgi?qreg_postestimation)
for features available after estimation.
