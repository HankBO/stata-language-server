## Syntax

Display the current setting

`spset`

Set data with shapefiles

`spshape2dta` ...<span options="26">{space 26}_(see
[<strong>[SP]</strong> spshape2dta](http://www.stata.com/help.cgi?spshape2dta))

Set data without shapefiles

`spset idvar` \[`,`
[<var class="command">options</var><strong></strong>](#options_table)\]

Modify how data are set with shapefiles

`spset` \[`idvar`\]`, modify`
\[[<var class="command">shpmodoptions</var><strong></strong>](#shpmodoptions)\]

Modify how data are set without shapefiles

`spset, modify`
\[[<var class="command">modoptions</var><strong></strong>](#modoptions)\]

Clear the setting

`spset, clear`

`idvar` is an existing, numeric variable that uniquely identifies the
geographic units, meaning the observations in cross-sectional data and
the panels in panel data.

`shapefile` refers to a Stata-format shapefile, specified with or
without the `.dta` suffix. Such files usually have names of the form
`name_shp.dta`.

| Options |                      | Description                                             |
|---------|----------------------|---------------------------------------------------------|
|         | `coord(xvar yvar)`   | designate `xvar` and `yvar` as the location coordinates |
|         | `coordsys(coordsys)` | specify how coordinates are interpreted                 |

| shpmodoptions |                      | Description                                        |
|---------------|----------------------|----------------------------------------------------|
|               | `coordsys(coordsys)` | change how coordinates are interpreted             |
|               | `noshpfile`          | break link with shapefile                          |
|               | `replace`            | replace current geographic identifier with `idvar` |

| modoptions |                      | Description                                         |
|------------|----------------------|-----------------------------------------------------|
|            | `coord(xvar yvar)`   | replace location coordinates with `xvar` and `yvar` |
|            | `coordsys(coordsys)` | change how coordinates are interpreted              |
|            | `nocoord`            | clear coordinate settings                           |
|            | `shpfile(shapefile)` | establish link to shapefile                         |
