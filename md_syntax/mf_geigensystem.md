## Syntax

`void`<span class="nowrap"> _ `geigensystem(A, B, X,`
`w, b)`

`void`<span class="nowrap"> _ `leftgeigensystem(A, B,`
`X, w, b)`

`void`<span class="nowrap"> _ `geigensystemselectr(A, B,`
`range, X, w, b)`

`void`<span class="nowrap"> _ `leftgeigensystemselectr(A,`
`B, range, X, w, b)`

`void`<span class="nowrap"> _ `geigensystemselecti(A, B,`
`index, X, w, b)`

`void`<span class="nowrap"> _ `leftgeigensystemselecti(A,`
`B, index, X, w, b)`

`void`<span class="nowrap"> _ `geigensystemselectf(A, B,`
`f, X, w, b)`

`void`<span class="nowrap"> _ `leftgeigensystemselectf(A,`
`B, f, X, w, b)`

where inputs are

|                        |                                                               |
|------------------------|---------------------------------------------------------------|
| `A`: `numeric matrix`  |                                                               |
| `B`: `numeric matrix`  |                                                               |
| `range`: `real vector` | (range of generalized eigenvalues to be selected)             |
| `index`: `real vector` | (indices of generalized eigenvalues to be selected)           |
| `f`: `pointer scalar`  | (points to a function used to select generalized eigenvalues) |

and outputs are

`Xnumeric matrixwnumeric vectorbnumeric vector`

The following routines are used in implementing the above routines:

`void _geigensystem_la(numeric matrix H, R, XL, XR,`
`w, b, string scalar side)`

`void _geigenselectr_la(numeric matrix H, R, XL, XR,`
`w, b, range, string scalar side)`

`void _geigenselecti_la(numeric matrix H, R, XL, XR,`
`w, b, index, string scalar side)`

`void _geigenselectf_la(numeric matrix H, R, XL, XR,`
`w, b, pointer scalar f, string scalar side)`

`real scalar _geigen_la(numeric matrix H, R, XL, XR,`
`w, select, string scalar side, string scalar howmany)`
