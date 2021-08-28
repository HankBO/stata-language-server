## Syntax

Simple correspondence analysis of two categorical variables

`ca rowvar colvar` _\[`if`\] \[`in`\]_
\[`weight`\] \[`, options`\]

Simple correspondence analysis with crossed (stacked) variables

`ca row_spec col_spec` _\[`if`\]
\[`in`\]_ \[`weight`\] \[`, options`\]

Simple correspondence analysis of an `n_r` x `n_c` matrix

`camat matname` \[`, options`\]

`spec` =
[varname](http://www.stata.com/help.cgi?varname)
\| `(newvar :`
[varlist](http://www.stata.com/help.cgi?varlist)`)`

and `matname` is an `n_r` x `n_c` matrix with `n_r`, `n_c`

2\.

| Options           |                       | Description                                                         |
|-------------------|-----------------------|---------------------------------------------------------------------|
| Model 2           |                       |                                                                     |
|                   | `dimensions(#)`       | number of dimensions (factors, axes); default is `dim(2)`           |
|                   | `normalize(nopts)`    | normalization of row and column coordinates                         |
|                   | `rowsupp(matname_r)`  | matrix of supplementary rows                                        |
|                   | `colsupp(matname_c)`  | matrix of supplementary columns                                     |
|                   | `rowname(string)`     | label for rows                                                      |
|                   | `colname(string)`     | label for columns                                                   |
|                   | `missing`             | treat missing values as ordinary values (`ca` only)                 |
| Codes (`ca` only) |                       |                                                                     |
|                   | `report(variables)` | report coding of crossing variables                                 |
|                   | `report(crossed)`   | report coding of crossed variables                                  |
|                   | `report(all)`       | report coding of crossing and crossed variables                     |
|                   | `length(min)`       | use minimal length unique codes of crossing variables               |
|                   | `length(#)`           | use `#` as coding length of crossing variables                      |
| Reporting         |                       |                                                                     |
|                   | `ddimensions(#)`      | number of singular values to be displayed; default is `ddim(.)`     |
|                   | `norowpoints`         | suppress table with row category statistics                         |
|                   | `nocolpoints`         | suppress table with column category statistics                      |
|                   | `compact`             | display tables in a compact format                                  |
|                   | `plot`                | plot the row and column coordinates                                 |
|                   | `maxlength(#)`        | maximum number of characters for labels; default is `maxlength(12)` |

| nopts |             | Description                                                    |
|-------|-------------|----------------------------------------------------------------|
|       | `symmetric` | symmetric coordinates (`canonical`); the default               |
|       | `standard`  | row and column standard coordinates                            |
|       | `row`       | row principal, column standard coordinates                     |
|       | `column`    | column principal, row standard coordinates                     |
|       | `principal` | row and column principal coordinates                           |
|       | `#`         | power `0` &lt;= `#` &lt;= `1` for row coordinates; seldom used |

`bootstrap`, `by`, `jackknife`, `rolling`, and `statsby` are allowed
with `ca`; see
[<strong>prefix</strong>](http://www.stata.com/help.cgi?prefix).
However, `bootstrap` and `jackknife` results should be interpreted with
caution; identification of the `ca` parameters involves data-dependent
restrictions, possibly leading to badly biased and overdispersed
estimates
([<strong>Milan and Whittaker 1995</strong>](#MW1995)).

Weights are not allowed with the
[<strong>bootstrap</strong>](http://www.stata.com/help.cgi?bootstrap)
prefix.

`aweight`s are not allowed with the
[<strong>jackknife</strong>](http://www.stata.com/help.cgi?jackknife)
prefix.

`fweight`s, `aweight`s, and `iweight`s are allowed with `ca`; see
[<strong>weight</strong>](http://www.stata.com/help.cgi?weight).

See
[<strong>[MV]</strong> ca postestimation](http://www.stata.com/help.cgi?ca_postestimation)
for features available after estimation.
