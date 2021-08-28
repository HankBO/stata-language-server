## Syntax

`jkstat`
\[[varlist](http://www.stata.com/help.cgi?varlist)\]
_\[`weight`\]_ _\[`if`\]
\[`in`\]_ \[`, options` \]

`jkstat` \[`namelist`\] \[`using filename`\] <span
class="command">\[`if`\] \[`in`\]_ \[`, options` \]

|                   |                                       |
|-------------------|---------------------------------------|
| `options`         | Description {p2line None}             |
| `notable`         | suppress table of output              |
| `noheader`        | suppress table header                 |
| `nolegend`        | suppress table legend                 |
| `verbose`         | display the full table legend         |
| `level(#)`        | confidence level for CIs              |
| `title(text)`     | title for jackknife results           |
| `stat(vector)`    | observed values                       |
| `strata(varname)` | strata                                |
| `mse`             | use MSE formula for variance estimate |

|     |                   |                        |
|-----|-------------------|------------------------|
|     | `display_options` | control column formats |

`fweight`s, `pweight`s, and `iweight`s are allowed with `jkstat`; see
[<strong>weight</strong>](http://www.stata.com/help.cgi?weight).

`jkstat` shares the features of all estimation commands, except that
`adjust`, `margins`, `predict`, and `predictnl` are not allowed; see
[<strong>estcom</strong>](http://www.stata.com/help.cgi?estcom).
