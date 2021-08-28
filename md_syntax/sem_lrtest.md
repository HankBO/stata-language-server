## Syntax

{`semgsem`<span options=")-">{c
)-}_`,`{right None:(fit model 1) }

`estimates store modelname1`

{`semgsem`<span options=")-">{c
)-}_`,`{right None:(fit model 2) }

`estimates store modelname2`

`lrtestmodelname1modelname2`{right None:(compare models) }

where one of the models is constrained and the other is unconstrained.
`lrtest` counts parameters to determine which model is constrained and
which is unconstrained, so it does not matter which model is which.

Warning concerning use with `sem`: Do not omit variables, observed or
latent, from the model. Constrain their coefficients to be 0 instead.
The models being compared must contain the same set of variables. This
is because the standard SEM likelihood value is a function of the
variables appearing in the model. Despite this fact, use of `lrtest` is
appropriate under the relaxed conditional normality assumption.

Note concerning `gsem`: The above warning does not apply to `gsem` just
as it does not apply to other Stata estimation commands. Whether you
omit variables or constrain coefficients to 0, results will be the same.
The generalized SEM likelihood is conditional on the exogenous
variables.
