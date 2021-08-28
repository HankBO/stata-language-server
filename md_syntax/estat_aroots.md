## Syntax

`estat aroots` \[`, options`\]

| Options                                 |                         | Description                                                                                                                                                           |
|-----------------------------------------|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                         | `nograph`               | suppress graph of the eigenvalues for the companion matrices                                                                                                          |
|                                         | `dlabel`                | label eigenvalues with the distance from the unit circle                                                                                                              |
|                                         | `modlabel`              | label eigenvalues with the modulus                                                                                                                                    |
| Grid                                    |                         |                                                                                                                                                                       |
|                                         | `nogrid`                | suppress polar grid circles                                                                                                                                           |
|                                         | `pgrid(`\[...\]`)`    | specify radii and appearance of polar grid circles; see `Options` for details                                                                                         |
| Plot                                    |                         |                                                                                                                                                                       |
|                                         | `marker_options`        | change look of markers (color, size, etc.)                                                                                                                            |
| Reference unit circle                   |                         |                                                                                                                                                                       |
|                                         | `rlopts(cline_options)` | affect rendition of reference unit circle                                                                                                                             |
| Y axis, X axis, Titles, Legend, Overall |                         |                                                                                                                                                                       |
|                                         | `twoway_options`        | any options other than `by()` documented in [<strong>[G-3]</strong> <em>twoway_options</em>](http://www.stata.com/help.cgi?twoway_options) |
