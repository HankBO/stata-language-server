## Syntax

Shapiro-Wilk normality test

`swilk`
[varlist](http://www.stata.com/help.cgi?varlist)
_\[`if`\] \[`in`\]_ \[`, swilk_options`\]

Shapiro-Francia normality test

`sfrancia`
[varlist](http://www.stata.com/help.cgi?varlist)
_\[`if`\] \[`in`\]_ \[`,`
`sfrancia_options`\]

| swilk\_options |                    | Description                                    |
|----------------|--------------------|------------------------------------------------|
| Main           |                    |                                                |
|                | `generate(newvar)` | create `newvar` containing W test coefficients |
|                | `lnnormal`         | test for three-parameter lognormality          |
|                | `noties`           | do not use average ranks for tied values       |

| sfrancia\_options |          | Description                                                                         |
|-------------------|----------|-------------------------------------------------------------------------------------|
| Main              |          |                                                                                     |
|                   | `boxcox` | use the Box-Cox transformation for W'; the default is to use the log transformation |
|                   | `noties` | do not use average ranks for tied values                                            |

`by` is allowed with `swilk` and `sfrancia`; see
[<strong>[D]</strong> by](http://www.stata.com/help.cgi?by).
