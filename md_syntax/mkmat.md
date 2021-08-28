## Syntax

`mkmat`
[varlist](http://www.stata.com/help.cgi?varlist)
_\[`if`\] \[`in`\]_ \[`,`
`matrix:(matname) nomissing rownames(varname) roweq(varname)`
`rowprefix(string) obs nchar(#)`\]

`svmat` _\[`type`\] \[_ `A` \[`,`
`names:(col`\|`eqcol`\|`matcol`\|`string)`\]

`matname A namelist` \[`, rows:(range) columns:(range)`
`explicit`\]

where `A` is the name of an existing matrix, `type` is a storage type
for new variables, and `namelist` is one of

1)<span options="2">{space 2}_a `varlist`, that is, names of
existing variables possibly abbreviated;

2)<span options="2">{space 2}_`_cons` and the names of existing
variables possibly abbreviated;

3)<span options="2">{space 2}_arbitrary names when the `explicit`
option is specified.

To reset problem-size limits, see
[<strong>[R]</strong> matsize](http://www.stata.com/help.cgi?matsize).
