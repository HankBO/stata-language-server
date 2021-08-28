## Syntax

Declaring a \_pb\_exp\_list object

`.obj` = `._pb_exp_list.new, stub(name)` \[`reset_options`\]

Resetting your \_pb\_exp\_list object

`.obj.reset, stub(name)` \[`reset_options`\]

Parsing the expression list

`.obj.parse` \[`name:`\] `exp` \[`, eform_option`
`passthru_options`\]

`.obj.parse` \[`(`\[`name:`\] `exp)` ...\] \[`, eform_option`
`passthru_options`\]

Computing point and variance estimates

`.obj.compute b V`

Posting the expressions to e()

`.obj.post_legend`

| reset\_options           |                 | Description                               |
|--------------------------|-----------------|-------------------------------------------|
| \*                       | `stub(name)`    | stub for default name generation          |
|                          | `eqstub(name)`  | stub for default equation name generation |
|                          | `cmdname(name)` | name of assumed estimation command        |
| \* `stub()` is required. |                 |                                           |
