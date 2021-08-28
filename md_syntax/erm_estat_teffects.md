## Syntax

`estat teffects` \[`, options`\]

| Options |                                                                                                            | Description                                                                                               |
|---------|------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
|         | `ate`                                                                                                      | estimate average treatment effect; the default                                                            |
|         | `atet`                                                                                                     | estimate average treatment effect on the treated                                                          |
|         | `pomean`                                                                                                   | estimate potential-outcome mean                                                                           |
|         | `tlevel(numlist)`                                                                                          | calculate treatment effects or potential-outcome means for specified treatment levels                     |
|         | `outlevel(numlist)`                                                                                        | calculate treatment effects or potential-outcome means for specified levels of ordinal dependent variable |
|         | `subpop(subspec)`                                                                                          | estimate for subpopulation                                                                                |
|         | `level(#)`                                                                                                 | set confidence level; default is `level(95)`                                                              |
|         | [<var class="command">display_options</var><strong></strong>](#display_options) | control columns and column formats, row spacing, line width and factor-variable labeling                  |
