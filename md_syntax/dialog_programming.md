## Syntax

<span class="nowrap">`VERSION #`\[`.##`\]
\[`valid_operating_systems`\]_

## Syntax

<span class="nowrap">`INCLUDE includefilename`_

where `includefilename` refers to `includefilename.idlg` and must be
specified without the suffix and without a path.

## Syntax

`DEFINE name`
{`.`\|`#`\|`+#`\|`-#`\|`@x`\|`@y`\|`@xsize`\|`,@ysize`}

## Syntax

<span class="nowrap">`POSITION x y xsize ysize`_

## Syntax

`LISTnewlistnameBEGINitemitemEND`

## Syntax

<span class="nowrap">`DIALOG newdialogname` \[`, title`("`string`")
`tabtitle`("`string`")\]_`control definition statementsINCLUDEDEFINE`

## Syntax

**CHECKBOX** `newcontrolname x y xsize ysize` \[`,`
`label("string") error("string") default(defnumval)`
`nomemory groupbox onclickon(iaction) onclickoff(iaction)`
`option(optionname) tooltip("string")`\]

## Syntax

`RADIO newcontrolname x y xsize ysize` \[`,`
\[`first`\|`middle`\|`last`\] `label("string")`
`error("string") default(defnumval) nomemory`
`onclickon(iaction) onclickoff(iaction) option(optionname)`
`tooltip("string")`\]

## Syntax

`SPINNER newcontrolname x y xsize ysize` \[`,`
`label("string") error("string") default(defnumval)`
`nomemory min(defnumval) max(defnumval) onchange(iaction)`
`option(optionname) tooltip("string")`\]

## Syntax

EDIT `newcontrolname x y xsize ysize` \[`, label`("`string`")
`error`("`string`") `default(defstrval) nomemory max(#)`
` numonly password onchange(iaction) option(optionname)`
`tooltip("string")`\]

## Syntax

{**VARLIST**\|**VARNAME**} {it:newcontrolname} `x y xsize ysize`
\[`, label`("`string`") `error`("`string`") `default(defstrval)`
`nomemory fv ts option(optionname) tooltip("string")`\]

## Syntax

`FILE newcontrolname x y xsize ysize` \[`,`
`label`("`string`") `error`("`string`") `default(defstrval) nomemory`
`buttonwidth(#) dialogtitle(string) save multiselect directory`
`filter(string) onchange(iaction) option(optionname)`
`tooltip("string")`\]

## Syntax

`LISTBOX newcontrolname x y xsize ysize` \[`,`
`label("string") error("string") nomemory`
`contents(conspec) values(listname) default(defstrval)`
`ondblclick(iaction)`
\[`onselchange(iaction)`\|`onselchangelist(listname)`\]
`option(optionname) tooltip("string")`\]

## Syntax

**COMBOBOX** `newcontrolname x y xsize ysize` \[`,`
`label("string") error("string")`
\[`regular|dropdown|dropdownlist`\] `default(defstrval) nomemory`
`contents(conspec) values(listname) append`
\[`onselchange(iaction)`\|`onselchangelist(listname)`\]
`option(optionname) tooltip("string")`\]

## Syntax

**BUTTON** `newcontrolname x y xsize ysize` \[`,`
`label("string") error("string") onpush(iaction)`
`tooltip("string")`\]

## Syntax

**TEXT** `newcontrolname x y xsize ysize` \[`,`
`label("string")` \[`left`\|`center`\|`right`\]\]

## Syntax

**TEXTBOX** `newcontrolname x y xsize ysize` \[`,`
`label("string")` \[`left`\|`center`\|`right`\]\]

## Syntax

**GROUPBOX** `newcontrolname x y xsize ysize` \[`,`
`label("string")`\]

## Syntax

FRAME `newcontrolname x y xsize ysize` \[`,`
`label("string")`\]

## Syntax

