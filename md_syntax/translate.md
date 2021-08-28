## Syntax

Print log and SMCL files

`print filename` \[`, like(ext) name(windowname)`
`override_options`\]

Translate log files to SMCL files and vice versa

`translate filename_in filename_out` \[`, translator(tname)`
`name(windowname) override_options replace`\]

View translator parameter settings

`translator query` \[`tname`\]

Change translator parameter settings

`translator set` \[`tname setopt setval`\]

Return translator parameter settings to default values

`translator reset tname`

List current mappings from one extension to another

`transmap query` \[`.ext`\]

Specify that files with one extension be treated the same as files with
another extension

`transmap define .ext_new .ext_old`

`filename` in `print`, in addition to being a filename to be printed,
may be specified as `@Results` to mean the Results window and `@Viewer`
to mean the Viewer window.

`filename_in` in `translate` may be specified just as `filename` in
`print`.

`tname` in `translator` specifies the name of a translator; see the
**[<strong>translator()</strong>](#translator)**
option under `Options for translate`.
