## Syntax

`void st_freadsignature(fh, id, ver, f_ver`\[`,`
`f_byteorder, f_date`\]`)`

`void st_fwritesignature(fh, id, ver)`

`real scalar _st_freadsignature(fh, id, ver,`
`quietly,`  
`f_ver`\[`, f_byteorder, f_date`\]`)`

`real scalar _st_fwritesignature(fh, id, ver,`
`quietly)`

where

`input:fhreal scalarfopen()idstring scalarverreal scalarquietlyreal scalaroutput:f_verreal scalarf_byteorderreal scalar`

`(optional)`

`f_datereal scalar%tc`

`(optional)`
