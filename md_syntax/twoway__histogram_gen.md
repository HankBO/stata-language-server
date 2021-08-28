## Syntax

`twoway__histogram_gen varname` \[`weight`\] \[`if exp`\] \[`in`
`range`\] \[`,` <span options="-(">{c
-(}_`discrete_options`\|`continuous_options`<span options=")-">{c
)-}_ `common_options`\]

where `discrete_options` are

`discrete_options`

Description

------------------------------------------------------------------------

`discrete`

specify data are discrete

`width(#)`

width of bins in `varname` units

`start(#)`

theoretical minimum value

------------------------------------------------------------------------

and where `continuous_options` are

`continuous_options`

Description

------------------------------------------------------------------------

`bin(#)`

`#` of bins

`width(#)`

width of bins in `varname` units

`start(#)`

lower limit of first bin

------------------------------------------------------------------------

and where `common_options` are

`common_options`

Description

------------------------------------------------------------------------

`density`

draw as density (default)

`fraction`

draw as fractions

`frequency`

draw as frequencies

`generate:(h xreplace)`

generate variables

`display`

display (bin) start and width

------------------------------------------------------------------------

`fweight`s are allowed; see
[<strong>weights</strong>](http://www.stata.com/help.cgi?weights).