COLOR `newcontrolname x y xsize ysize` \[`, label`("`string`")
`error`("`string`") `default(rgbvalue) nomemory onchange(iaction)`
`option(optionname) tooltip("string")`\]

## Syntax

EXP `newcontrolname x y xsize ysize` \[`, label`("`string`")
`error`("`string`") `default(defstrval) nomemory onchange(iaction)`
`option(optionname) tooltip("string")`\]

## Syntax

**HLINK** `newcontrolname x y xsize ysize` \[`,`
`label("string")` \[`left`\|`center`\|`right`\]
`onpush(iaction)`\]

## Syntax

`TREEVIEW newcontrolname x y xsize ysize` \[`,`
`label("string") error("string") nomemory`
`contents(conspec) values(listname) default(defstrval)`
`ondblclick(iaction)`
\[`onselchange(iaction)`\|`onselchangelist(listname)`\]
`option(optionname) tooltip("string")`\]

## Syntax

{**OK**\|**SUBMIT**\|**COPY**} {it:newbuttonname} \[`,`
`label("string") uaction(programname) target(target)`\]

**CANCEL** `newbuttonname` \[`, label("string")`\]

## Syntax

**HELP** `newbuttonname` \[`, view("viewertopic")`\]

**RESET** `newbuttonname`

## Syntax

{**MODAL**\|**SYNCHRONOUS\_ONLY**}

## Syntax

**SCRIPT**`newscriptname`**BEGIN**`iaction`**END**

where `iaction` is

`.`

`action memberfunction`

`gaction dialogname.controlname.memberfunction`

`dialogname.controlname.memberfunction`

`script scriptname`

`view topic`

`program programname`

See `2.5 I-actions and member functions` for more information on
`iactions`.

## Syntax

**PROGRAM**`programnameBEGINprogram_lineINCLUDEEND`

## Syntax

`ifexpifexp`

where `ifexp` may be

|                         |                                                    |
|-------------------------|----------------------------------------------------|
| `ifexp`                 | Meaning {p2line None}                              |
| (`ifexp`)               | order of evaluation                                |
| !`ifexp`                | logical not                                        |
| `ifexp` \| `ifexp`      | logical or                                         |
| `ifexp` & `ifexp`       | logical and                                        |
| `vname`                 | true if `vname` is not 0 and not `""`              |
| `vname.booleanfunction` | true if `vname.booleanfunction` evaluates to true  |
| `_rc`                   | see `5.5 Command-execution commands`.              |
| `_stbusy`               | true if Stata is busy                              |
| `H(vname)`              | true if `vname` is hidden or disabled              |
| `default(vname)`        | true if `vname` is its default value {p2line None} |

Note the recursive definition: An `ifexp` may be substituted into itself
to produce more complicated expressions, such as <span
class="nowrap">`((!d1.s1) & d1.s2) | d1.s3.isdefault()`_.

Also note that the order of evaluation is left to right; use
parentheses.

