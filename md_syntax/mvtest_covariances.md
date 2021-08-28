## Syntax

Multiple-sample tests

`mvtest covariances`
[varlist](http://www.stata.com/help.cgi?varlist)
_\[`if`\] \[`in`\]_ \[`weight`\]`,`
`by(groupvars)`
\[[<var class="command">multisample_options</var><strong></strong>](mvtest%20covariances##multisample_options)\]

One-sample tests

`mvtest covariances`
[varlist](http://www.stata.com/help.cgi?varlist)
_\[`if`\] \[`in`\]_ \[`weight`\] \[`,`
[<var class="command">one-sample_options</var><strong></strong>](mvtest%20covariances##one-sample_options)\]

| multisample\_options                                                                                                                                                                                                                                                                                                                               |                                                                 | Description                                                                           |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|---------------------------------------------------------------------------------------|
| Model                                                                                                                                                                                                                                                                                                                                              |                                                                 |                                                                                       |
| \*                                                                                                                                                                                                                                                                                                                                                 | `by(groupvars)`                                                 | compare subsamples with same values in `groupvars`                                    |
|                                                                                                                                                                                                                                                                                                                                                    | `missing`                                                       | treat missing values in `groupvars` as ordinary values                                |
|                                                                                                                                                                                                                                                                                                                                                    | `spherical`                                                     | test that covariance matrix is spherical                                              |
|                                                                                                                                                                                                                                                                                                                                                    | `compound`                                                      | test that covariance matrix is compound symmetric                                     |
|                                                                                                                                                                                                                                                                                                                                                    | `equals(C)`                                                     | test that covariance matrix equals matrix `C`                                         |
|                                                                                                                                                                                                                                                                                                                                                    | `block(varlist1` \[`||`                                     |                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                    | <span options="6">{space 6}_`varlist2` \[`||...`\]\]`)` | test that covariance matrix is block diagonal with blocks corresponding to `varlist#` |
| \* `by(groupvars)` is required. <span options="25 tabbed">{synoptset 25 tabbed}_{nobreak None} <span options="one-sample_options">{marker one-sample\_options}_{nobreak None} {synopthdr None:one-sample\_options} {synoptline None} {syntab None:Options} {synopt None}`diagonal`test that covariance matrix is diagonal; the default |                                                                 |                                                                                       |

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
