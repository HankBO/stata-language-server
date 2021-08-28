## Syntax

Confidence intervals for means, normal distribution

`ci means`
\[[varlist](http://www.stata.com/help.cgi?varlist)\]
_\[`if`\] \[`in`\]_ \[`weight`\] \[`,`
`options`\]

`cii means #obs #mean #sd` \[`, level(#)`\]

Confidence intervals for means, Poisson distribution

`ci means`
\[[varlist](http://www.stata.com/help.cgi?varlist)\]
_\[`if`\] \[`in`\]_ \[`weight`\]`, poisson`
\[`exposure(varname) options`\]

`cii means #exposure #events, poisson` \[`level(#)`\]

Confidence intervals for proportions

`ci  proportions `
\[[varlist](http://www.stata.com/help.cgi?varlist)\]
_\[`if`\] \[`in`\]_ \[`weight`\] \[`,`
`prop_options options`\]

`cii proportions #obs #succ` \[`, prop_options level(#)`\]

Confidence intervals for variances

`ci  variances`
\[[varlist](http://www.stata.com/help.cgi?varlist)\]
_\[`if`\] \[`in`\]_ \[`weight`\] \[`,`
`bonett options`\]

`cii variances #obs #variance` \[`, level(#)`\]

`cii variances #obs #variance #kurtosis, bonett`
\[`level(#)`\]

Confidence intervals for standard deviations

`ci variances`
\[[varlist](http://www.stata.com/help.cgi?varlist)\]
_\[`if`\] \[`in`\]_ \[`weight`\]`, sd`
\[`bonett options`\]

`cii variances #obs #sd, sd` \[`level(#)`\]

`cii variances #obs #sd #kurtosis, sd bonett`
\[`level(#)`\]

`#obs` must be a positive integer. `#exposure`, `#sd`, and `#variance`
must be a positive number. `#succ` and `#events` must be a nonnegative
integer or between 0 and 1. If the number is between 0 and 1, Stata
interprets it as the fraction of successes or events and converts it to
an integer number representing the number of successes or events. The
computation then proceeds as if two integers had been specified. If
option `bonett` is specified, you must additionally specify `#kurtosis`
with `cii variances`.

| prop\_options |            | Description                                       |
|---------------|------------|---------------------------------------------------|
|               | `exact`    | calculate exact confidence intervals; the default |
|               | `wald`     | calculate Wald confidence intervals               |
|               | `wilson`   | calculate Wilson confidence intervals             |
|               | `agresti`  | calculate Agresti-Coull confidence intervals      |
|               | `jeffreys` | calculate Jeffreys confidence intervals           |

| options |                | Description                                                              |
|---------|----------------|--------------------------------------------------------------------------|
|         | `level(#)`     | set confidence level; default is `level(95)`                             |
|         | `separator(#)` | draw separator line after every `#` variables; default is `separator(5)` |
|         | `total`        | add output for all groups combined (for use with `by` only)              |

`by` and `statsby` are allowed with `ci`; see
[<strong>prefix</strong>](http://www.stata.com/help.cgi?prefix).

`aweight`s are allowed with `ci means` for normal data, and `fweight`s
are allowed with all `ci` subcommands; see
[<strong>weight</strong>](http://www.stata.com/help.cgi?weight).
