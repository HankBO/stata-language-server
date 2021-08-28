## Syntax

`margins` \[`marginlist`\] _\[`if`\]
\[`in`\]_ \[`weight`\] \[`, pwcompare margins_options`\]

`margins` \[`marginlist`\] _\[`if`\]
\[`in`\]_ \[`weight`\] \[`, pwcompare(suboptions)`
`margins_options`\]

where `marginlist` is a list of factor variables or interactions that
appear in the current estimation results. The variables may be typed
with or without the `i.` prefix, and you may use any factor-variable
syntax:

`margins i.sex i.group i.sex#i.group, pwcomparemargins sex group sex#i.group, pwcomparemargins sex##group, pwcompare`

| suboptions           |             | Description                                               |
|----------------------|-------------|-----------------------------------------------------------|
| Pairwise comparisons |             |                                                           |
|                      | `cieffects` | show effects table with confidence intervals; the default |
|                      | `pveffects` | show effects table with p-values                          |
|                      | `effects`   | show effects table with confidence intervals and p-values |
|                      | `cimargins` | show table of margins and confidence intervals            |
|                      | `groups`    | show table of margins and group codes                     |
|                      | `sort`      | sort the margins or contrasts in each term                |

`fweight`s, `aweight`s, `iweight`s, and `pweight`s are allowed; see
[<strong>weight</strong>](http://www.stata.com/help.cgi?weight).
