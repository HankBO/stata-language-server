## Syntax

`t` = `tokeninit(`\[`wchars` \[`, pchars` \[`, qchars` \[`,`
`allownum` \[`, allowhex`\]\]\]\]\]`)`

`t` = `tokeninitstata()`

`void`<span class="nowrap"> _ `tokenset(t,`
`string scalar s)`

`string rowvector tokengetall(t)`

`string scalar`<span class="nowrap"> _ `tokenget(t)`

`string scalar`<span class="nowrap"> _ `tokenpeek(t)`

`string scalar`<span class="nowrap"> _ `tokenrest(t)`

`real scalar`<span class="nowrap"> _ `tokenoffset(t)`

`void`<span class="nowrap"> _ `tokenoffset(t,`
`real scalar offset)`

`string scalar`<span class="nowrap"> _ `tokenwchars(t)`

`void`<span class="nowrap"> _ `tokenwchars(t, string scalar`
`wchars)`

`string rowvector tokenpchars(t)`

`void`<span class="nowrap"> _ `tokenpchars(t,`
`string rowvector pchars)`

`string rowvector tokenqchars(t)`

`void`<span class="nowrap"> _ `tokenqchars(t,`
`string rowvector qchars)`

`real scalar`<span class="nowrap"> _ `tokenallownum(t)`

`void`<span class="nowrap"> _ `tokenallownum(t, real scalar`
`allownum)`

`real scalar`<span class="nowrap"> _ `tokenallowhex(t)`

`void`<span class="nowrap"> _ `tokenallowhex(t, real scalar`
`allowhex)`

where

`t` is `transmorphic` and contains the parsing environment information.
You obtain a `t` from `tokeninit()` or `tokeninitstata()` and then pass
`t` to the other functions.

`wchars` is a `string scalar` containing the characters to be treated as
whitespace, such as `" "`, `(" "+char(9))`, or `""`.

`pchars` is a `string rowvector` containing the strings to be treated as
parsing characters, such as `""` and `(">", "<", ">=", "<=")`. `""` and
[<strong>J(1,0,"")</strong>](mf_j##void_matrices)
are given the same interpretation: there are no parsing characters.

`qchars` is a `string rowvector` containing the character pairs to be
treated as quote characters. `""` (that is, empty string) is given the
same interpretation as
[<strong>J(1,0,"")</strong>](mf_j##void_matrices);
there are no quote characters. `qchars`= (`""""')  (that is, the
two-character string quote indicates that `"` is to be treated as open
quote and `"` is to be treated as close quote.
`qchars`= (`""""', `"`""'"')  indicates that, in addition,  `" 
is to be treated as open quote and `"'` as close quote. In a syntax that
did not use `<` and `>` as parsing characters, `qchars`=`("<>")` would
indicate that `<` is to be treated as open quote and `>` as close quote.

`allownum` is a `string scalar` containing 0 or 1. `allownum`=1
indicates that numbers such as 12.23 and 1.52e+02 are to be returned as
single tokens even in violation of other parsing rules.

`allowhex` is a `string scalar` containing 0 or 1. `allowhex`=1
indicates that numbers such as 1.921fb54442d18X+001 and 1.0x+a are to be
returned as single tokens even in violation of other parsing rules.
