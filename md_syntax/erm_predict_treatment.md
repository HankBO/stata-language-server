## Syntax

You previously fit a model by using the `entreat()` or `extreat()`
option,

`eregress   y    x1,entreat(treated =eintreg  yl yu  x1,entreat(treated =eprobit    y    x1,entreat(treated =eoprobit   y    x1,entreat(treated =eregress   y    x1,extreat(treated)eintreg  yl yu  x1,extreat(treated)eprobit    y    x1,extreat(treated)eoprobit   y    x1,extreat(treated)`

In these cases, `predict` has extra features. `predict`'s extra syntax
for these features is

`predict` _\[`type`\] \[_
[newvar](http://www.stata.com/help.cgi?newvar)
_\[`if`\] \[`in`\]_`,`
[<var class="command">treatstatistic</var><strong></strong>](#treatstatistic)
\[[<var class="command">treatmodifier</var><strong></strong>](#treatmodifier)
[<var class="command">oprobitmodifier</var><strong></strong>](#oprobitmodifier)\]

In some cases, more than one new variable needs to be specified:

`predict` _\[`type`\] \[_ <span
options="-(">{c -(}_`stub*`|[<var class="command">newvarlist</var><strong></strong>](http://www.stata.com/help.cgi?varlist)<span
options=")-">{c )-}_ _\[`if`\]
\[`in`\]_`,`
[<var class="command">treatstatistic</var><strong></strong>](#treatstatistic)
\[[<var class="command">treatmodifier</var><strong></strong>](#treatmodifier)
[<var class="command">oprobitmodifier</var><strong></strong>](#oprobitmodifier)\]

| treatstatistic |          | Description                           |
|----------------|----------|---------------------------------------|
|                | `pomean` | potential-outcome mean (POM)          |
|                | `te`     | treatment effect (TE)                 |
|                | `tet`    | treatment effect on the treated (TET) |

| treatmodifier |             | Description                                                                                                                                      |
|---------------|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
|               | `tlevel(#)` | treatment level for which [<var class="command">treatstatistic</var><strong></strong>](#treatstatistic) is calculated |

`#` may be specified as a value recorded in variable `treated`, such as
1, 2, ... or such as 1, 5, ..., depending on the values recorded.

`#` may also be specified as `#1`, `#2`, ..., meaning the first, second,
... values recorded in `treated`.

| oprobitmodifier |               | Description                                                                                                                                      |
|-----------------|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
|                 | `outlevel(#)` | ordered outcome for which [<var class="command">treatstatistic</var><strong></strong>](#treatstatistic) is calculated |

When used after models fit with `eoprobit`, `treatstatistic` is
calculated for the specified outcome, or for the first outcome if you do
not specify otherwise.

`outlevel(#)` specifies the outcome for which statistics are to be
calculated. `#` is specified in the same way as with `tlevel()`, but the
meaning is different. In the case of `outlevel()`, you are specifying
the outcome, not the treatment level.
