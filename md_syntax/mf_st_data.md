## Syntax

`real scalar`{nobreak None}

`_st_data(`{nobreak None}

`real scalar i,real scalar j)`

`real matrix`{nobreak None}

`st_data(`{nobreak None}

`real matrix i,rowvector j)`{right None:(1,2)}

`real matrix`{nobreak None}

`st_data(`{nobreak None}

`real matrix i,rowvector j,scalar selectvar)`{right
None:(1,2,3)}

`string scalar`{nobreak None}

`_st_sdata(`{nobreak None}

`real scalar i,real scalar j)`

`string matrix`{nobreak None}

`st_sdata(`{nobreak None}

`real matrix i,rowvector j`{right None:(1,2)}

`string matrix`{nobreak None}

`st_sdata(`{nobreak None}

`real matrix i,rowvector j,scalar selectvar)`{right
None:(1,2,3)}

where

1\. `i` may be specified as a 1 `x` 1 scalar, as a 1 `x` 1 scalar
containing missing, as a column vector of observation numbers, as a row
vector specifying an observation range, or as a `k x` 2 matrix
specifying both.

a\. `st_data(1, 2)` returns the first observation on the second
variable.

b\. `st_data(., 2)` returns all observations on the second variable.

c\. `st_data((1\2\5), 2)` returns observations 1, 2, and 5 on the second
variable.

d\. `st_data((1,5), 2)` returns observations 1 through 5 on the second
variable.

e\. `st_data((1,5\7,9), 2)` returns observations 1 through 5 and
observations 7 through 9 on the second variable.

When a range is specified, any element of the range (`i1`,`i2`) may be
specified to contribute zero observations if `i2`=`i1`-1.

2\. `j` may be specified as a real row vector or as a string scalar or
string row vector.

a\. `st_data(., .)` returns the values of all variables, all
observations of the Stata dataset.

b\. `st_data(., 1)` returns the value of the first variable, all
observations.

c\. `st_data(., (3,1,9))` returns the values of the third, first, and
ninth variables of all observations.

d\. `st_data(., ("mpg", "weight"))` returns the values of variables
`mpg` and `weight`, all observations.

e\. `st_data(., "mpg weight")` does the same as d above.

f\. `st_data(., ("gnp", "l.gnp"))` returns the values of `gnp` and the
lag of `gnp`, all observations.

g\. `st_data(., "gnp l.gnp")` does the same as f above.

h\. `st_data(., "mpg i.rep78")` returns the value of `mpg` and the 5
pseudovariables associated with `i.rep78`. There are 5 pseudovariables
because we are imagining that `auto.dta` is in memory; the actual number
is a function of the values taken on by the variable in the sample
specified. Factor variables can be specified only with string scalars;
specifying `("mpg", "i.rep78")` will not work.

3\. `selectvar` may be specified as real or as a string. Observations
for which `selectvar`!=0 will be selected. If `selectvar` is real, it is
interpreted as a variable number. If string, `selectvar` should contain
the name of a Stata variable.

Specifying `selectvar` as `""` or as missing (`.`) has the same result
as not specifying `selectvar`; no observations are excluded.

Specifying `selectvar` as `0` means that observations with missing
values of the variables specified by `j` are to be excluded.
