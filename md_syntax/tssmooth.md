## Syntax

`tssmooth smoother` _\[`type`\] \[_
[newvar](http://www.stata.com/help.cgi?newvar)
`= exp` _\[`if`\] \[`in`\]_ \[`, ...`\]

|                   |                          |                                                                                                                   |
|-------------------|--------------------------|-------------------------------------------------------------------------------------------------------------------|
| Smoother category |                          | `smoother`                                                                                                        |
| Moving average    |                          |                                                                                                                   |
|                   | with uniform weights     | [<strong>ma</strong>](http://www.stata.com/help.cgi?tssmooth%20ma)                     |
|                   | with specified weights   | [<strong>ma</strong>](http://www.stata.com/help.cgi?tssmooth%20ma)                     |
| Recursive         |                          |                                                                                                                   |
|                   | exponential              | [<strong>exponential</strong>](http://www.stata.com/help.cgi?tssmooth%20exponential)   |
|                   | double exponential       | [<strong>dexponential</strong>](http://www.stata.com/help.cgi?tssmooth%20dexponential) |
|                   | nonseasonal Holt-Winters | [<strong>hwinters</strong>](http://www.stata.com/help.cgi?tssmooth%20hwinters)         |
|                   | seasonal Holt-Winters    | [<strong>shwinters</strong>](http://www.stata.com/help.cgi?tssmooth%20shwinters)       |

|                  |     |                                                                                               |
|------------------|-----|-----------------------------------------------------------------------------------------------|
| Nonlinear filter |     | [<strong>nl</strong>](http://www.stata.com/help.cgi?tssmooth%20nl) |
