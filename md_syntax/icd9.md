## Syntax

Verify that variable contains defined codes

`icd9 check`
[varname](http://www.stata.com/help.cgi?varname)
_\[`if`\] \[`in`\]_ \[`, any list`
`generate(newvar)`\]

Clean variable and verify format of codes

`icd9 clean`
[varname](http://www.stata.com/help.cgi?varname)
_\[`if`\] \[`in`\]_ \[`, dots pad`\]

Generate new variable from existing variable

`icd9 generate`
[newvar](http://www.stata.com/help.cgi?newvar)
`=`
[varname](http://www.stata.com/help.cgi?varname)
_\[`if`\] \[`in`\]_`, category`

`icd9 generate`
[newvar](http://www.stata.com/help.cgi?newvar)
`=`
[varname](http://www.stata.com/help.cgi?varname)
_\[`if`\] \[`in`\]_`, description` \[`long`
`end`\]

`icd9 generate`
[newvar](http://www.stata.com/help.cgi?newvar)
`=`
[varname](http://www.stata.com/help.cgi?varname)
_\[`if`\] \[`in`\]_`, range(codelist)`

Display code descriptions

`icd9 lookup codelist`

Search for codes from descriptions

`icd9 search` \[`"`\]`text`\[`"`\] \[\[`"`\]`text`\[`"`\] `...`\]
\[`, or`\]

Display ICD-9 code source

`icd9 query`

`codelist` is

|                         |                           |
|-------------------------|---------------------------|
| `icd9code`              | (the particular code)     |
| `icd9code*`           | (all codes starting with) |
| `icd9code/icd9code` | (the code range)          |

or any combination of the above, such as `001* 018/019 E* 018.02`.
`icd9codes` must be typed with leading 0s. For example, type `001`;
typing `1` will result in an error.
