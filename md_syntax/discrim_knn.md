## Syntax

`discrim knn`
[varlist](http://www.stata.com/help.cgi?varlist)
_\[`if`\] \[`in`\]_ \[`weight`\]`,`
`group(groupvar) k(#)` \[`options`\]

| Options   |                                                                                                                                             | Description                                                                                                                                    |
|-----------|---------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| Model     |                                                                                                                                             |                                                                                                                                                |
| \*        | `group(groupvar)`                                                                                                                           | variable specifying the groups                                                                                                                 |
| \*        | `k(#)`                                                                                                                                      | number of nearest neighbors                                                                                                                    |
|           | `priors(priors)`                                                                                                                            | group prior probabilities                                                                                                                      |
|           | `ties(ties)`                                                                                                                                | how ties in classification are to be handled                                                                                                   |
| Measure   |                                                                                                                                             |                                                                                                                                                |
|           | `measure(`[<var class="command">measure</var><strong></strong>](http://www.stata.com/help.cgi?measure_option)`)` | similarity or dissimilarity measure; default is `measure(L2)`                                                                                  |
|           | `s2d(standard)`                                                                                                                           | convert similarity to dissimilarity: d(ij)=sqrt{s(ii)+s(jj)-2s(ij)}, the default |
|           | `s2d(oneminus)`                                                                                                                           | convert similarity to dissimilarity: d(ij)=1-s(ij)                                                                                             |
|           | `mahalanobis`                                                                                                                               | Mahalanobis transform continuous data before computing dissimilarities                                                                         |
| Reporting |                                                                                                                                             |                                                                                                                                                |
|           | `notable`                                                                                                                                   | suppress resubstitution classification table                                                                                                   |
|           | `lootable`                                                                                                                                  | display leave-one-out classification table                                                                                                     |

| priors |                | Description                                                                         |
|--------|----------------|-------------------------------------------------------------------------------------|
|        | `equal`        | equal prior probabilities; the default                                              |
|        | `proportional` | group-size-proportional prior probabilities                                         |
|        | `matname`      | row or column vector containing the group prior probabilities                       |
|        | `matrix_exp`   | matrix expression providing a row or column vector of the group prior probabilities |

| ties |           | Description                                                                                                           |
|------|-----------|-----------------------------------------------------------------------------------------------------------------------|
|      | `missing` | ties in group classification produce missing values; the default                                                      |
|      | `random`  | ties in group classification are broken randomly                                                                      |
|      | `first`   | ties in group classification are set to the first tied group                                                          |
|      | `nearest` | ties in group classification are assigned based on the closest observation, or missing if this still results in a tie |

\*`group()` and `k()` are required.

`statsby` and `xi` are allowed; see
[<strong>prefix</strong>](http://www.stata.com/help.cgi?prefix).

`fweight`s are allowed; see
[<strong>weight</strong>](http://www.stata.com/help.cgi?weight).

See
[<strong>[MV]</strong> discrim knn postestimation](http://www.stata.com/help.cgi?discrim_knn_postestimation)
for features available after estimation.
