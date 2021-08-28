## Syntax

`unicode convertfile srcfilename destfilename` \[`, options`\]

`srcfilename` is a text file that is to be converted from a given
encoding and `destfilename` is the destination text file that will use a
different encoding.

| Options |                                 | Description                                                                       |
|---------|---------------------------------|-----------------------------------------------------------------------------------|
|         | `srcencoding(`\[`string`\]`)` | encoding of the source file; UTF-8 if not specified                               |
|         | `dstencoding(`\[`string`\]`)` | encoding of the destination file; UTF-8 if not specified                          |
|         | `srccallback(method)`       | what to do if source file contains invalid byte sequence(s)                       |
|         | `dstcallback(method)`       | what to do if destination encoding does not support characters in the source file |
|         | `replace`                       | replace the destination file if it exists                                         |

| method |              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|--------|--------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|        | `stop`       | specify that `unicode convertfile` stop with an error if an invalid character is encountered; the default                                                                                                                                                                                                                                                                                                                                                          |
|        | `skip`       | specify that `unicode convertfile` skip invalid characters                                                                                                                                                                                                                                                                                                                                                                                                         |
|        | `substitute` | specify that `unicode convertfile` substitute invalid characters with the destination encoding's substitute character during conversion; the substitute character for Unicode encodings is **\\ufffd**                                                                                                                                                                                                                                                             |
|        | `escape`     | specify that `unicode convertfile` replace any Unicode characters not supported in the destination encoding with an escaped string of the hex value of the Unicode code point. The string is in 4-hex-digit form **\\uhhhh** for a code point less than or equal to **\\uffff**. The string is in 8-hex-digit form **\\Uhhhhhhhh** for code points greater than **\\uffff**. `escape` may only be specified when converting from a Unicode encoding such as UTF-8. |
