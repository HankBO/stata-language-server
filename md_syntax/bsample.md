## Syntax

`bsample` \[`exp`\] _\[`if`\] \[`in`\]_ \[`,`
`options`\]

where `exp` is a standard Stata expression specifying the size of the
sample; see
[<strong>exp</strong>](http://www.stata.com/help.cgi?exp).

`exp` must be less than or equal to
[<strong>_N</strong>](http://www.stata.com/help.cgi?_N)
(the number of observations) when neither the `cluster()` nor the
`strata()` option is specified. `_N` is the default when `exp` is not
specified.

Observations that do not meet the optional
[<strong>if</strong>](http://www.stata.com/help.cgi?if)
and
[<strong>in</strong>](http://www.stata.com/help.cgi?in)
criteria are dropped from the resulting dataset.

| Options |                     | Description                               |
|---------|---------------------|-------------------------------------------|
|         | `strata(varlist)`   | variables identifying strata              |
|         | `cluster(varlist)`  | variables identifying resampling clusters |
|         | `idcluster(newvar)` | create new cluster ID variable            |
|         | `weight(varname)`   | replace `varname` with frequency weights  |
