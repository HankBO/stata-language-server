## Syntax

Single-stage design

`svyset` \[`psu`\] \[`weight`\] \[`, design_options options`\]

Multiple-stage design

`svyset psu` \[`weight`\] \[`, design_options`\] \[`|| ssu ,`
`design_options`\] ... \[`options`\]

Clear the current settings

`svyset, clear`

Report the current settings

`svyset`

`psu` identifies the primary sampling units and may be `_n` or
[varname](http://www.stata.com/help.cgi?varname).
In the single-stage syntax, `psu` is optional and defaults to `_n`.

`_n` indicates that individuals were randomly sampled if the design does
not involve clustered sampling.

`varname` contains identifiers for the clusters in a clustered sampling
design.

`ssu` is `_n` or
[varname](http://www.stata.com/help.cgi?varname)
containing identifiers for sampling units (clusters) in subsequent
stages of the survey design.

`_n` indicates that individuals were randomly sampled within the last
sampling stage.

| design\_options |                   | Description                  |
|-----------------|-------------------|------------------------------|
| Main            |                   |                              |
|                 | `strata(varname)` | variable identifying strata  |
|                 | `fpc(varname)`    | finite population correction |
|                 | `weight(varname)` | stage-level sampling weight  |

| options                                                                                                                                  |                                                                                                         | Description                                                                                                                                                                                                     |
|------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Weights                                                                                                                                  |                                                                                                         |                                                                                                                                                                                                                 |
|                                                                                                                                          | `brrweight(varlist)`                                                                                    | balanced repeated replicate (BRR) weights                                                                                                                                                                       |
|                                                                                                                                          | `fay(#)`                                                                                                | Fay's adjustment                                                                                                                                                                                                |
|                                                                                                                                          | `bsrweight(varlist)`                                                                                    | bootstrap replicate weights                                                                                                                                                                                     |
|                                                                                                                                          | `bsn(#)`                                                                                                | bootstrap mean-weight adjustment                                                                                                                                                                                |
|                                                                                                                                          | `jkrweight(`[varlist](http://www.stata.com/help.cgi?varlist)`, jkropts)` | jackknife replicate weights                                                                                                                                                                                     |
|                                                                                                                                          | `sdrweight(`[varlist](http://www.stata.com/help.cgi?varlist)`, sdropts)` | successive difference replicate (SDR) weights                                                                                                                                                                   |
| SE                                                                                                                                       |                                                                                                         |                                                                                                                                                                                                                 |
|                                                                                                                                          | `vce(linearized)`                                                                                   | Taylor linearized variance estimation                                                                                                                                                                           |
|                                                                                                                                          | `vce(bootstrap)`                                                                                        | bootstrap variance estimation                                                                                                                                                                                   |
|                                                                                                                                          | `vce(brr)`                                                                                              | BRR variance estimation                                                                                                                                                                                         |
|                                                                                                                                          | `vce(jackknife)`                                                                                    | jackknife variance estimation                                                                                                                                                                                   |
|                                                                                                                                          | `vce(sdr)`                                                                                              | SDR variance estimation                                                                                                                                                                                         |
|                                                                                                                                          | `dof(#)`                                                                                                | design degrees of freedom                                                                                                                                                                                       |
|                                                                                                                                          | `mse`                                                                                                   | use the MSE formula with `vce(bootstrap)`, `vce(brr)`, `vce(jackknife)`, or `vce(sdr)`                                                                                                                          |
|                                                                                                                                          | `singleunit(method)`                                                                                    | strata with a single sampling unit; `method` may be `missing`, `certainty`, `scaled`, or `centered`                                                                                                             |
| Poststratification                                                                                                                       |                                                                                                         |                                                                                                                                                                                                                 |
|                                                                                                                                          | `poststrata(varname)`                                                                                   | variable identifying poststrata                                                                                                                                                                                 |
|                                                                                                                                          | `postweight(varname)`                                                                                   | poststratum population sizes                                                                                                                                                                                    |
| Calibration                                                                                                                              |                                                                                                         |                                                                                                                                                                                                                 |
|                                                                                                                                          | `rake(`[varlist](http://www.stata.com/help.cgi?varlist)`, calopts)`      | adjust weights using the raking-ratio method                                                                                                                                                                    |
|                                                                                                                                          | `regress(`[varlist](http://www.stata.com/help.cgi?varlist)`, calopts)`   | adjust weights using linear regression calibration                                                                                                                                                              |
|                                                                                                                                          | `clear`                                                                                                 | clear all settings from the data                                                                                                                                                                                |
|                                                                                                                                          | `noclear`                                                                                               | change some of the settings without clearing the others                                                                                                                                                         |
|                                                                                                                                          | `clear(opnames)`                                                                                        | clear the specified settings without clearing all others; `opnames` may be one or more of `weight`, `vce`, `dof`, `mse`, `bsrweight`, `brrweight`, `jkrweight`, `sdrweight`, `poststrata`, `rake`, or `regress` |
| `pweight`s and `iweight`s are allowed; see [<strong>weights</strong>](http://www.stata.com/help.cgi?weights). |                                                                                                         |                                                                                                                                                                                                                 |
| `clear`, `noclear`, and `clear()` are not shown in the dialog box.                                                                       |                                                                                                         |                                                                                                                                                                                                                 |

| jkropts |                                   | Description                                                      |
|---------|-----------------------------------|------------------------------------------------------------------|
|         | `stratum(#` \[`#` ...\]`)`    | stratum identifier for each jackknife replicate weight           |
|         | `fpc(#` \[`#` ...\]`)`        | finite population correction for each jackknife replicate weight |
|         | `multiplier(#` \[`#` ...\]`)` | variance multiplier for each jackknife replicate weight          |
|         | `reset`                           | reset characteristics for each jackknife replicate weight        |

| sdropts |                          | Description                                      |
|---------|--------------------------|--------------------------------------------------|
|         | `fpc(#` \[`#` ...\]`)` | finite population correction for the SDR weights |

| calopts                    |                | Description                                           |
|----------------------------|----------------|-------------------------------------------------------|
| \*                         | `totals(spec)` | population totals                                     |
|                            | `noconstant`   | suppress constant term                                |
|                            | `ll(#)`        | lower limit for weight ratios                         |
|                            | `ul(#)`        | upper limit for weight ratios                         |
|                            | `iterate(#)`   | maximum number of iterations                          |
|                            | `tolerance(#)` | convergence tolerance                                 |
|                            | `force`        | allow calibration adjustments that failed to converge |
| \* `totals()` is required. |                |                                                       |
