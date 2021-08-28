## Syntax

Produce default table

`power` ... `, table` ...

Suppress table

`power` ... `, notable` ...

Produce custom table

`power` ... `, table(`\[`colspec`\] \[`, tableopts`\]`)` ...

where `colspec` is

`column`\[`:label`\] \[`column`\[`:label`\] \[...\]\]

`column` is one of the columns defined
[<strong>below</strong>](#column), and
`label` is a column label (may contain quotes and compound quotes).

| tableopts                                                  |                     | Description                                                                                             |
|------------------------------------------------------------|---------------------|---------------------------------------------------------------------------------------------------------|
| Table                                                      |                     |                                                                                                         |
|                                                            | `add`               | add `column`s to the default table                                                                      |
|                                                            | `labels(labspec)`   | change default labels for specified columns; default labels are column names                            |
|                                                            | `widths(widthspec)` | change default column widths; default is specific to each column                                        |
|                                                            | `formats(fmtspec)`  | change default column formats; default is specific to each column                                       |
|                                                            | `noformat`          | do not use default column formats                                                                       |
|                                                            | `separator(#)`      | draw a horizontal separator line every `#` lines; default is `separator(0)`, meaning no separator lines |
|                                                            | `divider`           | draw divider lines between columns                                                                      |
|                                                            | `byrow`             | display rows as computations are performed; seldom used                                                 |
|                                                            | `noheader`          | suppress table header; seldom used                                                                      |
|                                                            | `continue`          | draw a continuation border in the table output; seldom used                                             |
| `noheader` and `continue` are not shown in the dialog box. |                     |                                                                                                         |

| column                                                                                                                            |                  | Description                                                                                                        |
|-----------------------------------------------------------------------------------------------------------------------------------|------------------|--------------------------------------------------------------------------------------------------------------------|
|                                                                                                                                   | `alpha`          | significance level                                                                                                 |
|                                                                                                                                   | `power`          | power                                                                                                              |
|                                                                                                                                   | `beta`           | type II error probability                                                                                          |
|                                                                                                                                   | `N`              | total number of subjects                                                                                           |
|                                                                                                                                   | `N1`             | number of subjects in the control group                                                                            |
|                                                                                                                                   | `N2`             | number of subjects in the experimental group                                                                       |
|                                                                                                                                   | `nratio`         | ratio of sample sizes, experimental to control                                                                     |
|                                                                                                                                   | `K`              | number of clusters                                                                                                 |
|                                                                                                                                   | `K1`             | number of clusters in the control group                                                                            |
|                                                                                                                                   | `K2`             | number of clusters in the experimental group                                                                       |
|                                                                                                                                   | `kratio`         | ratio of numbers of clusters, experimental to control                                                              |
|                                                                                                                                   | `M`              | cluster size                                                                                                       |
|                                                                                                                                   | `M1`             | cluster size in the control group                                                                                  |
|                                                                                                                                   | `M2`             | cluster size in the experimental group                                                                             |
|                                                                                                                                   | `mratio`         | ratio of cluster sizes, experimental to control                                                                    |
|                                                                                                                                   | `delta`          | effect size                                                                                                        |
|                                                                                                                                   | `target`         | target parameter                                                                                                   |
|                                                                                                                                   | `_all`           | display all supported columns                                                                                      |
|                                                                                                                                   | `method_columns` | columns specific to the [<strong>method</strong>](power##method) specified with `power` |
| By default, the following columns are displayed:                                                                                  |                  |                                                                                                                    |
| `alpha` and `power` are always displayed;                                                                                         |                  |                                                                                                                    |
| `N` is always displayed except for two-sample methods in a CRD;                                                                   |                  |                                                                                                                    |
| `N1` and `N2` are displayed for two-sample methods except for a CRD;                                                              |                  |                                                                                                                    |
| `kratio` and `mratio` are available for two-sample methods in a CRD;                                                              |                  |                                                                                                                    |
| `delta` is displayed when defined by the method;                                                                                  |                  |                                                                                                                    |
| additional columns specific to each `power` [<strong>method</strong>](power##method) may be displayed. |                  |                                                                                                                    |
