## Syntax

`spmatrix userdefined Wmatname =`
`fcnname(`[varlist](http://www.stata.com/help.cgi?varlist)`)`
_\[`if`\] \[`in`\]_ \[`, options`\]

`Wmatname` is a weighting matrix name, such as `W`.

`fcnname` is the name of a Mata function you have written, such as
`SinvD` or `Awind`.

1\. `fcnname` must start with the letter `S` or `A`, which indicates
whether the function produces a symmetric or an asymmetric result.

2\. `fcnname` receives two row-vector arguments and returns a scalar
result. For example,

Function `SinvD()` starts with `S` because for all `x` and `y`,
`SinvD(x, y)` = `SinvD(y, x)`.

| Options |                        | Description                                             |
|---------|------------------------|---------------------------------------------------------|
|         | `normalize(normalize)` | type of normalization; default is `normalize(spectral)` |
|         | `replace`              | replace existing weighting matrix                       |
