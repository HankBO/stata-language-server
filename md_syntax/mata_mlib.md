## Syntax

: `mata mlib create libname`<span class="nowrap"> _ \[`,`
`dir(path) replace size(#)` \]

: `mata mlib add`<span class="nowrap"> _ `libname fcnlist()`
\[`, dir(path) complete` \]

: `mata mlib index`

: `mata mlib query`

where `fcnlist()` is a `namelist` containing only function names, such
as

`fcnlist()`

------------------------------------------------------------------------

`myfunc()myfunc()myotherfunc()foo()f*() g*()*()`

------------------------------------------------------------------------

**[<strong>[M-3] namelists</strong>](http://www.stata.com/help.cgi?m3_namelists)**

and where `libname` is the name of a library. You must start `libname`
with the letter `l` and do not add the `.mlib` suffix as it will be
added for you. Examples of `libnames` include

`libname`

------------------------------------------------------------------------

`lmathlmath.mliblmoremathlmoremath.mliblnjclnjc.mlib`

------------------------------------------------------------------------

Also `libnames` that begin with the letters `lmata`, such as
`lmatabase`, are reserved for the names of official libraries.

This command is for use in Mata mode following Mata's colon prompt. To
use this command from Stata's dot prompt, type

`mata: mata mlib`
