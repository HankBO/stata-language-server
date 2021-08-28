## Syntax

Apply business calendar format

`format`
[varlist](http://www.stata.com/help.cgi?varlist)
`%tbcalname`

Apply detailed date format with business calendar format

`format`
[varlist](http://www.stata.com/help.cgi?varlist)
`%tbcalname`\[`:datetime-specifiers`\]

Convert between business dates and regular dates

{`generate`\|`replace`<span
options=")-">{c )-}_<span class="nowrap"> _ `bdate` =
`bofd("calname", regulardate)`

{`generate`\|`replace`<span
options=")-">{c )-}_ `regulardate` =
`dofb(bdate, "calname")`

File `calname.stbcal` contains the business calendar definition.

Details of the syntax follow:

1\. Definition.  
Business calendars are regular calendars with some dates crossed out:

A date that appears on the business calendar is called a business date.
11nov2011 is a business date. 12nov2011 is not a business date with
respect to this calendar.

Crossed-out dates are literally omitted. That is,

Stata's lead and lag operators work the same way.

2\. Business calendars are named.  
Assume that the above business calendar is named `simple`.

3\. Business calendars are defined in files named `calname.stbcal`,
such as `simple.stbcal`. Calendars may be supplied by StataCorp and
already installed, obtained from other users directly or via the SSC, or
written yourself. Calendars can also be created automatically from the
current dataset with the `bcal create` command; see
[<strong>[D] bcal</strong>](http://www.stata.com/help.cgi?bcal).
Stbcal-files are treated in the same way as ado-files.

You can obtain a list of all business calendars installed on your
computer by typing `bcal dir`; see
**[<strong>[D] bcal</strong>](http://www.stata.com/help.cgi?bcal)**.

4\. Datetime format.  
The date format associated with the business calendar named `simple` is
`%tbsimple`, which is to say <span class="nowrap">`%` + `t` + `b` +
`calname`_.

`%tbcalname`

5\. Format variables the usual way.  
You format variables to have business calendar formats just as you
format any variable, using the `format` command.

`format mydate %tbsimple`

specifies that existing variable `mydate` contains values according to
the business calendar named `simple`. See
**[<strong>[D] format</strong>](http://www.stata.com/help.cgi?format)**.

You may format variables `%tbcalname` regardless of whether the
corresponding stbcal-file exists. If it does not exist, the underlying
numeric values will be displayed in a `%g` format.

6\. Detailed date formats.  
You may include detailed datetime format specifiers by placing a colon
and the detail specifiers after the calendar's name.

`format mydate %tbsimple:CCYY.NN.DD`

would display 21nov2011 as 2011.11.21. See
**[<strong>[D] datetime display formats</strong>](http://www.stata.com/help.cgi?datetime_display_formats)**
for detailed datetime format specifiers.

7\. Reading business dates.  
To read files containing business dates, ignore the business date aspect
and read the files as if they contained regular dates. Convert and
format those dates as `%td`; see `HRF-to-SIF conversion functions` in
**[<strong>[D] datetime</strong>](http://www.stata.com/help.cgi?datetime)**.
Then convert the regular dates to `%tb` business dates:

`generate mydate = bofd("simple", regulardate)format mydate %tbsimpleassert mydate!=. if regulardate!=.`

The first statement performs the conversion.

The second statement attaches the `%tbsimple` date format to the new
variable `mydate` so that it will display correctly.

The third statement verifies that all dates recorded in `regulardate`
fit onto the business calendar. For instance, 12nov2011 does not appear
on the `simple` calendar but, of course, it does appear on the regular
calendar. If the data contained 12nov2011, that would be an error.
Function `bofd()` returns missing when the date does not appear on the
specified calendar.

8\. More on conversion.  
There are only two functions specific to business dates, `bofd()` and
`dofb()`. Their definitions are

`bdatebofd("calname,regulardate)regulardatedofb(bdate, "calname")`

`bofd()` returns missing if `regulardate` is missing or does not appear
on the specified business calendar. `dofb()` returns missing if `bdate`
contains missing.

9\. Obtaining day of week, etc.  
You obtain day of week, etc., by converting business dates to regular
dates and then using the standard functions. To obtain the day of week
of `bdate` on business calendar `calname`, type

`generate dow = dow(dofb(bdate, "calname"))`

See `Extracting date components from SIFs` in
**[<strong>[D] datetime</strong>](http://www.stata.com/help.cgi?datetime)**
for the other extraction functions.

10\. Stbcal-files.  
The stbcal-file for `simple`, the calendar shown below,

is

------------------------------------------------------------------------

------------------------------------------------------------------------

{cmd None}{txt None}

------------------------------------------------------------------------

------------------------------------------------------------------------

This calendar was so simple that we crossed out the Thanksgiving
holidays by specifying the dates to be omitted. In a real calendar, we
would change the last two lines,

{cmd None}{txt None}

to read

{cmd None}{txt None}

which says to omit the fourth (`+4`) Thursday of November in every year,
and omit the day after that (`+1`), too. See
**[<strong>[D] datetime business calendars creation</strong>](http://www.stata.com/help.cgi?datetime_business_calendars_creation)**.
