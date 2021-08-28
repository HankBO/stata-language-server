## Syntax

Cluster analysis of data

`cluster linkage`
\[[varlist](http://www.stata.com/help.cgi?varlist)\]
_\[`if`\] \[`in`\]_ \[`, cluster_options`\]

Cluster analysis of a dissimilarity matrix

`clustermat linkage`<span options="2">{space 2}_`matname`<span
options="2">{space 2}__\[`if`\]
\[`in`\]_ \[`, clustermat_options`\]

|                   |                                               |
|-------------------|-----------------------------------------------|
| `linkage`         | Description {p2line None}                     |
| `singlelinkage`   | single-linkage cluster analysis               |
| `averagelinkage`  | average-linkage cluster analysis              |
| `completelinkage` | complete-linkage cluster analysis             |
| `waveragelinkage` | weighted-average linkage cluster analysis     |
| `medianlinkage`   | median-linkage cluster analysis               |
| `centroidlinkage` | centroid-linkage cluster analysis             |
| `wardslinkage`    | Ward's linkage cluster analysis {p2line None} |

| cluster\_options |                    | Description                                                |
|------------------|--------------------|------------------------------------------------------------|
| Main             |                    |                                                            |
|                  | `measure(measure)` | similarity or dissimilarity measure                        |
|                  | `name(clname)`     | name of resulting cluster analysis                         |
| Advanced         |                    |                                                            |
|                  | `generate(stub)`   | prefix for generated variables; default prefix is `clname` |

| clustermat\_options |                     | Description                                                |
|---------------------|---------------------|------------------------------------------------------------|
| Main                |                     |                                                            |
|                     | `shape(shape)`      | shape (storage method) of `matname`                        |
|                     | `add`               | add cluster information to data currently in memory        |
|                     | `clear`             | replace data in memory with cluster information            |
|                     | `labelvar(varname)` | place dissimilarity matrix row names in `varname`          |
|                     | `name(clname)`      | name of resulting cluster analysis                         |
| Advanced            |                     |                                                            |
|                     | `force`             | perform clustering after fixing `matname` problems         |
|                     | `generate(stub)`    | prefix for generated variables; default prefix is `clname` |

|     |          |                                                       |
|-----|----------|-------------------------------------------------------|
|     | `shape`  | `matname` is stored as a                              |
|     | `full`   | square symmetric matrix; the default                  |
|     | `lower`  | vector of rowwise lower triangle (with diagonal)      |
|     | `llower` | vector of rowwise strict lower triangle (no diagonal) |
|     | `upper`  | vector of rowwise upper triangle (with diagonal)      |
|     | `uupper` | vector of rowwise strict upper triangle (no diagonal) |
