## Syntax

`declaration1fcnname(declaration2){c -(}declaration3{c )-}`

such as

`real matrixreal matrix X, real scalar ireal scalar     j, kreal vector     v`

`declaration1` is one of

`functiontypefunctionvoidfunction`

`declaration2` is

`typeargname,typeargname,`

where `argname` is the name you wish to assign to the argument.

`declaration3` are lines of the form of either of

`type`[varname](http://www.stata.com/help.cgi?varname)`,`[varname](http://www.stata.com/help.cgi?varname)`,externaltype`[varname](http://www.stata.com/help.cgi?varname)`,`[varname](http://www.stata.com/help.cgi?varname)`,`

`type` is defined as one of

`eltypeorgtype`

such as `real vector`

`eltype`

such as `real`

`orgtype`

such as `vector`

`eltype` and `orgtype` are each one of

`eltype              orgtype`

------------------------------------------------------------------------

------------------------------------------------------------------------

{cmd None}{txt None}

------------------------------------------------------------------------

------------------------------------------------------------------------

If `eltype`<span class="nowrap"> _is not specified, `transmorphic`
is assumed.  
If `orgtype` is not specified,<span class="nowrap"> _`matrix`<span
class="nowrap"> _is assumed.
