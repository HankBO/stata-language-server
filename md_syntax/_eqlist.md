## Syntax

Declare an `_eqlist` object

`.obj` = `._eqlist.new` \[`, reset_options`\]

Reset parse settings

`.obj.reset` \[`, reset_options`\]

Parse the command line

`.obj.parse command_line`

where `command_line` is

`eqlist` _\[`if`\] \[`in`\]_ <span
class="command">\[`weight`\]_ \[`, global_options`\]

`eqlist` is one or more of the following equation specifications

\[`eqid:`\]
\[[depvarlist](http://www.stata.com/help.cgi?depvarlist)
\[`=`\]\]
\[[indepvars](http://www.stata.com/help.cgi?indepvars)\]
_\[`if`\] \[`in`\]_ <span
class="command">\[`weight`\]_ \[`, equation_options`\]

and multiple equations are assumed to be bound in parentheses or
delimited by `||`.

Report the number of parameters to `s(value)`:

`.obj.dim`

Mark the estimation sample:

`.obj.markout`
\[[varname](http://www.stata.com/help.cgi?varname)\]
\[`, markout_options`\]

Remove collinear predictors:

`.obj.rmcoll`
\[[varname](http://www.stata.com/help.cgi?varname)\]
\[`, markout_options`\]

Rebuild the command line:

`.obj.rebuild` \[`, rebuild_options`\]

| reset\_options                                                                                                                                                                                                                   |                         | Description                                                                                                                                                                                                                        |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                                                                                                                                                                                  | `eqopts(opt_name)`      | on/off options to recognize in an equation specification                                                                                                                                                                           |
|                                                                                                                                                                                                                                  | `eqargopts(opt_name)`   | options with arguments to recognize in an equation specification                                                                                                                                                                   |
|                                                                                                                                                                                                                                  | `needvarlist`           | equation specifications require a [varlist](http://www.stata.com/help.cgi?varlist)                                                                                                                      |
|                                                                                                                                                                                                                                  | `commonopts(opt_spec)`  | options not specific to equations                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                  | `markopts(opt_name)`    | options taking a [varlist](http://www.stata.com/help.cgi?varlist) that should be marked for the estimation sample                                                                                       |
|                                                                                                                                                                                                                                  | `rmcollopts(opt_name)`  | options taking a [varlist](http://www.stata.com/help.cgi?varlist) that should be checked for collinear variables                                                                                        |
|                                                                                                                                                                                                                                  | `rmdcollopts(opt_name)` | options taking a [varlist](http://www.stata.com/help.cgi?varlist) with [depvarlist](http://www.stata.com/help.cgi?depvarlist) that should be checked for collinear variables |
|                                                                                                                                                                                                                                  | `numdepvars(#)`         | minimum number of [depvarlist](http://www.stata.com/help.cgi?depvarlist) required in each equation specification; default is 1                                                                          |
|                                                                                                                                                                                                                                  | `needequal`             | an equal sign is required for separating the [depvarlist](http://www.stata.com/help.cgi?depvarlist) from the [indepvars](http://www.stata.com/help.cgi?indepvars)            |
|                                                                                                                                                                                                                                  | `wtypes(weight_types)`  | allowed weight types; default is none                                                                                                                                                                                              |
|                                                                                                                                                                                                                                  | `ignorecons`            | ignore `noconstant` option                                                                                                                                                                                                         |
| `opt_spec` is an option specification as in [<strong>syntax</strong>](http://www.stata.com/help.cgi?syntax).                                                                                          |                         |                                                                                                                                                                                                                                    |
| `opt_name` is the name of an option for the `.parse` routine to identify. Use capital letters to specify minimum abbreviations as in [<strong>syntax</strong>](http://www.stata.com/help.cgi?syntax). |                         |                                                                                                                                                                                                                                    |

| markout\_options |                  | Description                                                                                 |
|------------------|------------------|---------------------------------------------------------------------------------------------|
|                  | `replace`        | replace the values in `varname`; default is to assume `varname` is a new variable           |
|                  | `alldepsmissing` | only mark out observations in which all the `depvars` in an equation contain missing values |

| rebuild\_options |                  | Description                                                                                                                                                                                            |
|------------------|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                  | `parentheses`    | bind equations in parentheses; default for specifications with two or more equations                                                                                                                   |
|                  | `unparfirsteq`   | do not bind the first equation in parentheses                                                                                                                                                          |
|                  | `or`             | delimit equations with `||` instead of binding them in parentheses                                                                                                                                     |
|                  | `equal`          | separate [depvarlist](http://www.stata.com/help.cgi?depvarlist) from the [indepvars](http://www.stata.com/help.cgi?indepvars) with an equal sign |
|                  | `unequalfirsteq` | do not put an equal sign in the first equation                                                                                                                                                         |
