## Syntax

Logistic regression for grouped data

`blogit`<span options="2">{space 2}_`pos_var pop_var`
\[[indepvars](http://www.stata.com/help.cgi?indepvars)\]
_\[`if`\] \[`in`\]_ \[`, blogit_options`\]

Probit regression for grouped data

`bprobit pos_var pop_var`
\[[indepvars](http://www.stata.com/help.cgi?indepvars)\]
_\[`if`\] \[`in`\]_ \[`, bprobit_options`\]

Weighted least-squares logistic regression for grouped data

`glogit`<span options="2">{space 2}_`pos_var pop_var`
\[[indepvars](http://www.stata.com/help.cgi?indepvars)\]
_\[`if`\] \[`in`\]_ \[`, glogit_options`\]

Weighted least-squares probit regression for grouped data

`gprobit pos_var pop_var`
\[[indepvars](http://www.stata.com/help.cgi?indepvars)\]
_\[`if`\] \[`in`\]_ \[`, gprobit_options`\]

| blogit\_options |                                | Description                                                                                                                                      |
|-----------------|--------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| Model           |                                |                                                                                                                                                  |
|                 | `noconstant`                   | suppress constant term                                                                                                                           |
|                 | `asis`                         | retain perfect predictor variables                                                                                                               |
|                 | `offset(varname)`              | include `varname` in model with coefficient constrained to 1                                                                                     |
|                 | `constraints(constraints)` | apply specified linear constraints                                                                                                               |
|                 | `collinear`                    | keep collinear variables                                                                                                                         |
| SE/Robust       |                                |                                                                                                                                                  |
|                 | `vce(vcetype)`                 | `vcetype` may be `oim`, `robust`, `cluster clustvar`, `bootstrap`, or `jackknife`                                                              |
| Reporting       |                                |                                                                                                                                                  |
|                 | `level(#)`                     | set confidence level; default is `level(95)`                                                                                                     |
|                 | `or`                           | report odds ratios                                                                                                                               |
|                 | `nocnsreport`                  | do not display constraints                                                                                                                       |
|                 | `display_options`              | control columns and column formats, row spacing, line width, display of omitted variables and base and empty cells, and factor-variable labeling |
| Maximization    |                                |                                                                                                                                                  |
|                 | `maximize_options`             | control the maximization process; seldom used                                                                                                    |
|                 | `nocoef`                       | do not display coefficient table; seldom used                                                                                                    |
|                 | `coeflegend`                   | display legend instead of statistics                                                                                                             |

| bprobit\_options |                                | Description                                                                                                                                      |
|------------------|--------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| Model            |                                |                                                                                                                                                  |
|                  | `noconstant`                   | suppress constant term                                                                                                                           |
|                  | `asis`                         | retain perfect predictor variables                                                                                                               |
|                  | `offset(varname)`              | include `varname` in model with coefficient constrained to 1                                                                                     |
|                  | `constraints(constraints)` | apply specified linear constraints                                                                                                               |
|                  | `collinear`                    | keep collinear variables                                                                                                                         |
| SE/Robust        |                                |                                                                                                                                                  |
|                  | `vce(vcetype)`                 | `vcetype` may be `oim`, `robust`, `cluster clustvar`, `bootstrap`, or `jackknife`                                                              |
| Reporting        |                                |                                                                                                                                                  |
|                  | `level(#)`                     | set confidence level; default is `level(95)`                                                                                                     |
|                  | `nocnsreport`                  | do not display constraints                                                                                                                       |
|                  | `display_options`              | control columns and column formats, row spacing, line width, display of omitted variables and base and empty cells, and factor-variable labeling |
| Maximization     |                                |                                                                                                                                                  |
|                  | `maximize_options`             | control the maximization process; seldom used                                                                                                    |
|                  | `nocoef`                       | do not display coefficient table; seldom used                                                                                                    |
|                  | `coeflegend`                   | display legend instead of statistics                                                                                                             |

| glogit\_options |                   | Description                                                                                                                                      |
|-----------------|-------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| SE              |                   |                                                                                                                                                  |
|                 | `vce(vcetype)`    | `vcetype` may be `ols`, `bootstrap`, or `jackknife`                                                                                              |
| Reporting       |                   |                                                                                                                                                  |
|                 | `level(#)`        | set confidence level; default is `level(95)`                                                                                                     |
|                 | `or`              | report odds ratios                                                                                                                               |
|                 | `display_options` | control columns and column formats, row spacing, line width, display of omitted variables and base and empty cells, and factor-variable labeling |
|                 | `coeflegend`      | display legend instead of statistics                                                                                                             |

| gprobit\_options |                   | Description                                                                                                                                      |
|------------------|-------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| SE               |                   |                                                                                                                                                  |
|                  | `vce(vcetype)`    | `vcetype` may be `ols`, `bootstrap`, or `jackknife`                                                                                              |
| Reporting        |                   |                                                                                                                                                  |
|                  | `level(#)`        | set confidence level; default is `level(95)`                                                                                                     |
|                  | `display_options` | control columns and column formats, row spacing, line width, display of omitted variables and base and empty cells, and factor-variable labeling |
|                  | `coeflegend`      | display legend instead of statistics                                                                                                             |

`indepvars` may contain factor variables; see
[<strong>fvvarlist</strong>](http://www.stata.com/help.cgi?fvvarlist).

`bootstrap`, `by`, `jackknife`, `rolling`, and `statsby` are allowed;
see
[<strong>prefix</strong>](http://www.stata.com/help.cgi?prefix).
`fp` is allowed with `blogit` and `bprobit`.

`nocoef` and `coeflegend` do not appear in the dialog box.

See
[<strong>[R]</strong> glogit postestimation](http://www.stata.com/help.cgi?glogit_postestimation)
for features available after estimation.
