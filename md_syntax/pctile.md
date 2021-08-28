## Syntax

Create variable containing percentiles

`pctile` _\[`type`\] \[_
[newvar](http://www.stata.com/help.cgi?newvar)
`= exp` _\[`if`\] \[`in`\]_ \[`weight`\]
\[`, pctile_options`\]

Create variable containing quantile categories

`xtile`
[newvar](http://www.stata.com/help.cgi?newvar)
`= exp` _\[`if`\] \[`in`\]_ \[`weight`\]
\[`, xtile_options`\]

Compute percentiles and store them in r()

`_pctile`
[varname](http://www.stata.com/help.cgi?varname)
_\[`if`\] \[`in`\]_ \[`weight`\] \[`,`
`_pctile_options`\]

| pctile\_options |                 | Description                                         |
|-----------------|-----------------|-----------------------------------------------------|
| Main            |                 |                                                     |
|                 | `nquantiles(#)` | number of quantiles; default is `nquantiles(2)`     |
|                 | `genp(newvarp)` | generate `newvarp` variable containing percentages  |
|                 | `altdef`        | use alternative formula for calculating percentiles |

| xtile\_options |                      | Description                                         |
|----------------|----------------------|-----------------------------------------------------|
| Main           |                      |                                                     |
|                | `nquantiles(#)`      | number of quantiles; default is `nquantiles(2)`     |
|                | `cutpoints(varname)` | use values of `varname` as cutpoints                |
|                | `altdef`             | use alternative formula for calculating percentiles |

| \_pctile\_options |                        | Description                                                      |
|-------------------|------------------------|------------------------------------------------------------------|
|                   | `nquantiles(#)`        | number of quantiles; default is `nquantiles(2)`                  |
|                   | `percentiles(numlist)` | calculate percentiles corresponding to the specified percentages |
|                   | `altdef`               | use alternative formula for calculating percentiles              |

`aweight`s, `fweight`s, and `pweight`s are allowed (see
[<strong>[U]</strong> 11.1.6 weight](http://www.stata.com/help.cgi?weight)),
except when the `altdef` option is specified, in which case no weights
are allowed.
