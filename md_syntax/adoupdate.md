## Syntax

`adoupdate` \[`pkglist`\] \[`, options`\]

| Options |                | Description                                                                                                                                                        |
|---------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|         | `update`       | perform update; default is to list packages that have updates, but not to update them                                                                              |
|         | `all`          | include packages that might have updates; default is to list or update only packages that are known to have updates                                                |
|         | `ssconly`      | check only packages obtained from SSC; default is to check all installed packages                                                                                  |
|         | `dir(dir)` | check packages installed in `dir`; default is to check those installed in [<strong>PLUS</strong>](http://www.stata.com/help.cgi?sysdir) |
|         | `verbose`      | provide output to assist in debugging network problems                                                                                                             |
