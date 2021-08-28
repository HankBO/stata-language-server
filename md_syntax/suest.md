## Syntax

`suest namelist` \[`, options`\]

where `namelist` is a list of one or more names under which estimation
results were stored via
[<strong>estimates store</strong>](http://www.stata.com/help.cgi?estimates%20store).
Wildcards may be used. `*` and `_all` refer to all stored results. A
period (`.`) may be used to refer to the last estimation results, even
if they have not (yet) been stored.

| Options                                         |                   | Description                                                                                                                                      |
|-------------------------------------------------|-------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| SE/Robust                                       |                   |                                                                                                                                                  |
|                                                 | `svy`             | survey data estimation                                                                                                                           |
|                                                 | `vce(vcetype)`    | `vcetype` may be `robust` or `cluster clustvar`                                                                                                |
| Reporting                                       |                   |                                                                                                                                                  |
|                                                 | `level(#)`        | set confidence level; default is `level(95)`                                                                                                     |
|                                                 | `dir`             | display a table describing the models                                                                                                            |
|                                                 | `eform(string)`   | report exponentiated coefficients and label as `string`                                                                                          |
|                                                 | `display_options` | control columns and column formats, row spacing, line width, display of omitted variables and base and empty cells, and factor-variable labeling |
|                                                 | `coeflegend`      | display legend instead of statistics                                                                                                             |
| `coeflegend` does not appear in the dialog box. |                   |                                                                                                                                                  |
