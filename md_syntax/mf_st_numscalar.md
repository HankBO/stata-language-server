## Syntax

`real`<span class="nowrap"> _
`st_numscalar(string scalar name)`

`void`<span class="nowrap"> _
`st_numscalar(string scalar name, real value)`

`void`<span class="nowrap"> _
`st_numscalar(string scalar name, real value,`
`string scalar hcat)`

`string st_numscalar_hcat(string scalar name)`

`string st_strscalar(string scalar name)`

`void`<span class="nowrap"> _
`st_strscalar(string scalar name, string value)`

where

1\. Functions allow `name` to be

a\. global scalar such as `"myname"`,

b\. `r()` scalar such as `"r(mean)"`,

c\. `e()` scalar such as `"e(N)"`, or

d\. `c()` scalar such as `"c(namelenchar)"`.

Note that string scalars never appear in `r()` and `e()`; thus (b) and
(c) do not apply to `st_strscalar()`.

2\. `st_numscalar(name)` and `st_strscalar(name)` return the
value of the specified Stata scalar. They return a 1 `x` 1 result if the
specified Stata scalar exists and return a 0 `x` 0 result otherwise.

3\. `st_numscalar(name, value)` and `st_strscalar(name,`
`value)` set or reset the contents of the specified Stata scalar.

4\. `st_numscalar(name, value)` and `st_strscalar(name,`
`value)` delete the specified Stata scalar if `value==J(0,0,.)` (if
`value` is 0 `x` 0).

5\. `st_numscalar(name, value, hcat)` sets or resets the
specified Stata scalar and sets or resets the hidden or historical
status when `name` is an `e()` or `r()` value. Allowed `hcat` values are
"`visible`", "`hidden`", "`historical`", and a string scalar release
number such as such as "`10`", "`10.1`", or any string release number
matching "`#`\[`#`\]\[`.`\[`#`\[`#`\]\]\]". See [**\[P\]
return**](http://www.stata.com/manuals14/preturn.pdf) for a description
of hidden and historical stored results.

When `st_numscalar(name, value)` is used to set an `e()` or
`r()` value, its `hcat` is set to "`visible`".

There is no three-argument form of `st_strscalar()` because there are no
`r()` or `e()` string scalar values.
