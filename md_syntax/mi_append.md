## Syntax

`mi append using filename` \[`, options`\]

| Options |                    | Description                                                                                                                  |
|---------|--------------------|------------------------------------------------------------------------------------------------------------------------------|
|         | `generate(newvar)` | create `newvar`; 0=master, 1=using                                                                                           |
|         | `nolabel`          | do not copy value labels from using                                                                                          |
|         | `nonotes`          | do not copy notes from using                                                                                                 |
|         | `force`            | string &lt;-&gt; numeric not type mismatch error                                                                             |
|         | `noupdate`         | see **[<strong>[MI] noupdate option</strong>](http://www.stata.com/help.cgi?mi_noupdate_option)** |

Notes:

1\. Jargon:  
master = data in memory  
<span class="nowrap"> _using = data on disk (`filename`)

2\. Master must be `mi set`; using may be `mi set`.

3\. `mi append` is logically equivalent to
**[<strong>append</strong>](http://www.stata.com/help.cgi?append)**.
The resulting data have `M` = max(`M_master`, `M_using)`, not their sum.
See
**[<strong>[MI] mi add</strong>](http://www.stata.com/help.cgi?mi_add)**
to append imputations holding `m`=0 constant.

4\. `mi append` syntactically differs from `append` in that multiple
using files may not be specified and the `keep(varlist)` option is
not allowed.

5\. `filename` must be enclosed in double quotes if `filename` contains
blanks or other special characters.
