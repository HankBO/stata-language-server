## Syntax

Cluster analysis of data

`cluster stop` \[`clname`\] \[`, options`\]

Cluster analysis of a dissimilarity matrix

`clustermat stop` \[`clname`\] `, variables(varlist)` \[`options`\]

where `clname` is the name of the cluster analysis. The default is the
most recently performed cluster analysis, which can be reset using the
`cluster use` command; see
[<strong>[MV] cluster utility</strong>](http://www.stata.com/help.cgi?cluster%20utility).

| Options                                                                                                                                                                                                                                                                 |                      | Description                                                     |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------|-----------------------------------------------------------------|
|                                                                                                                                                                                                                                                                         | `rule(calinski)`   | use Calinski-Harabasz pseudo-F index stopping rule; the default |
|                                                                                                                                                                                                                                                                         | `rule(duda)`         | use Duda-Hart Je(2)/Je(1) index stopping rule                   |
|                                                                                                                                                                                                                                                                         | `rule(rule_name)`    | use `rule_name` stopping rule; see `Options` for details        |
|                                                                                                                                                                                                                                                                         | `groups(numlist)`    | compute stopping rule for specified groups                      |
|                                                                                                                                                                                                                                                                         | `matrix(matname)`    | save the results in matrix `matname`                            |
| \*                                                                                                                                                                                                                                                                      | `variables(varlist)` | compute the stopping rule using `varlist`                       |
| \* `variables(varlist)` is required with a `clustermat` solution and optional with a `cluster` solution.                                                                                                                                                                |                      |                                                                 |
| `rule(rule_name)` is not shown in the dialog box. See [<strong>[MV]</strong> cluster programming subroutines](http://www.stata.com/help.cgi?cluster_subroutines) for information on how to add stopping rules to the `cluster stop` command. |                      |                                                                 |
