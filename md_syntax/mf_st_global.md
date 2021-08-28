## Syntax

`string scalar st_global(string scalar name)`

`void`<span class="nowrap"> _ `st_global(string scalar name,`
`string scalar contents)`

`void`<span class="nowrap"> _ `st_global(string scalar name,`
`string scalar contents, string scalar hcat)`

`string scalar st_global_hcat(string scalar name)`

where

1\. `name` is to contain

a\. global macro such as `"myname"`

b\. `r()` macro such as `"r(names)"`

c\. `e()` macro such as `"e(cmd)"`

d\. `s()` macro such as `"s(vars)"`

e\. `c()` macro such as `"c(current_date)"`

f\. dataset characteristic such as `"_dta[date]"`

g\. variable characteristic such as `"mpg[note]"`

2\. `st_global(name)` returns the contents of the specified Stata
global. It returns "" when the global does not exist.

3\. `st_global(name, contents)` sets or resets the contents of
the specified Stata global.

4\. `st_global(name, "")` deletes the specified Stata global. It
does this even if `name` is not a macro. `st_global("r(N)", "")` would
delete `r(N)` whether it were a macro, scalar, or matrix.

5\. `st_global(name, contents, hcat)` sets or resets the
contents of the specified Stata global, and it sets or resets the hidden
or historical status when `name` is an `e()` or `r()` value. Allowed
`hcat` values are "`visible`", "`hidden`", "`historical`", and a string
scalar release number such as such as "`10`", "`10.1`", or any string
release number matching "`#`\[`#`\]\[`.`\[`#`\[`#`\]\]\]". See [**\[P\]
return**](http://www.stata.com/manuals14/preturn.pdf) for a description
of hidden and historical `r()` and `e()` values.

When `st_global(name, contents)` is used to set an `e()` or
`r()` value, its `hcat` is set to "`visible`".

6\. `st_global_hcat(name)` returns the `hcat` associated with an
`e()` or `r()` value.
