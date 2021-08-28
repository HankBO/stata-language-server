## Syntax

Generate grouping variables for specified numbers of clusters

`cluster generate` {
[newvar](http://www.stata.com/help.cgi?newvar)
\| `stub` } `= groups(numlist)` \[`,`
`options` \]

Generate grouping variable by cutting the dendrogram

`cluster generate`
[newvar](http://www.stata.com/help.cgi?newvar)
`= cut(#)` \[`, name:(clname)` \]

| Options |                   | Description                                                            |
|---------|-------------------|------------------------------------------------------------------------|
|         | `name(clname)`    | name of cluster analysis to use in producing new variables             |
|         | `ties(error)` | produce error message for ties; default                                |
|         | `ties(skip)`  | ignore requests that result in ties                                    |
|         | `ties(fewer)` | produce results for largest number of groups smaller than your request |
|         | `ties(more)`  | produce results for smallest number of groups larger than your request |
