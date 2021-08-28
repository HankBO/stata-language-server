## Syntax

`pkequiv outcome treatment period sequence id` <span
class="command">\[`if`\] \[`in`\]_ \[`, options`\]

| Options |                   | Description                                                       |
|---------|-------------------|-------------------------------------------------------------------|
| Options |                   |                                                                   |
|         | `compare(string)` | compare the two specified values of the treatment variable        |
|         | `limit(#)`        | equivalence limit (between 0.01 and 0.99); default is 0.2         |
|         | `level(#)`        | set confidence level; default is `level(90)`                      |
|         | `fieller`         | calculate CI by Fieller's theorem                                 |
|         | `symmetric`       | calculate symmetric CI                                            |
|         | `anderson`        | Anderson and Hauck hypothesis test for bioequivalence             |
|         | `tost`            | two one-sided hypothesis tests for bioequivalence                 |
|         | `noboot`          | do not estimate probability that CI lies within confidence limits |
