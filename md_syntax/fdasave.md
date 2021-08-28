## Syntax

Save data in memory in FDA format

`fdasave filename` _\[`if`\] \[`in`\]_
\[`, fdasave_options`\]

`fdasave`
[varlist](http://www.stata.com/help.cgi?varlist)
[<strong>using</strong>](http://www.stata.com/help.cgi?using)
`filename` _\[`if`\] \[`in`\]_ \[`,`
`fdasave_options`\]

Read SAS XPORT file into Stata

`fdause filename` \[`, fdause_options`\]

Describe contents of SAS XPORT Transport file

`fdadescribe filename` \[`, member(mbrname)`\]

| fdasave\_options |                          | Description                                                      |
|------------------|--------------------------|------------------------------------------------------------------|
| Main             |                          |                                                                  |
|                  | `rename`                 | rename variables and value labels to meet SAS XPORT restrictions |
|                  | `replace`                | overwrite files if they already exist                            |
|                  | `vallabfile:(xpf)`       | save value labels in `formats.xpf`                               |
|                  | `vallabfile:(sascode)` | save value labels in SAS command file                            |
|                  | `vallabfile:(both)`      | save value labels in `formats.xpf` and in a SAS command file     |
|                  | `vallabfile:(none)`      | do not save value labels                                         |

| fdause\_options |                   | Description                                         |
|-----------------|-------------------|-----------------------------------------------------|
|                 | `clear`           | replace data in memory                              |
|                 | `novallabels`     | ignore accompanying `formats.xpf` file if it exists |
|                 | `member(mbrname)` | member to use; seldom used                          |
