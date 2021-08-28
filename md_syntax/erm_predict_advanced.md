## Syntax

`predict` _\[`type`\] \[_
[newvar](http://www.stata.com/help.cgi?newvar)
_\[`if`\] \[`in`\]_ \[`,`
[<var class="command">treatstatistic</var><strong></strong>](erm_predict_treatment##treatstatistic)
[<var class="command">howcalculated</var><strong></strong>](eregress_predict##howcalculated_options)
[<var class="command">treatmodifier</var><strong></strong>](erm_predict_treatment##treatmodifier)
[<var class="command">oprobitmodifier</var><strong></strong>](erm_predict_treatment##oprobitmodifier)
[<var class="command">advanced</var><strong></strong>](#advanced)\]

In some cases, more than one new variable needs to be specified:

`predict` _\[`type`\] \[_ <span
options="-(">{c -(}_`stub*`|[<var class="command">newvarlist</var><strong></strong>](http://www.stata.com/help.cgi?varlist)<span
options=")-">{c )-}_ _\[`if`\]
\[`in`\]_ \[`,`
[<var class="command">treatstatistic</var><strong></strong>](erm_predict_treatment##treatstatistic)
[<var class="command">howcalculated</var><strong></strong>](eregress_predict##howcalculated_options)
[<var class="command">treatmodifier</var><strong></strong>](erm_predict_treatment##treatmodifier)
[<var class="command">oprobitmodifier</var><strong></strong>](erm_predict_treatment##oprobitmodifier)
[<var class="command">advanced</var><strong></strong>](#advanced)\]

With the exception of `advanced`, you have seen this syntax in the other
`predict` manual entries. We will not cover old ground.

| advanced |                    | Description                                                                                                         |
|----------|--------------------|---------------------------------------------------------------------------------------------------------------------|
|          | `equation(depvar)` | calculate results for specified dependent variable                                                                  |
|          | `nooffset`         | ignore option `offset()` specified when model was fit in making calculation                                         |
|          | `pr(a, b)`         | calculate Pr(a &lt; xb + e\_i.`depvar` &lt; b); `a` and `b` are numbers or variable names                           |
|          | `e(a, b)`          | calculate E(y\_i \| a &lt; y\_i &lt; b), where y\_i = xb + e\_i.`depvar`; `a` and `b` are numbers or variable names |
|          | `scores`           | calculate equation-level score variables                                                                            |

Also note that even though option `mean` was not included in
`treatstatistic` for `eprobit` and `eoprobit`, it is allowed with them.
`mean` returns the probability of a positive outcome after `eprobit` and
returns the expected value of the outcome after `eoprobit`.
