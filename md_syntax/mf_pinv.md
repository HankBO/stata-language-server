## Syntax

`numeric matrix pinv(numeric matrix A)`

`numeric matrix pinv(numeric matrix A, rank)`

`numeric matrix pinv(numeric matrix A, rank,`
`real scalar tol)`

`real scalar`<span class="nowrap"> _ `_pinv(numeric matrix A)`

`real scalar`<span class="nowrap"> _ `_pinv(numeric matrix A,`
`real scalar tol)`

where the type of `rank` is irrelevant; the rank of `A` is returned
there.

To obtain a generalized inverse of a symmetric matrix with a different
normalization, see
**[<strong>[M-5] invsym()</strong>](http://www.stata.com/help.cgi?mf_invsym)**.
