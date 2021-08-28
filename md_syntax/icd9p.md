## Syntax

Verify that variable contains defined codes

`icd9p check`
[varname](http://www.stata.com/help.cgi?varname)
_\[`if`\] \[`in`\]_ \[`, any list`
`generate(newvar)`\]

Clean variable and verify format of codes

`icd9p clean`
[varname](http://www.stata.com/help.cgi?varname)
_\[`if`\] \[`in`\]_ \[`, dots pad`\]

Generate new variable from existing variable

`icd9p generate`
[newvar](http://www.stata.com/help.cgi?newvar)
`=`
[varname](http://www.stata.com/help.cgi?varname)
_\[`if`\] \[`in`\]_`, category`

`icd9p generate`
[newvar](http://www.stata.com/help.cgi?newvar)
`=`
[varname](http://www.stata.com/help.cgi?varname)
_\[`if`\] \[`in`\]_`, description` \[`long`
`end`\]

`icd9p generate`
[newvar](http://www.stata.com/help.cgi?newvar)
`=`
[varname](http://www.stata.com/help.cgi?varname)
_\[`if`\] \[`in`\]_`, range(codelist)`

Display code descriptions

`icd9p lookup codelist`

Search for codes from descriptions

`icd9p search` \[`"`\]`text`\[`"`\] \[\[`"`\]`text`\[`"`\] `...`\]
\[`, or`\]

Display ICD-9 code source

`icd9p query`

`codelist` is

|                         |                           |
|-------------------------|---------------------------|
| `icd9code`              | (the particular code)     |
| `icd9code*`           | (all codes starting with) |
| `icd9code/icd9code` | (the code range)          |

or any combination of the above, such as `50.21 37.7* 88.71/88.79`.
`icd9codes` must be typed with leading 0s. For example, type `01`;
typing `1` will result in an error.
