## Syntax

`append using filename` \[`filename ...`\] \[`, options`\]

You may enclose `filename` in double quotes and must do so if `filename`
contains blanks or other special characters.

| Options |                    | Description                                                 |
|---------|--------------------|-------------------------------------------------------------|
|         | `generate(newvar)` | `newvar` marks source of resulting observations             |
|         | `keep(varlist)`    | keep specified variables from appending dataset(s)          |
|         | `nolabel`          | do not copy value-label definitions from dataset(s) on disk |
|         | `nonotes`          | do not copy notes from dataset(s) on disk                   |
|         | `force`            | append string to numeric or numeric to string without error |
