## Syntax

Two samples, compute sample size for unbalanced designs

Compute total sample size

`power` ...`, nratio(numlist)` \[`nfractional`\] ...

Compute one group size given the other

`power` ..., `n#(numlist) compute(N1`\|`N2)` \[`nfractional`\]
...

Two samples, specify sample size for unbalanced designs

Specify total sample size and allocation ratio

`power` ...`, n(numlist) nratio(numlist)` \[`nfractional`\] ...

Specify one of the group sizes and allocation ratio

`power` ...`, n#(numlist) nratio(numlist)` \[`nfractional`\]
...

Specify total sample size and one of the group sizes

`power` ...`, n(numlist) n#(numlist)` ...

Specify group sizes

`power` ...`, n1(numlist) n2(numlist)` ...

| twosampleopts                                                                                                                                                                                                                                                                                                                                             |                     | Description                                                                       |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------|-----------------------------------------------------------------------------------|
| \*                                                                                                                                                                                                                                                                                                                                                        | `n(numlist)`        | total sample size; required to compute power or effect size                       |
| \*                                                                                                                                                                                                                                                                                                                                                        | `n1(numlist)`       | sample size of the control group                                                  |
| \*                                                                                                                                                                                                                                                                                                                                                        | `n2(numlist)`       | sample size of the experimental group                                             |
| \*                                                                                                                                                                                                                                                                                                                                                        | `nratio(numlist)`   | ratio of sample sizes, `N2/N1`; default is `nratio(1)`, meaning equal group sizes |
|                                                                                                                                                                                                                                                                                                                                                           | `compute(N1`\|`N2)` | solve for `N1` given `N2` or for `N2` given `N1`                                  |
|                                                                                                                                                                                                                                                                                                                                                           | `nfractional`       | allow fractional sample sizes                                                     |
| \* Specifying a list of values in at least two starred options, or at least two command arguments, or at least one starred option and one argument results in computations for all possible combinations of the values; see [<strong>numlist</strong>](http://www.stata.com/help.cgi?numlist). Also see the `parallel` option. |                     |                                                                                   |
