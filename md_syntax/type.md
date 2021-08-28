## Syntax

`type` \[`"`\]`filename`\[`"`\] \[`, options`\]

Note: Double quotes must be used to enclose `filename` if the name
contains blanks.

| Options |            | Description                                                                              |
|---------|------------|------------------------------------------------------------------------------------------|
|         | `asis`     | show file as is; default is to display files with suffix **.smcl** or **.sthlp** as SMCL |
|         | `smcl`     | display file as SMCL; default for files with suffix **.smcl** or **.sthlp**              |
|         | `showtabs` | display tabs as **&lt;T&gt;** rather than being expanded                                 |
|         | `starbang` | list lines in the file that begin with "`*!`"                                            |
|         | `lines(#)` | list first `#` lines                                                                     |
