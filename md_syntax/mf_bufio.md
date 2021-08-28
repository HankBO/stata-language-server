## Syntax

`colvector C = bufio()`

`real scalar`<span class="nowrap"> _ `bufbyteorder(C)`

`void`<span class="nowrap"> _ `bufbyteorder(C,`
`real scalar byteorder)`

`real scalar`<span class="nowrap"> _ `bufmissingvalue(C)`

`void`<span class="nowrap"> _ `bufmissingvalue(C,`
`real scalar version)`

`void`<span class="nowrap"> _ `bufput(C, B, offset,`
`bfmt, X)`

`scalar`<span class="nowrap"> _ `bufget(C, B, offset,`
`bfmt)`

`rowvector`<span class="nowrap"> _ `bufget(C, B,`
`offset, bfmt, c)`

`matrix`<span class="nowrap"> _ `bufget(C, B, offset,`
`bfmt, r, c)`

`void`<span class="nowrap"> _ `fbufput(C, fh, bfmt,`
`X)`

`scalar`<span class="nowrap"> _ `fbufget(C, fh, bfmt)`

`rowvector`<span class="nowrap"> _ `fbufget(C, fh,`
`bfmt, c)`

`matrix`<span class="nowrap"> _ `fbufget(C, fh, bfmt,`
`r, c)`

`real scalar`<span class="nowrap"> _
`bufbfmtlen(string scalar bfmt)`

`real scalar`<span class="nowrap"> _
`bufbfmtisnum(string scalar bfmt)`

where

`C`: `colvector` returned by `bufio()`

`B`: `string scalar` (buffer)

`offset`: `real scalar` (buffer position, starts at 0)

`fh`: file handle returned by
[<strong>fopen()</strong>](http://www.stata.com/help.cgi?mf_fopen)

`bfmt`: `string scalar` (binary format; see
[<strong>below</strong>](#bfmt))

`r`: `string scalar`

`c`: `string scalar`

`X`: value to be written; see
[<strong>Remarks</strong>](#remarks)

`bfmt` may contain

`bfmt`<span style="padding-left: 12.5rem;">_meaning

<span options="68">_

{nobreak None}

[<span data-options="-(">{c -(}_8|4<span data-options=")-">{c )-}_z<strong>%</strong>](#remarks6)

{nobreak None}

{nobreak None}

[<span data-options="-(">{c -(}_4|2|1<span data-options=")-">{c )-}_b[s|u]<strong>%</strong>](#remarks6)

{nobreak None}

[<strong>Stata</strong>](#Stata)

{nobreak None}

[<var class="command">#</var>s<strong>%</strong>](#remarks7)

{nobreak None}

{nobreak None}

[<var class="command">#</var>S<strong>%</strong>](#remarks7)

{nobreak None}

<span options="68">_
