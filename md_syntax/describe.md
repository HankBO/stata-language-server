## Syntax

Describe data in memory

`describe`
\[[varlist](http://www.stata.com/help.cgi?varlist)\]
\[`, memory_options`\]

Describe data in file

`describe`
\[[varlist](http://www.stata.com/help.cgi?varlist)\]
`using filename` \[`, file_options`\]

<table id="memory_options" class="syntab">
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">memory_options</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="si">simple</code></td>
<td>display only variable names</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="s">short</code></td>
<td>display only general information</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="f">fullnames</code></td>
<td>do not abbreviate variable names</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="n">numbers</code></td>
<td>display variable number along with name</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="replace">replace</code></td>
<td>make dataset, not written report, of description</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="clear">clear</code></td>
<td>for use with <code class="command">replace</code></td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="varl">varlist</code></td>
<td>store <code class="command">r(varlist)</code> and <code class="command">r(sortlist)</code> in addition to usual stored results; programmer's option</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="si">simple</code></td>
<td>display only variable names</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="varl">varlist</code></td>
<td>store <code class="command">r(varlist)</code> and <code class="command">r(sortlist)</code> in addition to usual stored results; programmer's option</td>
</tr>
</tbody><tfoot>
<tr class="even footnote">
<td colspan="3"><code class="command">varlist</code> does not appear in the dialog box. <span data-options="20">{synoptset 20}_<span>{nobreak None}_ <span data-options="file_options">{marker file_options}_<span>{nobreak None}_ <span>{synopthdr None:file_options}_ <span>{synoptline None}_ <span>{synopt None}<code class="command" data-options="s">short</code>_display only general information</td>
</tr>
<tr class="odd footnote">
<td colspan="3"><code class="command">varlist</code> does not appear in the dialog box. <span data-options="menu">{marker menu}_<span>{nobreak None}_ <span>{title None:Menu}_ <span>{phang2 None}_ <strong>Data &gt; Describe data &gt; Describe data in memory or in a file</strong> <span data-options="description">{marker description}_<span>{nobreak None}_ <span>{title None:Description}_ <span>{pstd None}_ <code class="command">describe</code> produces a summary of the dataset in memory or of the data stored in a Stata-format dataset. <span>{pstd None}_ For a compact listing of variable names, use <code class="command">describe, simple</code>. <span data-options="linkspdf">{marker linkspdf}_<span>{nobreak None}_ <span>{title None:Links to PDF documentation}_ [<strong>Stata/MP</strong>](http://www.stata.com/manuals14/ddescribequickstart.pdf">Quick start</a> <a href="http://www.stata.com/manuals14/ddescriberemarksandexamples.pdf">Remarks and examples</a> <span>{pstd None}_ The above sections are not included in this help file. <span data-options="options_memory">{marker options_memory}_<span>{nobreak None}_ <span>{title None:Options to describe data in memory}_ <span>{phang None}_ <code class="command" data-options="simple">simple</code> displays only the variable names in a compact format. <code class="command" data-options="simple">simple</code> may not be combined with other options. <span>{phang None}_ <code class="command" data-options="short">short</code> suppresses the specific information for each variable. Only the general information (number of observations, number of variables, size, and sort order) is displayed. <span>{phang None}_ <code class="command" data-options="fullnames">fullnames</code> specifies that <code class="command">describe</code> display the full names of the variables. The default is to present an abbreviation when the variable name is longer than 15 characters. <code class="command">describe using</code> always shows the full names of the variables, so <code class="command" data-options="fullnames">fullnames</code> may not be specified with <code class="command">describe using</code>. <span>{phang None}_ <code class="command" data-options="numbers">numbers</code> specifies that <code class="command">describe</code> present the variable number with the variable name. If <code class="command" data-options="numbers">numbers</code> is specified, variable names are abbreviated when the name is longer than eight characters. The <code class="command" data-options="numbers">numbers</code> and <code class="command" data-options="fullnames">fullnames</code> options may not be specified together. <code class="command" data-options="numbers">numbers</code> may not be specified with <code class="command">describe</code> <code class="command">using</code>. <span>{phang None}_ <code class="command" data-options="replace">replace</code> and <code class="command" data-options="clear">clear</code> are alternatives to the options above. <code class="command">describe</code> usually produces a written report, and the options above specify what the report is to contain. If you specify <code class="command" data-options="replace">replace</code>, however, no report is produced; the data in memory are instead replaced with data containing the information that the report would have presented. Each observation of the new data describes a variable in the original data; see <var class="command">describe, replace</var> below. <span>{pmore None}_ <code class="command" data-options="clear">clear</code> may be specified only when <code class="command" data-options="replace">replace</code> is specified. <code class="command" data-options="clear">clear</code> specifies that the data in memory be cleared and replaced with the description information, even if the original data have not been saved to disk. <span>{pstd None}_ The following option is available with <code class="command">describe</code> but is not shown in the dialog box: <span>{phang None}_ <code class="command" data-options="varlist">varlist</code>, an option for programmers, specifies that, in addition to the usual stored results, <code class="command">r(varlist)</code> and <code class="command">r(sortlist)</code> be stored, too. <code class="command">r(varlist)</code> will contain the names of the variables in the dataset. <code class="command">r(sortlist)</code> will contain the names of the variables by which the data are sorted. <span data-options="options_file">{marker options_file}_<span>{nobreak None}_ <span>{title None:Options to describe data in file}_ <span>{phang None}_ <code class="command" data-options="short">short</code> suppresses the specific information for each variable. Only the general information (number of observations, number of variables, size, and sort order) is displayed. <span>{phang None}_ <code class="command" data-options="simple">simple</code> displays only the variable names in a compact format. <code class="command" data-options="simple">simple</code> may not be combined with other options. <span>{pstd None}_ The following option is available with <code class="command">describe</code> but is not shown in the dialog box: <span>{phang None}_ <code class="command" data-options="varlist">varlist</code>, an option for programmers, specifies that, in addition to the usual stored results, <code class="command">r(varlist)</code> and <code class="command">r(sortlist)</code> be stored, too. <code class="command">r(varlist)</code> will contain the names of the variables in the dataset. <code class="command">r(sortlist)</code> will contain the names of the variables by which the data are sorted. <span>{pmore None}_ Because <a href="http://www.stata.com/help.cgi?statamp) and [<strong>Stata/SE</strong>](http://www.stata.com/help.cgi?specialedition) can create truly large datasets, there might be too many variables in a dataset for their names to be stored in <code class="command">r(varlist)</code>, given the current maximum length of macros, as determined by [<strong>set maxvar</strong>](http://www.stata.com/help.cgi?maxvar). Should that occur, <code class="command">describe using</code> will issue the error message "too many variables", r(103). <span data-options="remarks">{marker remarks}_<span>{nobreak None}_ <span>{title None:Remarks}_ <span>{pstd None}_ Remarks are presented under the following headings: [<strong>describe</strong>](#noreplace) [<strong>describe, replace</strong>](#replace) <span data-options="noreplace">{marker noreplace}_<span>{nobreak None}_ <span>{title None:describe}_ <span>{pstd None}_ If <code class="command">describe</code> is typed with no operands, the contents of the dataset currently in memory are described. <span>{pstd None}_ The <var class="command">varlist</var> in the <code class="command">describe using</code> syntax differs from standard Stata [<strong>varlists</strong>](http://www.stata.com/help.cgi?varlist) in two ways. First, you cannot abbreviate variable names; that is, you have to type <code class="command">displacement</code> rather than <code class="command">displ</code>. However, you can use the wildcard character (<code class="command">~</code>) to indicate abbreviations, for example, <code class="command">displ~</code>. Second, you may not refer to a range of variables; specifying <code class="command">age-income</code> is considered an error. <span data-options="replace">{marker replace}_<span>{nobreak None}_ <span>{title None:describe, replace}_ <span>{pstd None}_ <code class="command">describe</code> with the <code class="command">replace</code> option is rarely used, although you may sometimes find it convenient. <span>{pstd None}_ Think of <code class="command">describe,</code> <code class="command">replace</code> as separate from but related to <code class="command">describe</code> without the <code class="command">replace</code> option. Rather than producing a written report, <code class="command">describe,</code> <code class="command">replace</code> produces a new dataset that contains the same information a written report would. For instance, try the following: . <code class="command">sysuse auto, clear</code> . <code class="command">describe</code> <var class="command">(report appears; data in memory unchanged)</var> . <code class="command">list</code> <var class="command">(visual proof that data are unchanged)</var> . <code class="command">describe, replace</code> <var class="command">(no report appears, but the data in memory are changed!)</var> . <code class="command">list</code> <var class="command">(visual proof that data are changed)</var> <span>{pstd None}_ <code class="command">describe,</code> <code class="command">replace</code> changes the original data in memory into a dataset containing an observation for each variable in the original data. Each observation in the new data describes a variable in the original data. The new variables are
1. <code class="command">position</code>, a variable containing the numeric position of the original variable (1, 2, 3, ...).
2. <code class="command">name</code>, a variable containing the name of the original variable, such as <code class="command">"make"</code>, <code class="command">"price"</code>, <code class="command">"mpg"</code>, ....
3. <code class="command">type</code>, a variable containing the storage type of the original variable, such as <code class="command">"str18"</code>, <code class="command">"int"</code>, <code class="command">"float"</code>, ....
4. <code class="command">isnumeric</code>, a variable equal to 1 if the original variable was numeric and equal to 0 if it was string.
5. <code class="command">format</code>, a variable containing the display format of the original variable, such as <code class="command">"%-18s"</code>, <code class="command">"%8.0gc"</code>, ....
6. <code class="command">vallab</code>, a variable containing the name of the value label associated with the original variable, if any.
7. <code class="command">varlab</code>, a variable containing the variable label of the original variable, such as <code class="command">"Make and Model"</code>, <code class="command">"Price"</code>, <code class="command">"Mileage (mpg)"</code>, .... <span>{pstd None}_ In addition, the data contain the following characteristics:
<code class="command">_dta[d_filename]</code>, the name of the file containing the original data.
<code class="command">_dta[d_filedate]</code>, the date and time the file was written.
<code class="command">_dta[d_N]</code>, the number of observations in the original data.
<code class="command">_dta[d_sortedby]</code>, the variables on which the original data were sorted, if any. <span data-options="examples">{marker examples}_<span>{nobreak None}_ <span>{title None:Examples}_ <span>{hline None}_ <span>{pstd None}_Setup</td>
</tr>
<tr class="even footnote">
<td colspan="3"><code class="command">. webuse states</code> <span>{pstd None}_Describe dataset in memory</td>
</tr>
<tr class="odd footnote">
<td colspan="3"><code class="command">. describe</code> <span>{pstd None}_Describe dataset in memory, displaying full variable names</td>
</tr>
<tr class="even footnote">
<td colspan="3"><code class="command">. describe, fullnames</code> <span>{pstd None}_Describe dataset in memory, suppressing specific information about each variable</td>
</tr>
<tr class="odd footnote">
<td colspan="3"><code class="command">. describe, short</code> <span>{hline None}_ <span>{pstd None}_Setup</td>
</tr>
<tr class="even footnote">
<td colspan="3"><code class="command">. sysuse census</code> <span>{pstd None}_Describe all variables whose names begin with <code class="command">pop*</code> for the dataset in memory</td>
</tr>
<tr class="odd footnote">
<td colspan="3"><code class="command">. describe pop*</code> <span>{pstd None}_Describe the variables <code class="command">state</code>, <code class="command">region</code>, and <code class="command">pop18p</code> for the dataset in memory</td>
</tr>
<tr class="even footnote">
<td colspan="3"><code class="command">. describe state region pop18p</code> <span>{pstd None}_Describe the <code class="command">states</code> dataset located at the http://www.stata-press.com website</td>
</tr>
<tr class="odd footnote">
<td colspan="3"><code class="command">. describe using http://www.stata-press.com/data/r15/states</code></td>
</tr>
</tfoot>

</table>
