## Syntax

`mdslong`
[depvar](http://www.stata.com/help.cgi?depvar)
_\[`if`\] \[`in`\]_ \[`weight`\]`,`
`id(var1 var2)` \[`options`\]

Options

Description

Model

\*

`id(var1 var2)`

identify comparison pairs (object1,object2)

`method(method)`

method for performing MDS

`loss(loss)`

loss function

`transform(tfunction)`

permitted transformations of dissimilarities

`normalize(norm)`

normalization method; default is `normalize(principal)`

`s2d(standard)`

convert similarity to dissimilarity: dissim(ij) = sqrt<span
options="-(">{c -(}_sim(ii)+sim(jj)-2sim(ij)<span options=")-">{c
)-}_; the default

`s2d(oneminus)`

convert similarity to dissimilarity: dissim(ij) = 1-sim(ij)

`force`

correct problems in proximity information

`dimension(#)`

configuration dimensions; default is `dimension(2)`

`addconstant`

make distance matrix positive semidefinite (classical MDS only)

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

\* `id(var1 var2)` is required.

`by` and `statsby` are allowed; see
[<strong>prefix</strong>](http://www.stata.com/help.cgi?prefix).

`aweight`s and `fweight`s are allowed for methods `modern` and
`nonmetric`; see
[<strong>weights</strong>](http://www.stata.com/help.cgi?weights).

The maximum number of compared objects allowed is the maximum matrix
size; see
[<strong>[R]</strong> matsize](http://www.stata.com/help.cgi?matsize).

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
