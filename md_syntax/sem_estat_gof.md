## Syntax

`estat gof` \[`, options`\]

| Options |                   | Description                         |
|---------|-------------------|-------------------------------------|
|         | `stats(statlist)` | statistics to be displayed          |
|         | `nodescribe`      | suppress descriptions of statistics |

| statlist |             | Description                              |
|----------|-------------|------------------------------------------|
|          | `chi2`      | chi-squared tests; the default           |
|          | `rmsea`     | root mean squared error of approximation |
|          | `ic`        | information indices                      |
|          | `indices`   | indices for comparison against baseline  |
|          | `residuals` | measures based on residuals              |
|          | `all`       | all the above                            |

Note: The statistics reported by `chi2`, `rmsea`, and `indices` are
dependent on the assumption of joint normality of the observed
variables. If ` vce(sbentler)` is specified with `sem`, modified
versions of these statistics that are computed using the Satorra-Bentler
scaled chi-squared statistics will also be reported.
