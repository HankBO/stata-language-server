## Syntax

Compute MI estimates of coefficients using previously saved estimation
results

`mi estimate using miestfile` \[`, options`\]

Compute MI estimates of transformed coefficients using previously saved
estimation results

`mi estimate` \[`spec`\] `using miestfile` \[`, options`\]

where `spec` may be one or more terms of the form `(`\[`name:`\]
`exp)`. `exp` is any function of the parameter estimates allowed by
[<strong>nlcom</strong>](http://www.stata.com/help.cgi?nlcom).

`miestfile.ster` contains estimation results previously saved by `mi`
`estimate, saving(miestfile)`; see
[<strong>[MI]</strong> mi estimate](http://www.stata.com/help.cgi?mi_estimate).

| Options                                                                                                                 |                        | Description                                                                                                                                       |
|-------------------------------------------------------------------------------------------------------------------------|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| Options                                                                                                                 |                        |                                                                                                                                                   |
|                                                                                                                         | `nimputations(#)`      | specify number of imputations to use; default is to use all existing imputations                                                                  |
|                                                                                                                         | `imputations(numlist)` | specify which imputations to use                                                                                                                  |
|                                                                                                                         | `estimations(numlist)` | specify which estimation results to use                                                                                                           |
|                                                                                                                         | `mcerror`              | compute Monte Carlo error estimates                                                                                                               |
|                                                                                                                         | `ufmitest`             | perform unrestricted FMI model test                                                                                                               |
|                                                                                                                         | `nosmall`              | do not apply small-sample correction to the degrees of freedom                                                                                    |
| Tables                                                                                                                  |                        |                                                                                                                                                   |
|                                                                                                                         | \[`no`\]`citable`      | suppress/display standard estimation table containing parameter-specific confidence intervals; default is `citable`                               |
|                                                                                                                         | `dftable`              | display degrees-of-freedom table; `dftable` implies `nocitable`                                                                                   |
|                                                                                                                         | `vartable`             | display variance information about estimates; `vartable` implies `citable`                                                                        |
|                                                                                                                         | `table_options`        | control table output                                                                                                                              |
|                                                                                                                         | `display_options`      | control columns and column formats, row spacing, display of omitted variables and base and empty cells, and factor-variable labeling              |
| Reporting                                                                                                               |                        |                                                                                                                                                   |
|                                                                                                                         | `level(#)`             | set confidence level; default is `level(95)`                                                                                                      |
|                                                                                                                         | `dots`                 | display dots as estimations are performed                                                                                                         |
|                                                                                                                         | `noisily`              | display any output from [<strong>nlcom</strong>](http://www.stata.com/help.cgi?nlcom) if transformations are specified |
|                                                                                                                         | `trace`                | trace `nlcom` if transformations are specified; implies `noisily`                                                                                 |
|                                                                                                                         | `replay`               | replay command-specific results from each individual estimation in `miestfile.ster`; implies `noisily`                                          |
|                                                                                                                         | `cmdlegend`            | display the command legend                                                                                                                        |
|                                                                                                                         | `nogroup`              | suppress summary about groups displayed for `xt` commands                                                                                         |
|                                                                                                                         | `me_options`           | control output from mixed-effects commands                                                                                                        |
| Advanced                                                                                                                |                        |                                                                                                                                                   |
|                                                                                                                         | `errorok`              | allow estimation even when `nlcom` errors out in some imputations; such imputations are discarded from the analysis                               |
|                                                                                                                         | `coeflegend`           | display legend instead of statistics                                                                                                              |
|                                                                                                                         | `nowarning`            | suppress the warning about varying estimation sample                                                                                              |
|                                                                                                                         | `noerrnotes`           | suppress error notes associated with failed estimation results in `miestfile.ster`                                                              |
|                                                                                                                         | `showimputations`      | show imputations saved in `miestfile.ster`                                                                                                      |
|                                                                                                                         | `eform_option`         | display coefficients table in exponentiated form                                                                                                  |
|                                                                                                                         | `post`                 | post estimated coefficients and VCE to `e(b)` and `e(V)`                                                                                          |
| `coeflegend`, `nowarning`, `noerrnotes`, `showimputations`, `eform_option`, and `post` do not appear in the dialog box. |                        |                                                                                                                                                   |

| table\_options |               | Description                                                                                            |
|----------------|---------------|--------------------------------------------------------------------------------------------------------|
|                | `noheader`    | suppress table header(s)                                                                               |
|                | `notable`     | suppress table(s)                                                                                      |
|                | `nocoef`      | suppress table output related to coefficients                                                          |
|                | `nocmdlegend` | suppress command legend that appears in the presence of transformed coefficients when `nocoef` is used |
|                | `notrcoef`    | suppress table output related to transformed coefficients                                              |
|                | `nolegend`    | suppress table legend(s)                                                                               |
|                | `nocnsreport` | do not display constraints                                                                             |

See
[<strong>[MI]</strong> mi estimate postestimation](http://www.stata.com/help.cgi?mi_estimate_postestimation)
for features available after estimation. To replay results, type `mi`
`estimate` without arguments.
