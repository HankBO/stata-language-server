## Syntax

To enter summary statistics data (SSD), the commands are

`ssd init`
[varlist](http://www.stata.com/help.cgi?varlist)

`ssd set` \[`#`\] `observations #`

`ssd set` \[`#`\] `means vector`

`ssd set` \[`#`\] {`variances` | `sd`}
`vector`

`ssd set` \[`#`\] {`covariances` |
`correlations`} `matrix`

`ssd addgroup`
[varname](http://www.stata.com/help.cgi?varname)<span
options="8">{space 8}_(to add second group)

`ssd addgroup`<span options="16">{space 16}_(to add subsequent
groups)

`ssd unaddgroup #`<span options="12">{space 12}_(to remove
last group)

`ssd status` \[`#`\]<span options="14">{space 14}_(to review
status)

To build SSD from raw data, the command is

`ssd build`
[varlist](http://www.stata.com/help.cgi?varlist)
\[`, group(varname) clear`\]

To review the contents of SSD, the commands are

`ssd status` \[`#`\]

`ssd describe`

`ssd list` \[`#`\]

In an emergency (`ssd` will tell you when), you may use

`ssd repair`

In the above,

A `vector` can be any of the following:

1\. A space-separated list of numbers, for example,

`. ssd set means 1 2 3`

2\. ` (stata) matname`  
where `matname` is the name of a Stata 1 x `k` or `k` x 1 matrix, for
example,

`. ssd set variances (stata) mymeans`

3\. `(mata) matname`  
where `matname` is the name of a Mata 1 x `k` or `k` x 1 matrix, for
example,

`. ssd set sd (mata) mymeans`

A `matrix` can be any of the following:

1\. A space-separated list of numbers corresponding to the rows of the
matrix, with backslashes (`\`) between rows. The numbers are either the
lower triangle and diagonal or the diagonal and upper triangle of the
matrix, for example,

`. ssd set correlations 1 \ .2 1 \ .3 .5 1`

or

`. ssd set correlations 1 .2 .3 \ 1 .5 \ 1`

2\. `(ltd) # #` ...  
which is to say, a space-separated list of numbers corresponding to the
lower triangle and diagonal of the matrix, without backslashes between
rows, for example,

`. ssd set correlations (ltd) 1  .2 1  .3 .5 1`

3\. `(dut) # #` ...  
which is to say, a space-separated list of numbers corresponding to
diagonal and upper triangle of the matrix, without backslashes between
rows, for example,

`. ssd set correlations (dut) 1 .2 .3   1 .5   1`

4\. `(stata) matname`  
where `matname` is the name of a Stata `k` x `k` symmetric matrix, for
example,

`. ssd set correlations (stata) mymat`

5\. `(mata) matname`  
where `matname` is the name of a Mata `k` x `k` symmetric matrix, for
example,

`. ssd set correlations (mata) mymat`
