## Syntax

{nobreak None}

`A=asarray_create(keytype`{right None}`declare A                 `

\[, `keydim`

\[, `minsize`

\[, `minratio`

\[, `maxratio` \]\]\]\]\]`)`

{nobreak None}

`asarray(A,key,a)`{right None}`A[key] = a                `

{nobreak None}

`a=asarray(A,key)`{right None}`a = A[key] or a = notfound`

{nobreak None}

`asarray_remove(A,key)`{right None}`delete A[key] if it exists`

{nobreak None}

`bool=asarray_contains(A,key)`{right
None}`A[key] exists?            `

{nobreak None}

`N=asarray_elements(A)`{right None}`# of elements in A        `

{nobreak None}

`keys=asarray_keys(A)`{right None}`all keys in A             `

{nobreak None}

`loc=asarray_first(A)`{right
None}`location of first element `{right
None}`or NULL                   `

{nobreak None}

`loc=asarray_next(A,loc)`{right
None}`location of next element  `{right
None}`or NULL                   `

{nobreak None}

`key=asarray_key(A,loc)`{right
None}`key at loc                `

{nobreak None}

`a=asarray_contents(A,loc)`{right
None}`contents a at loc         `

{nobreak None}

`asarray_notfound(A,notfound)`{right
None}`set notfound value        `

{nobreak None}

`notfound=asarray_notfound(A)`{right
None}`query notfound value      `

where

`A:` Associative array `A[key]`. Created by `asarray_create()` and
passed to the other functions. If `A` is declared, it is declared
`transmorphic`.

`keytype:` Element type of keys; `"string"`, `"real"`, `"complex"`, or
`"pointer"`. Optional; default `"string"`.

`keydim:` Dimension of key; 1 &lt;= `keydim` &lt;= 50. Optional; default
1.

`minsize:` Initial size of hash table used to speed locating keys in
`A`; `real scalar`; 5 &lt;= `minsize` &lt;= 1,431,655,764. Optional;
default 100.

`minratio:` Fraction filled at which hash table is automatically
downsized; `real scalar`; 0 &lt;= `minratio` &lt;= 1. Optional; default
0.5.

`maxratio:` Fraction filled at which hash table is automatically
upsized; `real scalar`; 1 &lt; `maxratio` &lt;= `.` (meaning infinity).
Optional; default 1.5.

`key:` Key under which an element is stored in `A`; `string scalar` by
default; type and dimension are declared using `asarray_create()`.

`a:` Element of `A`; `transmorphic`; may be anything of any size;
different `A[key]` elements may have different types of contents.

`bool:` Boolean logic value; `real scalar`; equal to 1 or 0 meaning true
or false.

`N:` Number of elements stored in `A`; `real scalar`; 0 &lt;= `N` &lt;=
2,147,483,647.

`keys:` List of all keys that exist in `A`. Each row is a key. Thus
`keys` is a `string colvector` if keys are `string scalars`, a
`string matrix` if keys are `string vectors`, a `real colvector` if keys
are `real scalars`, etc. Note that `rows(keys)` = `N`.

`loc:` A location in `A`; `transmorphic`. The first location is returned
by `asarray_first()`, subsequent locations by `asarray_next()`.
`loc==NULL` when there are no more elements.

`notfound:` Value returned by `asarray(A, key)` when `key` does
not exist in `A`. `notfound = J(0,0,.)` by default.
