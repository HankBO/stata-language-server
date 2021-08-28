## Syntax

Multiple-sample tests

`mvtest means`
[varlist](http://www.stata.com/help.cgi?varlist)
_\[`if`\] \[`in`\]_ \[`weight`\]`,`
`by(groupvars)`
\[[<var class="command">multisample_options</var><strong></strong>](#multisample_options)\]

One-sample tests

`mvtest means`
[varlist](http://www.stata.com/help.cgi?varlist)
_\[`if`\] \[`in`\]_ \[`weight`\] \[`,`
[<var class="command">one-sample_options</var><strong></strong>](#one-sample_options)\]

| multisample\_options                                                                                                                                                                                                                                                                                                                                                                                                        |                     | Description                                                                                                                                              |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Model                                                                                                                                                                                                                                                                                                                                                                                                                       |                     |                                                                                                                                                          |
| \*                                                                                                                                                                                                                                                                                                                                                                                                                          | `by(groupvars)`     | compare subsamples with same values in `groupvars`                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                             | `missing`           | treat missing values in `groupvars` as ordinary values                                                                                                   |
| Options                                                                                                                                                                                                                                                                                                                                                                                                                     |                     |                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                             | `homogeneous`       | test for equal means with homogeneous covariance matrices across by-groups; the default                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                             | `heterogeneous`     | James's test for equal means, allowing heterogeneous covariance matrices across by-groups                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                             | `lr`                | likelihood-ratio test for equal means, allowing heterogeneous covariance matrices across by-groups                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                             | `protect(spec)` | run protection as a safeguard against local minimum with the group means as initial values; use only with `lr` option                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                             | `zero`              | test that means of [varlist](http://www.stata.com/help.cgi?varlist) are all equal to 0                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                             | `equals(M)`         | test that mean vector equals vector `M`                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                             | `linear(V)`         | test that mean vector of [varlist](http://www.stata.com/help.cgi?varlist) satisfies linear hypothesis described by matrix `V` |
| \* `by(groupvars)` is required. <span options="20 tabbed">{synoptset 20 tabbed}_{nobreak None} <span options="one-sample_options">{marker one-sample\_options}_{nobreak None} {synopthdr None:one-sample\_options} {synoptline None} {syntab None:Options} {synopt None}`equal`test that variables in [varlist](http://www.stata.com/help.cgi?varlist) have equal means; the default |                     |                                                                                                                                                          |

`bootstrap`, `by`, `jackknife`, `rolling`, and `statsby` are allowed;
see
[<strong>prefix</strong>](http://www.stata.com/help.cgi?prefix).

Weights are not allowed with the
[<strong>bootstrap</strong>](http://www.stata.com/help.cgi?bootstrap)
prefix.

`aweight`s are not allowed with the
[<strong>jackknife</strong>](http://www.stata.com/help.cgi?jackknife)
prefix.

`aweight`s and `fweight`s are allowed; see
[<strong>weight</strong>](http://www.stata.com/help.cgi?weight).
