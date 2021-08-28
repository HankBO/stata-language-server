## Syntax

Analyze files to be translated

`unicode analyze filespec` \[, `redo nodata`\]

Set encoding to be used during translation

`unicode encoding set` \[`"`\]`encoding`\[`"`\]

Translate or retranslate files

`unicode translate`<span class="nowrap"> _`filespec` \[`,`
`invalid`\[`(escape`\|`mark`\|`ignore)`\] `transutf8 nodata` \]

`unicode retranslate filespec` \[`,`
`invalid`\[`(escape`\|`mark`\|`ignore)`\] `transutf8 replace`
`nodata` \]

Restore backups of translated files

`unicode restore filespec` \[`, replace` \]

Delete backups of translated files

`unicode erasebackups, badidea`

`filespec` is a single filename or a file specification containing `*`
and `?` specifying one or more files, such as

`*.dta`

`*.do`

`*.*`

`*`

`myfile.*`

`year??data.dta`

`unicode` analyzes and translates `.dta` files and text files. It
assumes that filenames with suffix `.dta` contain Stata datasets and
that all other suffixes contain text. Those other suffixes are `.ado`,
`.do`, `.mata`, `.txt`, `.csv`, `.sthlp`, `.class`, `.dlg`, `.idlg`,
`.ihlp`, `.smcl`, and `.stbcal`.

Files with suffixes other than those listed are ignored. Thus "\*.\*"
would ignore any .docx files or files with other suffixes. If such files
contain text, they can be analyzed and translated by specifying the
suffix explicitly, such as info.README and \*.README.
