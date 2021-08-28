## Syntax

Business calendar `calname` and corresponding display format
`%tbcalname` are defined by the text file `calname.stbcal`, which
contains the following:

`* comments`

`version version_of_stata`

`purpose "text"`

`dateformat` {`ymd` \| `ydm` \| `myd` \|
`mdy` \| `dym` \| `dmy`}

`range date date`

`centerdate date`

\[`from` {`date`\|`.`<span
options=")-">{c )-}_ `to` <span options="-(">{c
-(}_`date`\|`.`}`:`\]<span
class="nowrap"> _`omit` ... \[`if`\]

...  
...

where

`omit` ... may be

`omit date pdate` \[`and pmlist`\]

`omit dayofweek dowlist`

`omit dowinmonth pm# dow` \[`of monthlist`\] \[`and pmlist`\]

\[`if`\] may be

`if restriction` \[`& restriction` ...\]

`restriction` is one of

`dow(dowlist)`  
`month(monthlist)`  
`year(yearlist)`  

`date` is a date written with the `year`, `month`, and `day` in the
order specified by `dateformat`. For instance, if `dateformat` is `dmy`,
a `date` can be `12apr2013`, `12-4-2013`, or `12.4.2013`.

`pdate` is a `date` or it is a `date` with character `*` substituted
where the year would usually appear. If `dateformat` is `dmy`, a `pdate`
can be `12apr2013`, `12-4-2013`, or `12.4.2013`; or it can be `12apr*`,
`12-4-*`, or `12.4.*`. `12apr*` means the 12th of April across all
years.

`dow` is a day of the week, in English. It may be abbreviated to as few
as 2 characters, and capitalization is irrelevant. Examples: `Sunday`,
`Mo`, `tu`, `Wed`, `th`, `Friday`, `saturday`.

`dowlist` is a `dow`, or it is a space-separated list of one or more
`dow`s enclosed in parentheses. Examples: `Sa`, `(Sa)`, `(Sa Su)`.

`month` is a month of the year, in English, or it is a month number. It
may be abbreviated to the minimum possible, and capitalization is
irrelevant. Examples: `January`, `2`, `Mar`, `ap`, `may`, `6`, `Jul`,
`aug`, `9`, `Octob`, `nov`, `12`.

`monthlist` is a `month`, or it is a space-separated list of one or more
`month`s enclosed in parentheses. Examples: `Nov`, `(Nov)`, `11`,
`(11)`, `(Nov Dec)`, `(11 12)`.

`year` is a 4-digit calendar year. Examples: `1872`, `1992`, `2013`,
`2050`.

`yearlist` is a `year`, or it is a space-separated list of one or more
`year`s enclosed in parentheses. Examples: `2013`, `(2013)`,
`(2013 2014)`.

`pm#` is a nonzero integer preceded by a plus or minus sign. Examples:
`-2`, `-1`, `+1`. `pm#` appears in `omit dowinmonth pm# dow of`
`monthlist`, where `pm#` specifies which `dow` in the month. `omit`
`dowinmonth +1 Th` means the first Thursday of the month. `omit`
`dowinmonth -1 Th` means the last Thursday of the month.

`pmlist` is a `pm#`, or it is a space-separated list of one or more
`pm#`s enclosed in parentheses. Examples: `+1`, `(+1)`, `(+1 +2)`,
`(-1 +1 +2)`. `pmlist` appears in the optional `and pmlist` allowed at
the end of `omit date` and `omit dowinmonth`, and it specifies
additional dates to be omitted. `and +1` means and the day after.
`and -1` means and the day before.
