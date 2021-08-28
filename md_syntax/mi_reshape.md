## Syntax

{it None}(The words {rm None:long} and {rm None:wide} in what follows
have nothing to do with mi styles mlong, flong, flongsep, and wide; they
have to do with reshape's concepts.){rm None}

`long`<span options="TLC">{c TLC}_

------------------------------------------------------------------------

<span options="TRC">{c TRC}_`wide`|`i  jstub`|<span
options="TLC">{c TLC}_

------------------------------------------------------------------------

<span options="TRC">{c TRC}_|

------------------------------------------------------------------------

||`istub`**1**`stub`**2**|<span
options="|">{c \|}_**1**|<span
options="|">{c \|}_

------------------------------------------------------------------------

||**2**<span
options="|">{c \|}_

------------------------------------------------------------------------

||<span
options="|">{c \|}_**1**|<span
options="|">{c \|}_|<span
options="|">{c \|}_**2**|<span
options="BLC">{c BLC}_

------------------------------------------------------------------------

<span options="BRC">{c BRC}_<span options="BLC">{c BLC}_

------------------------------------------------------------------------

<span options="BRC">{c BRC}_

`j` existing variable

/

`mi reshape widestub, i(i) j(j)mi reshape longstub, i(i) j(j)`

\\

`j` new variable

Basic syntax

Convert mi data from long form to wide form

`mi reshape`
[<strong>wide</strong>](mi%20reshape##overview)
`stubnames,`
`i(`[varlist](http://www.stata.com/help.cgi?varlist)`)`
`j(`[varname](http://www.stata.com/help.cgi?varname)`)`
\[`options`\]

Convert mi data from wide form to long form

`mi reshape`
[<strong>long</strong>](mi%20reshape##overview)
`stubnames,`
`i(`[varlist](http://www.stata.com/help.cgi?varlist)`)`
`j(`[varname](http://www.stata.com/help.cgi?varname)`)`
\[`options`\]

`options`<span style="padding-left: 14.5rem;">_Description

<span options="59">_

`i(`[varlist](http://www.stata.com/help.cgi?varlist)`)`{nobreak
None}

`i` variable(s)

`j(`[varname](http://www.stata.com/help.cgi?varname)
\[`values`\]`)`{nobreak None}

long-&gt;wide: `j`, existing variable

wide-&gt;long: `j`, new variable

optionally specify values to subset `j`

`string`{nobreak None}

`j` is string variable (default numeric)

<span options="59">_

where `values` is{nobreak None}

`#`\[`-#`\] \[...\]{nobreak None}

if `j` is numeric (default)

`"string"` \[`"string"` ...\]{nobreak None}

if `j` is string

and where `stubnames` are variable names (long-&gt;wide), or stubs of
variable names (wide-&gt;long). Unlike
[<strong>reshape</strong>](http://www.stata.com/help.cgi?reshape),
`stubnames` may not contain `@` to denote where `j` appears in the name;
all `stubnames` must follow the style `stub#`.
