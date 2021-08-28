## Syntax

`infile`
[<strong>using</strong>](http://www.stata.com/help.cgi?using)
`dfilename` _\[`if`\] \[`in`\]_ \[`,`
`options`\]

If `dfilename` is specified without an extension, `.dct` is assumed. If
`dfilename` contains embedded spaces, remember to enclose it in double
quotes.

| Options |                   | Description                              |
|---------|-------------------|------------------------------------------|
| Main    |                   |                                          |
|         | `using(filename)` | text dataset filename                    |
|         | `clear`           | replace data in memory                   |
| Options |                   |                                          |
|         | `automatic`       | create value labels from nonnumeric data |
|         | `ebcdic`          | treat text dataset as EBCDIC             |

A dictionary is a text file that is created with the Do-file Editor or
an editor outside Stata. This file specifies how Stata should read
fixed-format data from a text file. The syntax for a dictionary is

------------------------------------------------------------------------

------------------------------------------------------------------------

`infiledictionaryusingfilename{c -(}* comments may be included freely_lrecl(#)_firstlineoffile(#)_lines(#)_line(#)_newline(#)_column(#)_skip(#)typevarname:lblname%infmt"variable label"{c )-}(your data might appear here)`

------------------------------------------------------------------------

------------------------------------------------------------------------

where `%infmt` is { `%`\[`#`\[`.#`\]\]
{`f`\|`g`\|`e`<span options=")-">{c
)-}_ \| `%`\[`#`\]`s` \| `%`\[`#`\]`S`<span options=")-">{c
)-}_
