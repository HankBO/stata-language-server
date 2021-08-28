## Syntax

`clustermat linkage matname` ...

|                   |                                                                                                                                                                      |
|-------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `linkage`         | Description {p2line None}                                                                                                                                            |
| `singlelinkage`   | single-linkage cluster analysis                                                                                                                                      |
| `averagelinkage`  | average-linkage cluster analysis                                                                                                                                     |
| `completelinkage` | complete-linkage cluster analysis                                                                                                                                    |
| `waveragelinkage` | weighted-average linkage cluster analysis                                                                                                                            |
| `medianlinkage`   | median-linkage cluster analysis                                                                                                                                      |
| `centroidlinkage` | centroid-linkage cluster analysis                                                                                                                                    |
| `wardslinkage`    | Ward's linkage cluster analysis {p2line None} See [<strong>[MV]</strong> cluster linkage](http://www.stata.com/help.cgi?cluster_linkage). |

`clustermat stop` has similar syntax to that of `cluster stop`; see
[<strong>[MV]</strong> cluster stop](http://www.stata.com/help.cgi?cluster_stop).
For the remaining postclustering subcommands and user utilities, you may
specify either `cluster` or `clustermat` -- it does not matter which.
