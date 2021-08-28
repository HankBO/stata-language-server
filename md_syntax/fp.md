## Syntax

Estimation

`fp <term>` \[`, est_options`\]`: est_cmd`

`est_cmd` may be almost any estimation command that stores the `e(ll)`
result. To confirm whether `fp` works with a specific `est_cmd`, see the
documentation for that `est_cmd`.

Instances of `<term>` (with the angle brackets) that occur within
`est_cmd` are replaced in `est_cmd` by a varlist containing the
fractional powers of the variable `term`. These variables will be named
`term_1`, `term_2`, ....

`fp` performs `est_cmd` with this substitution, fitting a fractional
polynomial regression in `term`.

`est_cmd` in either this or the following syntax may not contain other
prefix commands; see
[<strong>prefix</strong>](http://www.stata.com/help.cgi?prefix).

Estimation (alternate syntax)

`fp`
`<term>(`[varname](http://www.stata.com/help.cgi?varname)`)`
\[`, est_options`\]`: est_cmd`

Use this syntax to specify that fractional powers of `varname` are to be
calculated. The fractional polynomial power variables will still be
named `term_1`, `term_2`, ....

Replay estimation results

`fp` \[`, replay_options`\]

Create specified fractional polynomial power variables

`fp generate` _\[`type`\] \[_
\[[newvar](http://www.stata.com/help.cgi?newvar)
`=`\]
[varname](http://www.stata.com/help.cgi?varname)`^(numlist)`
_\[`if`\] \[`in`\]_ \[`, gen_options`\]

| est\_options |                     | Description                                                                                                                                                                                                                          |
|--------------|---------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Main         |                     |                                                                                                                                                                                                                                      |
| `Search`     |                     |                                                                                                                                                                                                                                      |
|              | `powers(# # ... #)` | {nobreak None} powers to be searched; default is `powers(-2 -1 -.5 0 .5 1 2 3)`                                                                                                                                                      |
|              | `dimension(#)`      | {nobreak None} maximum degree of fractional polynomial; default is `dimension(2)`                                                                                                                                                    |
| `Or specify` |                     |                                                                                                                                                                                                                                      |
|              | `fp(# # ... #)`     | {nobreak None} use specified fractional polynomial {syntab None}`And then specify any of these options` {syntab None:Options} {synopt None}`classic`{nobreak None} perform automatic scaling and centering and omit comparison table |
|              | `replace`           | {nobreak None} replace existing fractional polynomial power variables named `term_1`, `term_2`, ...                                                                                                                              |
|              | `all`               | {nobreak None} generate `term_1`, `term_2`, ... in all observations; default is in observations `if esample()`                                                                                                                 |
|              | `scale(#_a #_b)`    | {nobreak None} use (`term`+`a`)/`b`; default is to use variable term as is                                                                                                                                                           |
|              | `scale`             | {nobreak None} specify `a` and `b` automatically                                                                                                                                                                                     |
|              | `center(#_c)`       | {nobreak None} report centered-on-`c` results; default is uncentered results                                                                                                                                                         |
|              | `center`            | {nobreak None} specify `c` to be the mean of (scaled) `term`                                                                                                                                                                         |
|              | `zero`              | {nobreak None} set `term_1`, `term_2`, ... to zero if (scaled) `term`&lt;=0; default is to issue an error message                                                                                                                |
|              | `catzero`           | {nobreak None} same as `zero` and include `term_0`=(`term`&lt;=0) among fractional polynomial power variables                                                                                                                      |
| Reporting    |                     |                                                                                                                                                                                                                                      |
|              | `replay_options`    | {nobreak None} specify how results are displayed                                                                                                                                                                                     |

| replay\_options |                     | Description                                                       |
|-----------------|---------------------|-------------------------------------------------------------------|
| Reporting       |                     |                                                                   |
|                 | `nocompare`         | {nobreak None} do not display model-comparison test results       |
|                 | `reporting_options` | any options allowed by `est_cmd` for replaying estimation results |

| gen\_options |                  | Description                                                                                                           |
|--------------|------------------|-----------------------------------------------------------------------------------------------------------------------|
| Main         |                  |                                                                                                                       |
|              | `replace`        | {nobreak None} replace existing fractional polynomial power variables named `term_1`, `term_2`, ...               |
|              | `scale(#_a #_b)` | {nobreak None} use (`term`+`a`)/`b`; default is to use variable term as is                                            |
|              | `scale`          | {nobreak None} specify `a` and `b` automatically                                                                      |
|              | `center(#_c)`    | {nobreak None} report centered-on-`c` results; default is uncentered results                                          |
|              | `center`         | {nobreak None} specify `c` to be the mean of (scaled) `term`                                                          |
|              | `zero`           | {nobreak None} set `term_1`, `term_2`, ... to zero if (scaled) `term`&lt;=0; default is to issue an error message |
|              | `catzero`        | {nobreak None} same as `zero` and include `term_0`=(`term`&lt;=0) among fractional polynomial power variables       |
