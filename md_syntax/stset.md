## Syntax

Single-record-per-subject survival data

`stset timevar` \[`if`\] \[`weight`\] \[`, single_options`\]

`streset` \[`if`\] \[`weight`\] \[`, single_options`\]

`st` \[`, nocmd notable`\]

`stset, clear`

Multiple-record-per-subject survival data

`stset timevar` \[`if`\] \[`weight`\] `, id(idvar)`
`failure(failvar`\[`==numlist`\]`)` \[`multiple_options`\]

`streset` \[`if`\] \[`weight`\] \[`, multiple_options`\]

`streset,` {`past`\|`future`\|`past future`}

`st` \[`, nocmd notable`\]

`stset, clear`

| single\_options |                                          | Description                                                                |
|-----------------|------------------------------------------|----------------------------------------------------------------------------|
| Main            |                                          |                                                                            |
|                 | `failure:(failvar`\[`==numlist`\]`)` | failure event                                                              |
|                 | `noshow`                                 | prevent other st commands from showing st setting information              |
| Options         |                                          |                                                                            |
|                 | `origin(time exp)`                 | define when a subject becomes at risk                                      |
|                 | `scale(#)`                               | rescale time value                                                         |
|                 | `enter(time exp)`                  | specify when subject first enters study                                    |
|                 | `exit(time exp)`                   | specify when subject exits study                                           |
| Advanced        |                                          |                                                                            |
|                 | `if(exp)`                                | select records for which `exp` is true; recommended rather than `if exp` |
|                 | `time0(varname)`                         | mechanical aspect of interpretation about records in dataset; seldom used  |

multiple\_options

Description

Main

\*

`"id(idvar)`

multiple-record ID variable

\*

`failure:(failvar`\[`== numlist`\]`)`

failure event

`noshow`

prevent other st commands from showing st setting information

Options

`scale(#)`

rescale time value

define when a subject becomes at risk specify when subject first enters
study specify when subject exits study

Advanced

`if(exp)`

select records for which `exp` is true; recommended rather than `if`
`exp`

`ever(exp)`

select subjects for which `exp` is ever true

`never(exp)`

select subjects for which `exp` is never true

`after(exp)`

select records within subject on or after the first time `exp` is true

`before(exp)`

select records within subject before the first time `exp` is true

`time0(varname)`

mechanical aspect of interpretation about records in dataset; seldom
used

