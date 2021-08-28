## Syntax

`impute`
[depvar](http://www.stata.com/help.cgi?depvar)
[indepvars](http://www.stata.com/help.cgi?indepvars)
_\[`if`\] \[`in`\]_ <span
class="command">\[`weight`\]_ `, generate(newvar1)`
\[`options`\]

| Options                                                                                                                                                            |                       | Description                                                             |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------|-------------------------------------------------------------------------|
| Main                                                                                                                                                               |                       |                                                                         |
| \*                                                                                                                                                                 | `generate(newvar1)`   | generate `newvar1` to contain the imputations                           |
|                                                                                                                                                                    | `nomissings(varlist)` | include `varlist` without missing values in the best-subset regressions |
|                                                                                                                                                                    | `all`                 | estimate using all observations (regardless of `if` and `in`)           |
|                                                                                                                                                                    | `regsample(exp)`      | estimate using observations specified in `exp`                          |
|                                                                                                                                                                    | `copyrest`            | copy out-of-sample values of dependent variable to generated variable   |
|                                                                                                                                                                    | `varp(newvar2)`       | create new variable to contain the variance of the prediction           |
| \* `generate(newvar1)` is required.                                                                                                                                |                       |                                                                         |
| `indepvars` and `varlist` may contain time-series operators; see [<strong>tsvarlist</strong>](http://www.stata.com/help.cgi?tsvarlist). |                       |                                                                         |
| `aweight`s and `fweight`s are allowed; see [<strong>weight</strong>](http://www.stata.com/help.cgi?weight).                             |                       |                                                                         |
