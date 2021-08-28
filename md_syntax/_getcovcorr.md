## Syntax

`_getcovcorr matname` \[ `, options` \]

|                   |                                                                |
|-------------------|----------------------------------------------------------------|
| `options`         | Description {p2line None}                                      |
| `correlation`     | return a correlation matrix                                    |
| `covariance`      | return a covariance matrix                                     |
| `shape(shape)`    | shape (storage method) of `matname`                            |
| `names(namelist)` | namelist; required with vectorized input                       |
| `sds(vector)`     | vector of standard deviations                                  |
| `means(vector)`   | vector of means                                                |
| `force`           | fixes input problems in names (see below)                      |
| `check(pd)`       | checks that `matname` is positive definite                     |
| `check(psd)`      | checks that `matname` is positive semidefinite                 |
| `forcepsd`        | modifies `matname` to be positive semidefinite                 |
| `tol(#)`          | tolerance for checking eigenvalues (see below) {p2line None}   |
| `shape`           | `matname` is stored as a {p2line None}                         |
| `full`            | square symmetric matrix                                        |
| `lower`           | vector of rowwise lower triangle (with diagonal)               |
| `upper`           | vector of rowwise lower triangle (with diagonal) {p2line None} |
