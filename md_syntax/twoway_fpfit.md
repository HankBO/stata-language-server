## Syntax

`twoway fpfit yvar xvar` _\[`if`\]
\[`in`\]_ \[`weight`\] \[`, options`\]

<table class="standard">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><var class="command">options</var></td>
<td>Description <span>{p2line None}_</td>
</tr>
<tr class="even">
<td><code class="command">estcmd:(</code><var class="command">est_cmd</var><code class="command">)</code></td>
<td>estimation command; default is <code class="command">regress</code></td>
</tr>
<tr class="odd">
<td><code class="command">estopts:(</code><var class="command">est_opts</var><code class="command">)</code></td>
<td>specifies <var class="command">est_opts</var> to estimate the fractional polynomial regression</td>
</tr>
<tr class="even">
<td><var class="command">cline_options</var></td>
<td>change look of predicted line</td>
</tr>
<tr class="odd">
<td><var class="command">axis_choice_options</var></td>
<td>associate plot with alternative axis</td>
</tr>
<tr class="even">
<td><var class="command">twoway_options</var></td>
<td>titles, legends, axes, added lines and text, by, regions, name, aspect ratio, etc. <span>{p2line None}_
<span data-options="est_cmd">{marker est_cmd}_ <var class="command">est_cmd</var> may be [<strong>clogit</strong>](http://www.stata.com/help.cgi?clogit), [<strong>glm</strong>](http://www.stata.com/help.cgi?glm), [<strong>intreg</strong>](http://www.stata.com/help.cgi?intreg), [<strong>logistic</strong>](http://www.stata.com/help.cgi?logistic), [<strong>logit</strong>](http://www.stata.com/help.cgi?logit), [<strong>mlogit</strong>](http://www.stata.com/help.cgi?mlogit), [<strong>nbreg</strong>](http://www.stata.com/help.cgi?nbreg), [<strong>ologit</strong>](http://www.stata.com/help.cgi?ologit), [<strong>oprobit</strong>](http://www.stata.com/help.cgi?oprobit), [<strong>poisson</strong>](http://www.stata.com/help.cgi?poisson), [<strong>probit</strong>](http://www.stata.com/help.cgi?probit), [<strong>regress</strong>](http://www.stata.com/help.cgi?regress), [<strong>rreg</strong>](http://www.stata.com/help.cgi?rreg), [<strong>stcox</strong>](http://www.stata.com/help.cgi?stcox), [<strong>stcrreg</strong>](http://www.stata.com/help.cgi?stcrreg), [<strong>streg</strong>](http://www.stata.com/help.cgi?streg), or [<strong>xtgee</strong>](http://www.stata.com/help.cgi?xtgee).
Options <code class="command">estcmd()</code> and <code class="command">estopts()</code> are <var class="command">unique</var>; see [<strong>repeated options</strong>](http://www.stata.com/help.cgi?repeated%20options). <span data-options="weight">{marker weight}_
<code class="command">aweight</code>s, <code class="command">fweight</code>s, and <code class="command">pweight</code>s are allowed. Weights, if specified, affect estimation but not how the weighted results are plotted. See [<strong>weight</strong>](http://www.stata.com/help.cgi?weight).</td>
</tr>
</tbody>
</table>

| est\_opts                                                                                                                                                                                                                                                                                                                                      |                     | Description                                                       |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------|-------------------------------------------------------------------|
|                                                                                                                                                                                                                                                                                                                                                | `degree(#)`         | degree of fractional polynomial to fit; default is `degree(2)`    |
|                                                                                                                                                                                                                                                                                                                                                | `noscaling`         | suppress scaling of first independent variable                    |
|                                                                                                                                                                                                                                                                                                                                                | `noconstant`        | suppress constant term                                            |
|                                                                                                                                                                                                                                                                                                                                                | `powers(numlist)`   | list of fractional polynomial powers from which models are chosen |
|                                                                                                                                                                                                                                                                                                                                                | `center(cent_list)` | specification of centering for the independent variables          |
|                                                                                                                                                                                                                                                                                                                                                | `all`               | include out-of-sample observations in generated variables         |
|                                                                                                                                                                                                                                                                                                                                                | `log`               | display iteration log                                             |
|                                                                                                                                                                                                                                                                                                                                                | `compare`           | compare models by degree                                          |
|                                                                                                                                                                                                                                                                                                                                                | `display_options`   | control column formats and line width                             |
|                                                                                                                                                                                                                                                                                                                                                | `other_est_opts`    | other options allowed by `est_cmd`                                |
| `cent_list` is a comma-separated list with elements [varlist](http://www.stata.com/help.cgi?varlist)`:`{`mean`\|`#`\|`no`}, except that the first element may optionally be of the form {`mean`\|`#`\|`no`} to specify the default for all variables. |                     |                                                                   |
