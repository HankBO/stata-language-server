## Syntax

`erm_cmd` ... \[`, extensions`
[<var class="command">options</var><strong></strong>](#synoptions)\]

`erm_cmd` is one of
[<strong>eregress</strong>](http://www.stata.com/help.cgi?eregress),
[<strong>eprobit</strong>](http://www.stata.com/help.cgi?eprobit),
[<strong>eoprobit</strong>](http://www.stata.com/help.cgi?eoprobit),
or
[<strong>eintreg</strong>](http://www.stata.com/help.cgi?eintreg).

| extensions |                         | Description                                      |
|------------|-------------------------|--------------------------------------------------|
| Model      |                         |                                                  |
|            | `endogenous(enspec)`    | model for endogenous covariates; may be repeated |
|            | `entreat(entrspec)`     | model for endogenous treatment assignment        |
|            | `extreat(extrspec)`     | exogenous treatment                              |
|            | `select(selspec)`       | probit model for selection                       |
|            | `tobitselect(tselspec)` | tobit model for selection                        |

| Options      |                                                                                                     | Description                                                                                                                                      |
|--------------|-----------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| Model        |                                                                                                     |                                                                                                                                                  |
|              | `noconstant`                                                                                        | suppress constant term                                                                                                                           |
|              | `offset(`[varname](http://www.stata.com/help.cgi?varname)\_o`)`          | include `varname`\_o in model with coefficient constrained to 1                                                                                  |
|              | `constraints(numlist)`                                                                              | apply specified linear constraints                                                                                                               |
|              | `collinear`                                                                                         | keep collinear variables                                                                                                                         |
| SE/Robust    |                                                                                                     |                                                                                                                                                  |
|              | `vce(vcetype)`                                                                                      | `vcetype` may be `oim`, `robust`, `cluster clustvar`, `opg`, `bootstrap`, or `jackknife`                                                       |
| Reporting    |                                                                                                     |                                                                                                                                                  |
|              | `level(#)`                                                                                          | set confidence level; default is `level(95)`                                                                                                     |
|              | `nocnsreport`                                                                                       | do not display constraints                                                                                                                       |
|              | `display_options`                                                                                   | control columns and column formats, row spacing, line width, display of omitted variables and base and empty cells, and factor-variable labeling |
| Integration  |                                                                                                     |                                                                                                                                                  |
|              | `intpoints(#)`                                                                                      | set the number of integration (quadrature) points for integration over four or more dimensions; default is `intpoints(128)`                      |
|              | `triintpoints(#)`                                                                                   | set the number of integration (quadrature) points for integration over three dimensions; default is `triintpoints(10)`                           |
| Maximization |                                                                                                     |                                                                                                                                                  |
|              | [<var class="command">maximize_options</var><strong></strong>](#maxopts) | control the maximization process; seldom used                                                                                                    |
|              | `coeflegend`                                                                                        | display legend instead of statistics                                                                                                             |

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

| enopts                                                                                                                                                                                                                                                                                                                                                                                         |                                                                                          | Description                                                                                   |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| Model                                                                                                                                                                                                                                                                                                                                                                                          |                                                                                          |                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                | `probit`                                                                                 | treat endogenous covariate as binary                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                | `oprobit`                                                                                | treat endogenous covariate as ordinal                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                | `povariance`                                                                             | estimate a different variance for each level of a binary or an ordinal endogenous covariate   |
|                                                                                                                                                                                                                                                                                                                                                                                                | `pocorrelation`                                                                          | estimate different correlations for each level of a binary or an ordinal endogenous covariate |
|                                                                                                                                                                                                                                                                                                                                                                                                | `nomain`                                                                                 | do not add endogenous covariate to main equation                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                | `noconstant`                                                                             | suppress constant term                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                | `pocorrelation`                                                                          | estimate different correlations for each potential outcome                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                | `nomain`                                                                                 | do not add treatment indicator to main equation                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                | `nocutsinteract`                                                                         | do not interact treatment with cutpoints                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                | `nointeract`                                                                             | do not interact treatment with covariates in main equation                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                | `noconstant`                                                                             | suppress constant term                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                | `offset(varname_o)`                                                                      | include `varname_o` in model with coefficient constrained to 1                                |
|                                                                                                                                                                                                                                                                                                                                                                                                | `pocorrelation`                                                                          | estimate different correlations for each potential outcome                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                | `nomain`                                                                                 | do not add treatment indicator to main equation                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                | `nocutsinteract`                                                                         | do not interact treatment with cutpoints                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                | `nointeract`                                                                             | do not interact treatment with covariates in main equation                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                | `ul(`[varname](http://www.stata.com/help.cgi?varname)\|`#)` | right-censoring variable or limit                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                | `main`                                                                                   | add selection indicator to main equation                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                | `noconstant`                                                                             | suppress constant term                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                | `offset(varname_o)`                                                                      | include `varname_o` in model with coefficient constrained to 1                                |
| `povariance` is available only with `eregress` and `eintreg`. <span options="entropts">{marker entropts}_{nobreak None} {synopthdr None:entropts} {synoptline None} {syntab None:Model} {synopt None}`povariance`estimate a different variance for each potential outcome                                                                                                                |                                                                                          |                                                                                               |
| `povariance` is available only with `eregress` and `eintreg`.                                                                                                                                                                                                                                                                                                                                  |                                                                                          |                                                                                               |
| `nocutsinteract` is available only with `eoprobit`. <span options="extropts">{marker extropts}_{nobreak None} {synopthdr None:extropts} {synoptline None} {syntab None:Model} {synopt None}`povariance`estimate a different variance for each potential outcome                                                                                                                          |                                                                                          |                                                                                               |
| `povariance` is available only with `eregress` and `eintreg`.                                                                                                                                                                                                                                                                                                                                  |                                                                                          |                                                                                               |
| `nocutsinteract` is available only with `eoprobit`. <span options="tselopts">{marker tselopts}_{nobreak None} <span options="31 tabbed">{synoptset 31 tabbed}_{nobreak None} {synopthdr None:tselopts} {synoptline None} {syntab None:Model} {synopt None}`ll(`[varname](http://www.stata.com/help.cgi?varname)\|`#)`left-censoring variable or limit |                                                                                          |                                                                                               |
