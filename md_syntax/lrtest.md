## Syntax

`lrtest modelspec1` \[`modelspec2`\] \[`, options`\]

`modelspec1` and `modelspec2` specify the restricted and unrestricted
model in any order. `modelspec#` is

`name`|`.`|`(namelist)`

`name` is the name under which estimation results were stored using
[<strong>estimates store</strong>](http://www.stata.com/help.cgi?estimates%20store),
and "`.`" refers to the last estimation results, whether or not these
were already stored. If `modelspec2` is not specified, the last
estimation result is used; this is equivalent to specifying `modelspec2`
as "`.`".

If `namelist` is specified for a composite model, `modelspec1` and
`modelspec2` cannot have names in common; for example,
`lrtest (A B C) (C D E)` is not allowed because both model
specifications include `C`.

| Options |         | Description                                                        |
|---------|---------|--------------------------------------------------------------------|
|         | `stats` | display statistical information about the two models               |
|         | `dir`   | display descriptive information about the two models               |
|         | `df(#)` | override the automatic degrees-of-freedom calculation; seldom used |
|         | `force` | force testing even when apparently invalid                         |
