## Syntax

Direct standardization

`dstdize charvar popvar stratavars` _\[`if`\]
\[`in`\]_`, by(groupvars)` \[`dstdize_options`\]

Indirect standardization

`istdize casevar_s popvar_s stratavars` <span
class="command">\[`if`\] \[`in`\]_ `using filename,`
{`popvars(casevar_p popvar_p)` \|  
{opt rate(ratevar\_p {\#\|crudevar\_p})}} \[`istdize_options`\]

`charvar` is the characteristic to be standardized across different
subpopulations identified by `groupvars`.

`popvar` defines the weights used in standardization.

`stratavars` defines the strata across which the weights are to be
averaged in `dstdize`. For `istdize`, `stratavars` defines the strata
for which `casevar_s` is measured.

`casevar_s` is the variable name for the study population's number of
cases. If `by(groupvars)` is specified, `casevar_s` must be constant or
missing within each group defined by combinations of `groupvars`.

`popvar_s` identifies the number of subjects in each strata in the study
population.

`filename` must be a Stata dataset and contain `popvar` and
`stratavars`.

| dstdize\_options                |                    | Description                                                       |
|---------------------------------|--------------------|-------------------------------------------------------------------|
| Main                            |                    |                                                                   |
| \*                              | `"by(groupvars)`   | study populations                                                 |
|                                 | `using(filename)`  | use standard population from Stata dataset                        |
|                                 | `base(#,string)`   | use standard population from a value of grouping variable         |
|                                 | `level(#)`         | set confidence level; default is `level(95)`                      |
| Options                         |                    |                                                                   |
|                                 | `saving(filename)` | save computed standard population distribution as a Stata dataset |
|                                 | `format(%fmt)`     | final summary table display format; default is `%10.0g`           |
|                                 | `print`            | include table summary of standard population in output            |
|                                 | `nores`            | suppress storing results in `r()`                                 |
| \* `by(groupvars)` is required. |                    |                                                                   |

istdize\_options

Description

Main

\*

`popvars(casevar_p popvar_p)`

for standard population, `casevar_p` is number of cases and `popvar_p`
is number of individuals

`level(#)`

set confidence level; default is `level(95)`

{p2coldent : \* {opt rate(ratevar\_p {\#\|crudevar\_p})}}{it:ratevar\_p}
is stratum-specific rates and {it:\#} or {it:crudevar\_p} is the crude
case rate value or variable{p\_end}

Options

`"by(groupvars)`

variables identifying study populations

`format(%fmt)`

final summary table display format; default is `%10.0g`

`print`

include table summary of standard population in output

\* Either `popvars(casevar_p popvar_p)` or {opt rate(ratevar\_p
{\#\|crudevar\_p})} must be specified. <span options="menu">{marker
menu}_{nobreak None} {title None:Menu} {title None:dstdize}
{phang2 None} **Statistics &gt; Epidemiology and related &gt; Other &gt;
Direct standardization** {title None:istdize} {phang2 None} **Statistics
&gt; Epidemiology and related &gt; Other &gt; Indirect standardization**
<span options="description">{marker description}_{nobreak None}
{title None:Description} {pstd None} `dstdize` produces standardized
rates, a weighted average of the stratum-specific rates. {pstd None}
`istdize` produces indirectly standardized rates that are appropriate
when the stratum-specific rates for the population being studied are
either unavailable or unreliable. {pstd None} `istdize` also calculates
a point estimate and exact confidence interval for the study
population's standardized mortality ratio (SMR) or the standardized
incidence ratio. <span options="linkspdf">{marker
linkspdf}_{nobreak None} {title None:Links to PDF documentation}
[Quick start](http://www.stata.com/manuals14/rdstdizequickstart.pdf)
[Remarks and
examples](http://www.stata.com/manuals14/rdstdizeremarksandexamples.pdf)
[Methods and
formulas](http://www.stata.com/manuals14/rdstdizemethodsandformulas.pdf)
{pstd None} The above sections are not included in this help file. <span
options="options_dstdize">{marker options\_dstdize}_{nobreak None}
{title None:Options for dstdize} {dlgtab None:Main} {phang None}
`"by(groupvars)` is required for the `dstdize` command; it specifies the
variables identifying the study populations. If `base()` is also
specified, there must be only one variable in the `by()` group. If you
do not have a variable for this option, you can generate one by using
something like `generate newvar=1` and then use `newvar` as the argument
to this option. {phang None} `using(filename)` or `base(#,string)` may
be used to specify the standard population. You may not specify both
options. `using(filename)` supplies the name of a `.dta` file containing
the standard population. The standard population must contain the
`popvar` and the `stratavars`. If `using()` is not specified, the
standard population distribution will be obtained from the data.
`base(#,string)` lets you specify one of the values of `groupvar` --
either a numeric value or a string -- to be used as the standard
population. If neither `base()` nor `using()` is specified, the entire
dataset is used to determine an estimate of the standard population.
{phang None} `level(#)` specifies the confidence level, as a percentage,
for a confidence interval of the adjusted rate. The default is
`level(95)` or as set by
[<strong>set level</strong>](http://www.stata.com/help.cgi?set%20level).
{dlgtab None:Options} {phang None} `saving(filename)` saves the computed
standard population distribution as a Stata dataset that can be used in
further analyses. {phang None} `format(%fmt)` specifies the format in
which to display the final summary table. The default is `%10.0g`.
{phang None} `print` includes a table summary of the standard population
before displaying the study population results. {phang None} `nores`
suppresses storing results in `r()`. This option is seldom specified.
Some results are stored in matrices. If there are more groups than
`matsize`, `dstdize` will report "matsize too small". Then you can
either increase `matsize` or specify `nores`. The `nores` option does
not change how results are calculated but specifies that results need
not be left behind for use by other programs. <span
options="options_istdize">{marker options\_istdize}_{nobreak None}
{title None:Options for istdize} {dlgtab None:Main} {phang None}
`popvars(casevar_p popvar_p)` or {opt rate(ratevar\_p
{\#\|crudevar\_p})} must be specified with `istdize`. Only one of these
two options is allowed. These options are used to describe the standard
population's data. {pmore None} With `popvars(casevar_p popvar_p)`,
`casevar_p` records the number of cases (deaths) for each stratum in the
standard population, and `popvar_p` records the total number of
individuals in each stratum (individuals at risk). {pmore None} With
{opt rate(ratevar\_p {\#\|crudevar\_p})}, {it:ratevar\_p} contains the
stratum-specific rates. `#`\|`crudevar_p` specifies the crude case rate
either by a variable name or by the crude case rate value. If a crude
rate variable is used, it must be the same for all observations,
although it could be missing for some. {phang None} `level(#)` specifies
the confidence level, as a percentage, for a confidence interval of the
adjusted rate. The default is `level(95)` or as set by
[<strong>set level</strong>](http://www.stata.com/help.cgi?set%20level).
{dlgtab None:Options} {phang None} `"by(groupvars)` specifies variables
identifying study populations when more than one exists in the data. If
this option is not specified, the entire study population is treated as
one group. {phang None} `format(%fmt)` specifies the format in which to
display the final summary table. The default is `%10.0g`. {phang None}
`print` outputs a table summary of the standard population before
displaying the study population results. <span
options="examples">{marker examples}_{nobreak None} {title
None:Examples} {hline None} {pstd None}Setup

`. webuse hbp`

`. generate pop = 1`

Obtain standardized rates of `hbp` by `city` and `year`, using the
`age`, `race`, and `sex` distribution of the cities and years combined
as the standard

    dstdize hbp pop age race sex, by(city year)

------------------------------------------------------------------------

Setup

    webuse kahn, clear

Obtain mortality rates by `state` using the standard population saved in
`popkahn.dta`

    istdize death pop age using http://www.stata-press.com/data/r15/popkahn, by(state) pop(deaths pop) print

------------------------------------------------------------------------
