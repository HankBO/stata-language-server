## Syntax

|                   |                                              |
|-------------------|----------------------------------------------|
| `pr_options`      | Description {p2line None}                    |
| `tmargin:(#)` | top margin, in inches, 0 &lt;= `#` &lt;= 20  |
| `lmargin:(#)` | left margin, in inches, 0 &lt;= `#` &lt;= 20 |
| `logo(on`\|`off)` | whether to display Stata logo {p2line None}  |

Current default values may be listed by typing

`. graph set print`

The defaults may be changed by typing

`. graph set print name value`

where `name` is the name of a `pr_option`, omitting the parentheses.
