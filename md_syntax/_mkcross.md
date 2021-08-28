## Syntax

`_mkcross`
[varlist](http://www.stata.com/help.cgi?varlist)
_\[`if`\] \[`in`\]_, `options`

| Options |                        | Description                                                                                  |
|---------|------------------------|----------------------------------------------------------------------------------------------|
|         | `generate(newvar)`     | required; name of the value-labeled "crossed" variable identifying combinations of `varlist` |
|         | `labelname(name)`      | name of value label for `newvar`; default is `newvar`                                        |
|         | `missing`              | treat missing values in crossing variables as ordinary values                                |
|         | `keyword`              | code missing values with keywords                                                            |
|         | `strok`                | string variables are allowed                                                                 |
|         | `coding(matname)`      | returns a coding matrix                                                                      |
|         | `length(#)`            | truncate codes of crossing variables at length `#`                                           |
|         | `length:(minimal)`   | generate minimal length unique codes for crossing variables                                  |
|         | `sep(str)`             | separator between codes of crossing variables; default `sep("_")`                            |
|         | `maxlength(#)`         | maximum crossed code length; default is `maxlength(12)`                                      |
|         | `start(#)`             | starting index for group values                                                              |
|         | `edit:(space:)`      | drop spaces from coding strings                                                              |
|         | `edit:(first:)`      | derive codes from first word in coding string                                                |
|         | `edit:(vowel:)`      | drop vowels and spaces from coding string                                                    |
|         | `case(lower)`        | convert coding strings to lower case                                                         |
|         | `case(upper)`        | convert coding strings to upper case                                                         |
|         | `case(first)`        | capitalize each word in coding strings                                                       |
|         | `report:(variables)` | display the coding for the nonnumeric crossing variables                                     |
|         | `report:(crossed)`   | display the codes (value labels) for the crossed variable                                    |
|         | `report:(all)`       | display the coding of the crossing and crossed variables                                     |
|         | `truncate(#)`          | maximum length for descriptions in crossed variable report table                             |
