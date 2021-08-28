## Syntax

{nobreak None}

`class AssociativeArray scalarA`{right
None}`create array with string scalar keys`

`or`

{nobreak None}

`A = AssociativeArray()`{right
None}`create array with string scalar keys`

{nobreak None}

`A.reinit(keytype`{right None}`"string", "real", "complex",` ...

\[`, keydim` {nobreak None}

{right None}`1 to 50`

\[`, minsize`{nobreak None}

{right None}`tuning parameter`

\[`, minratio`{nobreak None}

{right None}`tuning parameter`

\[`, maxratio` \]\]\]\]\]`)`{nobreak None}

{right None}`tuning parameter`

{nobreak None}

`A.put(key,val)`{right
None}`A[key] = val                              `

{nobreak None}

`val=A.get(key)`{right
None}`val = A[key] or val = notfound            `

{nobreak None}

`A.notfound(notfound)`{right
None}`change notfound value                     `

{nobreak None}

`notfound=A.notfound()`{right
None}`query notfound value                      `

{nobreak None}

`A.remove(key)`{right
None}`delete A[key] if it exists                `

{nobreak None}

`bool=A.exists(key)`{right
None}`A[key] exists?                            `

{nobreak None}

`val = A.firstval()`{right
None}`first val or notfound                     `

{nobreak None}

`val = A.nextval()`{right
None}`next val or notfound                      `

{nobreak None}

`key = A.key()`{right
None}`key corresponding to val                  `

{nobreak None}

`val = A.val()`{right
None}`val yet again                             `

{nobreak None}

`loc = A.firstloc()`{right None}`first location or NULL`

{nobreak None}

`loc = A.nextloc()`{right None}`next location or NULL`

{nobreak None}

`key = A.key(loc)`{right
None}`key at location                           `

{nobreak None}

`val = A.val(loc)`{right
None}`val at location                           `

{nobreak None}

`keys = A.keys()`{right
None}`N x keydim matrix of defined keys         `

{nobreak None}

`N = A.N()`{right
None}`N, number of defined keys                 `

{nobreak None}

`A.clear()`{right None}`clear array; set N equal to 0             `
