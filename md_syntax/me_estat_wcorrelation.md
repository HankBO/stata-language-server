## Syntax

`estat wcorrelation` \[`, options`\]

| options |                                                                                                                                 | Description                                                                                                                   |
|---------|---------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
|         | `at(at_spec)`                                                                                                                   | specify the cluster for which you want the correlation matrix; default is the first two-level cluster encountered in the data |
|         | `all`                                                                                                                           | display correlation matrix for all the data                                                                                   |
|         | `covariance`                                                                                                                    | display the covariance matrix instead of the correlation matrix                                                               |
|         | `list`                                                                                                                          | list the data corresponding to the correlation matrix                                                                         |
|         | `nosort`                                                                                                                        | list the rows and columns of the correlation matrix in the order they were originally present in the data                     |
|         | `iterate(#)`                                                                                                                    | maximum number of iterations to compute random effects; default is `iterate(50)`; only for use after `menl`                   |
|         | `tolerance(#)`                                                                                                                  | convergence tolerance when computing random effects; default is `tolerance(1e-4)`; only for use after `menl`                  |
|         | `format(%fmt)`                                                                                                                  | set the display format; default is `format(%6.3f)`                                                                            |
|         | [<var class="command">matlist_options</var><strong></strong>](http://www.stata.com/help.cgi?matlist) | style and formatting options that control how matrices are displayed                                                          |
