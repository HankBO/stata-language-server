## Syntax

After regress

`_predict` _\[`type`\] \[_
[newvar](http://www.stata.com/help.cgi?newvar)
_\[`if`\] \[`in`\]_ \[`, xb stdp stdf`
`stdr hat cooksd residuals rstandard rstudent nolabel`\]

After single-equation (SE) estimators

`_predict` _\[`type`\] \[_
[newvar](http://www.stata.com/help.cgi?newvar)
_\[`if`\] \[`in`\]_ \[`, xb stdp`
`nooffset nolabel`\]

After multiple-equation (ME) estimators

`_predict` _\[`type`\] \[_
[newvar](http://www.stata.com/help.cgi?newvar)
_\[`if`\] \[`in`\]_ \[`, xb stdp stddp`
`nooffset nolabel equation(eqno`\[`, eqno`\]`)`\]
