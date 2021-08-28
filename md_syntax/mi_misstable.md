## Syntax

`mi misstable summarize`
\[[varlist](http://www.stata.com/help.cgi?varlist)\]
\[`if`\] \[`, options`\]

`mi misstable patterns`<span class="nowrap">
_\[[varlist](http://www.stata.com/help.cgi?varlist)\]
\[`if`\] \[`, options`\]

`mi misstable tree`<span class="nowrap">
_\[[varlist](http://www.stata.com/help.cgi?varlist)\]
\[`if`\] \[`, options`\]

`mi misstable nested`<span class="nowrap">
_\[[varlist](http://www.stata.com/help.cgi?varlist)\]
\[`if`\] \[`, options`\]

| Options |                 | Description                                                                                                                                                       |
|---------|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Main    |                 |                                                                                                                                                                   |
|         | `exmiss`        | treat `.a`, `.b`, ..., `.z` as missing                                                                                                                            |
|         | `m(#)`      | run `misstable` on `m`=`#`; default `m`=0                                                                                                                         |
|         | `other_options` | see **[<strong>[R] misstable</strong>](http://www.stata.com/help.cgi?misstable)** (**generate()** is not allowed; **exok** is assumed) |
|         | `nopreserve`    | programmer's option; see **[<strong>[P] nopreserve option</strong>](http://www.stata.com/help.cgi?nopreserve)**                        |
