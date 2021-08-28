## Syntax

Overview

`long`<span options="TLC">{c TLC}_

------------------------------------------------------------------------

<span options="TRC">{c TRC}_`wide`|`i  jstub`|<span
options="TLC">{c TLC}_

------------------------------------------------------------------------

<span options="TRC">{c TRC}_|

------------------------------------------------------------------------

||`istub`**1**`stub`**2**|<span
options="|">{c \|}_**1**|<span
options="|">{c \|}_

------------------------------------------------------------------------

||**2**<span
options="|">{c \|}_

------------------------------------------------------------------------

||<span
options="|">{c \|}_**1**|<span
options="|">{c \|}_|<span
options="|">{c \|}_**2**|<span
options="BLC">{c BLC}_

------------------------------------------------------------------------

<span options="BRC">{c BRC}_<span options="BLC">{c BLC}_

------------------------------------------------------------------------

<span options="BRC">{c BRC}_

`j` existing variable

/

`reshape widestub, i(i) j(j)reshape longstub, i(i) j(j)`

\\

`j` new variable

`reshape widereshape longreshape longreshape wide`

Basic syntax

Convert data from wide form to long form

`reshape` [<strong>long</strong>](#overview)
`stubnames,`
`i(`[varlist](http://www.stata.com/help.cgi?varlist)`)`
\[`options`\]

Convert data from long form to wide form

`reshape` [<strong>wide</strong>](#overview)
`stubnames,`
`i(`[varlist](http://www.stata.com/help.cgi?varlist)`)`
\[`options`\]

Convert data back to long form after using reshape wide

`reshape` [<strong>long</strong>](#overview)

Convert data back to wide form after using reshape long

`reshape` [<strong>wide</strong>](#overview)

List problem observations when reshape fails

`reshape error`

<table id="options_table" class="standard">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><var class="command">options</var></td>
<td>Description <span data-options="8">{col 8}_<span>{hline None}_</td>
</tr>
<tr class="even">
<td data-options="8 37 37 2 ">* <code class="command" data-options="i(varlist)">i(varlist)</code></td>
<td>use <var class="command">varlist</var> as the ID variables</td>
</tr>
<tr class="odd">
<td><code class="command">j(</code>[varname](http://www.stata.com/help.cgi?varname) [<var class="command">values</var>]<code class="command">)</code></td>
<td>long-&gt;wide: <var class="command">varname</var>, existing variable</td>
</tr>
<tr class="even">
<td></td>
<td>wide-&gt;long: <var class="command">varname</var>, new variable</td>
</tr>
<tr class="odd">
<td></td>
<td>optionally specify values to subset <var class="command">varname</var></td>
</tr>
<tr class="even">
<td><code class="command">string</code></td>
<td><var class="command">varname</var> is a string variable (default is numeric) <span data-options="8">{col 8}_<span>{hline None}_
* <code class="command" data-options="i(varlist)">i(varlist)</code> is required.</td>
</tr>
</tbody>
</table>

where `values` is<span options="2">{space 2}_`#`\[`-#`\] \[...\]
<span options="13">{space 13}_if `varname` is numeric

(default)

`"string"` \[`"string"` ...\]{nobreak None}

if `varname` is string

and where `stubnames` are variable names (long-&gt;wide), or stubs of
variable names (wide-&gt;long), and either way, may contain `@`,
denoting where `j` appears or is to appear in the name.

In the example above, when we wrote "`reshape wide stub`", we could
have written "`reshape wide stub@`" because `j` by default ends up
as a suffix. Had we written `stu@b`, then the wide variables would
have been named `stu1b` and `stu2b`.

Advanced syntax

`reshape i`
[varlist](http://www.stata.com/help.cgi?varlist)

`reshape j`
[varname](http://www.stata.com/help.cgi?varname)
\[`values`\] \[`, string`\]

`reshape xij fvarnames` \[`, atwl(chars)`\]

`reshape xi`
\[[varlist](http://www.stata.com/help.cgi?varlist)\]

`reshape` \[`query`\]

`reshape clear`
