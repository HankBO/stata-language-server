## Syntax

`margins` \[`marginlist`\] _\[`if`\]
\[`in`\]_ \[`weight`\] \[`, contrast margins_options`\]

`margins` \[`marginlist`\] _\[`if`\]
\[`in`\]_ \[`weight`\] \[`, contrast(suboptions)`
`margins_options`\]

where `marginlist` is a list of factor variables or interactions that
appear in the current estimation results. The variables may be typed
with or without
[<strong>contrast operators</strong>](contrast##operators),
and you may use any factor-variable syntax:

`margins sex##group, contrastmargins sex##g.group, contrastmargins sex@group, contrast`

See the `operators (op.)` table in
[<strong>[R] contrast</strong>](http://www.stata.com/help.cgi?contrast)
for the list of contrast operators. Contrast operators may also be
specified on the variables in `margins`'s `over()` and `within()`
options to perform contrasts across the levels of those variables.

| suboptions |                                    | Description                                                                                |
|------------|------------------------------------|--------------------------------------------------------------------------------------------|
| Contrast   |                                    |                                                                                            |
|            | `overall`                          | add a joint hypothesis test for all specified contrasts                                    |
|            | `lincom`                           | treat user-defined contrasts as linear combinations                                        |
|            | `predict(op`\[`._predict`\]`)` | apply the `op.` contrast operator to the groups defined by multiple `predict()` options  |
|            | `atcontrast(op`\[`._at`\]`)`   | apply the `op.` contrast operator to the groups defined by `at()`                        |
|            | `predictjoint`                     | test jointly across all groups defined by multiple `predict()` options                     |
|            | `atjoint`                          | test jointly across all groups defined by `at()`                                           |
|            | `overjoint`                        | test jointly across all levels of the unoperated `over()` variables                        |
|            | `withinjoint`                      | test jointly across all levels of the unoperated `within()` variables                      |
|            | `marginswithin`                    | perform contrasts within the levels of the unoperated terms in `marginlist`                |
|            | `cieffects`                        | show effects table with confidence intervals                                               |
|            | `pveffects`                        | show effects table with p-values                                                           |
|            | `effects`                          | show effects table with confidence intervals and p-values                                  |
|            | `nowald`                           | suppress table of Wald tests                                                               |
|            | `noatlevels`                       | report only the overall Wald test for terms that use the within `@` or nested `|` operator |
|            | `nosvyadjust`                      | compute unadjusted Wald tests for survey results                                           |

`fweight`s, `aweight`s, `iweight`s, and `pweight`s are allowed; see
[<strong>weight</strong>](http://www.stata.com/help.cgi?weight).
