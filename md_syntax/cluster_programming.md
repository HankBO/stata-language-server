## Syntax

Obtain various attributes of a cluster analysis

`cluster query` \[`clname`\]

Set various attributes of a cluster analysis

`cluster set` \[`clname`\] \[`,`
[<var class="command">set_options</var><strong></strong>](cluster%20programming##set_options)\]

Delete attributes from a cluster analysis

`cluster delete clname` \[`,`
[<var class="command">delete_options</var><strong></strong>](cluster%20programming##delete_options)\]

Check similarity and dissimilarity measure name

`cluster parsedistance`
[<var class="command">measure</var><strong></strong>](http://www.stata.com/help.cgi?measure_option)

Compute similarity and dissimilarity measure

`cluster measures`
[varlist](http://www.stata.com/help.cgi?varlist)
_\[`if`\] \[`in`\]_ `,`
`compare:(numlist) generate:(newvarlist)`
\[[<var class="command">measures_options</var><strong></strong>](cluster%20programming##measures_options)\]

| set\_options |                          | Description                                                             |
|--------------|--------------------------|-------------------------------------------------------------------------|
|              | `addname`                | add `clname` to the master list of cluster analyses                     |
|              | `type(type)`             | set the cluster type for `clname`                                       |
|              | `method(method)`         | set the name of the clustering method for the cluster analysis          |
|              | `similarity(measure)`    | set the name of the similarity measure used for the cluster analysis    |
|              | `dissimilarity(measure)` | set the name of the dissimilarity measure used for the cluster analysis |
|              | `var(tag varname)`   | set `tag` that points to `varname`                                      |
|              | `char(tag charname)`     | set `tag` that points to `charname`                                     |
|              | `other(tag text)`        | set `tag` with `text` attached to the tag marker                        |
|              | `note(text)`             | add a note to the `clname`                                              |

| delete\_options |                  | Description                                                         |
|-----------------|------------------|---------------------------------------------------------------------|
|                 | `zap`            | delete all possible settings for `clname`                           |
|                 | `delname`        | remove `clname` from the master list of current cluster analysis    |
|                 | `type`           | delete the cluster type entry from `clname`                         |
|                 | `method`         | delete the cluster method entry from `clname`                       |
|                 | `similarity`     | delete the similarity entries from `clname`                         |
|                 | `dissimilarity`  | delete the dissimilarity entries from `clname`                      |
|                 | `notes(numlist)` | delete the specified numbered notes from `clname`                   |
|                 | `allnotes`       | remove all notes from `clname`                                      |
|                 | `var(tag)`       | remove `tag` from `clname`                                          |
|                 | `allvars`        | remove all the entries pointing to variables for `clname`           |
|                 | `varzap(tag)`    | same as `var()`, but also delete the referenced variable            |
|                 | `allvarzap`      | same as `allvars`, but also delete the variables                    |
|                 | `char(tag)`      | remove `tag` that points to a Stata characteristic from `clname`    |
|                 | `allchars`       | remove all entries pointing to Stata characteristics for `clname`   |
|                 | `charzap(tag)`   | same as `char()`, but also delete the characteristic                |
|                 | `allcharzap`     | same as `allchars`, but also delete the characteristics             |
|                 | `other(tag)`     | delete `tag` and its associated text from `clname`                  |
|                 | `allothers`      | delete all entries from `clname` that have been set using `other()` |

| measures\_options                                              |                        | Description                                                                           |
|----------------------------------------------------------------|------------------------|---------------------------------------------------------------------------------------|
| \*                                                             | `compare(numlist)`     | use `numlist` as the comparison observations                                          |
| \*                                                             | `generate(newvarlist)` | create `newvarlist` variables                                                         |
|                                                                | `measure`              | (dis)similarity measure; default is `L2`                                              |
|                                                                | `propvars`             | interpret observations implied by `if` and `in` as proportions of binary observations |
|                                                                | `propcompares`         | interpret comparison observations as proportions of binary observations               |
| \* `compare(numlist)` and `generate(newvarlist)` are required. |                        |                                                                                       |
