## Syntax

Test one interval hypothesis about continuous or discrete parameter

`bayestest interval exspec` \[`, luspec options`\]

Test one point hypothesis about discrete parameter

`bayestest interval exspec==#` \[`, options`\]

Test multiple hypotheses separately

`bayestest interval (testspec)` \[`(testspec)` ...\] \[`,`
`options`\]

Test multiple hypotheses jointly

`bayestest interval (jointspec)` \[`, options`\]

Full syntax

`bayestest interval (spec)` \[`(spec)` ...\] \[`,`
`options`\]

`exspec` is optionally labeled expression of model parameters,
\[`prlabel:`\]`expr`, where `prlabel` is a valid Stata name (or
`prob#` by default), and `expr` is a
[<strong>scalar model parameter</strong>](bayes_glossary##scalar_model_parameter)
or scalar expression containing (parentheses are optional) scalar model
parameters. The expression `expr` may not contain variable names.

`testspec` is `exspec`\[`, luspec`\] or `exspec==#` for discrete
parameters only.

`jointspec` is \[`prlabel:`\]`(testspec) (testspec)`
...`, joint`. The labels (if any) of `testspec` are ignored.

`spec` is one of `testspec` or `jointspec`.

|          |                                                               |                       |
|----------|---------------------------------------------------------------|-----------------------|
| `luspec` |                                                               | Null hypothesis       |
|          | `lower(#)` \[`upper(.)`\]                                     | `theta > #`           |
|          | `lower(`\#`,inclusive)` \[`upper(.)`\]                    | `theta >= #`          |
|          | \[`lower(.)`\] `upper(#)`                                     | `theta < #`           |
|          | \[`lower(.)`\] `upper(`\#`,inclusive)`                    | `theta <= #`          |
|          | `lower(#_l) upper(#_u)`                                     | `#_l < theta < #_u`   |
|          | `lower(#_l) upper(#_u,inclusive)`                   | `#_l < theta <= #_u`  |
|          | `lower(#_l,inclusive) upper(#_u)`                   | `#_l <= theta < #_u`  |
|          | `lower(#_l,inclusive) upper(#_u,inclusive)` | `#_l <= theta <= #_u` |

`lower(intspec)` and `upper(intspec)` specify the lower- and
upper-interval values, respectively.

`intspec` is

`#` \[`, inclusive`\]

where \# is the interval value, and suboption `inclusive` specifies that
this value should be included in the interval, meaning a closed
interval. Closed intervals make sense only for discrete parameters.

`intspec` may also contain a dot (`.`), meaning negative infinity for
`lower()` and positive infinity for `upper()`. Either option `lower(.)`
or option `upper(.)` must be specified.

| Options  |              | Description                                                            |
|----------|--------------|------------------------------------------------------------------------|
| Main     |              |                                                                        |
|          | `skip(#)`    | skip every `#` observations from the MCMC sample; default is `skip(0)` |
|          | `nolegend`   | suppress table legend                                                  |
| Advanced |              |                                                                        |
|          | `corrlag(#)` | specify maximum autocorrelation lag; default varies                    |
|          | `corrtol(#)` | specify autocorrelation tolerance; default is `corrtol(0.01)`          |
