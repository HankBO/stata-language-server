## Syntax

`dyndoc srcfile` \[`arguments`\] \[`, options`\]

`srcfile` is a plain text file containing Markdown-formatted text and
[<strong>Stata dynamic tags</strong>](http://www.stata.com/help.cgi?dynamic%20tags).

`arguments` are stored in the local macros  `1' ,  `2' , and so
on for use in `srcfile`; see <span options="frarg">{findalias
frarg}_.

You may enclose `srcfile` and `targetfile` in double quotes and must do
so if they contain blanks or other special characters.

| Options |                      | Description                                                      |
|---------|----------------------|------------------------------------------------------------------|
|         | `saving(targetfile)` | specify the target HTML file to be saved                         |
|         | `replace`            | replace the target HTML file if it already exists                |
|         | `hardwrap`           | replace hard wraps (actual line breaks) with the HTML tag `<br>` |
|         | `nomsg`              | suppress message of a link to `targetfile`                       |
|         | `nostop`             | do not stop when an error occurs                                 |