|                               |                                                                                                                                                                                               |
|-------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `booleanfunction`             | Meaning {p2line None}                                                                                                                                                                         |
| `isdefault()`                 | true if the value of `vname` is its default value                                                                                                                                             |
| `isenabled()`                 | true if `vname` is enabled                                                                                                                                                                    |
| `isnumlist()`                 | true if the value of `vname` is a `numlist`                                                                                                                                                   |
| `isvisible()`                 | true if `vname` is visible                                                                                                                                                                    |
| `isvalidname()`               | true if the value of `vname` is a valid Stata name                                                                                                                                            |
| `isvarname()`                 | true if the value of `vname` is the name of a variable in the current dataset                                                                                                                 |
| `iseq(argument)`              | true if the value of `vname` is equal to `argument`                                                                                                                                           |
| `isneq(argument)`             | true if the value of `vname` is not equal to `argument`                                                                                                                                       |
| `isgt(argument)`              | true if the value of `vname` is greater than `argument`                                                                                                                                       |
| `isge(argument)`              | true if the value of `vname` is greater than or equal to `argument`                                                                                                                           |
| `islt(argument)`              | true if the value of `vname` is less than `argument`                                                                                                                                          |
| `isle(argument)`              | true if the value of `vname` is less than or equal to `argument`                                                                                                                              |
| `isNumlistEQ(argument)`       | true if every value of `vname` is equal to `argument`, where `vname` may be a [<strong>numlist</strong>](http://www.stata.com/help.cgi?numlist)                    |
| `isNumlistLT(argument)`       | true if every value of `vname` is less than `argument`, where `vname` may be a [<strong>numlist</strong>](http://www.stata.com/help.cgi?numlist)                   |
| `isNumlistLE(argument)`       | true if every value of `vname` is less than or equal to `argument`, where `vname` may be a [<strong>numlist</strong>](http://www.stata.com/help.cgi?numlist)       |
| `isNumlistGT(argument)`       | true if every value of `vname` is greater than `argument`, where `vname` may be a [<strong>numlist</strong>](http://www.stata.com/help.cgi?numlist)                |
| `isNumlistGE(argument)`       | true if every value of `vname` is greater than or equal to `argument`, where `vname` may be a [<strong>numlist</strong>](http://www.stata.com/help.cgi?numlist)    |
| `isNumlistInRange(arg1,arg2)` | true if every value of `vname` is in between `arg1` and `arg2` inclusive, where `vname` may be a [<strong>numlist</strong>](http://www.stata.com/help.cgi?numlist) |
| `startswith(argument)`        | true if the value of `vname` starts with `argument`                                                                                                                                           |
| `endswith(argument)`          | true if the value of `vname` ends with `argument`                                                                                                                                             |
| `contains(argument)`          | true if the value of `vname` contains `argument`                                                                                                                                              |
| `iseqignorecase(argument)`    | true if the value of `vname` is equal to `argument` ignoring case {p2line None}                                                                                                               |

An `argument` can be a dialog control, a dialog property, or a literal.
If the `argument` is a literal it can be either string or numeric,
depending on the type of control the `booleanfunction` references.
String controls require that literals be quoted, and numeric controls
require that literals not be quoted.

## Syntax

`condition`

where `condition` may be

|                            |                           |
|----------------------------|---------------------------|
| `condition`                | Meaning {p2line None}     |
| (`condition`)              | order of evaluation       |
| !`condition`               | logical not               |
| `condition` \| `condition` | logical or                |
| `condition` & `condition`  | logical and {p2line None} |

## Syntax

**call** `iaction`

where `iaction` is

`.actionmemberfunctiongactiondialogname.controlname.memberfunctiondialogname.controlname.memberfunctionscriptscriptnameviewtopicprogramprogramname`

`iaction` "`action memberfunctionname`" is invalid in u-action
programs because there is no concept of a current control.

## Syntax

`exit` \[`#`\]

where `#`&gt;=0. The following exit codes have special meaning:

|                                         |                                                                   |
|-----------------------------------------|-------------------------------------------------------------------|
| <span options="2">{space 2}_`#`   | Definition {p2line None}                                          |
| <span options="2">{space 2}_0     | exit without error                                                |
| <span options="1">{space 1}_&gt;0 | exit with error                                                   |
| 101                                     | program exited because of a missing required object {p2line None} |

## Syntax

`close`

## Syntax

require `ename` \[`ename` \[ . . . \]\]

where each `ename` must be `string`.

## Syntax

`stopbox` {`stop|note|rusure`} \["`line1`" \["`line2`" \["`line3`"
\["`line4`" \]\]\]\]

## Syntax

by `ename`

where `ename` must contain a string and should refer to a **VARNAME**,
**VARLIST**, or **EDIT** control.

Use of `option()` communication: None.

## Syntax

**bysort** `ename`

where `ename` must contain a string and should probably refer to a
**VARNAME**, **VARLIST**, or **EDIT** control.

Use of `option()` communication: None.

## Syntax

**put**
\[[<strong>%</strong><var class="command">fmt</var><strong></strong>](http://www.stata.com/help.cgi?format)\]
`putel` \[\[%`fmt`\] `putel` \[ . . . \]\]

where `putel` may be

`"""string"vname/hidden vname/on vname/program programname`

The word "output" means "add to the current result" in what follows. The
`put` directives are defined as

`""` and `"string"`  
Outputs the fixed text specified.

`vname`  
Outputs the value of the control.

`/hidden vname`  
Outputs the value of the control, even if it is hidden or disabled.

`/on vname`  
Outputs nothing if ` vname==0`. `vname` must be numeric and should be
the result of a **CHECKBOX** or **RADIO** control. `/on` outputs the
text from the control's `option()` option. Also see `5.4.8.1 option` for
an alternative using the `option` command.

`/program programname`  
Outputs the `cmdstring, optstring` returned by `programname`.

If any `vname` is disabled or hidden and not preceded by `/hidden`,
`put` outputs nothing.

If the directive is preceded by `%fmt`, the specified `%fmt` is
always used to format the result. Otherwise, string results are
displayed as is, and numeric results are displayed in `%10.0g` format
and stripped of resulting leading and trailing blanks. See
[<strong>[D]</strong> format](http://www.stata.com/help.cgi?format).

Use of `option()` communication: See `/on` above.

## Syntax

**varlist** `el` \[ `el` \[ . . . \]\]

where an `el` is `ename` or `[ename]` (brackets significant).

Each `ename` must be string and should be the result from a **VARLIST**,
**VARNAME**, or **EDIT** control.

If `ename` is not enclosed in brackets, it must not be hidden or
disabled.

Use of `option()` communication: None.

## Syntax

**ifexp** `ename`

where `ename` must be a string control.

Use of `option()` communication: None.

## Syntax

**inrange** `ename_1 ename_2`

where `ename_1` and `ename_2` must be numeric controls.

Use of `option()` communication: None.

## Syntax

**weight** `ename_t ename_e`

where `ename_t` may be a string or numeric control and must have had
`option()` filled in with a weight type (one of `weight`, `fweight`,
`aweight`, `pweight`, or `iweight`), and `ename_e` must be a string
evaluating to the weight expression or variable name.

Use of `option()` communication: `ename_t` must have `option()` filled
in the weight type.

## Syntax

**beginoptions**`any dialog-programming command except`**beginoptions**`. . .`**endoptions**

Use of `option()` communication: None.

## Syntax

**option** `ename` \[`ename` \[ . . . \]\]

where `ename` must be a numeric control with 0 indicating that the
option is not desired.

Use of `option()` communication: `option()` specifies the name of the
option.

## Syntax

**optionarg** \[`style`\] `ename` \[ \[`style`\] `ename` \[. . .\] \]

where each `ename` may be a numeric or string control and `style` is

|                                                                                                                                      |                                    |
|--------------------------------------------------------------------------------------------------------------------------------------|------------------------------------|
| `style`                                                                                                                              | Meaning {p2line None}              |
| `/asis`                                                                                                                              | do not quote                       |
| `/quoted`                                                                                                                            | do quote                           |
| `/oquoted`                                                                                                                           | quote if necessary                 |
| [<strong>%</strong><var class="command">fmt</var><strong></strong>](http://www.stata.com/help.cgi?format) | for use with numeric {p2line None} |

Use of `option()` communication: `option()` specifies the name of the
option.

## Syntax

**stata**

**stata hidden** \[`immediate`\|`queue`\]

Use of `option()` communication: None.

## Syntax

**clear** \[`curstring`\|`cmdstring`\|`optstring`\]

Use of `option()` communication: None.

## Syntax

`create CHILD dialogname` \[`AS referenceName`\] \[`, nomodal`
`allowsubmit allowcopy message(string)`\]
