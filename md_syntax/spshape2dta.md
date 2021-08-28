## Syntax

`spshape2dta name` \[`, options`\]

| Options |                 | Description                                                                                             |
|---------|-----------------|---------------------------------------------------------------------------------------------------------|
|         | `clear`         | clear existing data from memory                                                                         |
|         | `replace`       | if `name.dta` or `name_shp.dta` exists, replace them                                                |
|         | `saving(name2)` | create new files named `name2.dta` and `name2_shp.dta` instead of `name.dta` and `name_shp.dta` |

`spshape2dta` translates files `name.shp` and `name.dbf`. They must
be in the current directory.

`spshape2dta` creates files `name.dta` and `name_shp.dta`. They will
be created in the current directory. The data in memory, if any, remain
unchanged.
