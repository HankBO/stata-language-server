## Syntax

`D = deriv_init()`

`(varies)`<span class="nowrap"> _ `deriv_init_evaluator(D` \[`,`
`&function()`\] `)`

`(varies)`<span class="nowrap"> _ `deriv_init_evaluatortype(D`
\[`, evaluatortype`\] `)`

`(varies)`<span class="nowrap"> _ `deriv_init_params(D` \[`,`
`real rowvector parameters`\] `)`

`(varies)`<span class="nowrap"> _ `deriv_init_argument(D,`
`real scalar k` \[`, X`\] `)`

`(varies)`<span class="nowrap"> _ `deriv_init_narguments(D`
\[`, real scalar K`\] `)`

`(varies)`<span class="nowrap"> _ `deriv_init_weights(D` \[`,`
`real colvector weights`\] `)`

`(varies)`<span class="nowrap"> _ `deriv_init_h(D` \[`,`
`real rowvector h`\] `)`

`(varies)`<span class="nowrap"> _ `deriv_init_scale(D` \[`,`
`real matrix scale`\] `)`

`(varies)`<span class="nowrap"> _ `deriv_init_bounds(D` \[`,`
`real rowvector minmax`\] `)`

`(varies)`<span class="nowrap"> _ `deriv_init_search(D` \[`,`
`search`\] `)`

`(varies)`<span class="nowrap"> _ `deriv_init_verbose(D` \[`,`
{`"on"` \| `"off"`<span options=")-">{c
)-}_\] `)`

`(varies)`<span class="nowrap"> _ `deriv(D,` <span
options="-(">{c -(}_`0` \| `1` \| `2`<span options=")-">{c
)-}_`)`

`real scalar`<span class="nowrap"> _ `_deriv(D,` <span
options="-(">{c -(}_`0` \| `1` \| `2`<span options=")-">{c
)-}_`)`

`real scalar`<span class="nowrap"> _ `deriv_result_value(D)`

`real vector deriv_result_values(D)`

`void`<span class="nowrap"> _ `_deriv_result_values(D, v)`

`real rowvector deriv_result_gradient(D)`

`void`<span class="nowrap"> _ `_deriv_result_gradient(D,`
`g)`

`real matrix`<span class="nowrap"> _ `deriv_result_scores(D)`

`void`<span class="nowrap"> _ `_deriv_result_scores(D, S)`

`real matrix deriv_result_Jacobian(D)`

`void`<span class="nowrap"> _ `_deriv_result_Jacobian(D,`
`J)`

`real matrix`<span class="nowrap"> _ `deriv_result_Hessian(D)`

`void`<span class="nowrap"> _ `_deriv_result_Hessian(D,`
`H)`

`real rowvector deriv_result_h(D)`

`real matrix`<span class="nowrap"> _ `deriv_result_scale(D)`

`real matrix`<span class="nowrap"> _ `deriv_result_delta(D)`

`real scalar`<span class="nowrap"> _
`deriv_result_errorcode(D)`

`string scalar`<span class="nowrap"> _
`deriv_result_errortext(D)`

`real scalar`<span class="nowrap"> _
`deriv_result_returncode(D)`

`void`<span class="nowrap"> _ `deriv_query(D)`

where `D`, if it is declared, should be declared

`transmorphicD`

and where `evaluatortype` optionally specified in
`deriv_init_evaluatortype()` is

|                 |                                                                                                                           |
|-----------------|---------------------------------------------------------------------------------------------------------------------------|
| `evaluatortype` | Description {p2line None}                                                                                                 |
| `"d"`           | `function()` returns `scalar` value                                                                                     |
| `"v"`           | `function()` returns `colvector` value                                                                                  |
| `"t"`           | `function()` returns `rowvector` value {p2line None} <span options="16">{col 16}_The default is `"d"` if not set. |

and where `search` optionally specified in `deriv_init_search()` is

|                 |                                                                                                                               |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------|
| `search`        | Description {p2line None}                                                                                                     |
| `"interpolate"` | use linear and quadratic interpolation to search for an optimal delta                                                         |
| `"bracket"`     | use a bracketed quadratic formula to search for an optimal delta                                                              |
| `"off"`         | do not search for an optimal delta {p2line None} <span options="16">{col 16}_The default is `"interpolate"` if not set. |
