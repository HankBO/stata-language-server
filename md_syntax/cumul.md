## Syntax

`cumul`
[varname](http://www.stata.com/help.cgi?varname)
_\[`if`\] \[`in`\]_ \[`weight`\] `,`
`generate(newvar)` \[`options`\]

| Options                                                                                                                                |                    | Description                                |
|----------------------------------------------------------------------------------------------------------------------------------------|--------------------|--------------------------------------------|
| Main                                                                                                                                   |                    |                                            |
| \*                                                                                                                                     | `generate(newvar)` | create variable `newvar`                   |
|                                                                                                                                        | `freq`             | use frequency units for cumulative         |
|                                                                                                                                        | `equal`            | generate equal cumulatives for tied values |
| \* `generate(newvar)` is required.                                                                                                     |                    |                                            |
| `by` is allowed; see [<strong>[D]</strong> by](http://www.stata.com/help.cgi?by).                           |                    |                                            |
| `fweight`s and `aweight`s are allowed; see [<strong>weight</strong>](http://www.stata.com/help.cgi?weight). |                    |                                            |
