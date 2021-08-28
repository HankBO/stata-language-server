## Syntax

`_mkvec matname` \[`, from(init_specs` \[`, copy skip`\]`)`
`update colnames(list_of_colfullnames) first error(string)` \]

where init\_specs is one of the following forms:

`vectorname`

{ \[`eqname:`\]`name=#` \|
`/eqname=#` } \[`...`\]

`##...`

If the last form above is used, then the `copy` option must be
specified.

`list_of_colfullnames` is a full matrix stripe, such as that returned by
the `colfullnames` macro function.
