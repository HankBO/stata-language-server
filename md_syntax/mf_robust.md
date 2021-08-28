## Syntax

`Initialization`

`R = robust_init()`

`Estimation sample and subpopulation specifications`

`(varies)`<span class="nowrap"> _ `robust_init_touse(R,`
`touse)`

`(varies)`<span class="nowrap"> _ `robust_init_subpop(R,`
`subpop)`

`Model specification`

Note: In all the following `robust_init_*()` functions, the last
argument is optional. Not specifying this argument causes the current,
unchanged setting to be returned.

`(varies)`<span class="nowrap"> _ `robust_init_scores(R,`
`S)`

`(varies)`<span class="nowrap"> _ `robust_init_covmat(R,`
`D)`

`(varies)`<span class="nowrap"> _ `robust_init_eq_n(R,`
`neq)`

`(varies)`<span class="nowrap"> _
`robust_init_eq_indepvars(R, i, X)`

`(varies)`<span class="nowrap"> _ `robust_init_eq_cons(R,`
`i,` { `"on"` \| `"off"` <span
options=")-">{c )-}_ `)`

`(varies)`<span class="nowrap"> _ `robust_init_minus(R,`
`m)`

`Sampling design specification`

`(varies)`<span class="nowrap"> _ `robust_init_svyset(R,`
{ `"off"` \| `"on"` <span options=")-">{c
)-}_ `)`

`(varies)`<span class="nowrap"> _ `robust_init_nstages(R,`
`K)`

`(varies)`<span class="nowrap"> _ `robust_init_stage_units(R,`
`k, units)`

`(varies)`<span class="nowrap"> _
`robust_init_stage_strata(R, k, strata)`

`(varies)`<span class="nowrap"> _ `robust_init_stage_fpc(R,`
`k, fpc)`

`(varies)`<span class="nowrap"> _ `robust_init_weight(R,`
`w)`

`(varies)`<span class="nowrap"> _ `robust_init_weighttype(R,`
{ `""` \| `"pweight"` \|  
`"fweight"` \| `"aweight"` } `)`

`(varies)`<span class="nowrap"> _ `robust_init_poststrata(R,`
`P)`

`(varies)`<span class="nowrap"> _ `robust_init_singleunit(R,`
`singleunit)`

`Miscellaneous settings`

`(varies)`<span class="nowrap"> _ `robust_init_V_srs(R,` <span
options="-(">{c -(}_ `"off"` \| `"on"` <span options=")-">{c
)-}_ `)`

`(varies)`<span class="nowrap"> _ `robust_init_verbose(R,`
{ `"on"` \| `"off"` <span options=")-">{c
)-}_ `)`

`Variance computation`

`real matrix`<span class="nowrap"> _ `robust(R)`

`real scalar`<span class="nowrap"> _ `_robust(R)`

`Results`

`real matrix`<span class="nowrap"> _ `robust_result_V(R)`

`real matrix`<span class="nowrap"> _ `robust_result_V_srs(R)`

`real matrix`<span class="nowrap"> _
`robust_result_V_srssub(R)`

`real matrix`<span class="nowrap"> _
`robust_result_V_srswr(R)`

`real matrix`<span class="nowrap"> _
`robust_result_V_srswrsub(R)`

`real matrix`<span class="nowrap"> _
`robust_result_stage_strata(R)`

`real matrix`<span class="nowrap"> _
`robust_result_stage_certain(R)`

`real matrix`<span class="nowrap"> _
`robust_result_stage_single(R)`

`real matrix`<span class="nowrap"> _
`robust_result_postsize(R)`

`real matrix`<span class="nowrap"> _
`robust_result_postsum(R)`

`real scalar`<span class="nowrap"> _ `robust_result_N(R)`

`real scalar`<span class="nowrap"> _ `robust_result_sum_w(R)`

`real scalar`<span class="nowrap"> _ `robust_result_N_sub(R)`

`real scalar`<span class="nowrap"> _
`robust_result_sum_wsub(R)`

`real scalar`<span class="nowrap"> _
`robust_result_N_clust(R)`

`real scalar`<span class="nowrap"> _
`robust_result_N_strata(R)`

`real scalar`<span class="nowrap"> _
`robust_result_N_strata_omit(R)`

`real scalar`<span class="nowrap"> _ `robust_result_census(R)`

`real scalar`<span class="nowrap"> _
`robust_result_singleton(R)`

`real scalar`<span class="nowrap"> _
`robust_result_errorcode(R)`

`string scalar`<span class="nowrap"> _
`robust_result_errortext(R)`

`real scalar`<span class="nowrap"> _
`robust_result_returncode(R)`

`Query status of robust specification`

`void`<span class="nowrap"> _ `robust_query(R)`

where `R`, if it is declared, should be declared

`transmorphicR`

and where `singleunit`, optionally specified in
`robust_init_singleunit()`, is

<table class="standard">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><var class="command">singleunit</var></td>
<td>Description <span>{p2line None}_</td>
</tr>
<tr class="even">
<td><code class="command">"missing"</code></td>
<td>return a robust matrix of zeros if there are strata with only one sampling unit</td>
</tr>
<tr class="odd">
<td><code class="command">"certainty"</code></td>
<td>treat strata with only one sampling unit as certainty units</td>
</tr>
<tr class="even">
<td><code class="command">"scaled"</code></td>
<td>use a scale version of <code class="command">"certainty"</code></td>
</tr>
<tr class="odd">
<td><code class="command">"centered"</code></td>
<td>center strata with only one sampling unit at the grand mean <span>{p2line None}_
The default is <code class="command">"missing"</code>.</td>
</tr>
</tbody>
</table>

Arguments `S`, `X`, `touse`, `units`, `strata`, `fpc`, `w`, and `P` are
assumed to be real matrices (or views) of the appropriate dimension or
`string scalar`s identifying Stata variables. A view matrix is generated
when these arguments identify Stata variables. The Stata variable
identified by the `touse` setting (if one was specified) is used to
auto-generate the views.

The `subpop` argument is assumed to be a column vector with the correct
number of rows or a `string scalar` identifying the subpopulation
observations according to the `subpop()` option of the
[<strong>svy</strong>](http://www.stata.com/help.cgi?svy)
prefix command.

No copy of the matrix arguments to the `robust_init_*()` functions
is made; a pointer is stored in `R`, so any changes to the specified
matrix will be reflected from within `robust()` and the
`robust_result_`\*`()` functions.
