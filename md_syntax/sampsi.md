## Syntax

`sampsi #1 #2` \[`, options`\]

| Options |                  | Description                                                                                      |
|---------|------------------|--------------------------------------------------------------------------------------------------|
| Main    |                  |                                                                                                  |
|         | `onesample`      | one-sample test; default is two-sample                                                           |
|         | `sd1(#)`         | standard deviation of sample 1                                                                   |
|         | `sd2(#)`         | standard deviation of sample 2                                                                   |
| Options |                  |                                                                                                  |
|         | `alpha(#)`       | significance level of test; default is `alpha(0.05)`                                             |
|         | `power(#)`       | power of test; default is `power(0.90)`                                                          |
|         | `n1(#)`          | size of sample 1                                                                                 |
|         | `n2(#)`          | size of sample 2                                                                                 |
|         | `ratio(#)`       | ratio of sample sizes; default is `ratio(1)`                                                     |
|         | `pre(#)`         | number of baseline measurements; default is `pre(0)`                                             |
|         | `post(#)`        | number of follow-up measurements; default is `post(1)`                                           |
|         | `nocontinuity`   | do not use continuity correction for two-sample test on proportions                              |
|         | `r0(#)`          | correlation between baseline measurements; default is `r0()=r1()`                                |
|         | `r1(#)`          | correlation between follow-up measurements                                                       |
|         | `r01(#)`         | correlation between baseline and follow-up measurements                                          |
|         | `onesided`       | one-sided test; default is two-sided                                                             |
|         | `method(method)` | analysis method where `method` is `post`, `change`, `ancova`, or `all`; default is `method(all)` |
