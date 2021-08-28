## Syntax

`changeeol filename1 filename2, eol(platform)` \[`options`\]

`filename1` and `filename2` must be filenames.

Note: Double quotes may be used to enclose the filenames, and the quotes
must be used if the filename contains embedded blanks.

| Options                 |                   | Description                                                                 |
|-------------------------|-------------------|-----------------------------------------------------------------------------|
| \*                      | `eol(windows)`    | convert to Windows-style end-of-line characters (`\r\n`)                    |
| \*                      | `eol(dos)`        | synonym for `eol(windows)`                                                  |
| \*                      | `eol(unix)`       | convert to Unix-style end-of-line characters (`\n`)                         |
| \*                      | `eol(mac)`        | convert to Mac-style end-of-line characters (`\n`)                          |
| \*                      | `eol(classicmac)` | convert to classic Mac-style end-of-line characters (`\r`)                  |
|                         | `replace`         | overwrite `filename2`                                                       |
|                         | `force`           | force to convert `filename1` to `filename2` if `filename1` is a binary file |
| \* `eol()` is required. |                   |                                                                             |
