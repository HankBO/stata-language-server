## Syntax

Classification table

`estat classtable` _\[`if`\] \[`in`\]_
\[`weight`\] \[`, classtable_options`\]

Classification error-rate estimation

`estat errorrate` _\[`if`\] \[`in`\]_
\[`weight`\] \[`, errorrate_options`\]

Group summaries

`estat grsummarize` \[`, grsummarize_options`\]

Classification listing

`estat list` _\[`if`\] \[`in`\]_ \[`,`
`list_options`\]

Estimation sample summary

`estat summarize` \[`, labels noheader noweights`\]

| classtable\_options |                  | Description                                                                   |
|---------------------|------------------|-------------------------------------------------------------------------------|
| Main                |                  |                                                                               |
|                     | `class`          | display the classification table; the default                                 |
|                     | `looclass`       | display the leave-one-out classification table                                |
| Options             |                  |                                                                               |
|                     | `priors(priors)` | group prior probabilities; defaults to `e(grouppriors)`                       |
|                     | `nopriors`       | suppress display of prior probabilities                                       |
|                     | `ties(ties)`     | how ties in classification are to be handled; defaults to `e(ties)`           |
|                     | `title(text)`    | title for classification table                                                |
|                     | `probabilities`  | display the average posterior probability of being classified into each group |
|                     | `nopercents`     | suppress display of percentages                                               |
|                     | `nototals`       | suppress display of row and column totals                                     |
|                     | `norowtotals`    | suppress display of row totals                                                |
|                     | `nocoltotals`    | suppress display of column totals                                             |

| priors |                | Description                                                                         |
|--------|----------------|-------------------------------------------------------------------------------------|
|        | `equal`        | equal prior probabilities                                                           |
|        | `proportional` | group-size-proportional prior probabilities                                         |
|        | `matname`      | row or column vector containing the group prior probabilities                       |
|        | `matrix_exp`   | matrix expression providing a row or column vector of the group prior probabilities |

| ties |           | Description                                                                                                                                     |
|------|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------|
|      | `missing` | ties in group classification produce missing values                                                                                             |
|      | `random`  | ties in group classification are broken randomly                                                                                                |
|      | `first`   | ties in group classification are set to the first tied group                                                                                    |
|      | `nearest` | ties in group classification are assigned based on the closest observation, or missing if this still results in a tie; after `discrim knn` only |

| errorrate\_options |                        | Description                                                               |
|--------------------|------------------------|---------------------------------------------------------------------------|
| Main               |                        |                                                                           |
|                    | `class`                | display the classification-based error-rate estimates table; the default  |
|                    | `looclass`             | display the leave-one-out classification-based error-rate estimates table |
|                    | `count`                | use a count-based error-rate estimate                                     |
|                    | `pp`\[`(ppopts)`\] | use a posterior-probability-based error-rate estimate                     |
| Options            |                        |                                                                           |
|                    | `priors(priors)`       | group prior probabilities; defaults to `e(grouppriors)`                   |
|                    | `nopriors`             | suppress display of prior probabilities                                   |
|                    | `ties(ties)`           | how ties in classification are to be handled; defaults to `e(ties)`       |
|                    | `title(text)`          | title for error-rate estimate table                                       |
|                    | `nototal`              | suppress display of total column                                          |

| ppopts |                | Description                  |
|--------|----------------|------------------------------|
|        | `stratified`   | present stratified results   |
|        | `unstratified` | present unstratified results |

| grsummarize\_options |                          | Description                             |
|----------------------|--------------------------|-----------------------------------------|
| Main                 |                          |                                         |
|                      | `n`\[`(%fmt)`\]      | group sizes                             |
|                      | `mean`\[`(%fmt)`\]   | means                                   |
|                      | `median`\[`(%fmt)`\] | medians                                 |
|                      | `sd`\[`(%fmt)`\]     | standard deviations                     |
|                      | `cv`\[`(%fmt)`\]     | coefficients of variation               |
|                      | `semean`\[`(%fmt)`\] | standard errors of the means            |
|                      | `min`\[`(%fmt)`\]    | minimums                                |
|                      | `max`\[`(%fmt)`\]    | maximums                                |
| Options              |                          |                                         |
|                      | `nototal`                | suppress overall statistics             |
|                      | `transpose`              | display groups by row instead of column |

| list\_options |                                                                                                                    | Description                                                         |
|---------------|--------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------|
| Main          |                                                                                                                    |                                                                     |
|               | `misclassified`                                                                                                    | list only misclassified and unclassified observations               |
|               | `classification(`[<var class="command">clopts</var><strong></strong>](#clopts)`)`       | control display of classification                                   |
|               | `probabilities(`[<var class="command">propts</var><strong></strong>](#propts)`)`        | control display of probabilities                                    |
|               | `varlist`\[`(`[<var class="command">varopts</var><strong></strong>](#varopts)`)`\]      | display discriminating variables                                    |
|               | \[`no`\]`obs`                                                                                                      | display or suppress the observation number                          |
|               | `id(`[varname](http://www.stata.com/help.cgi?varname) \[`format(%fmt)`\]`)`             | display identification variable                                     |
| Options       |                                                                                                                    |                                                                     |
|               | `weight`\[`(`[<var class="command">weightopts</var><strong></strong>](#weightopts)`)`\] | display frequency weights                                           |
|               | `priors(priors)`                                                                                                   | group prior probabilities; defaults to `e(grouppriors)`             |
|               | `ties(ties)`                                                                                                       | how ties in classification are to be handled; defaults to `e(ties)` |
|               | `separator(#)`                                                                                                     | display a horizontal separator every `#` lines                      |

| clopts |                | Description                                                                                       |
|--------|----------------|---------------------------------------------------------------------------------------------------|
|        | `noclass`      | do not display the standard classification                                                        |
|        | `looclass`     | display the leave-one-out classification                                                          |
|        | `notrue`       | do not show the group variable                                                                    |
|        | `nostar`       | do not display stars indicating misclassified observations                                        |
|        | `nolabel`      | suppress display of value labels for the group and classification variables                       |
|        | `format(%fmt)` | format for group and classification variables; default is `%5.0f` for unlabeled numeric variables |

| propts |                | Description                                          |
|--------|----------------|------------------------------------------------------|
|        | `nopr`         | suppress display of standard posterior probabilities |
|        | `loopr`        | display leave-one-out posterior probabilities        |
|        | `format(%fmt)` | format for probabilities; default is `format(%7.4f)` |

| varopts |                | Description                                                      |
|---------|----------------|------------------------------------------------------------------|
|         | `none`         | do not display discriminating variables; the default             |
|         | `first`        | display input variables before classifications and probabilities |
|         | `last`         | display input variables after classifications and probabilities  |
|         | `format(%fmt)` | format for input variables; default is the input variable format |

| weightopts |                | Description                                                                                                                          |
|------------|----------------|--------------------------------------------------------------------------------------------------------------------------------------|
|            | `none`         | do not display the weights                                                                                                           |
|            | `format(%fmt)` | format for the weight; default is `%3.0f` for weights &lt; 1,000, `%5.0f` for 1,000 &lt; weights &lt; 100,000, and `%8.0g` otherwise |

`fweight`s are allowed; see
[<strong>weight</strong>](http://www.stata.com/help.cgi?weight).
