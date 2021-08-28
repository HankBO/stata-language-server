## Syntax

Basic linear regression with endogenous covariates

`eregress`
[depvar](http://www.stata.com/help.cgi?depvar)
\[[indepvars](http://www.stata.com/help.cgi?indepvars)\]`,`
`endogenous(`[<var class="command">depvars</var>_en<strong></strong>](#enspec)
`=`
[<var class="command">varlist</var>_en<strong></strong>](#enspec)`)`
\[[<var class="command">options</var><strong></strong>](#synoptions)\]

Basic linear regression with endogenous treatment assignment

`eregress`
[depvar](http://www.stata.com/help.cgi?depvar)
\[[indepvars](http://www.stata.com/help.cgi?indepvars)\]`,`
`entreat(`[<var class="command">depvar</var>_tr<strong></strong>](#entrspec)
\[`=`
[<var class="command">varlist</var>_tr<strong></strong>](#entrspec)\]`)`
\[[<var class="command">options</var><strong></strong>](#synoptions)\]

Basic linear regression with exogenous treatment assignment

`eregress`
[depvar](http://www.stata.com/help.cgi?depvar)
\[[indepvars](http://www.stata.com/help.cgi?indepvars)\]`,`
`extreat(`[<var class="command">tvar</var><strong></strong>](#extrspec)`)`
\[[<var class="command">options</var><strong></strong>](#synoptions)\]

Basic linear regression with sample selection

`eregress`
[depvar](http://www.stata.com/help.cgi?depvar)
\[[indepvars](http://www.stata.com/help.cgi?indepvars)\]`,`
`select(`[<var class="command">depvar</var>_s<strong></strong>](#selspec)
`=`
[<var class="command">varlist</var>_s<strong></strong>](#selspec)`)`
\[[<var class="command">options</var><strong></strong>](#synoptions)\]

Basic linear regression with tobit sample selection

`eregress`
[depvar](http://www.stata.com/help.cgi?depvar)
\[[indepvars](http://www.stata.com/help.cgi?indepvars)\]`,`
`tobitselect(`[<var class="command">depvar</var>_s<strong></strong>](#tselspec)
`=`
[<var class="command">varlist</var>_s<strong></strong>](#tselspec)`)`
\[[<var class="command">options</var><strong></strong>](#synoptions)\]

Linear regression combining endogenous covariates, treatment, and
selection

`eregress`
[depvar](http://www.stata.com/help.cgi?depvar)
\[[indepvars](http://www.stata.com/help.cgi?indepvars)\]
_\[`if`\] \[`in`\]_
\[[<var class="command">weight</var><strong></strong>](#weight)\]
\[`,`
[<var class="command">extensions</var><strong></strong>](#extensions)
[<var class="command">options</var><strong></strong>](#synoptions)\]

| extensions |                         | Description                                      |
|------------|-------------------------|--------------------------------------------------|
| Model      |                         |                                                  |
|            | `endogenous(enspec)`    | model for endogenous covariates; may be repeated |
|            | `entreat(entrspec)`     | model for endogenous treatment assignment        |
|            | `extreat(extrspec)`     | exogenous treatment                              |
|            | `select(selspec)`       | probit model for selection                       |
|            | `tobitselect(tselspec)` | tobit model for selection                        |

| Options      |                                                                                            | Description                                                                                                                                      |
|--------------|--------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| Model        |                                                                                            |                                                                                                                                                  |
|              | `noconstant`                                                                               | suppress constant term                                                                                                                           |
|              | `offset(`[varname](http://www.stata.com/help.cgi?varname)\_o`)` | include `varname`\_o in model with coefficient constrained to 1                                                                                  |
|              | `constraints(numlist)`                                                                     | apply specified linear constraints                                                                                                               |
|              | `collinear`                                                                                | keep collinear variables                                                                                                                         |
| SE/Robust    |                                                                                            |                                                                                                                                                  |
|              | `vce(vcetype)`                                                                             | `vcetype` may be `oim`, `robust`, `cluster clustvar`, `opg`, `bootstrap`, or `jackknife`                                                       |
| Reporting    |                                                                                            |                                                                                                                                                  |
|              | `level(#)`                                                                                 | set confidence level; default is `level(95)`                                                                                                     |
|              | `nocnsreport`                                                                              | do not display constraints                                                                                                                       |
|              | `display_options`                                                                          | control columns and column formats, row spacing, line width, display of omitted variables and base and empty cells, and factor-variable labeling |
| Integration  |                                                                                            |                                                                                                                                                  |
|              | `intpoints(#)`                                                                             | set the number of integration (quadrature) points for integration over four or more dimensions; default is `intpoints(128)`                      |
|              | `triintpoints(#)`                                                                          | set the number of integration (quadrature) points for integration over three dimensions; default is `triintpoints(10)`                           |
| Maximization |                                                                                            |                                                                                                                                                  |
|              | `maximize_options`                                                                         | control the maximization process; seldom used                                                                                                    |
|              | `coeflegend`                                                                               | display legend instead of statistics                                                                                                             |

`enspec` is
[depvarlist](http://www.stata.com/help.cgi?depvarlist)\_en
`=`
[varlist](http://www.stata.com/help.cgi?varlist)\_en
\[`,`
[<var class="command">enopts</var><strong></strong>](#enopts)\]

where `depvars`\_en is a list of endogenous covariates. Each variable in
`depvars`\_en specifies an endogenous covariate model using the common
`varlist`\_en and options.

`entrspec` is
[depvar](http://www.stata.com/help.cgi?depvar)\_tr
\[`=`
[varlist](http://www.stata.com/help.cgi?varlist)\_tr\]
\[`,`
[<var class="command">entropts</var><strong></strong>](#entropts)\]

where `depvar`\_tr is a variable indicating treatment assignment.
`varlist`\_tr is a list of covariates predicting treatment assignment.

`extrspec` is `tvar` \[`,`
[<var class="command">extropts</var><strong></strong>](#extropts)\]

where `tvar` is a variable indicating treatment assignment.

`selspec` is
[depvar](http://www.stata.com/help.cgi?depvar)\_s
`=`
[varlist](http://www.stata.com/help.cgi?varlist)\_s
\[`, noconstant`
`offset(`[varname](http://www.stata.com/help.cgi?varname)\_o`)`\]

where `depvar`\_s is a variable indicating selection status. `depvar`\_s
must be coded as 0, indicating that the observation was not selected, or
1, indicating that the observation was selected. `varlist`\_s is a list
of covariates predicting selection.

`tselspec` is
[depvar](http://www.stata.com/help.cgi?depvar)\_s
`=`
[varlist](http://www.stata.com/help.cgi?varlist)\_s
\[`,`
[<var class="command">tselopts</var><strong></strong>](#tselopts)\]

where `depvar`\_s is a continuous variable. `varlist`\_s is a list of
covariates predicting `depvar`\_s. The censoring status of `depvar`\_s
indicates selection, where a censored `depvar`\_s indicates that the
observation was not selected and a noncensored `depvar`\_s indicates
that the observation was selected.

| enopts |                 | Description                                                                                   |
|--------|-----------------|-----------------------------------------------------------------------------------------------|
| Model  |                 |                                                                                               |
|        | `probit`        | treat endogenous covariate as binary                                                          |
|        | `oprobit`       | treat endogenous covariate as ordinal                                                         |
|        | `povariance`    | estimate a different variance for each level of a binary or an ordinal endogenous covariate   |
|        | `pocorrelation` | estimate different correlations for each level of a binary or an ordinal endogenous covariate |
|        | `nomain`        | do not add endogenous covariate to main equation                                              |
|        | `noconstant`    | suppress constant term                                                                        |

| entropts |                     | Description                                                    |
|----------|---------------------|----------------------------------------------------------------|
| Model    |                     |                                                                |
|          | `povariance`        | estimate a different variance for each potential outcome       |
|          | `pocorrelation`     | estimate different correlations for each potential outcome     |
|          | `nomain`            | do not add treatment indicator to main equation                |
|          | `nointeract`        | do not interact treatment with covariates in main equation     |
|          | `noconstant`        | suppress constant term                                         |
|          | `offset(varname_o)` | include `varname_o` in model with coefficient constrained to 1 |

| extropts |                 | Description                                                |
|----------|-----------------|------------------------------------------------------------|
| Model    |                 |                                                            |
|          | `povariance`    | estimate a different variance for each potential outcome   |
|          | `pocorrelation` | estimate different correlations for each potential outcome |
|          | `nomain`        | do not add treatment indicator to main equation            |
|          | `nointeract`    | do not interact treatment with covariates in main equation |

| tselopts |                                                                                          | Description                                                    |
|----------|------------------------------------------------------------------------------------------|----------------------------------------------------------------|
| Model    |                                                                                          |                                                                |
|          | `ll(`[varname](http://www.stata.com/help.cgi?varname)\|`#)` | left-censoring variable or limit                               |
|          | `ul(`[varname](http://www.stata.com/help.cgi?varname)\|`#)` | right-censoring variable or limit                              |
|          | `main`                                                                                   | add selection indicator to main equation                       |
|          | `noconstant`                                                                             | suppress constant term                                         |
|          | `offset(varname_o)`                                                                      | include `varname_o` in model with coefficient constrained to 1 |

`indepvars`, `varlist`\_en, `varlist`\_tr, and `varlist_s` may contain
factor variables; see
[<strong>fvvarlist</strong>](http://www.stata.com/help.cgi?fvvarlist).

`depvar`, `indepvars`, `depvars`\_en, `varlist`\_en, `depvar`\_tr,
`varlist`\_tr, `tvar`, `depvar_s`, and `varlist_s` may contain
time-series operators; see
[<strong>tsvarlist</strong>](http://www.stata.com/help.cgi?tsvarlist).

`bootstrap`, `by`, `jackknife`, `rolling`, `statsby`, and `svy` are
allowed; see
[<strong>prefix</strong>](http://www.stata.com/help.cgi?prefix).

Weights are not allowed with the
[<strong>bootstrap</strong>](http://www.stata.com/help.cgi?bootstrap)
prefix.

`vce()` and weights are not allowed with the
[<strong>svy</strong>](http://www.stata.com/help.cgi?svy)
prefix.

`fweight`s, `iweight`s, and `pweight`s are allowed; see
[<strong>weight</strong>](http://www.stata.com/help.cgi?weight).

`coeflegend` does not appear in the dialog box.

See
[<strong>[ERM]</strong> eregress postestimation](http://www.stata.com/help.cgi?eregress_postestimation)
for features available after estimation.
