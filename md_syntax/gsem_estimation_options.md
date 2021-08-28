## Syntax

`gsem`
[<var class="command">paths</var><strong></strong>](http://www.stata.com/help.cgi?sem%20and%20gsem%20path%20notation)
... `,` ... `estimation_options`

| estimation\_options |                                                                                           | Description                                                                                                             |
|---------------------|-------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
|                     | `method(`[<strong>ml</strong>](sem_option_method##method)`)` | method used to obtain the estimated parameters; only one method available with `gsem`                                   |
|                     | `vce(vcetype)`                                                                        | `vcetype` may be `oim`, `opg`, `robust`, or `cluster clustvar`                                                        |
|                     | `pweights(varlist)`                                                                   | sampling weight variables for each level                                                                                |
|                     | `fweights(varlist)`                                                                   | frequency weight variables for each level                                                                               |
|                     | `iweights(varlist)`                                                                   | importance weight variables for each level                                                                              |
|                     | `from(matname)`                                                                       | specify starting values                                                                                                 |
|                     | `startvalues(svmethod)`                                                               | method for obtaining starting values                                                                                    |
|                     | `startgrid`\[`(gridspec)`\]                                                           | perform a grid search to improve starting values                                                                        |
|                     | opts(gsem\_estimation\_options\#\#emopts():maxopts)                                       | control EM algorithm for improved starting values                                                                       |
|                     | imate                                                                                     | do not fit the model; show starting values instead                                                                      |
|                     | intm:ethod(intmethod)                                                                     | integration method                                                                                                      |
|                     | oints(\#)                                                                                 | set the number of integration (quadrature) points                                                                       |
|                     | adapt:opts(adaptopts)                                                                     | options for adaptive quadrature                                                                                         |
|                     |                                                                                           | apply sem's (not gsem's) rules for omitting observations with missing values                                            |
|                     |                                                                                           | use numerical derivative techniques                                                                                     |
|                     | erance(\#)                                                                                | set the rescaling tolerance to \# to prevent numerical overflow in models with continuous latent variables; rarely used |
|                     | maximize\_options                                                                         | control the maximization process for specified model; seldom used                                                       |

| intmethod |           | Description                                                  |
|-----------|-----------|--------------------------------------------------------------|
|           | aghermite | mean-variance adaptive Gauss-Hermite quadrature; the default |
|           | aghermite | mode-curvature adaptive Gauss-Hermite quadrature             |
|           | ermite    | nonadaptive Gauss-Hermite quadrature                         |
|           | lace      | Laplacian approximation                                      |

<table id="adaptopts" class="syntab">
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">adaptopts</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td class="normal"></td>
<td>[
<ul>
</ul>
]g</td>
<td>whether to display the iteration log for each numerical integral calculation</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td>ate(#)</td>
<td>set the maximum number of iterations of the adaptive technique; default is iterate(1001)</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td>erance(#)</td>
<td>set tolerance for determining convergence of the adaptive parameters; default is tolerance(1e-8)</td>
</tr>
</tbody>
</table>
