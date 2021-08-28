## Syntax

`numeric vector`<span class="nowrap"> _
`polyeval(numeric rowvector c, numeric vector x)`

`numeric rowvector polysolve(numeric vector y,`
`numeric vector x)`

`numeric rowvector polytrim(numeric vector c)`

`numeric rowvector polyderiv(numeric rowvector c,`
`real scalar i)`

`numeric rowvector polyinteg(numeric rowvector c,`
`real scalar i)`

`numeric rowvector polyadd(numeric rowvector c1,`
`numeric rowvector c2)`

`numeric rowvector polymult(numeric rowvector c1,`
`numeric rowvector c2)`

`void`<span class="nowrap"> _ `polydiv(numeric rowvector c1,`
`numeric rowvector c2,`  
`cq, cr)`

`complex rowvector polyroots(numeric rowvector c)`

In the above, row vector `c` contains the coefficients for a
`cols(c)`-1 degree polynomial. For instance,

`c`

records the polynomial

`xx`
