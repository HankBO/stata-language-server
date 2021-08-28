## Syntax

`spmatrix normalize spmatname` \[`, normalize(normalize)`\]

`spmatname` is the name of an existing spatial weighting matrix stored
in memory.

| normalize |            | Description                          |
|-----------|------------|--------------------------------------|
|           | `spectral` | spectral; the default                |
|           | `minmax`   | min--max                             |
|           | `row`      | row                                  |
|           | `none`     | do not normalize; leave matrix as is |
