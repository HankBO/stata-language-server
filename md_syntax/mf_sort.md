## Syntax

`transmorphic matrix`<span class="nowrap"> _
`sort(transmorphic matrix X, real rowvector idx)`

`void`<span class="nowrap"> _ `_sort(transmorphic matrix X,`
`real rowvector idx)`

`transmorphic matrix`<span class="nowrap"> _
`jumble(transmorphic matrix X)`

`void`<span class="nowrap"> _ `_jumble(transmorphic matrix X)`

`real colvector`<span class="nowrap"> _
`order(transmorphic matrix X, real rowvector idx)`

`real colvector`<span class="nowrap"> _
`unorder(real scalar n)`

`void`<span class="nowrap"> _
`_collate(transmorphic matrix X, real colvector p)`

where

1\. `X` may not be a pointer matrix.

2\. `p` must be a permutation column vector, a 1 `x c` vector
containing the integers 1, 2, ..., `c` in some order.
