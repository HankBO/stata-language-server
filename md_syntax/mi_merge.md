## Syntax

`mi merge 1:1`
[varlist](http://www.stata.com/help.cgi?varlist)
`using filename` \[`, options`\]

`mi merge m:1`
[varlist](http://www.stata.com/help.cgi?varlist)
`using filename` \[`, options`\]

`mi merge 1:m`
[varlist](http://www.stata.com/help.cgi?varlist)
`using filename` \[`, options`\]

`mi merge m:m`
[varlist](http://www.stata.com/help.cgi?varlist)
`using filename` \[`, options`\]

| Options |                                                                                         | Description                                                                                                                  |
|---------|-----------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|
| Options |                                                                                         |                                                                                                                              |
|         | `generate(`[newvar](http://www.stata.com/help.cgi?newvar)`)` | create `newvar` recording how observations matched                                                                           |
|         | `nolabel`                                                                               | do not copy value-label definitions from using                                                                               |
|         | `nonotes`                                                                               | do not copy notes from using                                                                                                 |
|         | `noreport`                                                                              | do not display result summary table                                                                                          |
|         | `force`                                                                                 | allow string/numeric variable type mismatch without error                                                                    |
| Results |                                                                                         |                                                                                                                              |
|         | `assert(results)`                                                                   | require observations to match as specified                                                                                   |
|         | `keep(results)`                                                                     | results to keep                                                                                                              |
|         | `noupdate`                                                                              | see **[<strong>[MI] noupdate option</strong>](http://www.stata.com/help.cgi?mi_noupdate_option)** |

Notes:

1\. Jargon:  
match variables = `varlist`, variables on which match performed  
<span class="nowrap"> _master = data in memory  
<span class="nowrap"> _using = data on disk (`filename`)

2\. Master must be `mi set`; using may be `mi set`.

3\. `mi merge` is syntactically and logically equivalent to
**[<strong>merge</strong>](http://www.stata.com/help.cgi?merge)**.

4\. `mi merge` syntactically differs from `merge` in that the
`nogenerate`, `sorted`, `keepusing()`, `update`, and `replace` options
are not allowed. Also, no `_merge` variable is created unless the
`generate()` option is specified.

5\. `filename` must be enclosed in double quotes if `filename` contains
blanks or other special characters.
