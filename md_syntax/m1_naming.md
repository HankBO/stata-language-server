## Syntax

A `name` is 1-32 characters long, the first character of which must be

`AZaz_`

and the remaining characters of which may be

`AZaz_09`

except that names may not be a word reserved by Mata (see
[<strong>[M-2] reswords</strong>](http://www.stata.com/help.cgi?m2_reswords)
for a list).

Examples of names include

`xx2alphalogarithm_of_xLogOfX`

Case matters: `alpha`, `Alpha`, and `ALPHA` are different names.

Variables and functions have separate name spaces, which means a
variable and a function can have the same name, such as `value` and
`value()`, and Mata will not confuse them.
