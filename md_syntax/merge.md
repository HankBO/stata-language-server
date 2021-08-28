## Syntax

One-to-one merge on specified key variables

`merge 1:1`
[varlist](http://www.stata.com/help.cgi?varlist)
`using filename` \[`, options`\]

Many-to-one merge on specified key variables

`merge m:1`
[varlist](http://www.stata.com/help.cgi?varlist)
`using filename` \[`, options`\]

One-to-many merge on specified key variables

`merge 1:m`
[varlist](http://www.stata.com/help.cgi?varlist)
`using filename` \[`, options`\]

Many-to-many merge on specified key variables

`merge m:m`
[varlist](http://www.stata.com/help.cgi?varlist)
`using filename` \[`, options`\]

One-to-one merge by observation

`merge 1:1 _n using filename` \[`, options`\]

| Options                                     |                                                                                                        | Description                                                                                                |
|---------------------------------------------|--------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| Options                                     |                                                                                                        |                                                                                                            |
|                                             | `keepusing(varlist)`                                                                                   | variables to keep from using data; default is all                                                          |
|                                             | `generate(newvar)`                                                                                     | name of new variable to mark merge results; default is `_merge`                                            |
|                                             | `nogenerate`                                                                                           | do not create `_merge` variable                                                                            |
|                                             | `nolabel`                                                                                              | do not copy value-label definitions from using                                                             |
|                                             | `nonotes`                                                                                              | do not copy notes from using                                                                               |
|                                             | `update`                                                                                               | update missing values of same-named variables in master with values from using                             |
|                                             | `replace`                                                                                              | replace all values of same-named variables in master with nonmissing values from using (requires `update`) |
|                                             | `noreport`                                                                                             | do not display match result summary table                                                                  |
|                                             | `force`                                                                                                | allow string/numeric variable type mismatch without error                                                  |
| Results                                     |                                                                                                        |                                                                                                            |
|                                             | `assert(`[<var class="command">results</var><strong></strong>](#results)`)` | specify required match results                                                                             |
|                                             | `keep(`[<var class="command">results</var><strong></strong>](#results)`)`   | specify which match results to keep                                                                        |
|                                             | `sorted`                                                                                               | do not sort; datasets already sorted                                                                       |
| `sorted` does not appear in the dialog box. |                                                                                                        |                                                                                                            |
