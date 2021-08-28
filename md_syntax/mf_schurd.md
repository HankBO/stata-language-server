## Syntax

`void`<span class="nowrap"> _ `schurd(X, T, Q)`

`void`<span class="nowrap"> _ `_schurd(X,` <span
class="nowrap"> _ `Q)`

`void`<span class="nowrap"> _ ` schurdgroupby(X, f,`
`T, Q, w, m)`

`void`<span class="nowrap"> _ `_schurdgroupby(X, f,` <span
class="nowrap"> _ `Q, w, m)`

where inputs are

`Xnumeric matrixfpointer scalar`

and outputs are

|                                      |                                                            |
|--------------------------------------|------------------------------------------------------------|
| `T`: `numeric matrix`                | (Schur-form matrix)                                        |
| `Q`: `numeric matrix`                | (orthogonal or unitary)                                    |
| `w`: `numeric vector` of eigenvalues |                                                            |
| `m`: `real scalar`                   | (the number of eigenvalues satisfy the grouping condition) |
