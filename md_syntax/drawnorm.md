## Syntax

`drawnorm newvarlist` \[`, options`\]

| Options |                        | Description                                                          |
|---------|------------------------|----------------------------------------------------------------------|
| Main    |                        |                                                                      |
|         | `clear`                | replace the current dataset                                          |
|         | `double`               | generate variable type as `double`; default is `float`               |
|         | `n(#)`                 | generate `#` observations; default is current number                 |
|         | `sds(vector)`          | standard deviations of generated variables                           |
|         | `corr(matrix,vector)`  | correlation matrix                                                   |
|         | `cov(matrix,vector)`   | covariance matrix                                                    |
|         | `cstorage:(full)`    | store correlation/covariance structure as a symmetric k\*k matrix    |
|         | `cstorage:(lower)`   | store correlation/covariance structure as a lower triangular matrix  |
|         | `cstorage:(upper)` | store correlation/covariance structure as an upper triangular matrix |
|         | `forcepsd`             | force the covariance/correlation matrix to be positive semidefinite  |
|         | `means(vector)`        | means of generated variables; default is `means(0)`                  |
| Options |                        |                                                                      |
|         | `seed(#)`              | seed for random-number generator                                     |
