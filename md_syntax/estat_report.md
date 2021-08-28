## Syntax

`estat report`
\[[varlist](http://www.stata.com/help.cgi?varlist)\]
\[`, options`\]

| Options                                         |                                                                                                            | Description                                                             |
|-------------------------------------------------|------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|
|                                                 | `sort(p`\[`, descending`\]`)`                                                                          | sort items by the estimated `p` parameters; `p` may be `a`, `b`, or `c` |
|                                                 | `byparm`                                                                                                   | arrange table rows by parameter rather than by item                     |
| Main                                            |                                                                                                            |                                                                         |
|                                                 | `alabel(string)`                                                                                           | specify the `a` parameter label; the default is `Discrim`               |
|                                                 | `blabel(string)`                                                                                           | specify the `b` parameter label; the default is `Diff`                  |
|                                                 | `clabel(string)`                                                                                           | specify the `c` parameter label; the default is `Guess`                 |
|                                                 | `seqlabel`                                                                                                 | label parameters in sequential order                                    |
|                                                 | `post`                                                                                                     | post estimated IRT parameters and their VCE as estimation results       |
| Reporting                                       |                                                                                                            |                                                                         |
|                                                 | `level(#)`                                                                                                 | set confidence level; default is `level(95)`                            |
|                                                 | `verbose`                                                                                                  | display estimation output in long form                                  |
|                                                 | [<var class="command">display_options</var><strong></strong>](#display_options) | control columns and column formats                                      |
|                                                 | `coeflegend`                                                                                               | display legend instead of statistics                                    |
| `coeflegend` does not appear in the dialog box. |                                                                                                            |                                                                         |
