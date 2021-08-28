## Syntax

`pkshape id sequence period1 period2` \[`periodlist`\] \[`,`
`options`\]

Variable `id` specifies unique subject identifiers. Variable `sequence`
specifies the sequence (numeric or string) in which treatments were
received. Variables `period1`, `period2`, and so on specify the
pharmacokinetic measurements such as AUC in the corresponding periods.

| Options |                     | Description                                                           |
|---------|---------------------|-----------------------------------------------------------------------|
|         | `order(string)`     | apply treatments in specified order; required with numeric `sequence` |
|         | `outcome(newvar)`   | name for outcome variable; default is `outcome(outcome)`              |
|         | `treatment(newvar)` | name for treatment variable; default is `treatment(treat)`            |
|         | `carryover(newvar)` | name for carryover variable; default is `carryover(carry)`            |
|         | `sequence(newvar)`  | name for sequence variable; default is `sequence(sequence)`           |
|         | `period(newvar)`    | name for period variable; default is `period(period)`                 |
