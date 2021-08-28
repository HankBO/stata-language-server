## Syntax

Load Haver data

`import haver seriesdblist` \[, `import_haver_options`\]

Load Haver data using a dataset that is loaded in memory

`import haver`, `frommemory` \[`import_haver_options`\]

Describe contents of Haver database

`import haver seriesdblist`, `describe`
\[`import_haver_describe_options`\]

Specify the directory where the Haver databases are stored

`set haverdir "path"` \[`, permanently`\]

| import\_haver\_options                                    |                                                    | Description                                                      |
|-----------------------------------------------------------|----------------------------------------------------|------------------------------------------------------------------|
|                                                           | `fin:(`\[`datestring`\]`,` \[`datestring`\]`)`     | load data within specified date range                            |
|                                                           | `fwithin:(`\[`datestring`\]`,` \[`datestring`\]`)` | same as `fin()` but exclude the end points of range              |
|                                                           | `tvar(varname)`                                    | create time variable `varname`                                   |
|                                                           | `case(lower`\|`upper)`                         | read variable names as lowercase or uppercase                    |
|                                                           | `hmissing(misval)`                                 | record missing values as `misval`                                |
|                                                           | `aggmethod(strict`\|`relaxed`\|`force)`          | set how temporal aggregation calculations deal with missing data |
|                                                           | `frommemory`                                       | load data using file in memory                                   |
|                                                           | `clear`                                            | clear data in memory before loading Haver database               |
| `frommemory` and `clear` do not appear in the dialog box. |                                                    |                                                                  |

<table id="import_haver_describe_options" class="syntab">
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">import_haver_describe_options</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd" style="has_footnote">
<td>*</td>
<td><code class="command" data-options="des">describe</code></td>
<td>describe contents of <var class="command">seriesdblist</var></td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="det">detail</code></td>
<td>list full series information table for each series</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command">saving(</code><var class="command">filename</var>[<code class="command">, verbose replace</code>]<code class="command">)</code></td>
<td>save series information to <var class="command">filename</var><code class="command">.dta</code></td>
</tr>
</tbody><tfoot>
<tr class="even footnote">
<td colspan="3">* <code class="command" data-options="describe">describe</code> is required. <span data-options="seriesdblist">{marker seriesdblist}_<span>{nobreak None}_
<var class="command">seriesdblist</var> is one or more of the following: <var class="command">dbfile</var> <var class="command">series</var><code class="command">@</code><var class="command">dbfile</var> <code class="command">(</code><var class="command">series series</var> ....<code class="command">)@</code><var class="command">dbfile</var>
where <var class="command">dbfile</var> is the name of a Haver Analytics database and <var class="command">series</var> contains a Haver Analytics series. Wildcards <code class="command">?</code> and <code class="command">*</code> are allowed in <var class="command">series</var>. <var class="command">series</var> and <var class="command">dbfile</var> are not case sensitive. <span data-options="seriesdblist_examples">{marker seriesdblist_examples}_<span>{nobreak None}_
Example: <code class="command">import haver gdp@usecon</code></td>
</tr>
<tr class="odd footnote">
<td colspan="3">Import series GDP from the USECON database.
Example: <code class="command">import haver gdp@usecon c1*@ifs</code></td>
</tr>
<tr class="even footnote">
<td colspan="3">Import series GDP from the USECON database, and import any series that starts with c1 from the IFS database.
Note: You must specify a path to the database if you did not use the <code class="command">set haverdir</code> command.</td>
</tr>
</tfoot>

</table>

Example: `import haver gdp@"C:\data\usecon" c1*@"C:\data\ifs"`

If you do not specify a path to the database and you did not
`set haverdir`, then `import haver` will look in the current working
directory for the database.
