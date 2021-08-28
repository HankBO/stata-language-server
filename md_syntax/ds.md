## Syntax

Simple syntax

`ds` \[`, alpha`\]

Advanced syntax

`ds`
\[[varlist](http://www.stata.com/help.cgi?varlist)\]
\[`, options`\]

| Options                                                                                                                                                                                                                                                             |                              | Description                                                                                                 |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------|-------------------------------------------------------------------------------------------------------------|
| Main                                                                                                                                                                                                                                                                |                              |                                                                                                             |
|                                                                                                                                                                                                                                                                     | `not`                        | list variables not specified in [varlist](http://www.stata.com/help.cgi?varlist) |
|                                                                                                                                                                                                                                                                     | `alpha`                      | list variables in alphabetical order                                                                        |
|                                                                                                                                                                                                                                                                     | `detail`                     | display additional details                                                                                  |
|                                                                                                                                                                                                                                                                     | `varwidth(#)`                | display width for variable names; default is `varwidth(12)`                                                 |
|                                                                                                                                                                                                                                                                     | `skip(#)`                    | gap between variables; default is `skip(2)`                                                                 |
| Advanced                                                                                                                                                                                                                                                            |                              |                                                                                                             |
|                                                                                                                                                                                                                                                                     | `has(spec)`                  | describe subset that matches `spec`                                                                         |
|                                                                                                                                                                                                                                                                     | `not(spec)`                  | describe subset that does not match `spec`                                                                  |
|                                                                                                                                                                                                                                                                     | `insensitive`                | perform case-insensitive pattern matching                                                                   |
|                                                                                                                                                                                                                                                                     | `indent(#)`                  | indent output; seldom used                                                                                  |
|                                                                                                                                                                                                                                                                     | `format patternlist`       | display format matching `patternlist`                                                                       |
|                                                                                                                                                                                                                                                                     | `varlabel` \[`patternlist`\] | variable label or variable label matching `patternlist`                                                     |
|                                                                                                                                                                                                                                                                     | `char` \[`patternlist`\]     | characteristic or characteristic matching `patternlist`                                                     |
|                                                                                                                                                                                                                                                                     | `vallabel` \[`patternlist`\] | value label or value label matching `patternlist`                                                           |
| `insensitive` and `indent(#)` are not shown in the dialog box. <span options="spec">{marker spec}_{nobreak None} <span options="24">{synoptset 24}_{nobreak None} {synopthdr None:spec} {synoptline None} {synopt None}`type typelist`specified types |                              |                                                                                                             |

`typelist` used in `has(type typelist)` and `not(type typelist)`
is a list of one or more types, each of which may be `numeric`,
`string`, `str#`, `strL`, `byte`, `int`, `long`, `float`, or `double`,
or may be a `numlist` such as `1/8` to mean <span class="nowrap">"`str1`
`str2` ... `str8`"_. Examples include

|                           |                                                               |
|---------------------------|---------------------------------------------------------------|
| `has(type int)`           | is of type `int`                                              |
| `has(type byte int long)` | is of integer `type`                                          |
| `not(type int)`           | is not of type `int`                                          |
| `not(type byte int long)` | is not of the integer `type`s                                 |
| `has(type numeric)`       | is a numeric variable                                         |
| `not(type string)`        | is not a string (`str#` or `strL`) variable (same as above) |
| `has(type 1/40)`          | is `str1`, `str2`, ..., `str40`                               |
| `has(type str#)`          | is `str1`, `str2`, ..., `str2045` but not `strL`              |
| `has(type strL)`          | is of type `strL` but not `str#`                            |
| `has(type numeric 1/2)`   | is numeric or `str1` or `str2`                                |

`patternlist` used in, for instance, `has(format patternlist)`, is a
list of one or more `patterns`. A pattern is the expected text with the
addition of the characters `*` and `?`. `*` indicates 0 or more
characters go here, and `?` indicates exactly 1 character goes here.
Examples include

|                               |                                         |
|-------------------------------|-----------------------------------------|
| `has(format *f)`              | format is `%#.#f`               |
| `has(format %t*)`             | has time or date format                 |
| `has(format %-*s)`            | is a left-justified string              |
| `has(varl *weight*)`          | variable label includes word `weight`   |
| `has(varl *weight* *Weight*)` | variable label has `weight` or `Weight` |

To match a phrase, enclose the phrase in quotes.

`has(varl "*some phrase*")some phrase`

If instead you used `has(varl *some phrase*)`, then only variables
having labels ending in `some` or starting with `phrase` would be
listed.
