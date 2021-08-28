## Syntax

{`local` \| `global`<span options=")-">{c
)-}_ `macname : list uniq macname`

{`local` \| `global`<span options=")-">{c
)-}_ `macname : list dups macname`

{`local` \| `global`<span options=")-">{c
)-}_ `macname : list sort macname`

{`local` \| `global`<span options=")-">{c
)-}_ `macname : list retokenize macname`

{`local` \| `global`<span options=")-">{c
)-}_ `macname : list clean macname`

{`local` \| `global`<span options=")-">{c
)-}_ `macname : list macname | macname`

{`local` \| `global`<span options=")-">{c
)-}_ `macname : list macname & macname`

{`local` \| `global`<span options=")-">{c
)-}_ `macname : list macname - macname`

{`local` \| `global`<span options=")-">{c
)-}_ `macname : list macname == macname`

{`local` \| `global`<span options=")-">{c
)-}_ `macname : list macname === macname`

{`local` \| `global`<span options=")-">{c
)-}_ `macname : list macname in macname`

{`local` \| `global`<span options=")-">{c
)-}_ `macname : list sizeof macname`

{`local` \| `global`<span options=")-">{c
)-}_ `macname : list posof "element" in macname`

Note: Where `macname` appears above, it is the name of a macro and not
its contents that you are to type. For example, you are to type

`local result : list list1 | list2`

and not

 local result : list "`list1'" | "`list2'" 

`macname`s that appear to the right of the colon are assumed to be the
names of local macros. You may type `local(macname)` to emphasize
that fact. Type `global(macname)` if you wish to refer to a global
macro.
