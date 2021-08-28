## Syntax

Zero-skewness log transform

`lnskew0`
[newvar](http://www.stata.com/help.cgi?newvar)
`= exp` _\[`if`\] \[`in`\]_ \[`,`
`options`\]

Zero-skewness Box-Cox transform

`bcskew0`
[newvar](http://www.stata.com/help.cgi?newvar)
`= exp` _\[`if`\] \[`in`\]_ \[`,`
`options`\]

| Options |            | Description                                                                                                           |
|---------|------------|-----------------------------------------------------------------------------------------------------------------------|
| Main    |            |                                                                                                                       |
|         | `delta(#)` | increment for derivative of skewness function; default is `delta(0.02)` for `lnskew0` and `delta(0.01)` for `bcskew0` |
|         | `zero(#)`  | value for determining convergence; default is `zero(0.001)`                                                           |
|         | `level(#)` | set confidence level; default is `level(95)`                                                                          |
