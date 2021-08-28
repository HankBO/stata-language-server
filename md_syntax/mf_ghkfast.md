## Syntax

`S = ghkfast_init(real scalar n, npts, dim, `
`string scalar method)`

`(varies)`<span class="nowrap"> _ `ghkfast_init_pivot(S`
\[`, real scalar pivot`\]`)`

`(varies)`<span class="nowrap"> _ `ghkfast_init_antithetics(S`
\[`, real scalar anti`\]`)`

`real scalar`<span class="nowrap"> _ `ghkfast_query_n(S)`

`real scalar`<span class="nowrap"> _ `ghkfast_query_npts(S)`

`real scalar`<span class="nowrap"> _ `ghkfast_query_dim(S)`

`string scalar`<span class="nowrap"> _
`ghkfast_query_method(S)`

`string scalar`<span class="nowrap"> _
`ghkfast_query_rseed(S)`

`real matrix`<span class="nowrap"> _
`ghkfast_query_pointset_i(S, i)`

`real colvector ghkfast(S, real matrix X, V)`

`real colvector ghkfast(S, real matrix X, V,`
`dfdx, dfdv)`

`real scalar ghkfast_i(S, real matrix X, V,  i)`

`real scalar ghkfast_i(S, real matrix X, V,`
`i, dfdx, dfdv)`

where `S`, if it is declared, should be declared

`transmorphicS`

and where `method` specified in `ghkfast_init()` is

`method`<span style="padding-left: 16.0rem;">_Description

<span options="60">_

`"halton"`<span style="padding-left: 16.0rem;">_Halton sequences

`"hammersley"`<span style="padding-left: 16.0rem;">_Hammersley's
variation of the Halton set

`"random"`<span style="padding-left: 16.0rem;">_pseudorandom
uniforms

`"ghalton"`<span style="padding-left: 16.0rem;">_generalized
Halton sequences

<span options="60">_
