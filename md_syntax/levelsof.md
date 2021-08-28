## Syntax

`levelsof`
[varname](http://www.stata.com/help.cgi?varname)
_\[`if`\] \[`in`\]_ \[`, options`\]

| Options |                       | Description                                                                                                          |
|---------|-----------------------|----------------------------------------------------------------------------------------------------------------------|
|         | `clean`               | display string values without compound double quotes                                                                 |
|         | `local(macname)`      | insert the list of values in the local macro `macname`                                                               |
|         | `missing`             | include missing values of [varname](http://www.stata.com/help.cgi?varname) in calculation |
|         | `separate(separator)` | separator to serve as punctuation for the values of returned list; default is a space                                |
|         | `matcell(matname)`    | save frequencies of distinct values in `matname`                                                                     |
|         | `matrow(matname)`     | save distinct values of [varname](http://www.stata.com/help.cgi?varname) in `matname`     |
|         | `hexadecimal`         | use hexadecimal format for numerical values                                                                          |
