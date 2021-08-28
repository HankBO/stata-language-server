## Syntax

`conren`

`conren style #`

`conren ul #`

`conren test`

`conren clear`

`set conren`

`set conren clear`

`set conren` \[ `sf` \| `bf` \| `it` \] <span options="-(">{c
-(}_ `result` \| \[`txt`\|`text`\] \| `input` \| `error` \| `link`
\| `hilite` } \[ `char` \[ `char ...` \]
\]

`set conren` <span options="-(">{char -(}_ `ulon` \| `uloff`
<span options=")-">{char )-}_ \[ `char` \[ `char ...` \] \]

`set conren reset` \[ `char` \[ `char ...` \] \]

where `char` is

<span options="-(">{char -(}_ `any_character` \| `<#>` <span
options=")-">{char )-}_

Note: This command is designed for Stata for Unix and, in particular,
the Stata you launch by typing `stata`, not `xstata`; also known as
Stata(console) or the non-GUI version of Stata. However, in windowed
versions of Stata, `conren` produces the current rendition table (the
output from `conren test`) in the Results window.
