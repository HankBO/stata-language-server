## Syntax

`bayestest model` \[`namelist`\] \[`, options`\]

where `namelist` is a name, a list of names, `_all`, or `*`. A name may
be `.`, meaning the current (active) estimates. `_all` and `*` mean the
same thing.

| Options  |                           | Description                                                                                                                      |
|----------|---------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| Main     |                           |                                                                                                                                  |
|          | `prior(numlist)`          | specify prior probabilities for tested models; default is all models are equally likely                                          |
| Advanced |                           |                                                                                                                                  |
|          | `marglmethod(method)` | specify marginal-likelihood approximation method; default is to use Laplace-Metropolis approximation, `lmetropolis`; rarely used |

| method |               | Description                               |
|--------|---------------|-------------------------------------------|
|        | `lmetropolis` | Laplace-Metropolis approximation; default |
|        | `hmean`       | harmonic-mean approximation               |
