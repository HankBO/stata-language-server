## Syntax

`void`<span class="nowrap"> _ `eigensystem(A, X, L`
\[`, rcond` \[`, nobalance`\]\]`)`

`void`<span class="nowrap"> _ `lefteigensystem(A, X, L`
\[`, rcond` \[`, nobalance`\]\]`)`

`complex rowvector`<span class="nowrap"> _ `eigenvalues(A`<span
class="nowrap"> _ \[`, rcond` \[`, nobalance`\]\]`)`

`void`<span class="nowrap"> _ `symeigensystem(A, X,`
`L)`

`real rowvector`<span class="nowrap"> _ `symeigenvalues(A)`

`void`<span class="nowrap"> _ `_eigensystem(A, X, L`
\[`, rcond` \[`, nobalance`\]\]`)`

`void`<span class="nowrap"> _ `_lefteigensystem(A, X, L`
\[`, rcond` \[`, nobalance`\]\]`)`

`complex rowvector`<span class="nowrap"> _ `_eigenvalues(A`<span
class="nowrap"> _ \[`, rcond` \[`, nobalance`\]\]`)`

`void`<span class="nowrap"> _ `_symeigensystem(A, X,`
`L)`

`real rowvector`<span class="nowrap"> _ `_symeigenvalues(A)`

where inputs are

`Anumeric matrixrcondreal scalarrcondnobalancereal scalar`

and outputs are

`Xnumeric matrixLnumeric vectorrcondreal vector`

The columns of `X` will contain the eigenvectors except when using
`_lefteigensystem()`, in which case the rows of `X` contain the
eigenvectors.

The following routines are used in implementing the above routines:

`real scalar _eigen_la(real scalar todo, numeric matrix A,`
`X, L, real scalar rcond, real scalar nobalance)`

`real scalar _symeigen_la(real scalar todo, numeric matrix A,`
`X, L)`
