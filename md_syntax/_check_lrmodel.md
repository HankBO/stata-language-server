## Syntax

`_check_lrmodel` \[`command_name`\] \[`, options`\]

| Options |                                | Description                                                                                   |
|---------|--------------------------------|-----------------------------------------------------------------------------------------------|
|         | `noskip`                       | specify that `noskip` is not allowed                                                          |
|         | `noconstant`                   | specify that `noconstant` is not allowed                                                      |
|         | `constraints(constraints)` | specify that `constraints()` is not allowed                                                   |
|         | `options(opts)`                | specify that user-defined `opts` are not allowed                                              |
|         | `robust`                       | specify that `robust` is not allowed                                                          |
|         | `cluster(clustvar)`            | specify that `cluster(clustvar)` is not allowed                                               |
|         | `vce(passthru)`                | specify that `passthru` (`robust` or `cluster`) is not allowed                                |
|         | `vcetype(vce_type)`            | specify that `vce_type` (`robust`, `cluster`, `bootstrap`, or `jackknife`) is not allowed     |
|         | `prefix(prefix_type)`          | specify that `prefix_type` (`jackknife`, `bootstrap`, `svy`, or `mi estimate`) is not allowed |
