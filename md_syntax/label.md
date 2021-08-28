## Syntax

Label dataset

`label data` \[`"label"`\]

Label variable

`label variable`
[varname](http://www.stata.com/help.cgi?varname)
\[`"label"`\]

Define value label

`label define lblname # "label"` \[`# "label" ...`\]
\[`, add modify replace nofix`\]

Assign value label to variables

`label values`
[varlist](http://www.stata.com/help.cgi?varlist)
`lblname` \[`, nofix`\]

Remove value labels

`label values`
[varlist](http://www.stata.com/help.cgi?varlist)
\[`.`\]

List names of value labels

`label dir`

List names and contents of value labels

`label list` \[`lblname` \[`lblname ...`\]\]

Copy value label

`label copy lblname lblname` \[`, replace`\]

Drop value labels

`label drop` {`lblname`
\[`lblname ...`\] \| `_all`}

Save value labels in do-file

`label save` \[`lblname` \[`lblname...`\]\] `using filename` \[`,`
`replace`\]

Labels for variables and values in multiple languages

`labellanguage`{right None:(see
}[<strong>[D]</strong> label language](http://www.stata.com/help.cgi?label_language))

where `#` is an integer or an extended missing value (`.a`, `.b`, ...,
`.z`).
