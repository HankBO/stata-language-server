## Syntax

`collapse clist` _\[`if`\] \[`in`\]_
\[`weight`\] \[`, options`\]

where `clist` is either

\[`(stat)`\]
[varlist](http://www.stata.com/help.cgi?varlist)
\[ \[`(stat)`\] `...` \]

\[`(stat)`\]
`target_var=`[varname](http://www.stata.com/help.cgi?varname)
\[`target_var=`[varname](http://www.stata.com/help.cgi?varname)
`...`\] \[ \[`(stat)`\] `...`\]

or any combination of the `varlist` or `target_var` forms, and `stat` is
one of

|              |                                                                                                   |
|--------------|---------------------------------------------------------------------------------------------------|
| `mean`       | means (default)                                                                                   |
| `median`     | medians                                                                                           |
| `p1`         | 1st percentile                                                                                    |
| `p2`         | 2nd percentile                                                                                    |
| `...`        | 3rd<span options="1">_49th percentiles                                                      |
| `p50`        | 50th percentile (same as `median`)                                                                |
| `...`        | 51st<span options="1">_97th percentiles                                                     |
| `p98`        | 98th percentile                                                                                   |
| `p99`        | 99th percentile                                                                                   |
| `sd`         | standard deviations                                                                               |
| `semean`     | standard error of the mean (`sd/sqrt(n)`)                                                         |
| `sebinomial` | standard error of the mean, binomial (`sqrt(p(1-p)/n)`)                                           |
| `sepoisson`  | standard error of the mean, Poisson (`sqrt(mean)`)                                                |
| `sum`        | sums                                                                                              |
| `rawsum`     | sums, ignoring optionally specified weight except observations with a weight of zero are excluded |
| `count`      | number of nonmissing observations                                                                 |
| `percent`    | percentage of nonmissing observations                                                             |
| `max`        | maximums                                                                                          |
| `min`        | minimums                                                                                          |
| `iqr`        | interquartile range                                                                               |
| `first`      | first value                                                                                       |
| `last`       | last value                                                                                        |
| `firstnm`    | first nonmissing value                                                                            |
| `lastnm`     | last nonmissing value                                                                             |

If `stat` is not specified, `mean` is assumed.

| Options                                                                                                                                                                                                                                                                                                                                                                                                                                                           |               | Description                                                                               |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|-------------------------------------------------------------------------------------------|
| Options                                                                                                                                                                                                                                                                                                                                                                                                                                                           |               |                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | `by(varlist)` | groups over which `stat` is to be calculated                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | `cw`          | casewise deletion instead of all possible observations                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | `fast`        | do not restore the original dataset should the user press **Break**; programmer's command |
| `varlist` and `varname` in `clist` may contain time-series operators; see [<strong>tsvarlist</strong>](http://www.stata.com/help.cgi?tsvarlist).                                                                                                                                                                                                                                                                                       |               |                                                                                           |
| `aweight`s, `fweight`s, `iweight`s, and `pweight`s are allowed; see [<strong>weight</strong>](http://www.stata.com/help.cgi?weight), and see [<strong>Weights</strong>](#weights) below. `pweight`s may not be used with `sd`, `semean`, `sebinomial`, or `sepoisson`. `iweight`s may not be used with `semean`, `sebinomial`, or `sepoisson`. `aweight`s may not be used with `sebinomial` or `sepoisson`. |               |                                                                                           |
| `fast` does not appear in the dialog box.                                                                                                                                                                                                                                                                                                                                                                                                                         |               |                                                                                           |
