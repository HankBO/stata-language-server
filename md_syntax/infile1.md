## Syntax

`infile`
[varlist](http://www.stata.com/help.cgi?varlist)
\[`_skip`\[`(#)`\]
\[[varlist](http://www.stata.com/help.cgi?varlist)
\[`_skip`\[`(#)`\] `...`\]\]\] `using filename` <span
class="command">\[`if`\] \[`in`\]_ \[`, options`\]

If `filename` is specified without an extension, `.raw` is assumed. If
`filename` contains embedded spaces, remember to enclose it in double
quotes.

| Options |                 | Description                                                        |
|---------|-----------------|--------------------------------------------------------------------|
| Main    |                 |                                                                    |
|         | `clear`         | replace data in memory                                             |
| Options |                 |                                                                    |
|         | `automatic`     | create value labels from nonnumeric data                           |
|         | `byvariable(#)` | organize external file by variables; `#` is number of observations |
