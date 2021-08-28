## Syntax

`runtest`
[varname](http://www.stata.com/help.cgi?varname)
\[`in`\] \[`, options`\]

| options |                | Description                                                                                                |
|---------|----------------|------------------------------------------------------------------------------------------------------------|
|         | `continuity`   | continuity correction                                                                                      |
|         | `drop`         | ignore values equal to the threshold                                                                       |
|         | `split`        | randomly split values equal to the threshold as above or below the threshold; default is to count as below |
|         | `mean`         | use mean as threshold; default is median                                                                   |
|         | `threshold(#)` | assign arbitrary threshold; default is median                                                              |
