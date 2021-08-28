## Syntax

`rotatemat matrix_L` \[`, options`\]

| Options      |                    | Description                                                                  |
|--------------|--------------------|------------------------------------------------------------------------------|
| Main         |                    |                                                                              |
|              | `orthogonal`       | restrict to orthogonal rotations; the default, except with `promax()`        |
|              | `oblique`          | allow oblique rotations                                                      |
|              | `rotation_methods` | rotation criterion                                                           |
|              | `normalize`        | rotate Kaiser normalized matrix                                              |
| Reporting    |                    |                                                                              |
|              | `format(%fmt)`     | display format for matrices; default is `format(%9.5f)`                      |
|              | `blanks(#)`        | display loadings as blanks when \|loading\| &lt; `#`; default is `blanks(0)` |
|              | `nodisplay`        | suppress all output except log and trace                                     |
|              | `noloading`        | suppress display of rotated loadings                                         |
|              | `norotation`       | suppress display of rotation matrix                                          |
|              | `matname(string)`  | descriptive label of the matrix to be rotated                                |
|              | `colnames(string)` | descriptive name for columns of the matrix to be rotated                     |
| Optimization |                    |                                                                              |
|              | `optimize_options` | control the maximization process; seldom used                                |

|                    |             |                                                   |
|--------------------|-------------|---------------------------------------------------|
| `rotation_methods` |             | Description                                       |
| \*                 | `varimax`   | varimax (`orthogonal` only); the default          |
|                    | `vgpf`      | varimax via the GPF algorithm (`orthogonal` only) |
|                    | `quartimax` | quartimax (`orthogonal` only)                     |
|                    | `equamax`   | equamax (`orthogonal` only)                       |
|                    | `parsimax`  | parsimax (`orthogonal` only)                      |
|                    | `entropy`   | minimum entropy (`orthogonal` only)               |
|                    | `tandem1`   | Comrey's tandem 1 principle (`orthogonal` only)   |
|                    | `tandem2`   | Comrey's tandem 2 principle (`orthogonal` only)   |

|                                                          |                        |                                                              |
|----------------------------------------------------------|------------------------|--------------------------------------------------------------|
| \*                                                       | `promax`\[`(#)`\]  | promax power `#` (implies `oblique`); default is `promax(3)` |
|                                                          | `oblimin`\[`(#)`\] | oblimin with gamma=`#`; default is `oblimin(0)`              |
|                                                          | `cf(#)`                | Crawford-Ferguson family with kappa=`#`, 0&lt;=`#`&lt;=1     |
|                                                          | `bentler`              | Bentler's invariant pattern simplicity                       |
|                                                          | `oblimax`              | oblimax                                                      |
|                                                          | `quartimin`            | quartimin                                                    |
|                                                          | `target(Tg)`           | rotate toward matrix `Tg`                                    |
|                                                          | `partial(Tg W)`        | rotate toward matrix `Tg`, weighted by matrix `W`            |
| \* `varimax` and `promax` ignore all `optimize_options`. |                        |                                                              |
