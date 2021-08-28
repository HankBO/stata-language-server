## Syntax

Survey design characteristics

`estat svyset`

Design and misspecification effects for point estimates

`estat effects` \[`, estat_effects_options`\]

Design and misspecification effects for linear combinations of point
estimates

`estat lceffects exp` \[`, estat_lceffects_options`\]

Subpopulation sizes

`estat size` \[`, estat_size_options`\]

Subpopulation standard-deviation estimates

`estat sd` \[`, estat_sd_options`\]

Singleton and certainty strata

`estat strata`

Coefficient of variation for survey data

`estat cv` \[`, estat_cv_options`\]

Goodness-of-fit test for binary response models using survey data

`estat gof` _\[`if`\] \[`in`\]_ \[`,`
`estat_gof_options`\]

Display covariance matrix estimates

`estat vce` \[`, estat_vce_options`\]

estat\_effects\_options

Description

report DEFF design effects report DEFT design effects report design
effects, assuming SRS within subpopulation report MEFF design effects
report MEFT design effects

`display_options`

control spacing and display of omitted variables and base and empty
cells

estat\_lceffects\_options

Description

report DEFF design effects report DEFT design effects report design
effects, assuming SRS within subpopulation report MEFF design effects
report MEFT design effects

estat\_size\_options

Description

report number of observations (within subpopulation) report
subpopulation sizes

estat\_sd\_options

Description

report subpopulation variances instead of standard deviations report
standard deviations, assuming SRS within subpopulation

| estat\_cv\_options |                   | Description                                                               |
|--------------------|-------------------|---------------------------------------------------------------------------|
|                    | `nolegend`        | suppress the table legend                                                 |
|                    | `display_options` | control spacing and display of omitted variables and base and empty cells |

estat\_gof\_options

Description

compute test statistic using quantiles compute test statistic using the
total estimator instead of the mean

{p\_end None}

|       |                                                             |
|-------|-------------------------------------------------------------|
| `all` | execute test for all observations in the data {p2line None} |
