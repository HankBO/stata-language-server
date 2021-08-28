## Syntax

`misstable summarize`
\[[varlist](http://www.stata.com/help.cgi?varlist)\]
_\[`if`\] \[`in`\]_ \[`,`
`summarize_options`\]

`misstable patterns`
\[[varlist](http://www.stata.com/help.cgi?varlist)\]
_\[`if`\] \[`in`\]_ \[`,`
`patterns_options`\]

`misstable tree`
\[[varlist](http://www.stata.com/help.cgi?varlist)\]
_\[`if`\] \[`in`\]_ \[`, tree_options`\]

`misstable nested`
\[[varlist](http://www.stata.com/help.cgi?varlist)\]
_\[`if`\] \[`in`\]_ \[`, nested_options`\]

| summarize\_options |                                   | Description                       |
|--------------------|-----------------------------------|-----------------------------------|
|                    | `all`                             | show all variables                |
|                    | `showzeros`                       | show zeros in table               |
|                    | `generate(stub` \[`, exok`\]`)` | generate missing-value indicators |

| patterns\_options |              | Description                                     |
|-------------------|--------------|-------------------------------------------------|
|                   | `asis`       | use variables in order given                    |
|                   | `frequency`  | report frequencies instead of percentages       |
|                   | `exok`       | treat `.a`, `.b`, ..., `.z` as nonmissing       |
|                   | `replace`    | replace data in memory with dataset of patterns |
|                   | `clear`      | okay to replace even if original unsaved        |
|                   | `bypatterns` | list by patterns rather than by frequency       |

| tree\_options |             | Description                               |
|---------------|-------------|-------------------------------------------|
|               | `asis`      | use variables in order given              |
|               | `frequency` | report frequencies instead of percentages |
|               | `exok`      | treat `.a`, `.b`, ..., `.z` as nonmissing |

| nested\_options |        | Description                               |
|-----------------|--------|-------------------------------------------|
|                 | `exok` | treat `.a`, `.b`, ..., `.z` as nonmissing |

In addition, programmer's option `nopreserve` is allowed with all
syntaxes; see
**[<strong>[P] nopreserve option</strong>](http://www.stata.com/help.cgi?nopreserve_option)**.
<span
options="do not even think of mentioning that nopreserve does not appear">{comment
do not even think of mentioning that nopreserve does not
appear}_{nobreak None} <span
options="in the dialog box.  Of course it doesn't.">{comment in the
dialog box. Of course it doesn't.}_{nobreak None}
