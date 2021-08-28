## Syntax

`snapspan idvar timevar`
[varlist](http://www.stata.com/help.cgi?varlist)
\[`, generate(newt0var) replace`\]

`idvar` records the subject ID and may be string or numeric.

`timevar` records the time of the snapshot; it must be numeric and may
be recorded on any scale: date, hour, minute, second, etc.

[varlist](http://www.stata.com/help.cgi?varlist)
are the "event" variables, meaning that they occur at the instant of
`timevar`. `varlist` can also include retrospective variables that are
to apply to the time span ending at the time of the current snapshot.
The other variables are assumed to be measured at the time of the
snapshot and thus apply from the time of the snapshot forward. See [ST
snapspanRemarksandexamplesSpecifyingvarlist`Specifying varlist`](http://www.stata.com/manuals14/stsnapspanremarksandexamplesspecifyingvarlist.pdf)
in **\[ST\] snapspan**.
