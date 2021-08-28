## Syntax

Import SAS XPORT Transport file into Stata

`import sasxport filename` \[`, import_options`\]

Describe contents of SAS XPORT Transport file

`import sasxport filename , describe` \[`member(mbrname)`\]

Export data in memory to a SAS XPORT Transport file

`export sasxport filename` _\[`if`\]
\[`in`\]_ \[`, export_options`\]

`export sasxport`
[varlist](http://www.stata.com/help.cgi?varlist)
`using filename` _\[`if`\] \[`in`\]_ \[`,`
`export_options`\]

| import\_options |                   | Description                                         |
|-----------------|-------------------|-----------------------------------------------------|
| Main            |                   |                                                     |
|                 | `clear`           | replace data in memory                              |
|                 | `novallabels`     | ignore accompanying `formats.xpf` file if it exists |
|                 | `member(mbrname)` | member to use; seldom used                          |

| export\_options |                          | Description                                                      |
|-----------------|--------------------------|------------------------------------------------------------------|
| Main            |                          |                                                                  |
|                 | `rename`                 | rename variables and value labels to meet SAS XPORT restrictions |
|                 | `replace`                | overwrite files if they already exist                            |
|                 | `vallabfile:(xpf)`       | save value labels in `formats.xpf`                               |
|                 | `vallabfile:(sascode)` | save value labels in SAS command file                            |
|                 | `vallabfile:(both)`      | save value labels in `formats.xpf` and in a SAS command file     |
|                 | `vallabfile:(none)`      | do not save value labels                                         |
