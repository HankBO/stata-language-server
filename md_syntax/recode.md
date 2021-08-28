## Syntax

Basic syntax

`recode`
[varlist](http://www.stata.com/help.cgi?varlist)
`(rule)` \[`(rule) ...`\] \[`, generate(newvar)`\]

Full syntax

`recode`
[varlist](http://www.stata.com/help.cgi?varlist)
`(erule)` \[`(erule) ...`\] _\[`if`\]
\[`in`\]_ \[`, options`\]

where the most common forms for `rule` are

{center None}<span options="TLC">{c TLC}_<span
options="16">_<span options="TT">{c TT}_<span
options="13">_<span options="TT">{c TT}_<span
options="27">_<span options="TRC">{c TRC}_{center None}<span
options="|">{c \|}_ `rule` | Example
| Meaning |{center None}<span options="LT">{c LT}_<span
options="16">_<span options="+">{c +}_<span
options="13">_<span options="+">{c +}_<span
options="27">_<span options="RT">{c RT}_{center None}<span
options="|">{c \|}_ `# = #` | 3
= 1 | 3 recoded to 1 |{center None}| `# # = #`
| 2 . = 9 |
2 and . recoded to 9 |{center None}<span
options="|">{c \|}_ `#/# = #` | 1/5 = 4 | 1 through 5 recoded
to 4 |{center None}| `nonmissing = #` | nonmiss
= 8 | all other nonmissing to 8 <span
options="|">{c \|}_{center None}|
`missing = #` | miss = 9 <span
options="|">{c \|}_ all other missings to 9 |{center None}<span options="BLC">{c BLC}_<span
options="16">_<span options="BT">{c BT}_<span
options="13">_<span options="BT">{c BT}_<span
options="27">_<span options="BRC">{c BRC}_

where `erule` has the form

`element` \[`element ...`\] `= el` \[`"label"`\]

`nonmissing = el` \[`"label"`\]

`missing = el` \[`"label"`\]

`else` \| `* = el` \[`"label"`\]

`element` has the form

`el` \| `el/el`

and `el` is

`#` \| `min` \| `max`

The keyword rules `missing`, `nonmissing`, and `else` must be the last
rules specified. `else` may not be combined with `missing` or
`nonmissing`.

| Options |                    | Description                                                                                  |
|---------|--------------------|----------------------------------------------------------------------------------------------|
| Options |                    |                                                                                              |
|         | `generate(newvar)` | generate `newvar` containing transformed variables; default is to replace existing variables |
|         | `prefix(str)`      | generate new variables with `str` prefix                                                     |
|         | `label(name)`      | specify a name for the value label defined by the transformation rules                       |
|         | `copyrest`         | copy out-of-sample values from original variables                                            |
|         | `test`             | test that rules are invoked and do not overlap                                               |
