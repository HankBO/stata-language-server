## Syntax

Compute sample size

`power twoway meanspec` \[`, power(numlist) options`\]

Compute power

`power twoway meanspec, n(numlist)` \[`options`\]

Compute effect size and target effect variance

`power twoway, n(numlist) power(numlist) nrows(#) ncols(#)`
\[`options`\]

where `meanspec` is either a matrix `matname` containing cell means or
individual cell means in a matrix form:

`m1_1 m1_2` \[...\] `\ m2_1 m2_2` \[...\] \[`\`...`\ mJ_1` ...
`mJ_K`\]

`mj_k`, where j = 1, 2, ..., J and k = 1, 2, ..., K, is the alternative
cell mean or the cell mean of the `j`th row and `k`th column under the
alternative hypothesis.

`matname` is the name of a Stata matrix with `J` rows and `K` columns
containing values of alternative cell means.

<table id="synoptions" class="syntab">
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">options</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd section">
<td colspan="3">Main</td>
</tr>
<tr class="even" style="has_footnote">
<td>*</td>
<td><code class="command" data-options="a">alpha(numlist)</code></td>
<td>significance level; default is <code class="command">alpha(0.05)</code></td>
</tr>
<tr class="odd" style="has_footnote">
<td>*</td>
<td><code class="command" data-options="p">power(numlist)</code></td>
<td>power; default is <code class="command">power(0.8)</code></td>
</tr>
<tr class="even" style="has_footnote">
<td>*</td>
<td><code class="command" data-options="b">beta(numlist)</code></td>
<td>probability of type II error; default is <code class="command">beta(0.2)</code></td>
</tr>
<tr class="odd" style="has_footnote">
<td>*</td>
<td><code class="command" data-options="n(numlist)">n(numlist)</code></td>
<td>total sample size; required to compute power or effect size</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="nfrac">nfractional</code></td>
<td>allow fractional sample sizes</td>
</tr>
<tr class="odd" style="has_footnote">
<td>*</td>
<td><code class="command" data-options="nperc">npercell(numlist)</code></td>
<td>number of subjects per cell; implies balanced design</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command">cellweights(</code><var class="command">wgtspec</var><code class="command">)</code></td>
<td>cell weights; default is one for each cell, meaning equal cell sizes</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="nr">nrows(#)</code></td>
<td>number of rows</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="nc">ncols(#)</code></td>
<td>number of columns</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command"></code>
<ul>
</ul>
f
<ul>
</ul>
actor(row|<code class="command"></code>
<ul>
</ul>
col
<ul>
</ul>
umn|<code class="command">rowcol)</code></td>
<td>tested effect</td>
</tr>
<tr class="even" style="has_footnote">
<td>*</td>
<td><code class="command" data-options="vareff">vareffect(numlist)</code></td>
<td>variance explained by the tested effect in <code class="command">factor()</code></td>
</tr>
<tr class="odd" style="has_footnote">
<td>*</td>
<td><code class="command" data-options="varrow(numlist)">varrow(numlist)</code></td>
<td>variance explained by the row effect; synonym for <code class="command">factor(row)</code> and <code class="command" data-options="vareffect(numlist)">vareffect(numlist)</code></td>
</tr>
<tr class="even" style="has_footnote">
<td>*</td>
<td><code class="command" data-options="varcol">varcolumn(numlist)</code></td>
<td>variance explained by the column effect; synonym for <code class="command">factor(column)</code> and <code class="command" data-options="vareffect(numlist)">vareffect(numlist)</code></td>
</tr>
<tr class="odd" style="has_footnote">
<td>*</td>
<td><code class="command" data-options="varrowcol">varrowcolumn(numlist)</code></td>
<td>variance explained by the row-column interaction effect; synonym for <code class="command">factor(rowcol)</code> and <code class="command" data-options="vareffect(numlist)">vareffect(numlist)</code></td>
</tr>
<tr class="even" style="has_footnote">
<td>*</td>
<td><code class="command" data-options="varerr">varerror(numlist)</code></td>
<td>error variance; default is <code class="command">varerror(1)</code></td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="showmat">showmatrices</code></td>
<td>display cell means and sample sizes as matrices</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="showmea">showmeans</code></td>
<td>display cell means</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="showcells">showcellsizes</code></td>
<td>display cell sample sizes</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="par">parallel</code></td>
<td>treat number lists in starred options or in command arguments as parallel when multiple values per option or argument are specified (do not enumerate all possible combinations of values) <span>{syntab None:Table}_ <span>{synopt None:[}<code class="command">no</code>]<code class="command">table</code>[<code class="command">(</code><var class="command">tablespec</var><code class="command">)</code>]_suppress table or display results as a table; see [<strong>[PSS]</strong> power, table](http://www.stata.com/help.cgi?power_opttable)</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command">saving(</code><var class="command">filename</var>[<code class="command">, replace</code>]<code class="command">)</code></td>
<td>save the table data to <var class="command">filename</var>; use <code class="command">replace</code> to overwrite existing <var class="command">filename</var></td>
</tr>
</tbody>
<tbody>
<tr class="odd section">
<td colspan="3">Graph</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command">graph</code>[<code class="command">(</code><var class="command">graphopts</var><code class="command">)</code>]</td>
<td>graph results; see [<strong>[PSS]</strong> power, graph](http://www.stata.com/help.cgi?power_optgraph)</td>
</tr>
</tbody>
<tbody>
<tr class="odd section">
<td colspan="3">Iteration</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="init(#)">init(#)</code></td>
<td>initial value for sample size or effect size; default is to use a bisection algorithm to bound the solution</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="iter">iterate(#)</code></td>
<td>maximum number of iterations; default is <code class="command">iterate(500)</code></td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="tol">tolerance(#)</code></td>
<td>parameter tolerance; default is <code class="command">tolerance(1e-12)</code></td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="ftol">ftolerance(#)</code></td>
<td>function tolerance; default is <code class="command">ftolerance(1e-12)</code></td>
</tr>
<tr class="even">
<td class="normal"></td>
<td>[<code class="command">no</code>]<code class="command" data-options="log">log</code></td>
<td>suppress or display iteration log</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td>[<code class="command">no</code>]<code class="command" data-options="dots">dots</code></td>
<td>suppress or display iterations as dots</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="noti">notitle</code></td>
<td>suppress the title</td>
</tr>
</tbody><tfoot>
<tr class="even footnote">
<td colspan="3">* Specifying a list of values in at least two starred options, or at least two command arguments, or at least one starred option and one argument results in computations for all possible combinations of the values; see [<strong>numlist</strong>](http://www.stata.com/help.cgi?numlist). Also see the <code class="command">parallel</code> option.</td>
</tr>
<tr class="odd footnote">
<td colspan="3"><code class="command">notitle</code> does not appear in the dialog box.</td>
</tr>
</tfoot>

</table>

| wgtspec |                                               | Description                                                                                                  |
|---------|-----------------------------------------------|--------------------------------------------------------------------------------------------------------------|
|         | `#1_1` ... `#1_K \`...`\ #J_1` ... `#J_K` | `J`x`K` cell weights; weights must be positive and must be integers unless option `nfractional` is specified |
|         | `matname`                                     | `J`x`K` matrix containing cell weights                                                                       |

where `tablespec` is

`column`\[`:label`\] \[`column`\[`:label`\] \[...\]\] \[`,`
`tableopts`\]

`column` is one of the columns defined below, and `label` is a column
label (may contain quotes and compound quotes).

| column                                                                                                    |                   | Description                                          |
|-----------------------------------------------------------------------------------------------------------|-------------------|------------------------------------------------------|
|                                                                                                           | `alpha`           | significance level                                   |
|                                                                                                           | `power`           | power                                                |
|                                                                                                           | `beta`            | type II error probability                            |
|                                                                                                           | `N`               | total number of subjects                             |
|                                                                                                           | `N_per_cell`      | number of subjects per cell                          |
|                                                                                                           | `N_avg`           | average number of subjects per cell                  |
|                                                                                                           | `N#1_#2`    | number of subjects in cell (`#1,#2`)                 |
|                                                                                                           | `delta`           | effect size                                          |
|                                                                                                           | `N_rc`            | number of cells                                      |
|                                                                                                           | `N_r`             | number of rows                                       |
|                                                                                                           | `N_c`             | number of columns                                    |
|                                                                                                           | `m#1_#2`    | cell mean (`#1`,`#2`)                                |
|                                                                                                           | `Var_r`           | variance explained by the row effect                 |
|                                                                                                           | `Var_c`           | variance explained by the column effect              |
|                                                                                                           | `Var_rc`          | variance explained by the row-column interaction     |
|                                                                                                           | `Var_e`           | error variance                                       |
|                                                                                                           | `cwgt#1_#2` | cell weight (`#1`,`#2`)                              |
|                                                                                                           | `target`          | target parameter; synonym for target effect variance |
|                                                                                                           | `_all`            | display all supported columns                        |
| Column `beta` is shown in the default table in place of column `power` if specified.                      |                   |                                                      |
| Column `N_per_cell` is available and is shown in the default table only for balanced designs.             |                   |                                                      |
| Column `N_avg` is shown in the default table only for unbalanced designs.                                 |                   |                                                      |
| Columns `N#1_#2`, `N_rc`, `m#1_#2`, and `cwgt#1_#2` are not shown in the default table. |                   |                                                      |
