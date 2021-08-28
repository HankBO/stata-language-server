## Syntax

Factor analysis of data

`factor`
[varlist](http://www.stata.com/help.cgi?varlist)
_\[`if`\] \[`in`\]_ \[`weight`\] \[`,`
`method options`\]

Factor analysis of a correlation matrix

`factormat matname, n(#)` \[ `method options`
`factormat_options`\]

`matname` is a square Stata matrix or a vector containing the rowwise
upper or lower triangle of the correlation or covariance matrix. If a
covariance matrix is provided, it is transformed into a correlation
matrix for the factor analysis.

| method  |       | Description                   |
|---------|-------|-------------------------------|
| Model 2 |       |                               |
|         | `pf`  | principal factor; the default |
|         | `pcf` | principal-component factor    |
|         | `ipf` | iterated principal factor     |
|         | `ml`  | maximum-likelihood factor     |

| Options                                        |                    | Description                                                                     |
|------------------------------------------------|--------------------|---------------------------------------------------------------------------------|
| Model 2                                        |                    |                                                                                 |
|                                                | `factors(#)`       | maximum number of factors to be retained                                        |
|                                                | `mineigen(#)`      | minimum value of eigenvalues to be retained                                     |
|                                                | `citerate(#)`      | communality reestimation iterations (`ipf` only)                                |
| Reporting                                      |                    |                                                                                 |
|                                                | `blanks(#)`        | display loadings as blanks when \|loadings\| &lt; `#`                           |
|                                                | `altdivisor`       | use trace of correlation matrix as the divisor for reported proportions         |
| Maximization                                   |                    |                                                                                 |
|                                                | `protect(#)`       | perform `#` optimizations and report the best solution (`ml` only)              |
|                                                | `random`           | use random starting values (`ml` only); seldom used                             |
|                                                | `"seed(seed)`      | random-number seed (`ml` with `protect()` or `random` only)                     |
|                                                | `maximize_options` | control the maximization process; seldom used (`ml` only)                       |
|                                                | `norotated`        | display unrotated solution, even if rotated results are available (replay only) |
| `norotated` does not appear in the dialog box. |                    |                                                                                 |

| factormat\_options                     |                    | Description                                                           |
|----------------------------------------|--------------------|-----------------------------------------------------------------------|
| Model                                  |                    |                                                                       |
|                                        | `shape(full)`  | `matname` is a square symmetric matrix; the default                   |
|                                        | `shape(lower)` | `matname` is a vector with the rowwise lower triangle (with diagonal) |
|                                        | `shape(upper)` | `matname` is a vector with the rowwise upper triangle (with diagonal) |
|                                        | `names(namelist)`  | variable names; required if `matname` is triangular                   |
|                                        | `forcepsd`         | modifies `matname` to be positive semidefinite                        |
| \*                                     | `n(#)`             | number of observations                                                |
|                                        | `sds(matname2)`    | vector with standard deviations of variables                          |
|                                        | `means(matname3)`  | vector with means of variables                                        |
| \* `n(#)` is required for `factormat`. |                    |                                                                       |

`bootstrap`, `by`, `jackknife`, `rolling`, and `statsby` are allowed
with `factor`; see
[<strong>prefix</strong>](http://www.stata.com/help.cgi?prefix).
However, `bootstrap` and `jackknife` results should be interpreted with
caution; identification of the `factor` parameters involves
data-dependent restrictions, possibly leading to badly biased and
overdispersed estimates
([<strong>Milan and Whittaker 1995</strong>](#MW1995)).

Weights are not allowed with the
[<strong>bootstrap</strong>](http://www.stata.com/help.cgi?bootstrap)
prefix.

`aweight`s are not allowed with the
[<strong>jackknife</strong>](http://www.stata.com/help.cgi?jackknife)
prefix.

`aweight`s and `fweight`s are allowed with `factor`; see
[<strong>weight</strong>](http://www.stata.com/help.cgi?weight).

See
[<strong>[R]</strong> factor postestimation](http://www.stata.com/help.cgi?factor_postestimation)
for features available after estimation.
