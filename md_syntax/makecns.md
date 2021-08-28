## Syntax

`makecns` \[`clist`\|`matname`\] \[`, options`\]

`matcproc T a C`

where `clist` is a list of constraint numbers, separated by commas or
dashes; `matname` is an existing matrix representing the constraints and
must have one more column than the **e(b)** and **e(V)** matrices.

`T`, `a`, and `C` are names of new or existing matrices.

| Options |              | Description                                                                    |
|---------|--------------|--------------------------------------------------------------------------------|
|         | `nocnsnotes` | do not display notes when constraints are dropped                              |
|         | `displaycns` | display the system-stored constraint matrix                                    |
|         | `r`          | return the accepted constraints in **r()**; this option overrides `displaycns` |
