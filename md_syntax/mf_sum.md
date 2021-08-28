## Syntax

`numeric colvector rowsum(numeric matrix Z` \[`, missing`\]`)`

`numeric rowvector colsum(numeric matrix Z` \[`, missing`\]`)`

`numeric scalar`<span class="nowrap"> _ `sum(numeric matrix Z`
\[`, missing`\]`)`

`numeric colvector quadrowsum(numeric matrix Z` \[`, missing`\]`)`

`numeric rowvector quadcolsum(numeric matrix Z` \[`, missing`\]`)`

`numeric scalar`<span class="nowrap"> _
`quadsum(numeric matrix Z` \[`, missing`\]`)`

where optional argument `missing` is a `real scalar` that determines how
missing values in `Z` are treated:

1\. Specifying `missing` as 0 is equivalent to not specifying the
argument; missing values in `Z` are treated as contributing 0 to the
sum.

2\. Specifying `missing` as 1 (or nonzero) specifies that missing values
in `Z` are to be treated as missing values and to turn the sum to
missing.
