## Syntax

`real scalar`<span class="nowrap"> _ `st_vlexists(name)`

`void`<span class="nowrap"> _ `st_vldrop(name)`

`string matrix st_vlmap(name, real matrix values)`

`real matrix`<span class="nowrap"> _ `st_vlsearch(name,`
`string matrix text)`

`void`<span class="nowrap"> _ `st_vlload(name, values,`
`text)`

`void`<span class="nowrap"> _ `st_vlmodify(name,`
`real colvector values,`  
`string colvector text)`

where `name` is `string scalar` and where the types of `values` and
`text` in `st_vlload()` are irrelevant because they are replaced.
