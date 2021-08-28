## Syntax

`manova`
[depvarlist](http://www.stata.com/help.cgi?depvarlist)
`= term` \[\[`/`\] \[`term` \[`/`\] `...`\]\] <span
class="command">\[`if`\] \[`in`\]_ <span
class="command">\[`weight`\]_ \[`, options`\]

where `term` is of the form <span options="2">{space 2}_
`varname`\[{`*`\|`|`<span options=")-">{c
)-}_`varname`\[`...`\]\]

| Options                                                                                                                                                                     |                       | Description                                                     |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------|-----------------------------------------------------------------|
| Model                                                                                                                                                                       |                       |                                                                 |
|                                                                                                                                                                             | `category(varlist)`   | names of variables in the `terms` that are categorical or class |
|                                                                                                                                                                             | `class(varlist)`      | synonym for `category(varlist)`                                 |
|                                                                                                                                                                             | `continuous(varlist)` | names of variables in the `terms` that are continuous           |
|                                                                                                                                                                             | `noconstant`          | suppress constant term                                          |
| Reporting                                                                                                                                                                   |                       |                                                                 |
|                                                                                                                                                                             | `detail`              | report categorical variable value mappings                      |
| `bootstrap`, `by`, `jackknife`, and `statsby` are allowed; see [<strong>prefix</strong>](http://www.stata.com/help.cgi?prefix).                  |                       |                                                                 |
| Weights are not allowed with the [<strong>bootstrap</strong>](http://www.stata.com/help.cgi?bootstrap) prefix.                                   |                       |                                                                 |
| `aweight`s are not allowed with the [<strong>jackknife</strong>](http://www.stata.com/help.cgi?jackknife) prefix.                                |                       |                                                                 |
| `aweight`s and `fweight`s are allowed; see [<strong>weight</strong>](http://www.stata.com/help.cgi?weight)                                       |                       |                                                                 |
| See [<strong>manova_postestimation_10</strong>](http://www.stata.com/help.cgi?manova_postestimation_10) for features available after estimation. |                       |                                                                 |
