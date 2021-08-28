## Syntax

Poststratification adjusted sampling weights

`svygen poststratify new_weight_var` <span
class="command">\[`weight`\]_ _\[`if`\]
\[`in`\]_ \[`, poststrata(varname) postweight(varname)`
`nocheck`\]

Balanced repeated replicate (BRR) weights

`svygen brr stub` _\[`weight`\]_ <span
class="command">\[`if`\] \[`in`\]_`, Hadamard(matname)`
`strata(varname)` \[`psu(varname) fay(#) poststrata(varname)`
`postweight(varname) nocheck`\]

Jackknife replicate weights

`svygen jackknife stub` \[`multiplier`\] <span
class="command">\[`weight`\]_ _\[`if`\]
\[`in`\]_ \[`, strata(varname) psu(varname) fpc(varname)`
`poststrata(varname) postweight(varname)`\]

Successive difference replicate (SDR) weights

`svygen sdr stub` _\[`weight`\]_ <span
class="command">\[`if`\] \[`in`\]_`, Hadamard(matname)`
\[`psu(varname) poststrata(varname) postweight(varname) nocheck`\]

`pweight`s and `iweight`s are allowed; see
[<strong>weights</strong>](http://www.stata.com/help.cgi?weights).
