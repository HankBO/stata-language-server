## Syntax

A `stylelist` is a generic list of style elements and shorthands;
specific examples of `stylelists` include `symbolstylelist`,
`colorstylelist`, etc.

A `stylelist` is

`elel`

where each `el` may be

|                              |                                              |
|------------------------------|----------------------------------------------|
| `el`                         | Description {p2line None}                    |
| `as_defined_by_style`        | what `symbolstyle`, `colorstyle`, ... allows |
| `"as defined by style"`  | must quote `el`s containing spaces           |
| \`"`as "defined" by style`"' | compound quote `el`s containing quotes       |
| `.`                          | specifies the "default"                      |
| `=`                          | repeat previous `el`                         |
| `..`                         | repeat previous `el` until end               |
| `...`                        | same as `..` {p2line None}                   |

If the list ends prematurely, it is as if the list were padded out with
`.` (meaning the default for the remaining elements).

If the list has more elements than required, extra elements are ignored.

`=` in the first element is taken to mean `.` (period).

If the list allows numbers including missing values, if missing value is
not the default, and if you want to specify missing value for an
element, you must enclose the period in quotes: `"."`.

`msymbol(O d p o)msymbol(O . p)mcolor(blue . green green)mcolor(blue . green =)mcolor(blue blue blue blue)mcolor(blue = = =)mcolor(blue ...)`
