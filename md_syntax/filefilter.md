## Syntax

`filefilter oldfile newfile ,`  
{ `from(oldpattern) to(newpattern)`  
<span options="2">{space 2}_\| `ascii2ebcdic` \| `ebcdic2ascii`
} \[`options`\]

where `oldpattern` and `newpattern` for ASCII characters are

`"string"` or {cmd None}`string`{cmd None}

|                                                                                          |                                       |
|------------------------------------------------------------------------------------------|---------------------------------------|
| `string`<span options="2">{space 2}_`:= [char[char[char[...]]]]` |                                       |
| `char`<span options="4">{space 4}_`:= regchar | code`                        |                                       |
| `regchar :=` ASCII 32-91, 93-127, or                                                   |                                       |
| extended ASCII 128, 161-255; excludes '\\'                                               |                                       |
| `code`<span options="4">{space 4}_`:= \BS`                                       | backslash                             |
| `\r`                                                                                     | carriage return                       |
| `\n`                                                                                     | newline                               |
| `\t`                                                                                     | tab                                   |
| `\M`                                                                                     | Classic Mac EOL, or \\r               |
| `\W`                                                                                     | Windows EOL, or \\r\\n                |
| `\U`                                                                                     | Unix or Mac EOL, or \\n               |
| `\LQ`                                                                                    | left single quote, \`                 |
| `\RQ`                                                                                    | right single quote, '                 |
| `\Q`                                                                                     | double quote, "                       |
| `\$`                                                                                     | dollar sign, $                        |
| `\###d`                                                                              | 3-digit \[0-9\] decimal ASCII         |
| `\##h`                                                                               | 2-digit \[0-9,A-F\] hexadecimal ASCII |

| Options                                                                                                        |                    | Description                                         |
|----------------------------------------------------------------------------------------------------------------|--------------------|-----------------------------------------------------|
| \*                                                                                                             | `from(oldpattern)` | find `oldpattern` to be replaced                    |
| \*                                                                                                             | `to(newpattern)`   | use `newpattern` to replace occurrences of `from()` |
| \*                                                                                                             | `ascii2ebcdic`     | convert file from ASCII to EBCDIC                   |
| \*                                                                                                             | `ebcdic2ascii`     | convert file from EBCDIC to ASCII                   |
|                                                                                                                | `replace`          | replace `newfile` if it already exists              |
| \* Both `from(oldpattern)` and `to(newpattern)` are required, or `ascii2ebcdic` or `ebcdic2ascii` is required. |                    |                                                     |
