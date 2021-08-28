## Syntax

The formats for displaying Stata internal form (SIF) dates and times in
human readable form (HRF) are SIF type present SIF in HRF

------------------------------------------------------------------------

`%tcdetails%tCdetails%tddetails%twdetails%tmdetails%tqdetails%thdetails%tydetails`

------------------------------------------------------------------------

The optional `details` allows you to control how results appear and is
composed of a sequence of the following codes:

------------------------------------------------------------------------

`CCccYYyyJJJjjjMonMonthmonmonthNNnnDDddDAYNAMEDaynameDayDadaydahqWWwwHHHhhHhhMMmmSSss.s.ss.sssama.m.AMA.M..,:-_/\!cc+`

------------------------------------------------------------------------

`++%tchh:MM+am%tchh:MMam%tc+hh+:+MM+am`

When `details` is not specified, it is equivalent to specifying

|

------------------------------------------------------------------------

<span options="+">{c +}_

------------------------------------------------------------------------

`%tC`|`%tCDDmonCCYY_HH:MM:SS%tc`<span
options="|">{c \|}_`%tcDDmonCCYY_HH:MM:SS`|`%td`|`%tdDDmonCCYY`<span
options="|">{c \|}_`%tw`|`%twCCYY!www%tm`|`%tmCCYY!mnn%tq`|`%tqCCYY!qq%th`|`%thCCYY!hh%ty`|`%tyCCYY`

------------------------------------------------------------------------

<span options="BT">{c BT}_

------------------------------------------------------------------------

That is, typing

. `format mytimevar %tc`

has the same effect as typing

. `format mytimevar %tcDDmonCCYY_HH:MM:SS`

Format `%tcDDmonCCYY_HH:MM:SS` is interpreted as

<span options="TLC">{c TLC}_<span options="63">_<span
options="TRC">{c TRC}_

|`%tcDDmonCCYY_HH:MM:SS`<span
options="|">{c \|}_|<span
options="|">{c \|}_|<span
options="|">{c \|}_|`%`<span
options="|">{c \|}_|<span
options="|">{c \|}_

<span options="BLC">{c BLC}_<span options="63">_<span
options="BRC">{c BRC}_
