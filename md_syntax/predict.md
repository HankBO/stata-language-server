## Syntax

After single-equation (SE) models

`predict` _\[`type`\] \[_
[newvar](http://www.stata.com/help.cgi?newvar)
_\[`if`\] \[`in`\]_ \[`, single_options`\]

After multiple-equation (ME) models

`predict` _\[`type`\] \[_
[newvar](http://www.stata.com/help.cgi?newvar)
_\[`if`\] \[`in`\]_ \[`,`
`multiple_options`\]

`predict` _\[`type`\] \[_ <span
options="-(">{c -(}_`stub*`|`newvar1` ... `newvarq`} <span
class="command">\[`if`\] \[`in`\]_ `, scores`

| single\_options |                 | Description                                                         |
|-----------------|-----------------|---------------------------------------------------------------------|
| Main            |                 |                                                                     |
|                 | `xb`            | calculate linear prediction                                         |
|                 | `stdp`          | calculate standard error of the prediction                          |
|                 | `score`         | calculate first derivative of the log likelihood with respect to xb |
| Options         |                 |                                                                     |
|                 | `nooffset`      | ignore any `offset()` or `exposure()` variable                      |
|                 | `other_options` | command-specific options                                            |

| multiple\_options |                                     | Description                                    |
|-------------------|-------------------------------------|------------------------------------------------|
| Main              |                                     |                                                |
|                   | `equation(eqno`\[`,eqno`\]`)` | specify equations                              |
|                   | `xb`                                | calculate linear prediction                    |
|                   | `stdp`                              | calculate standard error of the prediction     |
|                   | `stddp`                             | calculate the difference in linear predictions |
| Options           |                                     |                                                |
|                   | `nooffset`                          | ignore any `offset()` or `exposure()` variable |
|                   | `other_options`                     | command-specific options                       |
