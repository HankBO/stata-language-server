## Syntax

`gsem paths` ...`,` ... `family_and_link_options`

| family\_and\_link\_options |                       | Description                                               |
|----------------------------|-----------------------|-----------------------------------------------------------|
|                            | `family(family)`      | distribution family; default is `family(gaussian)`        |
|                            | `link(link)`          | link function; default varies per family                  |
|                            | `cloglog`             | synonym for `family(bernoulli) link(cloglog)`             |
|                            | `exponential`         | synonym for `family(exponential) link(log)`               |
|                            | `gamma`               | synonym for `family(gamma) link(log)`                     |
|                            | `logit`               | synonym for `family(bernoulli) link(logit)`               |
|                            | `loglogistic`         | synonym for `family(loglogistic) link(log)`               |
|                            | `lognormal`           | synonym for `family(lognormal) link(log)`                 |
|                            | `llogistic`           | synonym for `family(llogistic) link(log)`                 |
|                            | `lnormal`             | synonym for `family(lnormal) link(log)`                   |
|                            | `mlogit`              | synonym for `family(multinomial) link(logit)`             |
|                            | `nbreg`               | synonym for `family(nbreg mean) link(log)`                |
|                            | `ocloglog`            | synonym for `family(ordinal) link(cloglog)`               |
|                            | `ologit`              | synonym for `family(ordinal) link(logit)`                 |
|                            | `oprobit`             | synonym for `family(ordinal) link(probit)`                |
|                            | `poisson`             | synonym for `family(poisson) link(log)`                   |
|                            | `probit`              | synonym for `family(bernoulli) link(probit)`              |
|                            | `regress`             | synonym for `family(gaussian) link(identity)`             |
|                            | `weibull`             | synonym for `family(weibull) link(log)`                   |
|                            | `exposure(varname_e)` | include ln(`varname_e`) with coefficient constrained to 1 |
|                            | `offset(varname_o)`   | include `varname_o` with coefficient constrained to 1     |

| family |                                                                                                   | Description                                      |
|--------|---------------------------------------------------------------------------------------------------|--------------------------------------------------|
|        | `gaussian` \[`, options`\]                                                                      | Gaussian (normal); the default                   |
|        | `bernoulli`                                                                                       | Bernoulli                                        |
|        | `beta`                                                                                            | beta                                             |
|        | `binomial` \[`#` \| [varname](http://www.stata.com/help.cgi?varname)\] | binomial; default number of binomial trials is 1 |
|        | `ordinal`                                                                                         | ordinal                                          |
|        | `multinomial`                                                                                     | multinomial                                      |
|        | `poisson` \[`, poisson`\]                                                                       | Poisson                                          |
|        | `nbinomial` \[`mean` \| `constant`\]                                                              | negative binomial; default dispersion is `mean`  |
|        | `exponential` \[`, survival`\]                                                                  | exponential                                      |
|        | `gamma` \[`, survival`\]                                                                        | gamma                                            |
|        | `loglogistic` \[`, survival`\]                                                                  | loglogistic                                      |
|        | `lognormal` \[`, survival`\]                                                                    | lognormal                                        |
|        | `weibull` \[`, survival`\]                                                                      | Weibull                                          |
|        | `pointmass #`                                                                                   | point-mass density at `#`                        |

| link |            | Description           |
|------|------------|-----------------------|
|      | `identity` | identity              |
|      | `log`      | log                   |
|      | `logit`    | logit                 |
|      | `probit`   | probit                |
|      | `cloglog`  | complementary log-log |

| options                                                     |                                                                                                 | Description                             |
|-------------------------------------------------------------|-------------------------------------------------------------------------------------------------|-----------------------------------------|
|                                                             | `ldepvar(varname)`                                                                              | lower depvar for interval-response data |
|                                                             | `udepvar(varname)`                                                                              | upper depvar for interval-response data |
|                                                             | `lcensored(`[varname](http://www.stata.com/help.cgi?varname)\|`#)` | lower limit for left-censoring          |
|                                                             | `rcensored(`[varname](http://www.stata.com/help.cgi?varname)\|`#)` | upper limit for right-censoring         |
| Only allowed with `family(gaussian)` with `link(identity)`. |                                                                                                 |                                         |

| poisson |                                                                                                  | Description                     |
|---------|--------------------------------------------------------------------------------------------------|---------------------------------|
|         | `ltruncated(`[varname](http://www.stata.com/help.cgi?varname)\|`#)` | lower limit for left-truncation |

| survival                                                                                               |                                                                                                  | Description                               |
|--------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|-------------------------------------------|
|                                                                                                        | `ltruncated(`[varname](http://www.stata.com/help.cgi?varname)\|`#)` | lower limit for left-truncation           |
|                                                                                                        | `failure(varname)`                                                                               | indicator for failure event               |
|                                                                                                        | `ph`                                                                                             | proportional hazards parameterization     |
|                                                                                                        | `aft`                                                                                            | accelerated failure-time parameterization |
| `ph` is allowed only with families `exponential` and `weibull`.                                        |                                                                                                  |                                           |
| `aft` is allowed only with families `exponential`, `gamma`, `loglogistic`, `lognormal`, and `weibull`. |                                                                                                  |                                           |

If you specify both `family()` and `link()`, not all combinations make
sense. You may choose from the following combinations:

------------------------------------------------------------------------

------------------------------------------------------------------------
