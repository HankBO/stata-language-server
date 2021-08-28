## Syntax

Declare data in memory to be count-time data and run checks on data

`ctset timevar nfailvar` \[`ncensvar` \[`nentvar`\]\] \[`,`
`by(varlist) noshow` \]

Specify whether to display identities of key ct variables

`ctset,` {`show` \| `noshow`}

Clear ct setting

`ctset, clear`

Display identity of key ct variables and rerun checks on data

{`ctset` \| `ct`}

where `timevar` refers to the time of failure, censoring, or entry. It
should contain times &gt;= 0.

`nfailvar` records the number failing at time `timevar`.

`ncensvar` records the number censored at time `timevar`.

`nentvar` records the number entering at time `timevar`.

Stata sequences events at the same time as

at `timevar` <span options="7">{space 7}_ `nfailvar` failures
occurred,

then at `timevar`+0 <span options="5">{space 5}_ `ncensvar`
censorings occurred,

finally at `timevar`+0+0 <span options="4">{space 4}_ `nentvar`
subjects entered the data.
