## Syntax

`bayesstats ic` \[`namelist`\] \[`, options`\]

where `namelist` is a name, a list of names, `_all`, or `*`. A name may
be `.`, meaning the current (active) estimates. `_all` and `*` mean the
same thing.

| Options  |                       | Description                                                                                                                      |
|----------|-----------------------|----------------------------------------------------------------------------------------------------------------------------------|
| Main     |                       |                                                                                                                                  |
|          | `basemodel(name)`     | specify a base or reference model; default is the first-listed model                                                             |
|          | `bayesfactor`         | report BFs instead of the default log BFs                                                                                        |
|          | `diconly`             | report only DIC                                                                                                                  |
| Advanced |                       |                                                                                                                                  |
|          | `marglmethod(method)` | specify marginal-likelihood approximation method; default is to use Laplace-Metropolis approximation, `lmetropolis`; rarely used |

| method |               | Description                                   |
|--------|---------------|-----------------------------------------------|
|        | `lmetropolis` | Laplace-Metropolis approximation; the default |
|        | `hmean`       | harmonic-mean approximation                   |
