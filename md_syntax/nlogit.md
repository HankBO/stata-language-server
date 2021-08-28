## Syntax

Nested logit regression

`nlogit`
[depvar](http://www.stata.com/help.cgi?depvar)
\[[indepvars](http://www.stata.com/help.cgi?indepvars)\]
_\[`if`\] \[`in`\]_ \[`weight`\] \[`||`
`lev1_equation` \[`|| lev2_equation` ...\]\] `|| altvar:`
\[`byaltvarlist`\]`, case(varname)` \[`nlogit_options`\]

where the syntax of `lev#_equation` is

`altvar:` \[`byaltvarlist`\] \[`, base(#,lbl) estconst`\]

Create variable based on specification of branches

`nlogitgen newaltvar = altvar (branchlist)` \[`, nolog`\]

<span options="branchlist">{marker branchlist}_ where `branchlist`
is

`branch, branch` \[`, branch ...`\]

and `branch` is

\[`label:`\] `alternative` \[`| alternative` \[`|`
`alternative ...`\] \]

Display tree structure

`nlogittree altvarlist` _\[`if`\] \[`in`\]_
\[`weight`\] \[`, nlogittree_options`\]

| nlogit\_options                 |                                | Description                                                                                                                                                                                  |
|---------------------------------|--------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Model                           |                                |                                                                                                                                                                                              |
| \*                              | `case(varname)`                | use `varname` to identify cases                                                                                                                                                              |
|                                 | `base(#,lbl)`                  | use the specified level or label of `altvar` as the base alternative for the bottom level                                                                                                    |
|                                 | `noconstant`                   | suppress the constant terms for the bottom-level alternatives                                                                                                                                |
|                                 | `nonnormalized`                | use the nonnormalized parameterization                                                                                                                                                       |
|                                 | `altwise`                      | use alternativewise deletion instead of casewise deletion                                                                                                                                    |
|                                 | `constraints(constraints)` | apply specified linear constraints                                                                                                                                                           |
|                                 | `collinear`                    | keep collinear variables                                                                                                                                                                     |
| SE/Robust                       |                                |                                                                                                                                                                                              |
|                                 | `vce(vcetype)`                 | `vcetype` may be `oim`, `robust`, `cluster clustvar`, `bootstrap`, or `jackknife`                                                                                                          |
| Reporting                       |                                |                                                                                                                                                                                              |
|                                 | `level(#)`                     | set confidence level; default is `level(95)`                                                                                                                                                 |
|                                 | `notree`                       | suppress display of tree-structure output; see also [<strong>nolabel</strong>](#treedisp) and [<strong>nobranches</strong>](#treedisp) |
|                                 | `nocnsreport`                  | do not display constraints                                                                                                                                                                   |
|                                 | `display_options`              | control columns and column formats, row spacing, line width, display of omitted variables and base and empty cells, and factor-variable labeling                                             |
| Maximization                    |                                |                                                                                                                                                                                              |
|                                 | `maximize_options`             | control the maximization process; seldom used                                                                                                                                                |
| \* `case(varname)` is required. |                                |                                                                                                                                                                                              |

| nlogittree\_options |                    | Description                                            |
|---------------------|--------------------|--------------------------------------------------------|
| Main                |                    |                                                        |
|                     | `choice(depvar)`   | use `depvar` as the choice indicator variable          |
|                     | `case(varname)`    | use `varname` to identify cases                        |
|                     | `generate(newvar)` | create `newvar` to identify invalid observations       |
|                     | `nolabel`          | suppress the value labels in tree-structure output     |
|                     | `nobranches`       | suppress drawing branches in the tree-structure output |

`byaltvarlist` may contain factor variables; see
[<strong>fvvarlist</strong>](http://www.stata.com/help.cgi?fvvarlist).

`bootstrap`, `by`, `fp`, `jackknife`, and `statsby` are allowed; see
[<strong>prefix</strong>](http://www.stata.com/help.cgi?prefix).

Weights are not allowed with the
[<strong>bootstrap</strong>](http://www.stata.com/help.cgi?bootstrap)
prefix.

`fweight`s, `iweight`s, and `pweight`s are allowed with `nlogit`, and
`fweight`s are allowed with `nlogittree`; see
[<strong>weight</strong>](http://www.stata.com/help.cgi?weight).
Weights for `nlogit` must be constant within case.

See
[<strong>[R]</strong> nlogit postestimation](http://www.stata.com/help.cgi?nlogit_postestimation)
for features available after estimation.
