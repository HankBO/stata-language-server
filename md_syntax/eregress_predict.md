## Syntax

You previously fit the model

`eregress y x1,`

The equation specified immediately after the `eregress` command is
called the main equation. It is

`yx1y`

`predict` calculates predictions for `y` in the main equation. The other
equations in the model are called auxiliary equations or complications.

The syntax of `predict` is

`predict` _\[`type`\] \[_
[newvar](http://www.stata.com/help.cgi?newvar)
_\[`if`\] \[`in`\]_ \[`, stdstatistics`
`howcalculated`\]

| stdstatistics |        | Description                                   |
|---------------|--------|-----------------------------------------------|
|               | `mean` | linear prediction; the default                |
|               | `xb`   | linear prediction excluding all complications |

| howcalculated |                    | Description                                         |
|---------------|--------------------|-----------------------------------------------------|
|               | default            | not fixed; base values from data                    |
|               | `fix(endogvars)`   | fix specified endogenous covariates                 |
|               | `base(valspecs)`   | specify base values of any variables                |
|               | `target(valspecs)` | more convenient way to specify `fix()` and `base()` |

Note: The `fix()` and `base()` options affect results only in models
with endogenous variables in the main equation. The `target()` option is
sometimes a more convenient way to specify the `fix()` and `base()`
options.

`endogvars` are names of one or more endogenous variables appearing in
the main equation.

`valspecs` specify the values for variables at which predictions are to
be evaluated. Each `valspec` is of the form

`varname=#varname=(exp)varname=othervarname`

For instance, `base(valspecs)` could be `base(w1=0)` or
`base(w1=0 w2=1)`.

Notes:

\(1\) `predict` can also calculate treatment-effect statistics. See
[<strong>[ERM] predict treatment</strong>](http://www.stata.com/help.cgi?erm_predict_treatment).

\(2\) `predict` can also make predictions for the other equations in
addition to the main-equation predictions discussed here. See
[<strong>[ERM] predict advanced</strong>](http://www.stata.com/help.cgi?erm_predict_advanced).
