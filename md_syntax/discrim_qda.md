## Syntax

`discrim qda`
[varlist](http://www.stata.com/help.cgi?varlist)
_\[`if`\] \[`in`\]_ \[`weight`\]`,`
`group(groupvar)` \[`options`\]

| Options   |                   | Description                                  |
|-----------|-------------------|----------------------------------------------|
| Model     |                   |                                              |
| \*        | `group(groupvar)` | variable specifying the groups               |
|           | `priors(priors)`  | group prior probabilities                    |
|           | `ties(ties)`      | how ties in classification are to be handled |
| Reporting |                   |                                              |
|           | `notable`         | suppress resubstitution classification table |
|           | `lootable`        | display leave-one-out classification table   |

| priors |                | Description                                                                         |
|--------|----------------|-------------------------------------------------------------------------------------|
|        | `equal`        | equal prior probabilities; the default                                              |
|        | `proportional` | group-size-proportional prior probabilities                                         |
|        | `matname`      | row or column vector containing the group prior probabilities                       |
|        | `matrix_exp`   | matrix expression providing a row or column vector of the group prior probabilities |

| ties |           | Description                                                      |
|------|-----------|------------------------------------------------------------------|
|      | `missing` | ties in group classification produce missing values; the default |
|      | `random`  | ties in group classification are broken randomly                 |
|      | `first`   | ties in group classification are set to the first tied group     |

\*`group()` is required.

`statsby` and `xi` are allowed; see
[<strong>prefix</strong>](http://www.stata.com/help.cgi?prefix).

`fweight`s are allowed; see
[<strong>weight</strong>](http://www.stata.com/help.cgi?weight).

See
[<strong>[MV]</strong> discrim qda postestimation](http://www.stata.com/help.cgi?discrim_qda_postestimation)
for features available after estimation.
