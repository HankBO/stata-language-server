## Syntax

`graph export newfilename.suffix` \[`, options`\]

`options`

Description

------------------------------------------------------------------------

`name(windowname)`

name of Graph window to export

`as(fileformat)`

desired format of output

`replace`

`newfilename` may already exist

`override_options`

override defaults in conversion

------------------------------------------------------------------------

If `as()` is not specified, the output format is determined by the
suffix of `newfilename.suffix`:

Implied

`suffix`

option<span style="padding-left: 17.5rem;">_Output format

------------------------------------------------------------------------

`.ps`

`as(ps)`<span style="padding-left: 17.5rem;">_PostScript

`.eps`

`as(eps)`<span style="padding-left: 17.5rem;">_EPS (Encapsulated
PostScript)

`.svg`

`as(svg)`<span style="padding-left: 17.5rem;">_SVG (Scalable
Vector Graphics)

`.wmf`

`as(wmf)`<span style="padding-left: 17.5rem;">_Windows Metafile

`.emf`

`as(emf)`<span style="padding-left: 17.5rem;">_Windows Enhanced
Metafile

`.pdf`

`as(pdf)`<span style="padding-left: 17.5rem;">_PDF (Portable
Document Format)

`.png`

`as(png)`<span style="padding-left: 17.5rem;">_PNG (Portable
Network Graphics)

`.tif`

`as(tif)`<span style="padding-left: 17.5rem;">_TIFF (Tagged Image
File Format)

` other`

must specify `as()`

------------------------------------------------------------------------

`ps`, `eps`, and `svg` are available for all versions of Stata; ` png`
and `tif` are available for all versions of Stata except Stata(console);
and `wmf` and `emf` are available only for Stata for Windows.

`override_options`

Description

------------------------------------------------------------------------

`ps_options`

when exporting to `ps`

`eps_options`

when exporting to `eps`

`svg_options`

when exporting to `svg`

`tif_options`

when exporting to `tif`

`png_options`

when exporting to `png`

------------------------------------------------------------------------

There are no override\_options for the `pdf` format.
