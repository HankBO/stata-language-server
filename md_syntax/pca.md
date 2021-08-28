## Syntax

Principal component analysis of data

`pca`
[varlist](http://www.stata.com/help.cgi?varlist)
_\[`if`\] \[`in`\]_ \[`weight`\] \[`,`
`options`\]

Principal component analysis of a correlation or covariance matrix

`pcamat matname , n(#)` \[`options pcamat_options`\]

`matname` is a k x k symmetric matrix or a k(k+1)/2 long row or column
vector containing the upper or lower triangle of the correlation or
covariance matrix.

| Options                                         |                   | Description                                                                                                                          |
|-------------------------------------------------|-------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| Model 2                                         |                   |                                                                                                                                      |
|                                                 | `components(#)`   | retain maximum of `#` principal components; `factors()` is a synonym                                                                 |
|                                                 | `mineigen(#)`     | retain eigenvalues larger than `#`; default is `1e-5`                                                                                |
|                                                 | `correlation`     | perform PCA of the correlation matrix; the default                                                                                   |
|                                                 | `covariance`      | perform PCA of the covariance matrix                                                                                                 |
|                                                 | `vce(none)`   | do not compute VCE of the eigenvalues and vectors; the default                                                                       |
|                                                 | `vce(normal)` | compute VCE of the eigenvalues and vectors assuming multivariate normality                                                           |
| Reporting                                       |                   |                                                                                                                                      |
|                                                 | `level(#)`        | set confidence level; default is `level(95)`                                                                                         |
|                                                 | `blanks(#)`       | display loadings as blank when \|loadings\| &lt; `#`                                                                                 |
|                                                 | `novce`           | suppress display of SEs even though calculated                                                                                       |
| \#                                              | `means`           | display summary statistics of variables                                                                                              |
| Advanced                                        |                   |                                                                                                                                      |
|                                                 | `tol(#)`          | advanced option; see [<var class="command">Options</var><strong></strong>](#options_advanced) for details |
|                                                 | `ignore`          | advanced option; see [<var class="command">Options</var><strong></strong>](#options_advanced) for details |
|                                                 | `norotated`       | display unrotated results, even if rotated results are available (replay only)                                                       |
| \# `means` is not allowed with `pcamat`.        |                   |                                                                                                                                      |
| `norotated` is not available in the dialog box. |                   |                                                                                                                                      |

| pcamat\_options                    |                     | Description                                                           |
|------------------------------------|---------------------|-----------------------------------------------------------------------|
| Model                              |                     |                                                                       |
|                                    | `shape:(full)`  | `matname` is a square symmetric matrix; the default                   |
|                                    | `shape:(lower)` | `matname` is a vector with the rowwise lower triangle (with diagonal) |
|                                    | `shape:(upper)` | `matname` is a vector with the rowwise upper triangle (with diagonal) |
|                                    | `names(namelist)`   | variable names; required if `matname` is triangular                   |
|                                    | `forcepsd`          | modifies `matname` to be positive semidefinite                        |
| \*                                 | `n(#)`              | number of observations                                                |
|                                    | `sds(matname2)`     | vector with standard deviations of variables                          |
|                                    | `means(matname3)`   | vector with means of variables                                        |
| \* `n()` is required for `pcamat`. |                     |                                                                       |

`bootstrap`, `by`, `jackknife`, `rolling`, `statsby`, and `xi` are
allowed with `pca`; see
[<strong>prefix</strong>](http://www.stata.com/help.cgi?prefix).
However, `bootstrap` and `jackknife` results should be interpreted with
caution; identification of the `pca` parameters involves data-dependent
restrictions, possibly leading to badly biased and overdispersed
estimates
([<strong>Milan and Whittaker 1995</strong>](#MW1995)).

Weights are not allowed with the
[<strong>bootstrap</strong>](http://www.stata.com/help.cgi?bootstrap)
prefix.

`aweight`s are not allowed with the
[<strong>jackknife</strong>](http://www.stata.com/help.cgi?jackknife)
prefix.

`aweight`s and `fweight`s are allowed with `pca`; see
[<strong>weight</strong>](http://www.stata.com/help.cgi?weight).

See
[<strong>[MV]</strong> pca postestimation](http://www.stata.com/help.cgi?pca_postestimation)
for features available after estimation.
