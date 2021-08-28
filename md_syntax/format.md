## Syntax

Set formats

`format`
[varlist](http://www.stata.com/help.cgi?varlist)
`%fmt`

`format %fmt`
[varlist](http://www.stata.com/help.cgi?varlist)

Set style of decimal point

`set dp` {`comma`\|`period`<span
options=")-">{c )-}_ \[`, permanently`\]

Display long formats

`format`
\[[varlist](http://www.stata.com/help.cgi?varlist)\]

where `%fmt` can be a numerical, date, business calendar, or string
format.

`%fmt`

------------------------------------------------------------------------

`%#.#g%9.0g%#.#f%9.2f%#.#e%10.7e%21x%21x%16H%16H%16L%16L%8H%8H%8L%8L%#.#gc%9.0gc%#.#fc%9.2fc%0#.#f%09.2f%-#.#g%-9.0g%-#.#f%-9.2f%-#.#e%-10.7e%-#.#gc%-9.0gc%-#.#fc%-9.2fc`

------------------------------------------------------------------------

You may substitute comma (`,`) for period (`.`) in any of  
the above formats to make comma the decimal point. In  
`%9,2fc`, 1000.03 is 1.000,03. Or you can `set dp comma`.

------------------------------------------------------------------------

`%tc%tc%tC%tC%td%td%tw%tw%tm%tm%tq%tq%th%th%ty%ty%tg%tg%-tc%-tc%-tC%-tC%-td%-td`

------------------------------------------------------------------------

There are many variations allowed. See  
[<strong>[D]</strong> datetime display formats](http://www.stata.com/help.cgi?datetime_display_formats).

------------------------------------------------------------------------

`%tbcalname%tbsimple:datetime-specifierscalname.stbcal`

------------------------------------------------------------------------

See
[<strong>[D]</strong> datetime business calendars](http://www.stata.com/help.cgi?datetime_business_calendars).

------------------------------------------------------------------------

`%#s%15s%-#s%-20s%~#s%~12s`

------------------------------------------------------------------------

The centered format is for use with
[<strong>display</strong>](http://www.stata.com/help.cgi?display)
only.
