## Syntax

`hexdump filename` \[`, options`\]

| Options |              | Description                                                                                             |
|---------|--------------|---------------------------------------------------------------------------------------------------------|
|         | `analyze`    | display a report on the dump rather than the dump itself                                                |
|         | `tabulate`   | display a full tabulation of the ASCII and extended ASCII characters in the `analyze` report            |
|         | `noextended` | do not display printable extended ASCII characters                                                      |
|         | `results`    | store results containing the frequency with which each character code was observed; programmer's option |
|         | `from(#)`    | dump or analyze first byte of the file; default is to start at first byte, `from(0)`                    |
|         | `to(#)`      | dump or analyze last byte of the file; default is to continue to the end of the file                    |
