## Syntax

Attach notes to dataset

`notes` \[`evarname`\]`: text`

List all notes

`notes`

List specific notes

`notes` \[`list`\] `evarlist` \[`in #`\[`/#`\]\]

Search for a text string across all notes in all variables and \_dta

`notes search` \[`sometext`\]

Replace a note

`notes replace evarname in # : text`

Drop notes

`notes drop evarlist` \[`in #`\[`/#`\]\]

Renumber notes

`notes renumber evarname`

where `evarname` is `_dta` or a varname, `evarlist` is a varlist that
may contain `_dta`, and `#` is a number or the letter `l`.

If `text` includes the letters `TS` surrounded by blanks, the `TS` is
removed, and a time stamp is substituted in its place.
