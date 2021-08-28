## Syntax

`spmatrix fromdata spmatname =`
[varlist](http://www.stata.com/help.cgi?varlist)
\[`, options`\]

`spmatname` is the name of the spatial weighting matrix to be created.

| Options |                        | Description                                              |
|---------|------------------------|----------------------------------------------------------|
|         | `idistance`            | store reciprocal of elements                             |
|         | `normalize(normalize)` | type of normalization; default is `normalized(spectral)` |
|         | `replace`              | replace existing weighting matrix                        |
