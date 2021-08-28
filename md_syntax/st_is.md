## Syntax

Verify that data in memory are survival-time data

`st_is 2` { `full` \| `analysis` <span
options=")-">{c )-}_

Display or do not display summary of survival-time variables

`st_show` \[`noshow`\]

Risk-group summaries

`st_ct "`\[`byvars`\]`" -> newtvar newpopvar newfailvar`
\[`newcensvar` \[`newentvar`\]\]

You must have `stset` your data before using `st_is`, `st_show`, and
`st_ct`; see
[<strong>[ST]</strong> stset](http://www.stata.com/help.cgi?stset).
