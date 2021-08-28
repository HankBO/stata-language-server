## Syntax

Symmetry and marginal homogeneity tests

`symmetry casesvar controlvar` _\[`if`\]
\[`in`\]_ \[`weight`\] \[`, options`\]

Immediate form of symmetry and marginal homogeneity tests

`symmi #`11 `#`12 \[`...`\]`\ #`21 `#`22 \[`...`\] \[`\...`\]
_\[`if`\] \[`in`\]_ \[`, options`\]

| Options                                                                                                                 |           | Description                                                      |
|-------------------------------------------------------------------------------------------------------------------------|-----------|------------------------------------------------------------------|
| Main                                                                                                                    |           |                                                                  |
|                                                                                                                         | `notable` | suppress output of contingency table                             |
|                                                                                                                         | `contrib` | report contribution of each off-diagonal cell pair               |
|                                                                                                                         | `exact`   | perform exact test of table symmetry                             |
|                                                                                                                         | `mh`      | perform two marginal homogeneity tests                           |
|                                                                                                                         | `trend`   | perform a test for linear trend in the (log) relative risk (RR)  |
|                                                                                                                         | `cc`      | use continuity correction when calculating test for linear trend |
| `fweight`s are allowed; see [<strong>weight</strong>](http://www.stata.com/help.cgi?weight). |           |                                                                  |
