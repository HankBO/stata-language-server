## Syntax

`ifexp{c -(}`

or<span style="padding-left: 26.0rem;">_`if exp`
`single_command`

`multiple_commands{c )-}`

which, in either case, may be followed by

`else{c -(}`

or<span style="padding-left: 26.0rem;">_`else single_command`

`multiple_commands{c )-}`

If you put braces following the `if` or `else`,

1\. the open brace must appear on the same line as the `if` or `else`;

2\. nothing may follow the open brace except, of course, comments; the
first command to be executed must appear on a new line;

3\. the close brace must appear on a line by itself.
