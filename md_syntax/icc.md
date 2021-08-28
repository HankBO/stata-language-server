## Syntax

Calculate intraclass correlations for one-way random-effects model

`icc`
[depvar](http://www.stata.com/help.cgi?depvar)
`target` _\[`if`\] \[`in`\]_ \[`,`
[<var class="command">oneway_options</var><strong></strong>](#oneway_options)\]

Calculate intraclass correlations for two-way random-effects model

`icc`
[depvar](http://www.stata.com/help.cgi?depvar)
`target rater` _\[`if`\] \[`in`\]_ \[`,`
[<var class="command">twoway_re_options</var><strong></strong>](#twoway_re_options)\]

Calculate intraclass correlations for two-way mixed-effects model

`icc`
[depvar](http://www.stata.com/help.cgi?depvar)
`target rater` _\[`if`\] \[`in`\]_`,`
`mixed`
\[[<var class="command">twoway_me_options</var><strong></strong>](#twoway_me_options)\]

| oneway\_options |                      | Description                                                                        |
|-----------------|----------------------|------------------------------------------------------------------------------------|
| Main            |                      |                                                                                    |
|                 | `absolute`           | estimate absolute agreement; the default                                           |
|                 | `testvalue(#)`       | test whether intraclass correlations equal `#`; default is `testvalue(0)`          |
| Reporting       |                      |                                                                                    |
|                 | `level(#)`           | set confidence level; default is `level(95)`                                       |
|                 | `format(%fmt)` | display format for statistics and confidence intervals; default is `format(%9.0g)` |

| twoway\_re\_options |                      | Description                                                                        |
|---------------------|----------------------|------------------------------------------------------------------------------------|
| Main                |                      |                                                                                    |
|                     | `absolute`           | estimate absolute agreement; the default                                           |
|                     | `consistency`        | estimate consistency of agreement                                                  |
|                     | `testvalue(#)`       | test whether intraclass correlations equal `#`; default is `testvalue(0)`          |
| Reporting           |                      |                                                                                    |
|                     | `level(#)`           | set confidence level; default is `level(95)`                                       |
|                     | `format(%fmt)` | display format for statistics and confidence intervals; default is `format(%9.0g)` |

| twoway\_me\_options     |                      | Description                                                                        |
|-------------------------|----------------------|------------------------------------------------------------------------------------|
| Main                    |                      |                                                                                    |
| \*                      | `mixed`              | estimate intraclass correlations for a mixed-effects model                         |
|                         | `consistency`        | estimate consistency of agreement; the default                                     |
|                         | `absolute`           | estimate absolute agreement                                                        |
|                         | `testvalue(#)`       | test whether intraclass correlations equal `#`; default is `testvalue(0)`          |
| Reporting               |                      |                                                                                    |
|                         | `level(#)`           | set confidence level; default is `level(95)`                                       |
|                         | `format(%fmt)` | display format for statistics and confidence intervals; default is `format(%9.0g)` |
| \* `mixed` is required. |                      |                                                                                    |

`bootstrap`, `by`, `jackknife`, and `statsby` are allowed; see
[<strong>prefix</strong>](http://www.stata.com/help.cgi?prefix).
