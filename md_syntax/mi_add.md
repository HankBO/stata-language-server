## Syntax

`mi add`
[varlist](http://www.stata.com/help.cgi?varlist)
`using filename` \[`, options`\]

| Options |                  | Description                                                                                                                  |
|---------|------------------|------------------------------------------------------------------------------------------------------------------------------|
|         | `assert(master)` | assert all observations found in master                                                                                      |
|         | `assert(match)`  | assert all observations found in master and in using                                                                         |
|         | `noupdate`       | see **[<strong>[MI] noupdate option</strong>](http://www.stata.com/help.cgi?mi_noupdate_option)** |

Notes:

1\. Jargon:  
match variables = `varlist`, variables on which match performed  
<span class="nowrap"> _master = data in memory  
<span class="nowrap"> _using = data on disk (`filename`)

2\. Master must be `mi set`.

3\. Using must be `mi set`.

4\. `filename` must be enclosed in double quotes if `filename` contains
blanks or other special characters.
