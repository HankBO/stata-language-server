## Syntax

`sem` ... \[`,` ... `method(method) vce(vcetype)` ...\]

method

Description

maximum likelihood; the default with missing values asymptotic
distribution free

vcetype

Description

observed information matrix; the default expected information matrix
outer product of gradients Satorra-Bentler estimator
Huber/White/sandwich estimator

`cluster clustvar`

generalized Huber/White/sandwich estimator

`bootstrap` \[`, bootstrap_options`\]

bootstrap estimation

`jackknife` \[`, jackknife_options`\]

jackknife estimation

`pweight`s and `iweight`s are not allowed with `sbentler`.

The following combinations of `method()` and `vce()` are allowed:

|`oimeimopgsbentlerrobustclusterbootstrapjackknife`

------------------------------------------------------------------------

<span options="+">{c +}_

------------------------------------------------------------------------

`ml`|`mlmv`|`adf`|

------------------------------------------------------------------------

<span options="BT">{c BT}_

------------------------------------------------------------------------
