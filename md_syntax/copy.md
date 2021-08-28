## Syntax

`copy filename1 filename2` \[`, options`\]

`filename1` may be a filename or a URL. `filename2` may be the name of a
file or a directory. If `filename2` is a directory name, `filename1`
will be copied to that directory. `filename2` may not be a URL.

Note: Double quotes may be used to enclose the filenames, and the quotes
must be used if the filename contains embedded blanks.

| Options                                      |           | Description                                                            |
|----------------------------------------------|-----------|------------------------------------------------------------------------|
|                                              | `public`  | make `filename2` readable by all                                       |
|                                              | `text`    | interpret `filename1` as text file and translate to native text format |
|                                              | `replace` | may overwrite `filename2`                                              |
| `replace` does not appear in the dialog box. |           |                                                                        |
