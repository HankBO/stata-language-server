## Syntax

`matrix dissimilarity matname =`
\[[varlist](http://www.stata.com/help.cgi?varlist)\]
_\[`if`\] \[`in`\]_ <span
class="nowrap">\[`, options`\]_

|                      |                                                                         |
|----------------------|-------------------------------------------------------------------------|
| `options`            | Description {p2line None}                                               |
| `measure`            | similarity or dissimilarity measure; default is `L2` (Euclidean)        |
| `observations`       | compute similarity or dissimilarities between observations; the default |
| `variables`          | compute similarities or dissimilarities between variables               |
| `names(varname)`     | row/column names for `matname` (allowed with `observations`)            |
| `allbinary`          | check that all values are 0, 1, or missing                              |
| `proportions`        | interpret values as proportions of binary values                        |
| `dissim(method)` | change similarity measure to dissimilarity measure {p2line None}        |

where `method` transforms similarities to dissimilarities by using

`oneminusstandard`
