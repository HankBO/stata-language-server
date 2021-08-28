## Syntax

`mi impute method` ... \[`, impute_options` ... \]

<table id="methods" class="syntab">
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">method</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd section">
<td colspan="3">Univariate</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td>[](http://www.stata.com/help.cgi?mi_impute_regress)
<ul>
</ul>
ress<strong></strong></td>
<td>linear regression for a continuous variable</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td>[<strong>pmm</strong>](http://www.stata.com/help.cgi?mi_impute_pmm)</td>
<td>predictive mean matching for a continuous variable</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td>[<strong>truncreg</strong>](http://www.stata.com/help.cgi?mi_impute_truncreg)</td>
<td>truncated regression for a continuous variable with a restricted range</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td>[<strong>intreg</strong>](http://www.stata.com/help.cgi?mi_impute_intreg)</td>
<td>interval regression for a continuous partially observed (censored) variable</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td>[](http://www.stata.com/help.cgi?mi_impute_logit)
<ul>
</ul>
t<strong></strong></td>
<td>logistic regression for a binary variable</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td>[](http://www.stata.com/help.cgi?mi_impute_ologit)
<ul>
</ul>
it<strong></strong></td>
<td>ordered logistic regression for an ordinal variable</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td>[](http://www.stata.com/help.cgi?mi_impute_mlogit)
<ul>
</ul>
it<strong></strong></td>
<td>multinomial logistic regression for a nominal variable</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td>[<strong>poisson</strong>](http://www.stata.com/help.cgi?mi_impute_poisson)</td>
<td>Poisson regression for a count variable</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td>[<strong>nbreg</strong>](http://www.stata.com/help.cgi?mi_impute_nbreg)</td>
<td>negative binomial regression for an overdispersed count variable</td>
</tr>
</tbody>
<tbody>
<tr class="odd section">
<td colspan="3">Multivariate</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td>[](http://www.stata.com/help.cgi?mi_impute_monotone)
<ul>
</ul>
otone<strong></strong></td>
<td>sequential imputation using a monotone-missing pattern</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td>[](http://www.stata.com/help.cgi?mi_impute_chained)
<ul>
</ul>
ed<strong></strong></td>
<td>sequential imputation using chained equations</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td>[<strong>mvn</strong>](http://www.stata.com/help.cgi?mi_impute_mvn)</td>
<td>multivariate normal regression</td>
</tr>
</tbody>
<tbody>
<tr class="odd section">
<td colspan="3">User-defined</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td>[<var class="command">usermethod</var><strong></strong>](http://www.stata.com/help.cgi?mi_impute_usermethod)</td>
<td>user-defined imputation methods</td>
</tr>
</tbody>
</table>

| impute\_options                                                                                                                                              |                                                                                                                                                                                                                                  | Description                                                                                                                                                                          |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Main                                                                                                                                                         |                                                                                                                                                                                                                                  |                                                                                                                                                                                      |
| \*                                                                                                                                                           | `add(#)`                                                                                                                                                                                                                         | specify number of imputations to add; required when no imputations exist                                                                                                             |
| \*                                                                                                                                                           | `replace`                                                                                                                                                                                                                        | replace imputed values in existing imputations                                                                                                                                       |
|                                                                                                                                                              | `rseed(#)`                                                                                                                                                                                                                       | specify random-number seed                                                                                                                                                           |
|                                                                                                                                                              | `double`                                                                                                                                                                                                                         | store imputed values in double precision; the default is to store them as `float`                                                                                                    |
|                                                                                                                                                              | `by(`[<var class="command">varlist</var><strong></strong>](http://www.stata.com/help.cgi?varlist) \[`,` [<var class="command">byopts</var><strong></strong>](#byopts)\]`)` | impute separately on each group formed by `varlist` (not allowed with `usermethod`)                                                                                                  |
| Reporting                                                                                                                                                    |                                                                                                                                                                                                                                  |                                                                                                                                                                                      |
|                                                                                                                                                              | `dots`                                                                                                                                                                                                                           | display dots as imputations are performed                                                                                                                                            |
|                                                                                                                                                              | `noisily`                                                                                                                                                                                                                        | display intermediate output                                                                                                                                                          |
|                                                                                                                                                              | `nolegend`                                                                                                                                                                                                                       | suppress all table legends                                                                                                                                                           |
| Advanced                                                                                                                                                     |                                                                                                                                                                                                                                  |                                                                                                                                                                                      |
|                                                                                                                                                              | `force`                                                                                                                                                                                                                          | proceed with imputation, even when missing imputed values are encountered                                                                                                            |
|                                                                                                                                                              | `noupdate`                                                                                                                                                                                                                       | do not perform `mi update` (not allowed with `usermethod`); see [<strong>[MI]</strong> noupdate option](http://www.stata.com/help.cgi?mi_noupdate_option) |
| \* `add(#)` is required when no imputations exist; `add(#)` or `replace` is required if imputations exist.                                                   |                                                                                                                                                                                                                                  |                                                                                                                                                                                      |
| `noupdate` does not appear in the dialog box.                                                                                                                |                                                                                                                                                                                                                                  |                                                                                                                                                                                      |
| You must `mi set` your data before using `mi impute`; see [<strong>[MI]</strong> mi set](http://www.stata.com/help.cgi?mi_set). |                                                                                                                                                                                                                                  |                                                                                                                                                                                      |
