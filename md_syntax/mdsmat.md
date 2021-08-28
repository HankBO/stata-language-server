## Syntax

`mdsmat matname` \[`, options`\]

Options

Description

Model

`method(method)`

method for performing MDS

`loss(loss)`

loss function

`transform(tfunction)`

permitted transformations of dissimilarities

`normalize(norm)`

normalization method; default is `normalize(principal)`

`names(namelist)`

variable names corresponding to row and column names of the matrix;
required with all but `shape(full)`

`shape(full)`

`matname` is a square symmetric matrix; the default

`shape(lower)`

`matname` is a vector with the rowwise lower triangle (with diagonal)

`shape(llower)`

`matname` is a vector with the rowwise strictly lower triangle (no
diagonal)

`shape(upper)`

`matname` is a vector with the rowwise upper triangle (with diagonal)

`shape(uupper)`

`matname` is a vector with the rowwise strictly upper triangle (no
diagonal)

`s2d(standard)`

convert similarity to dissimilarity: dissim(ij) = sqrt<span
options="-(">{c -(}_sim(ii)+sim(jj)-2sim(ij)<span options=")-">{c
)-}_

`s2d(oneminus)`

convert similarity to dissimilarity: dissim(ij) = 1-sim(ij)

Model 2

`dimension(#)`

configuration dimensions; default is `dimension(2)`

`force`

fix problems in proximity information

`addconstant`

make distance matrix positive semidefinite (classical MDS only)

`weight(matname)`

specifies a weight matrix with the same shape as the proximity matrix

Reporting

maximum number of eigenvalues to display; default is (classical MDS
only) display table with configuration coordinates suppress
configuration plot

Minimization

`initialize(initopt)`

start with configuration given in `initopt`

`tolerance(#)`

tolerance for configuration matrix; default is `tolerance(1e-4)`

`ltolerance(#)`

tolerance for loss criterion; default is `ltolerance(1e-8)`

`iterate(#)`

perform maximum of `#` iterations; default is `iterate(1000)`

`protect(#)`

perform `#` optimizations and report best solution; default is
`protect(1)`

`nolog`

suppress the iteration log

`trace`

display current configuration in iteration log

`gradient`

display current gradient matrix in iteration log

`sdprotect(#)`

advanced; see
[<var class="command">Options</var><strong></strong>](#sdprotect())
below

`sdprotect(#)` does not appear in the dialog box.

See
[<strong>[MV]</strong> mds postestimation](http://www.stata.com/help.cgi?mds_postestimation)
for features available after estimation.

| method |             | Description                                                                                                                        |
|--------|-------------|------------------------------------------------------------------------------------------------------------------------------------|
|        | `classical` | classical MDS; default if neither `loss()` nor `transform()` is specified                                                          |
|        | `modern`    | modern MDS; default if `loss()` or `transform()` is specified; except when `loss(stress)` and `transform(monotonic)` are specified |
|        | `nonmetric` | nonmetric (modern) MDS; default when `loss(stress)` and `transform(monotonic)` are specified                                       |

|        |            |                                                                              |
|--------|------------|------------------------------------------------------------------------------|
| `loss` |            | Description                                                                  |
|        | `stress`   | stress criterion, normalized by distances; the default                       |
|        | `nstress`  | stress criterion, normalized by disparities                                  |
|        | `sstress`  | squared stress criterion, normalized by distances                            |
|        | `nsstress` | squared stress criterion, normalized by disparities                          |
|        | `strain`   | strain criterion (with `transform(identity)` is equivalent to classical MDS) |
|        | `sammon `  | Sammon mapping                                                               |

|             |             |                                                                                     |
|-------------|-------------|-------------------------------------------------------------------------------------|
| `tfunction` |             | Description                                                                         |
|             | `identity`  | no transformation; disparity = dissimilarity; the default                           |
|             | `power`     | power alpha: disparity = dissimilarity^alpha                                        |
|             | `monotonic` | weakly monotonic increasing functions (nonmetric scaling); only with `loss(stress)` |

|        |                                 |                                                                                      |
|--------|---------------------------------|--------------------------------------------------------------------------------------|
| `norm` |                                 | Description                                                                          |
|        | `principal`                     | principal orientation; location=0; the default                                       |
|        | `classical`                     | Procrustes rotation toward classical solution                                        |
|        | `target(matname)`\[`, copy`\] | Procrustes rotation toward `matname`; ignore naming conflicts if `copy` is specified |

|           |                               |                                                                      |
|-----------|-------------------------------|----------------------------------------------------------------------|
| `initopt` |                               | Description                                                          |
|           | `classical`                   | start with classical solution; the default                           |
|           | `random`\[`(#)`\]         | start at random configuration, setting seed to `#`                   |
|           | `from(matname)`\[`, copy`\] | start from `matname`; ignore naming conflicts if `copy` is specified |
