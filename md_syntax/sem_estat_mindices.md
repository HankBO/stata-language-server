## Syntax

`estat mindices` \[`, options`\]

<table class="syntab">
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">Options</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="showp">showpclass(pclassname)</code></td>
<td>restrict output to parameters in specified parameter classes</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="min">minchi2(#)</code></td>
<td>display only tests with modification index <span class="nowrap">(MI) _
<ul>
</ul>
<var class="command">#</var></td>
</tr>
</tbody>
</table>

|              |                                                       |
|--------------|-------------------------------------------------------|
| `pclassname` | Description {p2line None}                             |
| `scoef`      | structural coefficients                               |
| `scons`      | structural intercepts                                 |
| `mcoef`      | measurement coefficients                              |
| `mcons`      | measurement intercepts                                |
| `serrvar`    | covariances of structural errors                      |
| `merrvar`    | covariances of measurement errors                     |
| `smerrcov`   | covariances between structural and measurement errors |
| `meanex`     | means of exogenous variables                          |
| `covex`      | covariances of exogenous variables {p2line None}      |
| `all`        | all the above                                         |
| `none`       | none of the above {p2line None}                       |
