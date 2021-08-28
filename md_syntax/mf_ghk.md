## Syntax

`S = ghk_init(real scalar npts)`

`(varies)`<span class="nowrap"> _ `ghk_init_method(S`
\[`, string scalar method`\]`)`

`(varies)`<span class="nowrap"> _ `ghk_init_start(S`
\[`, real scalar start`\]`)`

`(varies)`<span class="nowrap"> _ `ghk_init_pivot(S`
\[`, real scalar pivot`\]`)`

`(varies)`<span class="nowrap"> _ `ghk_init_antithetics(S`
\[`, real scalar anti`\]`)`

`real scalar`<span class="nowrap"> _ `ghk_query_npts(S)`

`real scalar`<span class="nowrap"> _
`ghk(S, real vector x, V)`

`real scalar`<span class="nowrap"> _
`ghk(S, real vector x, V, `
`real rowvector dfdx, dfdv)`

where `S`, if declared, should be declared

`transmorphic S`

and where `method`, optionally specified in `ghk_init_method()`, is

`method`<span style="padding-left: 16.0rem;">_Description

<span options="60">_

`"halton"`<span style="padding-left: 16.0rem;">_Halton sequences

`"hammersley"`<span style="padding-left: 16.0rem;">_Hammersley's
variation of the Halton set

`"random"`<span style="padding-left: 16.0rem;">_pseudorandom
uniforms

<span options="60">_
