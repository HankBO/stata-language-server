## Syntax

`void`<span class="nowrap"> _ `eigensystemselectr(A,`
`range, X, L)`

`void`<span class="nowrap"> _ `lefteigensystemselectr(A,`
`range, X, L)`

`void`<span class="nowrap"> _ `eigensystemselecti(A,`
`index, X, L)`

`void`<span class="nowrap"> _ `lefteigensystemselecti(A,`
`index, X, L)`

`void`<span class="nowrap"> _ `eigensystemselectf(A,`
`f,`<span class="nowrap"> _ `X, L)`

`void`<span class="nowrap"> _ `lefteigensystemselectf(A,`
`f,`<span class="nowrap"> _ `X, L)`

`void`<span class="nowrap"> _ `symeigensystemselectr(A,`
`range, X, L)`

`void`<span class="nowrap"> _ `symeigensystemselecti(A,`
`index, X, L)`

where inputs are

|                        |                                                  |
|------------------------|--------------------------------------------------|
| `A`: `numeric matrix`  |                                                  |
| `range`: `real vector` | (range of eigenvalues to be selected)            |
| `index`: `real vector` | (indices of eigenvalues to be selected)          |
| `f`: `pointer scalar`  | (points to a function used to select eigenvalue) |

and outputs are

`Xnumeric matrixLnumeric vector`

The following routines are used in implementing the above routines:

`void _eigenselecti_la(numeric matrix A, XL, XR, L,`
`string scalar side, real vector index)`

`void _eigenselectr_la(numeric matrix A, XL, XR, L,`
`string scalar side, real vector range)`

`void _eigenselectf_la(numeric matrix A, XL, XR, L,`
`string scalar side, pointer scalar f)`

`real scalar _eigenselect_la(numeric matrix A, XL, XR,`
`L, select, string scalar side, real scalar noflopin)`

`real scalar _symeigenselect_la(numeric matrix A, X, L,`
`ifail, real scalar type, lower, upper, abstol)`
