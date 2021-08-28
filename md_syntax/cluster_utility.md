## Syntax

Directory-style listing of currently defined clusters

`clusterdir`

Detailed listing of clusters

`cluster list` \[`clnamelist`\] \[`,`
[<var class="command">list_options</var><strong></strong>](#list_options)
\]

Drop cluster analyses

`cluster drop` { `clnamelist` \| `_all`
}

Mark a cluster analysis as the most recent one

`cluster use clname`

Rename a cluster

`cluster rename oldclname newclname`

Rename variables attached to a cluster

`cluster renamevar oldvarname`
[newvar](http://www.stata.com/help.cgi?newvar)
\[`, name(clname)` \]

`cluster renamevar oldstub newstub , prefix` \[ `name(clname)`
\]

| list\_options                            |                 | Description                                                         |
|------------------------------------------|-----------------|---------------------------------------------------------------------|
| Options                                  |                 |                                                                     |
|                                          | `notes`         | list cluster notes                                                  |
|                                          | `type`          | list cluster analysis type                                          |
|                                          | `method`        | list cluster analysis method                                        |
|                                          | `dissimilarity` | list cluster analysis dissimilarity measure                         |
|                                          | `similarity`    | list cluster analysis similarity measure                            |
|                                          | `vars`          | list variable names attached to the cluster analysis                |
|                                          | `chars`         | list any characteristics attached to the cluster analysis           |
|                                          | `other`         | list any "other" information                                        |
|                                          | `all`           | list all items and information attached to the cluster; the default |
| `all` does not appear in the dialog box. |                 |                                                                     |
