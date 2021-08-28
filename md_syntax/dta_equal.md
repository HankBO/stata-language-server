## Syntax

`dta_equal filename1 filename2` \[`, options`\]

`dta_equal`<span class="nowrap"> _`.`<span class="nowrap">
_`filename2` \[`, options`\]

| Options |                     | Description                                             |
|---------|---------------------|---------------------------------------------------------|
|         | `exclude(varnames)` | exclude `varnames` from comparison                      |
|         | `uniq1`             | exclude variables unique to `filename1` from comparison |
|         | `uniq2`             | exclude variables unique to `filename2` from comparison |
|         | `noneok`            | it is okay if no variables in common after exclusions   |
