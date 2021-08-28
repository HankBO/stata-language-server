## Syntax

Tabulate failure rates

`strate`
\[[varlist](http://www.stata.com/help.cgi?varlist)\]
_\[`if`\] \[`in`\]_ \[`, strate_options`\]

Calculate rate ratios with the Mantel-Haenszel method

`stmh`
[varname](http://www.stata.com/help.cgi?varname)
\[[varlist](http://www.stata.com/help.cgi?varlist)\]
_\[`if`\] \[`in`\]_ \[`, options`\]

Calculate rate ratios with the Mantel-Cox method

`stmc`
[varname](http://www.stata.com/help.cgi?varname)
\[[varlist](http://www.stata.com/help.cgi?varlist)\]
_\[`if`\] \[`in`\]_ \[`, options`\]

| strate\_options                         |                                       | Description                                                                                                                                                           |
|-----------------------------------------|---------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Main                                    |                                       |                                                                                                                                                                       |
|                                         | `per(#)`                              | units to be used in reported rates                                                                                                                                    |
|                                         | `smr(varname)`                        | use `varname` as reference-rate variable to calculate SMRs                                                                                                            |
|                                         | `cluster(varname)`                    | cluster variable to be used by the jackknife                                                                                                                          |
|                                         | `jackknife`                           | report jackknife confidence intervals                                                                                                                                 |
|                                         | `missing`                             | include missing values as extra categories                                                                                                                            |
|                                         | `level(#)`                            | set confidence level; default is `level(95)`                                                                                                                          |
|                                         | `output:(filename`\[`,replace`\]`)` | save summary dataset as `filename`; use `replace` to overwrite existing `filename`                                                                                    |
|                                         | `nolist`                              | suppress listed output                                                                                                                                                |
|                                         | `graph`                               | graph rates against exposure category                                                                                                                                 |
|                                         | `nowhisker`                           | omit confidence intervals from the graph                                                                                                                              |
| Plot                                    |                                       |                                                                                                                                                                       |
|                                         | `marker_options`                      | change look of markers (color, size, etc.)                                                                                                                            |
|                                         | `marker_label_options`                | add marker labels; change look or position                                                                                                                            |
|                                         | `cline_options`                       | affect rendition of the plotted points                                                                                                                                |
| CI plot                                 |                                       |                                                                                                                                                                       |
|                                         | `ciopts(rspike_options)`              | affect rendition of the confidence intervals (whiskers)                                                                                                               |
| Add plots                               |                                       |                                                                                                                                                                       |
|                                         | `"addplot(plot)`                      | add other plots to the generated graph                                                                                                                                |
| Y axis, X axis, Titles, Legend, Overall |                                       |                                                                                                                                                                       |
|                                         | `twoway_options`                      | any options other than `by()` documented in [<strong>[G-3]</strong> <em>twoway_options</em>](http://www.stata.com/help.cgi?twoway_options) |

| Options |                      | Description                                  |
|---------|----------------------|----------------------------------------------|
| Main    |                      |                                              |
|         | `by(varlist)`        | tabulate rate ratio on `varlist`             |
|         | `compare(num1,den2)` | compare categories of exposure variable      |
|         | `missing`            | include missing values as extra categories   |
|         | `level(#)`           | set confidence level; default is `level(95)` |

You must `stset` your data before using `strate`, `stmh`, and `stmc`;
see
[<strong>[ST]</strong> stset](http://www.stata.com/help.cgi?stset).

`by` is allowed with `stmh` and `stmc`; see
[<strong>[D]</strong> by](http://www.stata.com/help.cgi?by).

`fweight`s, `iweight`s, and `pweights` may be specified using `stset`;
see
[<strong>[ST]</strong> stset](http://www.stata.com/help.cgi?stset).
