## Syntax

Verify that variable contains defined codes

`icd10 check`
[varname](http://www.stata.com/help.cgi?varname)
_\[`if`\] \[`in`\]_ \[`, checkopts`\]

Clean variable and verify format of codes

`icd10 clean`
[varname](http://www.stata.com/help.cgi?varname)
_\[`if`\] \[`in`\]_`,` <span options="-(">{c
-(}_`generate(newvar)` \| `replace`<span options=")-">{c
)-}_ \[`cleanopts`\]

Generate new variable from existing variable

`icd10 generate`
[newvar](http://www.stata.com/help.cgi?newvar)
`=`
[varname](http://www.stata.com/help.cgi?varname)
_\[`if`\] \[`in`\]_`,` <span options="-(">{c
-(}_`category` \| `short`}
\[`check`\]

`icd10 generate`
[newvar](http://www.stata.com/help.cgi?newvar)
`=`
[varname](http://www.stata.com/help.cgi?varname)
_\[`if`\] \[`in`\]_`, description`
\[`genopts`\]

`icd10 generate`
[newvar](http://www.stata.com/help.cgi?newvar)
`=`
[varname](http://www.stata.com/help.cgi?varname)
_\[`if`\] \[`in`\]_`, range(codelist)`
\[`check`\]

Display code descriptions

`icd10 lookup codelist` \[`, version(#)`\]

Search for codes from descriptions

`icd10 search` \[`"`\]`text`\[`"`\] \[\[`"`\]`text`\[`"`\] `...`\]
\[`, searchopts`\]

Display ICD-10 version

`icd10 query`

`codelist` is one of the following:

|                           |                           |
|---------------------------|---------------------------|
| `icd10code`               | (the particular code)     |
| `icd10code*`            | (all codes starting with) |
| `icd10code/icd10code` | (the code range)          |

or any combination of the above, such as `A27.0 G40* Y60/Y69.9`.

| checkopts |                    | Description                                              |
|-----------|--------------------|----------------------------------------------------------|
|           | `fmtonly`          | check only format of the codes                           |
|           | `summary`          | frequency of each invalid or undefined code              |
|           | `list`             | list observations with invalid or undefined ICD-10 codes |
|           | `generate(newvar)` | create new variable marking invalid codes                |
|           | `version(#)`       | year to check codes against; default is `version(2016)`  |

| cleanopts                                                                                                                                                                                                                                                                                                |                    | Description                                                              |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------|--------------------------------------------------------------------------|
| \*                                                                                                                                                                                                                                                                                                       | `generate(newvar)` | create new variable containing cleaned codes                             |
| \*                                                                                                                                                                                                                                                                                                       | `replace`          | replace existing codes with the cleaned codes                            |
|                                                                                                                                                                                                                                                                                                          | `check`            | check that variable contains ICD-10 codes before cleaning                |
|                                                                                                                                                                                                                                                                                                          | `nodots`           | format codes without a period                                            |
|                                                                                                                                                                                                                                                                                                          | `pad`              | add space to the right of three-character codes                          |
|                                                                                                                                                                                                                                                                                                          | `pad`              | add spaces to the right of the code; must specify `addcode(begin)`       |
|                                                                                                                                                                                                                                                                                                          | `nodots`           | format codes without a period; must specify `addcode()`                  |
|                                                                                                                                                                                                                                                                                                          | `check`            | check that variable contains ICD-10 codes before generating new variable |
|                                                                                                                                                                                                                                                                                                          | `version(#)`       | select description from year `#`; default is `version(2016)`             |
| \* Either `generate()` or `replace` is required. <span options="genopts">{marker genopts}_{nobreak None} <span options="18">{synoptset 18}_{nobreak None} {synopthdr None:genopts} {synoptline None} {synopt None}`addcode(begin`\|`end)`add code to the beginning or end of the description |                    |                                                                          |

| searchopts |              | Description                                      |
|------------|--------------|--------------------------------------------------|
|            | `or`         | match any keyword                                |
|            | `matchcase`  | match case of keywords                           |
|            | `version(#)` | select description from year `#`; default is all |
