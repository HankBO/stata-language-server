## Syntax

`real scalar st_fopen(filename, suffix, mode,`
`replace, public)`

`real scalar st_fopen(filename, suffix, mode,`
`replace)`

`real scalar st_fopen(filename, suffix, mode)`

where

`filename`: `string scalar` containing filename or path and filename
such as `"myfile"` or `"myfile.dta"`; `filename` is updated by
`st_fopen()` to contain the full name of the file, which would be
`"myfile.dta"` in both examples

`suffix`: `string scalar` containing default suffix with leading period,
such as `".dta"`

`mode`: `string scalar` containing `"r"`, `"w"`, or `"rw"`

`replace`: relevant only if `mode` is `"w"` or `"rw"`;  
if `mode` is `"w"`, `replace` is an optional `real scalar` containing

2<span class="nowrap"> _file may be overwritten (but is left in
place for read/write access) and display note if file does not exist,

1<span class="nowrap"> _file may be replaced (and is erased before
opening if it already exists) and display note if file does not exist,

0<span class="nowrap"> _file may not be replaced,

-1<span class="nowrap"> _file may be replaced (and is erased
before opening if it already exists) but do not show note if file does
not exist, or

-2<span class="nowrap"> _file may be overwritten (but is left in
place for read/write access) but do not show note if file does not
exist.

`replace`&lt;0 treated as -1; `replace`&gt;0 treated as 1;
`replace`==`.` treated as 0; `replace` not specified treated as 0

if `mode` is `"rw"`, `replace` is an optional `real scalar` containing

1<span class="nowrap"> _file may be replaced and display note if
it is,

0<span class="nowrap"> _file may not be replaced, or

-1<span class="nowrap"> _file may be replaced but do not show note
if it is.

`replace`&lt;-1 treated as -2; `replace`&gt;1 treated as 2;
`replace`==`.` treated as 0; `replace` not specified treated as 0

`public`: relevant only if `mode` is `"w"` or `"rw"`;  
optional `real scalar` containing

0<span class="nowrap"> _file to be private or

1<span class="nowrap"> _file to be public

All nonzero (including missing) treated as 1; 1 assumed if `public` not
specified
