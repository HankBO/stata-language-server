## Syntax

`cluster kmeans` <span options="1">{space 1}_
\[[varlist](http://www.stata.com/help.cgi?varlist)\]
_\[`if`\] \[`in`\]_ `, k(#)` \[ `options`
\]

`cluster kmedians`
\[[varlist](http://www.stata.com/help.cgi?varlist)\]
_\[`if`\] \[`in`\]_ `, k(#)` \[ `options`
\]

| Options                |                         | Description                                                      |
|------------------------|-------------------------|------------------------------------------------------------------|
| Main                   |                         |                                                                  |
| \*                     | `k(#)`                  | perform cluster analysis resulting in \# groups                  |
|                        | `measure(measure)`      | similarity or dissimilarity measure; default is `L2` (Euclidean) |
|                        | `name(clname)`          | name of resulting cluster analysis                               |
| Options                |                         |                                                                  |
|                        | `start(start_option)` | obtain `k` initial group centers by using `start_option`         |
|                        | `keepcenters`           | append the `k` final group means or medians to the data          |
| Advanced               |                         |                                                                  |
|                        | `generate(groupvar)`    | name of grouping variable                                        |
|                        | `iterate(#)`            | maximum number of iterations; default is `iterate(10000)`        |
| \* `k(#)` is required. |                         |                                                                  |
