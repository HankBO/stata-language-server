## Syntax

Compute sample size

`power`
[<var class="command">usermethod</var><strong></strong>](#usermethod)
... \[`, power(numlist)`
[<var class="command">poweropts</var><strong></strong>](power##power_options)
[<var class="command">useropts</var><strong></strong>](#useropts)\]

Compute power

`power`
[<var class="command">usermethod</var><strong></strong>](#usermethod)
...`,`
[<var class="command">nspec</var><strong></strong>](#nspec)
\[[<var class="command">poweropts</var><strong></strong>](power##power_options)
[<var class="command">useropts</var><strong></strong>](#useropts)\]

Compute effect size

`power`
[<var class="command">usermethod</var><strong></strong>](#usermethod)
...`,`
[<var class="command">nspec</var><strong></strong>](#nspec)
`power(numlist)`
\[[<var class="command">poweropts</var><strong></strong>](power##power_options)
[<var class="command">useropts</var><strong></strong>](#useropts)\]

`usermethod` is the name of the method you would like to add to the
`power` command. When naming your `power` methods, you should follow the
same convention as for naming the programs you add to Stata -- do not
pick "nice" names that may later be used by Stata's official methods.

`useropts` are the options supported by your method `usermethod`.

`nspec` contains `n(numlist)` for a one-sample test or any of the
sample-size options of
[<var class="command">poweropts</var><strong></strong>](power##power_options)
such as `n1(numlist)` and `n2(numlist)` for a two-sample test.
