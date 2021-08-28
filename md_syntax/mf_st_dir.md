## Syntax

`string colvector st_dir(cat, subcat, pattern)`

`string colvector st_dir(cat, subcat, pattern, adorn)`

where

`cat`: `string scalar` containing `"local"`, `"global"`, `"r()"`,
`"e()"`, `"s()"`, or `"char"`

`subcat`: `string scalar` containing `"macro"`, `"numscalar"`,
`"strscalar"`, `"matrix"`, or, if `cat`==`"char"`, `"_dta"` or a name.

`pattern`: `string scalar` containing a pattern as defined in
**[<strong>[M-5] strmatch()</strong>](http://www.stata.com/help.cgi?mf_strmatch)**

`adorn`: `string scalar` containing 0 or non-0

The valid `cat`--`subcat` combinations and their meanings are

`catsubcat`

------------------------------------------------------------------------

`"local"     "macro""global"    "macro""global"    "numscalar""global"    "strscalar""global"    "matrix""r()"       "macro"r()"r()"       "numscalar"r()"r()"       "matrix"r()"e()"       "macro"e()"e()"       "numscalar"e()"e()"       "matrix"e()"s()"       "macro"s()"char"      "_dta"_dta[]"char"      "name"name[]`

------------------------------------------------------------------------

`st_dir()` returns an empty list if an invalid `cat`--`subcat`
combination is specified.
