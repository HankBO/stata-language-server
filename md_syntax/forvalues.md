## Syntax

`forvalueslname=range{c -(}Stata commands referring to  `lname'{c )-}range`{center
None}`#1(#d)#2` <span options="4">{space 4}_ meaning `#1`
to `#2` in steps of `#d` {center None}`#1/#2` <span
options="7">{space 7}_ meaning `#1` to `#2` in steps of 1 {center
None}`#1 #t to #2` <span options="1">{space 1}_ meaning `#1`
to `#2` in steps of `#t` - `#1`{center None}`#1 #t :`<span
options="2">{space 2}_`#2` <span options="1">{space 1}_
meaning `#1` to `#2` in steps of `#t` - `#1`

The loop is executed as long as calculated values of   lname'`
are

`#2`, assuming that `#d` &gt; 0.

Braces must be specified with `forvalues`, and

1\. the open brace must appear on the same line as `forvalues`;

2\. nothing may follow the open brace except, of course, comments; the
first command to be executed must appear on a new line;

3\. the close brace must appear on a line by itself.
