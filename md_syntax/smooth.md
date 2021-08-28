## Syntax

`smooth smoother` \[`, twice`\]
[varname](http://www.stata.com/help.cgi?varname)
_\[`if`\] \[`in`\]_ `, generate(newvar)`

where `smoother` is specified as `Sm`\[`Sm`\[`...`\]\] and `Sm` is one
of

{`123456789`<span
options=")-">{c )-}_`R3RSSRSR...EH`

The numbers specified in `smoother` represent the span of a running
median smoother. For example, a number 3 specifies that each value be
replaced by the median of the point and the two adjacent data values.
The letter H indicates that a Hanning linear smoother, which is a span-3
smoother with binomial weights, be applied.

The letters E, S, and R are three refinements that can be combined with
the running median and Hanning smoothers. First, the endpoints of a
smooth can be given special treatment. This is specified by the E
operator. Second, smoothing by 3, the span-3 running median, tends to
produce flat-topped hills and valleys. The splitting operator, S,
"splits" these repeated values, applies the endpoint operator to them,
and then "rejoins" the series. Third, it is sometimes useful to repeat
an odd-span median smoother or the splitting operator until the smooth
no longer changes. Following a digit or an S with an R specifies this
type of repetition.

Finally, the `twice` operator specifies that after smoothing, the
smoother be reapplied to the resulting rough and that any recovered
signal be added back to the original smooth.

Letters may be specified in lowercase if preferred. Examples of <span
class="nowrap">`smoother` \[`,twice`\]_ include

`3RSSH` <span options="2">{space 2}_ `3RSSH,twice` <span
options="2">{space 2}_ `4253H` <span options="2">{space 2}_
`4253H,twice` <span options="2">{space 2}_ `43RSR2H,twice`

`3rssh` <span options="2">{space 2}_ `3rssh,twice` <span
options="2">{space 2}_ `4253h` <span options="2">{space 2}_
`4253h,twice` <span options="2">{space 2}_ `43rsr2h,twice`
