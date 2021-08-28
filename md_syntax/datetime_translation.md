## Syntax

The string-to-numeric date and time translation functions are

|

------------------------------------------------------------------------

<span options="+">{c +}_

------------------------------------------------------------------------

|`clock(HRFstr,mask,topyear)`|`Clock(HRFstr,mask,topyear)`||`date(HRFstr,mask,topyear)`||`weekly(HRFstr,mask,topyear)`|`monthly(HRFstr,mask,topyear)`|`quarterly(HRFstr,mask,topyear)`<span
options="|">{c
\|}_`halfyearly(HRFstr,mask,topyear)`<span
options="|">{c \|}_`yearly(HRFstr,mask,topyear)`

------------------------------------------------------------------------

<span options="BT">{c BT}_

------------------------------------------------------------------------

where

`HRFstr` is the string value (HRF) to be translated,

`topyear` is described in `Working with two-digit years`, below,

and `mask` specifies the order of the date and time components and is a
string composed of a sequence of these elements:

|

------------------------------------------------------------------------

<span options="+">{c +}_

------------------------------------------------------------------------

`M`|`D`|`Y`|`19Y`|`xx20Y`|`xx`<span
options="|">{c \|}_`h`|`m`<span
options="|">{c \|}_`s`|<span
options="|">{c \|}_`#`|

------------------------------------------------------------------------

<span options="BT">{c BT}_

------------------------------------------------------------------------

Blanks are also allowed in `mask`, which can make the `mask` easier to
read, but they otherwise have no significance.

Examples of `masks` include

`"MDY"`<span class="nowrap"> _`HRFstr` contains month, day, and
year, in that order.

`"MD19Y"`<span class="nowrap"> _means the same as `"MDY"` except
that `HRFstr` may contain two-digit years, and when it does, they are to
be treated as if they are 4-digit years beginning with 19.

`"MDYhms"`<span class="nowrap"> _`HRFstr` contains month, day,
year, hour, minute, and second, in that order.

`"MDY hms"`<span class="nowrap"> _means the same as `"MDYhms"`;
the blank has no meaning.

`"MDY#hms"`<span class="nowrap"> _means that one element between
the year and the hour is to be ignored. For example, `HRFstr` contains
values like `"1-1-2010 at 15:23:17"` or values like
`"1-1-2010 at 3:23:17 PM"`.
