## Syntax

`real scalar`<span class="nowrap"> _ `fopen(string scalar fn,`
`mode)`

`real scalar`<span class="nowrap"> _ `fopen(string scalar fn,`
`mode, public)`

`real scalar`<span class="nowrap"> _
`_fopen(string scalar fn, mode)`

`real scalar`<span class="nowrap"> _
`_fopen(string scalar fn, mode, public)`

where

[<var class="command">mode</var><strong></strong>](#mode):
`string scalar` containing "`r`", "`w`", "`rw`", or "`a`"

[<var class="command">public</var><strong></strong>](#public):
optional `real scalar` containing zero or nonzero

In what follows, `fh` is the value returned by `fopen()` or `_fopen()`:

`void`<span class="nowrap"> _ `fclose(fh)`

`real scalar`<span class="nowrap"> _ `_fclose(fh)`

`string scalar`<span class="nowrap"> _ `fget(fh)`

`string scalar _fget(fh)`

`string scalar`<span class="nowrap"> _ `fgetnl(fh)`

`string scalar _fgetnl(fh)`

`string scalar`<span class="nowrap"> _ `fread(fh,`
`real scalar len)`

`string scalar _fread(fh, real scalar len)`

`void`<span class="nowrap"> _ `fput(fh, string scalar s)`

`real scalar`<span class="nowrap"> _ `_fput(fh,`
`string scalar s)`

`void`<span class="nowrap"> _ `fwrite(fh,`
`string scalar s)`

`real scalar`<span class="nowrap"> _ `_fwrite(fh,`
`string scalar s)`

`matrix`<span class="nowrap"> _ `fgetmatrix(fh`
\[`, real scalar isstrict`\]`)`

`matrix`<span class="nowrap"> _ `_fgetmatrix(fh`
\[`, real scalar isstrict`\]`)`

`void`<span class="nowrap"> _ `fputmatrix(fh,`
`transmorphic matrix X)`

`real scalar`<span class="nowrap"> _ `_fputmatrix(fh,`
`transmorphic matrix X)`

`real scalar`<span class="nowrap"> _ `fstatus(fh)`

`real scalar`<span class="nowrap"> _ `ftell(fh)`

`real scalar`<span class="nowrap"> _ `_ftell(fh)`

`void`<span class="nowrap"> _ `fseek(fh,`
`real scalar offset, real scalar whence)`

`real scalar`<span class="nowrap"> _ `_fseek(fh,`
`real scalar offset, real scalar whence)`

(`whence` is coded -1, 0, or 1, meaning from start of file, from current
position, or from end of file; `offset` is signed: positive values mean
after `whence` and negative values mean before)

`void`<span class="nowrap"> _ `ftruncate(fh)`

`real scalar`<span class="nowrap"> _ `_ftruncate(fh)`
