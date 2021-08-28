## Syntax

`numeric vector`<span class="nowrap"> _
`runningsum(numeric vector x` \[`, missing`\]`)`

`numeric vector quadrunningsum(numeric vector x` \[`,`
`missing`\]`)`

`void`<span class="nowrap"> _ `_runningsum(y,`
`numeric vector x` \[`, missing`\]`)`

`void`<span class="nowrap"> _ `_quadrunningsum(y,`
`numeric vector x` \[`, missing`\]`)`

where optional argument `missing` is a `real scalar` that determines how
missing values in `x` are treated:

1\. Specifying `missing` as 0 is equivalent to not specifying the
argument; missing values in `x` are treated as contributing 0 to the
sum.

2\. Specifying `missing` as 1 specifies that missing values in `x` are
to be treated as missing values and turn the sum to missing.