\* `id()` and `failure()` are required with `stset`
multiple-record-per-subject survival data. <span
options="weight">{marker weight}_{nobreak None} {phang None}
`fweight`s, `iweight`s, and `pweight`s are allowed; see
[<strong>weight</strong>](http://www.stata.com/help.cgi?weight).
**Examples** Time measured from 0, all failed `. stset ftime` Time
measured from 0, censoring `. stset ftime, failure(died)` Time measured
from 0, censoring & ID `. stset ftime, failure(died) id(id)` Time
measured from 0, failure codes `. stset ftime, failure(died==2,3)` Time
measured from dob, censoring
`. stset ftime, failure(died) origin(time dob)` {pmore None} You cannot
harm your data by using `stset`, so feel free to experiment. <span
options="menu">{marker menu}_{nobreak None} {title None:Menu}
{phang None} **Statistics &gt; Survival analysis &gt; Setup and
utilities &gt;** **Declare data to be survival-time data** <span
options="description">{marker description}_{nobreak None} {title
None:Description} {pstd None} st refers to survival-time data, which are
fully described below. {pstd None} `stset` declares the data in memory
to be st data, informing Stata of key variables and their roles in a
survival-time analysis. When you `stset` your data, `stset` runs various
data consistency checks to ensure that what you have declared makes
sense. If the data are weighted, you specify the weights when you
`stset` the data, not when you issue the individual st commands. {pstd
None} `streset` changes how the st dataset is declared. In
multiple-record data, `streset` can also temporarily set the sample to
include records from before the time at risk (called the past) and
records after failure (called the future). Then typing `streset` without
arguments resets the sample back to the analysis sample. {pstd None}
`st` displays how the dataset is currently declared. {pstd None}
Whenever you type `stset` or `streset`, Stata runs or reruns data
consistency checks to ensure that what you are now declaring (or
declared in the past) makes sense. Thus if you have made any changes to
your data or simply wish to verify how things are, you can type
`streset` with no options. {pstd None} `stset, clear` is for use by
programmers. It causes Stata to forget the st markers, making the data
no longer st data to Stata. The data remain unchanged. It is not
necessary to `stset, clear` before doing another `stset`. <span
options="linkspdf">{marker linkspdf}_{nobreak None} {title
None:Links to PDF documentation} [Quick
start](http://www.stata.com/manuals14/ststsetquickstart.pdf) [Remarks
and
examples](http://www.stata.com/manuals14/ststsetremarksandexamples.pdf)
{pstd None} The above sections are not included in this help file. <span
options="options_stset">{marker options\_stset}_{nobreak None}
{title None:Options for use with stset and streset} {dlgtab None:Main}
<span options="id()">{marker id()}_{nobreak None} {phang None}
`id(idvar)` specifies the subject-ID variable; observations with equal,
nonmissing values of `idvar` are assumed to be the same subject. `idvar`
may be string or numeric. Observations for which `idvar` is missing (.
or "") are ignored. {pmore None} When `id()` is not specified, each
observation is assumed to represent a different subject and thus
constitutes a one-record-per-subject survival dataset. {pmore None} When
you specify `id()`, the data are said to be multiple-record data, even
if it turns out that there is only one record per subject. Perhaps they
would better be called potentially multiple-record data. {pmore None} If
you specify `id()`, `stset` requires that you specify `failure()`.
{pmore None} Specifying `id()` never hurts; we recommend it because a
few st commands, such as `stsplit`, require an ID variable to have been
specified when the dataset was `stset`. {phang None}
`failure(failvar`\[`== numlist`\]`)` specifies the failure event.
{pmore None} If `failure()` is not specified, all records are assumed to
end in failure. This is allowed with single-record data only. {pmore
None} If `failure(failvar)` is specified, `failvar` is interpreted as an
indicator variable; 0 and missing mean censored, and all other values
are interpreted as representing failure. {pmore None} If
`failure(failvar == numlist)` is specified, records with
`failvar` taking on any of the values in `numlist` are assumed to end in
failure, and all other records are assumed to be censored. {phang None}
`noshow` prevents other st commands from showing the key st variables at
the top of their output. {dlgtab None:Options} {phang None}
`origin(`\[[varname](http://www.stata.com/help.cgi?varname)
`== numlist`\] `time exp` \| `min)` and `scale(#)` define analysis
time; that is, `origin()` defines when a subject becomes at risk.
Subjects become at risk when time = `origin()`. All analyses are
performed in terms of time since becoming at risk, called analysis time.
{pmore None} Let us use the terms `time` for how time is recorded in the
data and `t` for analysis time. Analysis time `t` is defined `time` -
`origin() t` = <span options="15">_ `scale()` {pmore None} `t`
is time from origin in units of scale. {pmore None} By default,
`origin(time 0)` and `scale(1)` are assumed, meaning that `t` =
`time`. Then you must ensure that `time` in your data is measured as
time since becoming at risk. Subjects are exposed at `t` = `time` = 0
and later fail. Observations with `t` = `time` &lt;= 0 are ignored
because information before becoming at risk is irrelevant. {pmore None}
`origin()` determines when the clock starts ticking. `scale()` plays no
substantive role, but it can be handy for making `t` units more readable
(such as converting days to years). {pmore None} `origin(time exp)`
sets the origin to `exp`. For instance, if `time` were recorded as
dates, such as 05jun1998, in your data and variable `expdate` recorded
the date when subjects were exposed, you could specify `origin(time`
`expdate)`. If instead all subjects were exposed on 12nov1997, you could
specify `origin(time mdy(11,12,1997))`. {pmore None} `origin(time`
`exp)` may be used with single- or multiple-record data. {pmore None}
`origin(varname == numlist)` is for use with multiple-record
data; it specifies the origin indirectly. If `time` were recorded as
dates in your data, variable `obsdate` recorded the (ending) date
associated with each record, and subjects became at risk upon, say,
having a certain operation -- and that operation were indicated by
`code==217` -- then you could specify `origin(code==217)`.
`origin(code==217)` would mean, for each subject, that the origin time
is the earliest time at which `code==217` is observed. Records before
that would be ignored (because `t` &lt; 0). Subjects who never had
`code==217` would be ignored entirely. {pmore None} `origin(varname`
`== numlist time exp)` sets the origin to the later of the two
times determined by `varname==numlist` and `exp`. {pmore None}
`origin(min)` sets origin to the earliest time observed, minus 1. This
is an odd thing to do and is described in [example
10](http://www.stata.com/manuals14/ststsetremarksandexamplesex10.pdf) in
**\[ST\] stset**. {pmore None} `origin()` is an important concept; see
[ST
stsetRemarksandexamplesKeyconcepts`Key concepts`](http://www.stata.com/manuals14/ststsetremarksandexampleskeyconcepts.pdf),
[ST
stsetRemarksandexamplesTwoconceptsoftime`Two concepts of time`](http://www.stata.com/manuals14/ststsetremarksandexamplestwoconceptsoftime.pdf),
and [ST
stsetRemarksandexamplesThesubstantivemeaningofanalysistime`The substantive meaning of analysis time`](http://www.stata.com/manuals14/ststsetremarksandexamplesthesubstantivemeaningofanalysistime.pdf)
in **\[ST\] stset**. {pmore None} `scale()` makes results more readable.
If you have `time` recorded in days (such as Stata dates, which are
really days since 01jan1960), specifying `scale(365.25)` will cause
results to be reported in years. {phang None}
`enter(`\[[varname](http://www.stata.com/help.cgi?varname)
`== numlist`\] `time exp)` specifies when a subject first comes
under observation, meaning that any failures, were they to occur, would
be recorded in the data. {pmore None} Do not confuse `enter()` and
`origin()`. `origin()` specifies when a subject first becomes at risk.
In many datasets, becoming at risk and coming under observation are
coincident. Then it is sufficient to specify `origin()`. {pmore None}
`enter(time exp)`, `enter(varname == numlist)`, and
`enter(varname == numlist time exp)` follow the same syntax
as `origin()`. In multiple-record data, both `varname == numlist`
and `time exp` are interpreted as the earliest time implied, and if
both are specified, the later of the two times is used. {phang None}
`exit(failure` \|
\[[varname](http://www.stata.com/help.cgi?varname)
`== numlist`\] `time exp)` specifies the latest time under which
the subject is both under observation and at risk. The emphasis is on
latest; obviously, subjects also exit the risk pool when their data run
out. {pmore None} `exit(failure)` is the default. When the first failure
event occurs, the subject is removed from the analysis risk pool, even
if the subject has subsequent records in the data and even if some of
those subsequent records document other failure events. Specify
`exit(time .)` if you wish to keep all records for a subject after
failure. You want to do this if you have multiple-failure data. {pmore
None} `exit(varname == numlist)`, `exit(time exp)`, and
`exit(varname == numlist time exp)` follow the same syntax
as `origin()` and `enter()`. In multiple-record data, both `varname`
`== numlist` and `time exp` are interpreted as the earliest time
implied. `exit` differs from `origin()` and `enter()` in that if both
are specified, the earlier of the two times is used. {dlgtab
None:Advanced} {phang None} `if(exp)`, `ever(exp)`, `never(exp)`,
`after(exp)`, and `before(exp)` select relevant records. {pmore None}
`if(exp)` selects records for which `exp` is true. We strongly recommend
specifying this `if()` option rather than `if exp` following `stset`
or `streset`. They differ in that `if exp` removes the data from
consideration before calculating beginning and ending times and other
quantities. The `if()` option, on the other hand, sets the restriction
after all derived variables are calculated. See [ST
stsetRemarksandexamplesif()versusifexp`if() versus if exp`](http://www.stata.com/manuals14/ststsetremarksandexamplesif()versusifexp.pdf)
in **\[ST\] stset**. {pmore None} `if()` may be specified with single-
or multiple-record data. The remaining selection options are for use
with multiple-record data only. {pmore None} `ever(exp)` selects only
subjects for which `exp` is ever true. {pmore None} `never(exp)` selects
only subjects for which `exp` is never true. {pmore None} `after(exp)`
selects records within subject on or after the first time `exp` is true.
{pmore None} `before(exp)` selects records within subject before the
first time `exp` is true. {phang None} `time0(varname)` is seldom
specified because most datasets do not contain this information.
`time0()` should be used exclusively with multiple-record data, and even
then you should consider whether `origin()` or `enter()` would be more
appropriate. {pmore None} `time0()` specifies a mechanical aspect of
interpretation about the records in the dataset, namely, the beginning
of the period spanned by each record. See [ST
stsetRemarksandexamplesIntermediateexitandreentrytimes(gaps)`Intermediate exit and reentry times (gaps)`](http://www.stata.com/manuals14/ststsetremarksandexamplesintermediateexitandreentrytimes(gaps).pdf)
in **\[ST\] stset**. <span options="options_streset">{marker
options\_streset}_{nobreak None} {title None:Options unique to
streset} {phang None} `past` expands the `stset` sample to include the
entire recorded past of the relevant subjects, meaning that it includes
observations before becoming at risk and those excluded because of
`after()`, etc. {phang None} `future` expands the `stset` sample to
include the records on the relevant subjects after the last record that
previously was included, if any, which typically means to include all
observations after failure or censoring. {phang None} `past future`
expands the `stset` sample to include all records on the relevant
subjects. {pstd None} Typing `streset` without arguments resets the
sample to the analysis sample. See [ST
stsetRemarksandexamplesPastandfuturerecords`Past and future records`](http://www.stata.com/manuals14/ststsetremarksandexamplespastandfuturerecords.pdf)
in **\[ST\] stset** for more information. <span
options="options_st">{marker options\_st}_{nobreak None} {title
None:Options for use with st} {phang None} `nocmd` suppresses displaying
the last `stset` command. {phang None} `notable` suppresses displaying
the table summarizing what has been `stset`. <span
options="examples">{marker examples}_{nobreak None} {title
None:Example: Single-record-per-subject} {pstd None}The failure-time
(analysis-time) variable is `failtime`
