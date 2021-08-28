## Syntax

`real matrix`<span class="nowrap"> _
`st_matrix(string scalar name)`

`string matrix st_matrixrowstripe(string scalar name)`

`string matrix st_matrixcolstripe(string scalar name)`

`void`<span class="nowrap"> _ `st_matrix(string scalar name,`
`real matrix X)`

`void`<span class="nowrap"> _ `st_matrix(string scalar name,`
`real matrix X,`  
`string scalar hcat)`

`void`<span class="nowrap"> _
`st_matrixrowstripe(string scalar name, string matrix s)`

`void`<span class="nowrap"> _
`st_matrixcolstripe(string scalar name, string matrix s)`

`void`<span class="nowrap"> _
`st_replacematrix(string scalar name, real matrix X)`

`string scalar st_matrix_hcat(name)`

where

1\. All functions allow `name` to be

a\. global matrix name such as `"mymatrix"`,

b\. `r()` matrix such as `"r(Z)"`, or

c\. `e()` matrix such as `"e(V)"`.

2\. `st_matrix(name)` returns the contents of the specified Stata
matrix. It returns `J(0,0,.)` if the matrix does not exist.

3\. `st_matrix(name, X)` sets or resets the contents of the
specified Stata matrix. Row and column stripes are set to the default
`r1`, `r2`, ..., and `c1`, `c2`, ....

4\. `st_replacematrix(name, X)` is an alternative way to replace
existing Stata matrices. The number of rows and columns of `X` must
match the Stata matrix being replaced, and in return, the row and column
stripes are not replaced.

5\. `st_matrix(name, X)` deletes the specified Stata matrix if
`value==J(0,0,.)` (if value is 0 `x` 0).

6\. Neither `st_matrix()` nor `st_replacematrix()` can be used to set,
replace, or delete special Stata `e()` matrices `e(b)`, `e(V)`, or
`e(Cns)`. Only Stata commands `ereturn post` and `ereturn repost`
can be used to set these special matrices; see
**[<strong>[P] ereturn</strong>](http://www.stata.com/help.cgi?ereturn)**.
Also see
**[<strong>[M-5] stata()</strong>](http://www.stata.com/help.cgi?mf_stata)**
for executing Stata commands from Mata.

7\. `st_matrix(name, X, hcat)` sets or resets the specified
Stata matrix and sets the hidden or historical status when setting a
Stata `e()` or `r()` matrix. Allowed `hcat` values are "`visible`",
"`hidden`", "`historical`", and a string scalar release number such as
"`10`", "`10.1`", or any string release number matching
"`#`\[`#`\]\[`.`\[`#`\[`#`\]\]\]". See [**\[P\]
return**](http://www.stata.com/manuals14/preturn.pdf) for a description
of hidden and historical stored results.

8\. `st_matrix_hcat(name)` returns the `hcat` associated with a
Stata `e()` or `r()` matrix.

9\. `st_matrixrowstripe()` and `st_matrixcolstripe()` allow querying and
resetting the row and column stripes of existing or previously created
Stata matrices.
